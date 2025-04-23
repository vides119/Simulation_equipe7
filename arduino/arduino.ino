//constantes
const float R0 = 9913.0; // bas droit
const float R1 = 9879.0; // haut droit
const float R2 = 9726.0; // haut gauche
const float R3 = 9912.0; // bas gauche
const float R0_25 = 10000.0;
const float R1_25 = 10000.0;
const float R2_25 = 10000.0;
const float R3_25 = 10000.0;
const double A = 0.00335401643468053;
const double B = 0.000256523550896126;
const double C = 0.00000260597012072052;
const double D = 0.000000063292612648746;

// prédiction t3
float T_ambiant;
float T_boucle = 1;
float a12 = 0.8865*T_boucle/(2*22.507+T_boucle);
float b12 = (2*22.507-T_boucle)/(2*22.507+T_boucle);
volatile float pred_t12[2] = {0};
volatile float cmd_t12[2] = {0};
volatile float pred_t2;

// équation récurente PID
float k_p = 0.238;
float k_i = 0.005;
float k_d = 1;
float N_d = 0.1;
volatile float u[2] = {0, 0};
volatile float u_p[2] = {0, 0};
volatile float u_i[2] = {0, 0};
volatile float u_d[2] = {0, 0};
volatile float e[2] = {0, 0};

//mesures
float gains[4] = {2.94, 4.17, 6.25, 6.25};
float offsets[4] = {-1.7, -1.9, -2.1, -2.1};
volatile float adc0;
volatile float adc1;
volatile float adc2;
volatile float adc3;
volatile float vr0, vr1, vr2, vr3;
volatile float r0, r1, r2, r3;
volatile float t0, t1, t2, t3;

//modes prototype et variables globales
enum MODE 
{
  IDLE,
  REGUL,
  COMMAND
};
enum MODE mode = IDLE;
float consigne;
float commande;


void identifie_amplis(float gains[4], float offsets[4], const int N);
void update_temp();
void update_command();
void identifie_amplis(float gains[4], float offsets[4], const int N);
void idle_loop();
void load_params();
void asservissement_loop();
void command_loop();


void setup() {
  Serial.begin(115200);
  cli(); //stop interrupts

  //Fast PWM, 10 bits, Timer 1, no prescaler
  //Output OC1A = PB5 = pin 11  commande auto-identification
  //Output OC1B = PB6 = pin 12  commande principale
  //Output OC1C = PB7 = pin 13
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  TCCR1A = (1 << COM1A1) | (1 << COM1B1) | (1 << COM1C1) | (1 << WGM11) | (1 << WGM10);
  TCCR1B = (1 << WGM12) | (1 << CS10);
  OCR1B = 511; //commande à 0


  /* ADC setup
  reference=AREF(01), ADMUS = 0b010_____
  prescalar 128
  déclenche une première conversion pour terminer le reset
  */
  ADCSRA = 0; //reset
  delay(1);
  ADMUX = (1 << REFS0);
  ADCSRA = (1 << ADEN) |
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
  ADCSRA |= (1 << ADSC);
  while (ADCSRA & (1 << ADSC));
  ADCSRA = (1 << ADEN) | (1 << ADIE) | //réactive interruptions
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);


  //Timer 3 interrupt vector
  // CTC mode, 256 prescaler
  TCNT3 = 0;
  TCCR3A = 0;
  TCCR3B = 0;
  TCCR3B = (1 << WGM32) | (1 << CS32) | (1 << CS30);
  TIMSK3 = (0 << OCIE3A); //Disable interrupt
  OCR3A = 15625*T_boucle; //freq = 15625 / OCR3A
  sei();
}


/*-------------------------------------------------------------------------
------------- ROUTINES INTERRUPTION ----------------------------------------
-------------------------------------------------------------------------*/


// Routine interruption timer 3
// Commencer chaine de sample en débutant une conversion à l'ADC0
ISR(TIMER3_COMPA_vect)
{
  ADMUX = (1 << REFS0);
  delayMicroseconds(24);
  ADCSRA |= (1 << ADSC);
}

// Routine interruption sample ADC terminé
// À chaque fin de conversion, on lit l'ADC et commence conversion
// avec le prochain ADC.
ISR(ADC_vect)
{
  static int adc_mux = 0; //compteur traque quel ADC doit être samplé
  switch (adc_mux)
  {
    case 0:
      adc0 = ADC;
      adc_mux = 1;
      break;
    case 1:
      adc1 = ADC;
      adc_mux = 2;
      break;
    case 2:
      adc2 = ADC;
      adc_mux = 4;
      break;
    case 4:
      adc3 = ADC;
      adc_mux = 0;
      update_temp();
      update_command();
      break;
    default:
      adc_mux = 0;
  }

  if (adc_mux != 0)
  {
  ADMUX = (1 << REFS0) | (adc_mux);
  delayMicroseconds(24);
  ADCSRA |= (1 << ADSC);
  }
}


/*-------------------------------------------------------------------------
------------- FONCTIONS UTILITAIRES ---------------------------------------
-------------------------------------------------------------------------*/


// prédit t3 à partir de t2, calcule la commande avec le PID si nécessaire, envoie la commande
void update_command()
{
  if (mode == COMMAND)
  {
    //prédiction température t2
    cmd_t12[0] = t1 - T_ambiant;
    pred_t12[0] = a12*(cmd_t12[0] + cmd_t12[1]) + b12*pred_t12[1];

    pred_t2 = pred_t12[0] + T_ambiant;

    pred_t12[1] = pred_t12[0];
    cmd_t12[1] = cmd_t12[0];
  
    consigne = -1;
    OCR1B = (commande+1)*511.5;
  }
  else if ((mode == REGUL) && (consigne >= 20))
  {
    //prédiction température t2
    cmd_t12[0] = t1 - T_ambiant;
    pred_t12[0] = a12*(cmd_t12[0] + cmd_t12[1]) + b12*pred_t12[1];

    pred_t2 = pred_t12[0] + T_ambiant;

    pred_t12[1] = pred_t12[0];
    cmd_t12[1] = cmd_t12[0];

    //calcul commande à partir consigne PID/PI
    e[0] = consigne - pred_t2;
    u_p[0] = k_p * e[0];
    u_i[0] = u_i[1] + 0.5*k_i*T_boucle*(e[0]+e[1]);
    u_d[0] = u_d[1]*(2-N_d*T_boucle)/(2+N_d*T_boucle) + ((2*k_d*N_d)/(2+k_d*N_d))*(e[0]-e[1]);
    u[0] = u_p[0] + u_i[0] + u_d[0];

    //clamp
    u[0] = (u[0] > 1) ? 1: u[0];
    u[0] = (u[0] < -1) ? -1: u[0];
    u_i[0] = (u_i[0] > 1) ? 1: u_i[0];
    u_i[0] = (u_i[0] < -1) ? -1: u_i[0];

    //move next
    u[1] = u[0];
    u_p[1] = u_p[0];
    u_i[1] = u_i[0];
    u_d[1] = u_d[0];
    e[1] = e[0];

    commande = u[0];
    OCR1B = (commande+1)*511.5;
  }
  float temps = millis()/1000.0f;
  Serial.print(temps);Serial.print(",");Serial.print(commande);Serial.print(",");Serial.print(consigne);Serial.print(",");Serial.print(t0);Serial.print(",");Serial.print(t1);Serial.print(",");Serial.print(t2);Serial.print(",");Serial.println(pred_t2);
}

// calcule les températures à partir des valeurs de ADC et des gains/offsets
void update_temp()
{
  vr0 = (adc0*5.0) / (1024.0*gains[0]) - offsets[0]; // vérifier signe offset
  vr1 = (adc1*5.0) / (1024.0*gains[1]) - offsets[1];
  vr2 = (adc2*5.0) / (1024.0*gains[2]) - offsets[2];
  vr3 = (adc3*5.0) / (1024.0*gains[3]) - offsets[3];

  //convert to resistance
  r0 = (vr0*R0) / (5.0-vr0);
  r1 = (vr1*R1) / (5.0-vr1);
  r2 = (vr2*R2) / (5.0-vr2);
  r3 = (vr3*R3) / (5.0-vr3);
  
  // compenser pour résistance entrée amplificateurs
  r0 = 940000*r0 / (940000-r0);
  r1 = 1380000*r1 / (1380000-r1);
  r2 = 870000*r2 / (870000-r2);
  r3 = 870000*r3 / (870000-r3);

  //calcul température
  t0 = 1 / (A + B*log(r0/R0_25) + C*pow(log(r0/R0_25), 2) + D*pow(log(r0/R0_25), 3)) - 273.15;
  t1 = 1 / (A + B*log(r1/R1_25) + C*pow(log(r1/R1_25), 2) + D*pow(log(r1/R1_25), 3)) - 273.15;
  t2 = 1 / (A + B*log(r2/R2_25) + C*pow(log(r2/R2_25), 2) + D*pow(log(r2/R2_25), 3)) - 273.15;
  t3 = 1 / (A + B*log(r3/R3_25) + C*pow(log(r3/R3_25), 2) + D*pow(log(r3/R3_25), 3)) - 273.15;
}

/*
Fonction d'auto-identification des amplificateurs
La commande prend ~1 seconde à atteindre 100% de sa valeur (d'où le délai)
Voir la section 7 du rapport pour les formules
*/
void identifie_amplis(float gains[4], float offsets[4], const int N) {
  ADCSRA = (1 << ADEN) | //désactive interruptions ADC
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
  float sigma_x[4] = {0};
  float sigma_y[4] = {0};
  float sigma_xy[4] = {0};
  float sigma_xx[4] = {0};
  float x, y;
  const int FREQ_STEP = 140 / N; //(575-140)/N
  for (int i=0; i<N; i++)
  {
    OCR1A = 435 + FREQ_STEP*i;
    Serial.println(OCR1A);
    
    delay(1500);

    //Vin
    ADMUX = (1 << REFS0) | 3;
    delay(1);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    x = 5.0*ADC/1023;
    Serial.println(x);

    //Vout0 - ADC0
    ADMUX = (1 << REFS0);
    delay(1);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    y = 5.0*ADC/1023;
    Serial.println(y);
    sigma_x[0] += x;
    sigma_y[0] += y;
    sigma_xy[0] += x*y;
    sigma_xx[0] += x*x;

    //Vout1 - ADC1
    ADMUX = (1 << REFS0) | 1;
    delay(1);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    y = 5.0*ADC/1023;
    Serial.println(y);
    sigma_x[1] += x;
    sigma_y[1] += y;
    sigma_xy[1] += x*y;
    sigma_xx[1] += x*x;

    //Vout2 - ADC2
    ADMUX = (1 << REFS0) | 2;
    delay(1);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    y = 5.0*ADC/1023;
    Serial.println(y);
    sigma_x[2] += x;
    sigma_y[2] += y;
    sigma_xy[2] += x*y;
    sigma_xx[2] += x*x;

    //Vout3 - ADC4
    ADMUX = (1 << REFS0) | 4;
    delay(1);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    y = 5.0*ADC/1023;
    Serial.println(y);
    sigma_x[3] += x;
    sigma_y[3] += y;
    sigma_xy[3] += x*y;
    sigma_xx[3] += x*x;
  }
  //calcul gain et offset
  gains[0] = (sigma_xy[0] - sigma_x[0]*sigma_y[0]/N) / (sigma_xx[0] - sigma_x[0]*sigma_x[0]/N);
  gains[1] = (sigma_xy[1] - sigma_x[1]*sigma_y[1]/N) / (sigma_xx[1] - sigma_x[1]*sigma_x[1]/N);
  gains[2] = (sigma_xy[2] - sigma_x[2]*sigma_y[2]/N) / (sigma_xx[2] - sigma_x[2]*sigma_x[2]/N);
  gains[3] = (sigma_xy[3] - sigma_x[3]*sigma_y[3]/N) / (sigma_xx[3] - sigma_x[3]*sigma_x[3]/N);
  offsets[0] = (sigma_y[0]/gains[0] - sigma_x[0])/N;
  offsets[1] = (sigma_y[1]/gains[1] - sigma_x[1])/N;
  offsets[2] = (sigma_y[2]/gains[2] - sigma_x[2])/N;
  offsets[3] = (sigma_y[3]/gains[3] - sigma_x[3])/N;
  Serial.print("Gain 0: ");Serial.print(gains[0]);Serial.print(" Offset 0: ");Serial.println(offsets[0]);
  Serial.print("Gain 1: ");Serial.print(gains[1]);Serial.print(" Offset 1: ");Serial.println(offsets[1]);
  Serial.print("Gain 2: ");Serial.print(gains[2]);Serial.print(" Offset 2: ");Serial.println(offsets[2]);
  Serial.print("Gain 3: ");Serial.print(gains[3]);Serial.print(" Offset 3: ");Serial.println(offsets[3]);
  ADCSRA = (1 << ADEN) | (1 << ADIE) | //réactive interruptions
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}


/*-------------------------------------------------------------------------
------------- INTERFACE SÉRIE ---------------------------------------------
---------------------------------------------------------------------------*/

// boucle principale: call la routine du mode correspondant
void loop()
{
  switch (mode)
  {
    case IDLE:
      OCR1B = 511;
      idle_loop();
      break;
    case REGUL:
      asservissement_loop();
      break;
    case COMMAND:
      command_loop();
      break; 
    default:
      mode = IDLE;
      break;
  }
}

/*
Routine mode IDLE (Attente)
Écoute le port série, éxécute la commande s'il y a lieu
*/
void idle_loop()
{
  if (Serial.available())
  {
    char comm = Serial.read();
    switch (comm)
    {
      //stay idle
      case 'A':
        break;

      //start régulation
      case 'B':
        TIMSK3 = (1 << OCIE3A); //start interrupts
        ADCSRA = (1 << ADEN) | (1 << ADIE) | //réactive interruptions
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
        consigne = 25;
        memset(pred_t12, 0.88656*(t1-T_ambiant)+T_ambiant, sizeof(pred_t12));
        memset(cmd_t12, t1, sizeof(cmd_t12));
        memset(e, 0, sizeof(e));
        memset(u_i, 0, sizeof(u_i));
        memset(u_p, 0, sizeof(u_p));
        mode = REGUL;
        break;

      //start commande
      case 'C':
        TIMSK3 = (1 << OCIE3A); //start interrupts
        ADCSRA = (1 << ADEN) | (1 << ADIE) | //réactive interruptions
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
        commande = 0;
        memset(pred_t12, 0.88656*(t1-T_ambiant)+T_ambiant, sizeof(pred_t12));
        memset(cmd_t12, t1, sizeof(cmd_t12));
        mode = COMMAND;
        break;
      
      //start calibration
      case 'D':
        TIMSK3 = (0 << OCIE3A); //disable interrupt (supposé être déjà fait)
        identifie_amplis(gains, offsets, 20);
        Serial.println("ACK");
        break;
      
      //transfert paramètres
      case 'E':
        TIMSK3 = (0 << OCIE3A); //disable interrupt (supposé être déjà fait)
        Serial.println("ACK");
        load_params();
        break;
    }
  }
}

// fonction transfert paramètres
void load_params()
{
  // période d'échantillonnage
  while (Serial.available() <= 0);
  T_boucle = Serial.parseFloat();
  OCR3A = 15625*T_boucle; //freq = 62.5k / OCR3A
  a12 = 0.8865*T_boucle/(2*22.507+T_boucle);
  b12 = (2*22.507-T_boucle)/(2*22.507+T_boucle);
  Serial.println("ACK");

  // gain P
  while (Serial.available() <= 0);
  k_p = Serial.parseFloat();
  Serial.println("ACK");

  // gain I
  while (Serial.available() <= 0);
  k_i = Serial.parseFloat();
  Serial.println("ACK");

  // gain D
  while (Serial.available() <= 0);
  k_d = Serial.parseFloat();
  Serial.println("ACK");

  // fréquence angulaire de coupure du PIDF
  while (Serial.available() <= 0);
  N_d = Serial.parseFloat();
  Serial.println("ACK");

  // température 
  while (Serial.available() <= 0);
  T_ambiant = Serial.parseFloat();
  Serial.println("ACK");

  Serial.println("DONE");
  mode = IDLE;
}

// lit la consigne (en deg Cielsus)
// termine l'asservissement si la consigne < 0
void asservissement_loop()
{
  if (Serial.available())
  {
    consigne = Serial.parseFloat();
    if (consigne < 0)
    {
      mode = IDLE;
      TIMSK3 = (0 << OCIE3A); //disable interrupt
      ADCSRA = (1 << ADEN) | (0 << ADIE) | //disable interrupt
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    }
  }
}


// lit la commande
// termine la commande si en dehors de [-1, 1]
void command_loop()
{
  if (Serial.available())
  {
    commande = Serial.parseFloat();
    if ((commande < -1) || (commande > 1))
    {
      mode = IDLE;
      TIMSK3 = (0 << OCIE3A); //Disable interrupt
      ADCSRA = (1 << ADEN) | (0 << ADIE) | //disable interrupt
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    }
  }
}
