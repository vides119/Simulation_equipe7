import threading
import time
import customtkinter
import serial
from tkinter import messagebox
from PIL import Image
from frontend.simulationGUI import SimulationGUI
from frontend.prototypeGUI import PrototypeGUI
from backend.Prototype.Prototype import Prototype

class homeApp(customtkinter.CTk):
    """ Fenetre principale du programme """
    def __init__(self):
        super().__init__()
        self.current_theme = "Dark" # Peut etre "Light" ou "Dark" ou "system"
        self.port_ouvert = False
        self.simulation_ouvert = False
        self.en_cours = False # Pour faire tourner la fonction du thread seulement si la fenetre prototype s'ouvre
        self.calibration_done = False
        self.stop_event = threading.Event()

        # Détection de la fermeture de la fenêtre
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.title("")
        self.geometry("700x500")
        self.minsize(650,450)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=2)

        # En-tête (barre de titre)
        self.header_frame = customtkinter.CTkFrame(self, fg_color="#484a4a", corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)

        # Titre
        self.label_title = customtkinter.CTkLabel(
            self.header_frame, 
            text="ACCUEIL", 
            font=("Aptos Serif", 14), 
            padx=20, 
            text_color="white"
        )
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Mot d'acceuil
        self.label_welcome = customtkinter.CTkLabel(
            self,
            text="BIENVENUE!", 
            font=("Aptos Serif", 35), 
            padx=20, 
            text_color="white"
        )
        self.label_welcome.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Charger les images pour le thème
        self.light_image = customtkinter.CTkImage(Image.open("frontend/icons/light.png"), size=(20, 20))
        self.dark_image = customtkinter.CTkImage(Image.open("frontend/icons/dark.png"), size=(20, 20))
        self.auto_image = customtkinter.CTkImage(Image.open("frontend/icons/auto.png"), size=(20, 20))

        # Boutons de thème
        self.light_theme_button = customtkinter.CTkButton(
            self.header_frame, image=self.light_image, text="", width=30, height=30,
            fg_color="transparent", hover_color="#484a4a",
            command=lambda: self.set_theme("Light")
        )
        self.light_theme_button.grid(row=0, column=1, padx=(0, 15), sticky="e")

        self.dark_theme_button = customtkinter.CTkButton(
            self.header_frame, image=self.dark_image, text="", width=30, height=30,
            fg_color="transparent", hover_color="#484a4a",
            command=lambda: self.set_theme("Dark")
        )
        self.dark_theme_button.grid(row=0, column=2, padx=(0, 15), sticky="e")

        self.auto_theme_button = customtkinter.CTkButton(
            self.header_frame, image=self.auto_image, text="", width=30, height=30,
            fg_color="transparent", hover_color="#484a4a",
            command=lambda: self.set_theme("system")
        )
        self.auto_theme_button.grid(row=0, column=3, padx=(0, 35), sticky="e")
        customtkinter.set_appearance_mode(self.current_theme)
        self.update_theme_buttons(self.current_theme)  # Initialiser l'état

        # Conteneur pour centrer les boutons
        self.button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, sticky="nsew")
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Conteneur horizontal pour les trois boutons
        self.button_container = customtkinter.CTkFrame(self.button_frame, fg_color="transparent")
        self.button_container.pack(side="top", pady=60)

        # Boutons centrés pour choisir les options
        self.button1 = customtkinter.CTkButton(self.button_container, text="Simulation", command=self.open_simulation_window ,width=200, height=40, fg_color="#1160f2")
        self.button1.pack(side="left", padx=10)
        self.button2 = customtkinter.CTkButton(self.button_container, text="Prototype", command=self.open_prototype_window, width=200, height=40, fg_color="#1160f2")
        self.button2.pack(side="left", padx=10)

        # Cadre en dessous des boutons pour choisir le port Série
        self.label = customtkinter.CTkLabel(self.button_frame, text="Port série", font=("Aptos Serif", 14))
        self.label.pack(side="top")
        self.port_menu_frame = customtkinter.CTkFrame(self.button_frame, fg_color="transparent")
        self.port_menu_frame.pack(side="top") 
        self.portmenu = customtkinter.CTkOptionMenu(self.port_menu_frame, values=["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"], width=110, height=30, fg_color="#1160f2")
        self.portmenu.set("COM3")
        self.portmenu.pack(pady=5)

        # Représentent les deux fenetres enfants
        self.simulation_window = None
        self.protoype_window = None
    
    def set_calibration_done(self, val):
        """setter du param qui dit si on a deja calibé"""
        self.calibration_done = val
    
    def get_calibration_done(self):
        """getter du param qui dit si on a deja calibé"""
        return self.calibration_done

    def set_theme(self, theme):
        """ Pour changer le thème de la fenêtre """
        self.current_theme = theme
        customtkinter.set_appearance_mode(theme)
        self.update_theme_buttons(theme)

        # Appliquer le thème aux la fenêtres enfants si elles existent
        if self.simulation_window and self.simulation_window.winfo_exists():
            if self.current_theme != self.simulation_window.current_theme:
                self.simulation_window.set_theme(theme)
        
        if self.protoype_window and self.protoype_window.winfo_exists():
            if self.current_theme != self.protoype_window.current_theme:
                self.protoype_window.set_theme(theme)
    
    def update_theme_buttons(self, theme):
        """ Gère l'effet visuel des boutons si le thème change """
        default_fg = "transparent"
        black_fg = "#303030"
        light_fg = "#918d8d"
        
        self.light_theme_button.configure(
            fg_color=light_fg if theme == "Light" else default_fg,
            hover_color="#484a4a" if theme == "Light" else "#1f1d1d"
        )
        self.dark_theme_button.configure(
            fg_color=black_fg if theme == "Dark" else default_fg,
            hover_color="#484a4a" if theme == "Light" else "#1f1d1d"
        )
        self.auto_theme_button.configure(
            fg_color=black_fg if theme == "system" else default_fg,
            hover_color="#484a4a" if theme == "Light" else "#1f1d1d"
        )
        self.label_welcome.configure(text_color="black" if theme == "Light" else "white")
        self.label_title.configure(text_color="#2b2a2a" if theme == "Light" else "white")
        self.header_frame.configure(fg_color="#c7c1c1" if theme == "Light" else "#484a4a")

    def open_simulation_window(self):
        """ Permet d'ouvrir la fenetre de simulation """
        if self.simulation_window is None or not self.simulation_window.winfo_exists():
            # Parametres de configuration
            title = "SIMULATEUR DE TEMPERATURE DE LA PLAQUE"

            simulation_values =[
                "Durée [s]",
                "Température ambiante [°C]",
                "Coefficient de convection [W.m⁻².°C⁻¹]",
                "Maillage : x [-] , y [-]",
                "Facteur de temps [-]"
            ]

            plaque_values = [
                "Longueur [m]", 
                "Largeur [m]", 
                "Epaisseur [m]",
                "Chaleur spécifique [J.kg⁻¹.°C⁻¹]",
                "Densité [kg/m³]", 
                "Conductivité thermique [W.m⁻¹.°C⁻¹]"
            ]

            actuateur_values = [
                "Commande [W]",
                "Moment d'allumage [s]",
                "Durée [s]",
                "Position : x [m] , y [m]",
                "Dimension : x [m] , y [m]"
            ]

            pertubation_values = [
                "Valeur [W]",
                "Moment d'allumage [s]",
                "Durée [s]",
                "Position : x [m] , y [m]"
            ]

            thermistances_values = [
                "Thermistance 1 : x [m] , y [m]",
                "Thermistance 2 : x [m] , y [m]",
                "Thermistance 3 : x [m] , y [m]"
            ]

            self.simulation_window = SimulationGUI(self, self.current_theme, title, simulation_values, plaque_values, actuateur_values, pertubation_values, thermistances_values)
            self.simulation_window.focus()
            self.simulation_ouvert = True
        else:
            self.simulation_window.focus()  # Redonner le focus
            self.simulation_window.set_theme(self.current_theme) # Applique le thème actuel à la fenêtre enfant
    
    def open_prototype_window(self):
        """ Permet d'ouvrir la fenetre du prototype """
        if self.protoype_window is None or not self.protoype_window.winfo_exists():
            # Parametres de configuration
            title = "PROTOTYPE"

            parametres =[
                "Période d'échantillonnage [s]",
                "Kp [-]",
                "Ki [-]",
                "Kd [-]",
                "N [-]",
                "Température ambiante [°C]"
            ]

            param_affichage = [
                "Commande [V]",
                "Thermistance 1 [°C]", 
                "Thermistance 2 [°C]", 
                "Thermistance 3 [°C]",
                "Température prédite [°C]"
            ]

            port = self.portmenu.get()
            baud = 115200 # Baud rate du port série
            
            try:
                if not self.port_ouvert: #  Pour eviter de bloquer si on reouvre la fenetre apres fermeture car le port serie est toujours ouvert
                    self.serial = serial.Serial(port, baud) # Pour eviter d'echouer la creation de la fenetre si erreur
                    self.port = port
                    self.prototype = None#Prototype(serial=self.serial)
                if self.port != port: # Permet d'eviter dès de la 2e fois, que la fenetre s'ouvre alors qu'on selectionné le mauvais COM
                    pass#raise serial.SerialException
                
                # Creation de la fenetre
                self.protoype_window = PrototypeGUI(self, self.prototype, self.current_theme, title, parametres, param_affichage)
                self.protoype_window.focus()
                self.en_cours = True

                if not self.port_ouvert: # On part les threads du graphique et de la stabilité (situés ici pour éviter la duplication de thread à chaque ouverture de la fenetre)
                    self.update_plot_thread = threading.Thread(target=self.update_plot, daemon=True)
                    self.update_plot_thread.start()
                    self.update_stability_thread = threading.Thread(target=self.update_stability, daemon=True)
                    self.update_stability_thread.start()
                    
                print(self.update_plot_thread)
                print(self.update_stability_thread)
                self.port_ouvert = True
            except serial.SerialException:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir ce port série !")
        else:
            self.protoype_window.focus()  # Redonner le focus
            self.protoype_window.set_theme(self.current_theme) # Applique le thème actuel à la fenêtre enfant

    def update_plot(self):
        """Fonction du thread pour update les courbes"""
        while self.en_cours:
            if self.protoype_window.winfo_exists():
                self.protoype_window.update_plot()
            time.sleep(0.1)
    
    def update_stability(self):
        """Fonction du thread qui met à jour le voyant de stabilité"""
        while self.en_cours:
            if self.protoype_window.winfo_exists():
                self.protoype_window.update_stability()
            time.sleep(0.1)
            
    
    def on_close(self):
        """Arrête la mise à jour du graphique et ferme proprement la fenêtre."""
        if self.port_ouvert:
            if self.protoype_window.winfo_exists():
                messagebox.showerror("Error", "Veuillez d'abord terminer avec la fenêtre prototype.")
            elif self.simulation_ouvert:
                if not self.simulation_window.winfo_exists():
                    self.en_cours = False
                    self.stop_event.set()  # Signale au thread qui update de s'arrêter immédiatement
                    self.update_plot_thread.join()
                    print(self.update_plot_thread)
                    self.update_stability_thread.join()
                    print(self.update_stability_thread)
                    self.prototype.stop_read_loop() # Stopper le thread qui communique avec l'Arduino
                    self.prototype.change_FIFO(None)
                    self.prototype._read_loop_thread.join()
                    print(self.prototype._read_loop_thread)
                    self.serial.close()
                    self.destroy()  # Détruit la fenêtre customTkinter
                else:
                    messagebox.showerror("Error", "Veuillez d'abord terminer avec la fenêtre simulation.")
            else: # La simulation n'a pas été ouverte on peut fermer le tout
                self.en_cours = False
                self.stop_event.set()  # Signale au thread qui update de s'arrêter immédiatement
                self.update_plot_thread.join()
                print(self.update_plot_thread)
                self.update_stability_thread.join()
                print(self.update_stability_thread)
                self.prototype.stop_read_loop() # Stopper le thread qui communique avec l'Arduino
                self.prototype.change_FIFO(None)
                self.prototype._read_loop_thread.join()
                print(self.prototype._read_loop_thread)
                self.serial.close()
                self.destroy()  # Détruit la fenêtre customTkinter
        elif self.simulation_ouvert:
            if self.simulation_window.winfo_exists():
                messagebox.showerror("Error", "Veuillez d'abord terminer avec la fenêtre simulation.")
            else:
                self.destroy()  # Détruit la fenêtre customTkinter
        else: # Rien n'a été ouvert
            self.destroy()  # Détruit la fenêtre customTkinter