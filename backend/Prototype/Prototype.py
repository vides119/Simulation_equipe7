import time
import threading

class CSVWriter:
    """Objet CSV writer de type FIFO
    """
    def __init__(self):
        # Stockage pour le tracé, -10.0 = Val par défaut qui permet de savoir si on a fait un ajout
        self.data = {
            "temps": -10.0,
            "consigne": -10.0,
            "command": -10.0,
            "t0": -10.0,
            "t1": -10.0,
            "t2": -10.0,
            "pred_t2": -10.0,
        }

    def append(self, line:str):
        line = line[:line.find("\r")]
        fields = line.split(",")
        #print(fields)
        if len(fields) != len(self.data):
            print(fields)
            raise ValueError("Each line must contain exactly 5 fields")
        
        # Convertir les valeurs en float
        values = list(map(float, fields))

        # Ajouter les nouvelles valeurs aux tableaux numpy
        for key, value in zip(self.data.keys(), values):
            self.data[key] = value

    def get_data(self):
        """Retourne les données sous forme de dictionnaire de numpy arrays."""
        return self.data
    
    def reset_data(self):
        for key in self.data.keys():
            self.data[key] = -10.0

class Prototype():
    """Initialise la communication série avec le prototype et encapsule son fonctionnement.\n
    On peut donner un objet de type "FIFO" pour la lecture du port série. L'interface va alors
    mettre les lectures du port série dans la FIFO au lieu de "print". L'objet FIFO doit au minimum
    avoir une méthode .append(args)

    Args:
        serial (_type_, optional): Objet Serial.
        fifo (_type_, optional): Objet FIFO. Defaults to None.
    """
    def __init__(self, serial, fifo=None):
        self._serial = serial
        self._fifo = fifo
        self._read_loop_thread = threading.Thread(target=self._read_loop, args=[], daemon=True)
        print(self._read_loop_thread)
        self._read_loop_pause = False
        self._read_loop_running = False
        self._mode = "IDLE"
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, new_mode: str):
        """Change de façon sécuritaire le mode du prototype

        Args:
            new_mode (str): mode, choisir parmi: "IDLE", "REGUL", "COMMAND"

        Raises:
            ValueError: Le mode choisi ne fait pas partie des choix
        """
        if new_mode not in ["IDLE", "REGUL", "COMMAND"]:
            raise ValueError(f"{new_mode} ne fait pas partie des modes permis: 'IDLE', 'REGUL', 'COMMAND'")
        if self._mode in ["REGUL", "COMMAND"]:
            #termine mode courant
            self._serial.write("-5".encode())
        
        if new_mode == "IDLE":
            self._serial.write("A".encode())
            self._mode = "IDLE"
        if new_mode == "REGUL":
            self._serial.write("B".encode())
            self._mode = "REGUL"
        if new_mode == "COMMAND":
            self._serial.write("C".encode())
            self._mode = "COMMAND"
            

    def _read_loop(self):
        while self._read_loop_running:
            while self._serial.in_waiting > 0 and not self._read_loop_pause:
                line = self._serial.readline().decode()
                if self._fifo is None:
                    print(line)
                else:
                    self._fifo.append(line)

    def pause_read_loop(self):
        """Désactive la lecture du port série dans le thread de lecture
        """
        self._read_loop_pause = True
    
    def resume_read_loop(self):
        """Active la lecture du port série dans le thread de lecture.
        """
        self._read_loop_pause = False

    def start_read_loop(self) -> bool:
        """Démarre le thread de lecture du port série

        Returns:
            bool: L'état du thread
        """
        self._read_loop_pause = False
        self._read_loop_running = True
        self._read_loop_thread.start()
        return self._read_loop_thread.is_alive()
    
    def stop_read_loop(self) -> bool:
        """Termine le thread de lecture du port série

        Returns:
            bool: L'état du thread
        """
        self._read_loop_running = False
        return self._read_loop_thread.is_alive()

    def change_FIFO(self, fifo):
        """Change la FIFO de l'interface. La FIFO doit avoir une méthode .append().

        Args:
            fifo (_type_): Objet type FIFO
        """
        self._fifo = fifo
    
    def auto_identification(self, verbose=False):
        """Commence la routine d'auto-identification des amplificateurs. Gèle
        le programme jusqu'à la fin de l'auto-identification.

        Args:
            verbose (bool, optional): print l'état du prototype. Defaults to False.
        """
        if self._mode != "IDLE":
            self.mode = "IDLE"
        self.pause_read_loop()
        self._serial.write("D".encode())
        #wait for ACK
        waiting = True
        while waiting:
            while self._serial.in_waiting > 0:
                line = self._serial.readline().decode()
                if verbose == True:
                    print(line)
                if line == "ACK\r\n":
                    waiting = False
                    break
        self.resume_read_loop()
        if verbose:
            print("auto-identification terminée")
        
    
    def write_consigne(self, consigne: float):
        """Écrit une consigne sur le port série. Cette opération n'a de sens qu'en mode asservissement.

        Args:
            consigne (float): consigne

        Raises:
            RuntimeError: Le prototype n'est pas en mode asservissement
            ValueError: La consigne n'est pas plus grande que 0
        """
        if self._mode != "REGUL":
            raise RuntimeError(f"On ne peut pas écrire une consigne si le prototype n'est pas\
                               en mode consigne (présentement en mode {self._mode})")
        if consigne < 0:
            raise ValueError(f"{consigne} est plus petit que 0.")
        self._serial.write(str(round(consigne, 2)).encode())
        
    def write_command(self, command: float):
        """Écrit une commande sur le port série. Cette opération n'a de sens qu'en mode commande.

        Args:
            command (float): commande

        Raises:
            RuntimeError: Le prototype n'est pas en mode commande
            ValueError: La commande n'est pas dans l'intervalle [-1, 1]
        """
        if self._mode != "COMMAND":
            raise RuntimeError(f"On ne peut pas écrire une commande si le prototype n'est pas\
                                en mode commande(présentement en mode {self._mode})")
        if -1 > command or command > 1:
            raise ValueError(f"{command} n'est pas entre -1 et 1.")
        self._serial.write(str(round(command, 2)).encode())
    
    def write_params(self, *params, verbose = False) -> bool:
        """Change les paramètres du prototype. Attention de bien mettre le nombre de
        paramètres attendus par le prototype.

        Args:
            verbose (bool, optional): print l'état du prototype. Defaults to False.

        Returns:
            bool: Le succès de l'opération
        """
        if self.mode != "IDLE":
            self.mode = "IDLE"

        self.pause_read_loop()
        #envoie la commande de début et attend une réponse
        self._serial.write("E".encode())
        waiting = True
        while waiting:
            while self._serial.in_waiting > 0:
                line = self._serial.readline().decode()
                if line == "ACK\r\n":
                    waiting = False
                    break
        if verbose:
            print("ack, transfert commencé")

        #envoie les paramètres et attend une réponse pour chacun
        for i, param in enumerate(params):
            self._serial.write(str(param).encode())
            #wait for ack
            waiting = True
            while waiting:
                while self._serial.in_waiting > 0:
                    line = self._serial.readline().decode()
                    if line == "ACK\r\n":
                        waiting = False
                        break
            if verbose:
                print(f"param {i} envoyé et reçu")
        #attend la confirmation finale
        waiting = True
        while waiting:
            while self._serial.in_waiting > 0:
                line = self._serial.readline().decode()
                if line == "DONE\r\n":
                    waiting = False
                    break
        self.resume_read_loop()
        if verbose:
            print("chargement paramètres terminé")
        return True

if __name__ == "__main__":
    interface = Prototype()
    time.sleep(0.002)
    interface.mode="COMMAND"
    time.sleep(0.002)
    interface.write_command(0.3)
    #interface.auto_identification(verbose=True)
    #interface.write_params(0.5, 1, 1, 1, verbose=True)
    interface.start_read_loop()
    try:
        fifo = CSVWriter("echelon_0V3.csv")
        while True:
            if interface.mode == "IDLE":
                mode = input("Mode: ")
                if mode == "LOG":
                    interface.change_FIFO(fifo)
                    mode = "COMMAND"
                interface.mode = mode
            elif interface.mode == "COMMAND":
                cmd = float(input("Cmd: "))
                try:
                    interface.write_command(cmd)
                except ValueError:
                    interface.change_FIFO(fifo)
                    interface.write_command(0)
            elif interface.mode == "REGUL":
                cmd = float(input("Cons: "))
                try:
                    interface.write_command(cmd)
                except ValueError:
                    interface.mode = "IDLE"
    except KeyboardInterrupt:
        interface.stop_read_loop()
        interface._serial.close()