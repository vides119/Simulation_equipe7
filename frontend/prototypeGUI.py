import csv
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
import time
from pathlib import Path
from tkinter import messagebox
from PIL import Image
from backend.Prototype.Prototype import CSVWriter
import backend.fileOperations as fileOperations
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class PrototypeScrollableFrame(customtkinter.CTkScrollableFrame): # Corps de la page
    """Classe representant le corps de la page de l'interface graphique pour le prototype"""
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1) # Limite le cadran des boutons load et save

        
        self.data = {} # Les données à récupérer à l'écran
        self.dict_param_affichage = {} # Les données à afficher à l'écran

        # Bloc température de la plaque
        self.thermistances_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.thermistances_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew", rowspan=2)
        self.thermistances_frame.grid_columnconfigure(0, weight=1)

        label_thermistances = customtkinter.CTkLabel(
            self.thermistances_frame,
            text="Commande et température des thermistances",
            font=("Aptos Serif", 16, "bold")
        )
        label_thermistances.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc params
        self.parametres_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.parametres_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.parametres_frame.grid_columnconfigure(0, weight=1)

        label_parametres = customtkinter.CTkLabel(
            self.parametres_frame,
            text="Paramètres du régulateur",
            font=("Aptos Serif", 16, "bold")
        )
        label_parametres.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc boutons load et save
        self.save_load_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.save_load_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.save_load_frame.grid_columnconfigure(0, weight=1)

        # Bloc pour le graphique
        self.graphe_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=0)
        self.graphe_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
        self.graphe_frame.grid_columnconfigure(0, weight=1)

        # Ajout des paramètres à afficher à l'écran
        for i, value in enumerate(master.param_affichage):
            label = customtkinter.CTkLabel(self.thermistances_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.grid(row=i*2 + 1, column=0, padx=20, pady=(10,0), sticky="w")

            # Pour customiser les champs d'affichage
            textbox_frame = customtkinter.CTkFrame(self.thermistances_frame, fg_color="transparent")
            textbox_frame.grid(row=i*2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

            textbox = customtkinter.CTkTextbox(
                textbox_frame,
                height=35,
                border_width=0.5,
                bg_color="transparent",
                border_color="#484a4a",
                font=("Aptos Serif", 12),
                corner_radius=5
            )
            textbox.delete("0.0", "end")
            textbox.insert("0.0", "...")
            textbox.pack(fill="x", padx=10)

            # Ajout à la liste
            self.dict_param_affichage[value] = textbox

        # Ajout des paramètres à récupérer à l'écran
        for i, value in enumerate(master.parametres):
            label = customtkinter.CTkLabel(self.parametres_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.grid(row=i*2 + 1, column=0, padx=20, pady=(10,0), sticky="w")

            # Pour customiser les champs de saisie
            entry_frame = customtkinter.CTkFrame(self.parametres_frame, fg_color="transparent")
            entry_frame.grid(row=i*2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

            entry = customtkinter.CTkEntry(
                entry_frame,
                height=35,
                border_width=0.5,
                bg_color="transparent",
                border_color="#484a4a",
                font=("Aptos Serif", 12),
                corner_radius=5,
                placeholder_text="..."
            )
            entry.pack(fill="x", padx=10)

            # Ajout à la liste
            self.data[value] = entry
        
        # Valeurs par défaut
        default ={
            "Période d'échantillonnage [s]": "1",
            "Kp [-]": "0.2327",
            "Ki [-]": "0.001504",
            "Kd [-]": "4.5",
            "N [-]": "2.668",
            "Température ambiante [°C]": "23.7"
        }
        self.setEntries(default)
    
    def getData(self): # Retourne le dictionnaire label + entry
        return self.data
    
    def getChampsThermistances(self):
        return self.dict_param_affichage
    
    def setEntries(self, data): # Permet de modifier chaque entry grace au fichier JSON
        for label, entry in self.data.items():
            entry.delete(0, customtkinter.END)
            entry.insert(0, data.get(label, ""))
    
    def setChampsThermistances(self, dict_param_affichage):
        for label, textbox in self.dict_param_affichage.items():
            textbox.delete("0.0", "end")
            textbox.insert("0.0", dict_param_affichage.get(label, ""))

    def emptyEntries(self): # Verifie si des champs sont vides
        for entry in self.data.values():
            if entry.get() == "":
                return True
        return False
    
    def validateEntries(self): # Verifie si les champs sont des float
        invalid_fields = []
        for label, entry in self.data.items():
            try:
                v = float(entry.get())
            except ValueError:
                invalid_fields.append(label)
                entry.configure(border_color="red") # Marquer en rouge les champs incorrects
            else:
                if v < 0:
                    invalid_fields.append(label)
                    entry.configure(border_color="red") # Marquer en rouge les champs incorrects
                else:
                    entry.configure(border_color="#616161") # Remettre la couleur
        return invalid_fields
    
    def invalid_or_empty(self): # Appelle les deux fonctions de verification pour checker si tout est bon
        invalid_fields = self.validateEntries() # Colorie en rouge si champ incorrect

        if self.emptyEntries():
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs!")
            return True
        elif invalid_fields:
            error_message = "Les champs suivants contiennent des valeurs incorrectes :\n"
            error_message += "\n".join(invalid_fields)
            messagebox.showerror("Erreur", error_message)
            return True
    
        return False



class PrototypeGUI(customtkinter.CTkToplevel): # Fenetre principale
    """Classe representant l'interface graphique pour le prototype"""
    def __init__(self, parent, prototype, theme, title, parametres, param_affichage):
        super().__init__(parent)
        # Initialise du prototype et met le thread de lecture en pause
        self.prototype = prototype # Il est fait dans la fenetre principale pour eviter la duplication de thread
        self.prototype.pause_read_loop()

        self.parent = parent  # Stocke la référence à la fenêtre principale
        self.current_theme = theme  # Stocker le thème actuel
        self.title_header = title # Stocker le texte d'entete de la fenetre
        self.parametres = parametres
        self.param_affichage = param_affichage
        self.en_marche = False
        self.FIFO_charge = False
        self.first_update = True
        self.exporter = False
        self.first_data_to_export = True # Permet d'ajuster la colonne du temps dans l'exportation par rapport au temps de la 1e valeur
        self.start_export_time = 0.0
        self.range_time = 120 # Pour que la courbe glisse et affiche les donnees dans un range de 2 minutes
        self.filename = self.makeFileName() # Servira pour l'enregistrement
        self.FIFO = CSVWriter()
        self.temps_moyennage = 60 # On fait la moyenne sur les valeurs qui correspondent à 1 minute puis elle est coulissante
        self.taille_echantillon = int(self.temps_moyennage) # Valeur par defaut pour la taille echantillonnale du calcul de stabilité (60 secondes // Période d'echantillonnage)
        self.echantillon = np.zeros(self.taille_echantillon) # Tableau numpy qu'on va utiliser de facon circulaire pour trouver l'ecart-type
        self.index_circulaire = 0 # Pour parcourir le tableau echantillonnal
        self.echantillon_full = False  # Indique si le tableau d'echantillon est rempli une première fois
        self.previous_time_update = -10.0 # Pour eviter que le thread update lise les memes lignes plusieurs fois (le thread tourne plus vite que l'Arduino)
        self.previous_time_stability = -10.0 # Pour eviter que le thread update lise les memes lignes plusieurs fois (le thread tournent plus vite que l'Arduino)
        self.protocol("WM_DELETE_WINDOW", self.on_close) # Détection de la fermeture de la fenêtre

        self.title("")
        self.geometry("900x700")
        self.parent.iconify()
        self.state('zoomed')
        self.minsize(800,550)
        self.grid_rowconfigure((0,2), weight=0) # Ligne d'en-tête
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        # En-tête (Contient 2 colonnes, titre + thème de couleur)
        self.header_frame = customtkinter.CTkFrame(self, fg_color="#484a4a", corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="ew", columnspan=2)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1) # Colonne du titre
        self.header_frame.grid_columnconfigure(1, weight=0) # Colonne thème de couleur

        # Titre
        self.label_title = customtkinter.CTkLabel(
            self.header_frame, 
            text=self.title_header, 
            font=("Aptos Serif", 14), 
            padx = 20, 
            text_color="white"
        )
        self.label_title.grid(row=0, column=0, padx=10, pady=10 ,sticky="w")

        # Charger les images pour le theme de la fenetre
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

        self.update_theme_buttons(theme)  # Initialiser le bon état

        # Contenu de la fenetre
        self.scrollable_body_frame = PrototypeScrollableFrame(self) # Instance du corps de la page
        self.scrollable_body_frame.grid(row=1, column=0, padx=10, pady=(10,0), sticky="nsew", columnspan=2)

        # Conteneur boutons save et load 
        save_load_button_frame = customtkinter.CTkFrame(self.scrollable_body_frame.save_load_frame, fg_color="transparent")
        save_load_button_frame.grid(row=0, column=0, padx=(10,10) ,columnspan=2, pady=10, sticky="nsew")
        save_load_button_frame.grid_columnconfigure(0, weight=1)
        save_load_button_frame.grid_columnconfigure(1, weight=1)
        
        self.load_button = customtkinter.CTkButton(save_load_button_frame, text="Charger", command=self.load_file, height=35, fg_color="#3d7cf2")
        self.load_button.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.save_button = customtkinter.CTkButton(save_load_button_frame, text="Enregistrer", command=self.save_file, height=35, fg_color="#3d7cf2")
        self.save_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Ajouter un cadre pour afficher la figure Matplotlib
        self.plot_frame = customtkinter.CTkFrame(self.scrollable_body_frame.graphe_frame, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.plot_frame.grid(row=0, column=0, padx=0, pady=20, sticky="nsew")
        
        # Reveiller le thread de lecture du port serie et le faire attendre
        if not parent.port_ouvert:
            self.prototype.start_read_loop()
            self.prototype.pause_read_loop()
        else:
            self.prototype.resume_read_loop()
            self.prototype.pause_read_loop()
        
        # Initialisation du graphique
        self.init_plot()  

        # Ajouter le cadre de la partie interactive
        self.commande_consigne_frame = customtkinter.CTkFrame(self.scrollable_body_frame.graphe_frame, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.commande_consigne_frame.grid(row=0, column=1, padx=(20,0), pady=20, sticky="nsew")
        self.commande_consigne_frame.grid_columnconfigure(0, weight=1)

        # Titre partie interactive
        label_graphe = customtkinter.CTkLabel(
            self.commande_consigne_frame,
            text="Partie interactive",
            font=("Aptos Serif", 16, "bold")
        )
        label_graphe.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Indicateur de stabilité
        self.stabilite_frame = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.stabilite_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.stabilite_frame.columnconfigure(0, weight=1)
        self.radio_var = customtkinter.IntVar(value=1)
        self.indicateur_stabilite = customtkinter.CTkRadioButton(self.stabilite_frame, text="Stabilité", fg_color="#cc2328", hover_color="#cc2328", variable=self.radio_var,value=1)
        self.indicateur_stabilite.grid(row=0, column=0, padx=35 ,sticky="n")

        # Ajouter le champ consigne à coté du graphique
        self.label1 = customtkinter.CTkLabel(self.commande_consigne_frame, text="Commande [V]", font=("Aptos Serif", 14, "bold"))
        self.label1.grid(row=2, column=0, padx=20, sticky="n")
        self.entry_frame1 = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.entry_frame1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.commande = customtkinter.CTkEntry(
            self.entry_frame1,
            height=35,
            border_width=0.5,
            bg_color="transparent",
            border_color="#484a4a",
            font=("Aptos Serif", 12),
            corner_radius=5,
            placeholder_text="..."
        )
        self.commande.pack(fill="x", padx=10)
        self.commande.delete(0, customtkinter.END)
        self.commande.insert(0, 0.5) # Valeur par defaut

        # Ajouter le champ consigne à coté du graphique
        self.label2 = customtkinter.CTkLabel(self.commande_consigne_frame, text="Consigne [°C]", font=("Aptos Serif", 14, "bold"))
        self.label2.grid(row=4, column=0, padx=20, sticky="n")
        self.entry_frame2 = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.entry_frame2.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.consigne = customtkinter.CTkEntry(
            self.entry_frame2,
            height=35,
            border_width=0.5,
            bg_color="transparent",
            border_color="#484a4a",
            font=("Aptos Serif", 12),
            corner_radius=5,
            placeholder_text="..."
        )
        self.consigne.pack(fill="x", padx=10)
        self.consigne.delete(0, customtkinter.END)
        self.consigne.insert(0, 25) # Valeur par defaut

        # Le mode du prototype
        self.mode_frame = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.mode_frame.grid(row=6, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.mode_prototype = customtkinter.CTkSegmentedButton(self.mode_frame, values=["Commande", "Consigne"], height=40, selected_color="#3d7cf2")
        self.mode_prototype.pack(fill="x", padx=10)
        self.mode_prototype.set("Commande")

        # Bouton pour envoyer le mode et la valeur à l'Arduino
        self.send_frame = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.send_frame.grid(row=7, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.send_button = customtkinter.CTkButton(self.send_frame, text="Envoyer", command=self.interagir, height=40, fg_color="#3d7cf2")
        self.send_button.pack(fill="x", padx=10)

        # Bouton commencer l'enregistrement dans un fichier csv
        self.exporter_frame = customtkinter.CTkFrame(self.commande_consigne_frame, fg_color="transparent")
        self.exporter_frame.grid(row=8, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.exporter_button = customtkinter.CTkButton(self.exporter_frame, text="Exporter", command=self.start_exporter, height=40, fg_color="#3d7cf2")
        self.exporter_button.pack(fill="x", padx=10)

        # Conteneur boutons
        self.export_run_button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.export_run_button_frame.grid(row=2, column=0, pady=10, sticky="ew", columnspan=2)
        self.export_run_button_frame.grid_columnconfigure(0, weight=1)

        # Sous-frame boutons
        self.button_container = customtkinter.CTkFrame(self.export_run_button_frame, fg_color="transparent")
        self.button_container.grid(row=0, column=0, sticky="e", padx=(0,35),pady=10)
        self.button_container.grid_columnconfigure((0, 1, 2), weight=1)

        # Bouton Calibrer
        self.run_button = customtkinter.CTkButton(self.button_container, text="Calibrer", command=self.calibrer, height=40, fg_color="#1160f2")
        self.run_button.grid(row=0, column=0, padx=(10,0), pady=10)

        # Bouton Arreter
        self.arret_button = customtkinter.CTkButton(self.button_container, text="Arrêter", command=self.arret, height=40, fg_color="#cc2328", hover_color="#662628")
        self.arret_button.grid(row=0, column=1, padx=(10,0), pady=10)

        # Bouton Lancer
        self.run_button = customtkinter.CTkButton(self.button_container, text="Démarrer", command=self.lancer_proto, height=40, fg_color="#35cf30", hover_color="#286926")
        self.run_button.grid(row=0, column=2, padx=(10,0), pady=10)

    
    def set_theme(self, theme):
        """Permet de changer le thème des fenetres"""
        self.current_theme = theme
        customtkinter.set_appearance_mode(theme)
        self.update_theme_buttons(theme)

        # Changer aussi chez le parent
        if hasattr(self.parent, 'set_theme'):
            self.parent.set_theme(theme)
    
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
        self.label_title.configure(text_color="#2b2a2a" if theme == "Light" else "white")
        self.header_frame.configure(fg_color="#c7c1c1" if theme == "Light" else "#484a4a")

    def save_file(self):
        """Permet de sauvegarder les paramètres dans un fichier JSON"""
        self.parent.iconify()
        fileOperations.save_file(data_owner=self.scrollable_body_frame)

    def load_file(self):
        """Permet d'ouvir le fichier JSON et charger les données"""
        self.parent.iconify()
        fileOperations.load_file(data_owner=self.scrollable_body_frame)
    
    def start_exporter(self):
        """Permet de lancer l'exportation des données du graphe vers un fichier csv"""
        self.parent.iconify()
        if self.en_marche:
            if not self.exporter:
                self.filename = self.makeFileName()
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    if self.prototype.mode == "COMMAND":
                        writer.writerow(["temps", "Commande", "t1", "t2", "t3", "t3_pred"])
                    else:
                        writer.writerow(["temps", "Consigne" ,"Commande", "t1", "t2", "t3", "t3_pred"])
                self.exporter = True
                messagebox.showinfo("Info", f"Enregistrement en temps réel dans {self.filename}")
            else:
                messagebox.showinfo("Info", f"Opération déjà en cours dans {self.filename}")
        else:
            messagebox.showinfo("Info", "Opération impossible!\nVeuillez d'abord démarrer l'enemble.")
    
    def lancer_proto(self): # Fonction pour lancer le protoype
        """Permet de démarrer le prototype"""
        self.parent.iconify()
        
        if not self.parent.get_calibration_done(): # Si on a jamais calibré le proto et on veut quand meme demarrer
            messagebox.showwarning("Warning", "Veuillez d'abord partir la calibration pour le prototype !")
            return False
        
        self.commande.configure(border_color="#616161") # Remettre la couleur
        self.consigne.configure(border_color="#616161") # Remettre la couleur
        if self.scrollable_body_frame.invalid_or_empty():
            pass # Toutes les actions de verification des champs sont faites dans la fonction du if
        else:
            if not self.en_marche: # Il faut stopper la simulation avant de pourvoir demarrer à nouveau
                mode = "COMMAND" if self.mode_prototype.get() == "Commande" else "REGUL"
                if mode == "COMMAND":
                    if not self.validate_commande():
                        self.commande.configure(border_color="red")
                        messagebox.showerror("Erreur", "Veuillez saisir une commande correcte !")
                        return False
                    commande = float(self.commande.get())
                    if commande < -1 or commande > 1:
                        self.commande.configure(border_color="red")
                        self.en_marche = False
                        messagebox.showerror("Erreur", "La commande doit être entre -1W et 1W")
                        return False
                else:
                    if not self.validate_consigne():
                        self.consigne.configure(border_color="red")
                        messagebox.showerror("Erreur", "Veuillez saisir une consigne correcte !")
                        return False
                    consigne = float(self.consigne.get())
                    if consigne < 20 or consigne > 30:
                        self.consigne.configure(border_color="red")
                        self.en_marche = False
                        messagebox.showerror("Erreur", "La consigne doit être entre 20°C et 30°C")
                        return False
                
                data = self.scrollable_body_frame.getData()
                param1 = float(data["Période d'échantillonnage [s]"].get())
                param2 = float(data["Kp [-]"].get())
                param3 = float(data["Ki [-]"].get())
                param4 = float(data["Kd [-]"].get())
                param5 = float(data["N [-]"].get())
                param6 = float(data["Température ambiante [°C]"].get())
                self.prototype.write_params(param1, param2, param3, param4, param5, param6, verbose=True)
                self.en_marche = self.envoyer_mode() # True si tout est bon sinon False donc pas de demarrage
                
                if self.en_marche: # On charge le FIFO si on est dans un mode de lecture
                    self.prototype.change_FIFO(self.FIFO)
                    self.prototype.resume_read_loop()
                    time.sleep(0.1) # On attend pour etre certain que le thread qui trace la courbe aura les données correctes
                    self.taille_echantillon = int(self.temps_moyennage // param1) # Division entiere entre le temps de moyennage et la periode d'echantillonnage pour avoir le nbre d'entrees qu'on aura en 1minute
                    self.echantillon = np.zeros(self.taille_echantillon)
                    self.FIFO_charge = True # Le thread qui trace la courbe peut commencer ainsi que celui qui s'occupe de controler la stabilité
                else:
                    messagebox.showerror("Erreur", "Echec du démarrage!\nVeuillez vétifier le mode.")
    
    def arret(self): # Fonction qui arrete tout
        """Stoppe l'animation en temps réel et réinitialise tout"""
        if self.en_marche:
            self.parent.iconify()
            print("Arret prototype...")
            self.indicateur_stabilite.configure(fg_color="#cc2328", hover_color="#cc2328")
            self.en_marche = False # Met en pause la fonction du thread qui trace la courbe et celui de la stabilité
            self.FIFO_charge = False # Met en pause la fonction du thread qui trace la courbe et celui de la stabilité
            self.index_circulaire = 0
            self.echantillon_full = False 
            self.prototype.pause_read_loop()
            self.prototype.mode = "IDLE"
            self.FIFO.reset_data()
            self.first_update = True
            self.previous_time_update = -10.0
            self.previous_time_stability = -10.0
            if self.exporter:
                self.exporter = False
                self.first_data_to_export = True
                messagebox.showinfo("Info", f"Exportation complétée avec succès à {self.filename}")
            self.reset_plot()

    def interagir(self):
        """Permet d'envoyer une valeur de commande ou consigne en temps réel"""
        self.commande.configure(border_color="#616161") # Remettre la couleur
        self.consigne.configure(border_color="#616161") # Remettre la couleur
        if not self.en_marche:
            messagebox.showinfo("Info", "Opération impossible!\nVeuillez d'abord démarrer l'enemble.")
        else:
            mode = "COMMAND" if self.mode_prototype.get() == "Commande" else "REGUL"
            if mode != self.prototype.mode:
                messagebox.showinfo("Info", "Le mode intéractif s'applique pour le mode au démarrage.\nPour changer de mode veuillez cliquer sur arrêter puis reprendre avec le nouveau mode.")
                self.mode_prototype.set("Consigne") if mode == "COMMAND" else self.mode_prototype.set("Commande")
            elif mode == "COMMAND":
                if not self.validate_commande():
                    self.commande.configure(border_color="red")
                    messagebox.showinfo("Info", "Veuillez saisir une commande correcte !")
                else:
                    commande = float(self.commande.get())
                    if commande < -1 or commande > 1:
                        self.commande.configure(border_color="red")
                        messagebox.showinfo("Info", "La commande doit être entre -1V et 1V")
                    else:
                        self.envoyer_mode()
            elif mode == "REGUL":
                if not self.validate_consigne():
                    self.consigne.configure(border_color="red")
                    messagebox.showinfo("Info", "Veuillez saisir une consigne correcte !")
                else:
                    consigne = float(self.consigne.get())
                    if consigne < 20 or consigne > 30:
                        self.consigne.configure(border_color="red")
                        messagebox.showinfo("Info", "La consigne doit être entre 20°C et 30°C")
                    else:
                        self.envoyer_mode()
    
    def envoyer_mode(self):
        """Envoie le mode et la commande si on est en mode commande et fait pareil si c'est la consigne"""
        self.parent.iconify()

        mode = "COMMAND" if self.mode_prototype.get() == "Commande" else "REGUL"
        if mode == "COMMAND":
            commande = float(self.commande.get())
            if self.prototype.mode != mode:
                self.prototype.mode = mode
            self.prototype.write_command(commande)
            return True
        else:
            consigne = float(self.consigne.get())
            if self.prototype.mode != mode:
                self.prototype.mode = mode
            self.prototype.write_consigne(consigne)
            return True
        
    def calibrer(self):
        """Effectue le calcul de calibration pour les amplificateurs"""
        self.parent.iconify()
        if not self.en_marche:
            messagebox.showwarning("Warning", "Assurez de monter les interrupteurs sur le prototype!\nSi c'est fait cliquez sur OK pour commencer et attendez la fin de l'opération.")
            self.prototype.auto_identification(verbose=True)
            self.parent.set_calibration_done(True)
            messagebox.showwarning("Warning", "Calibration complétée avec succès.\nAssurez vous de ramener les interrupteurs à leur position intiale!\nSi c'est fait cliquez sur OK pour terminer.")
        else:
            messagebox.showinfo("Info", "Impossible d'effectuer l'opération !\nVeuillez d'abord cliquer sur arrêter.")
    
    def init_plot(self):
        """Initialise le graphique Matplotlib dans l'interface."""
        plt.style.use('default')
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, figsize=(5, 6), sharex=True,  gridspec_kw={'height_ratios': [2, 1]})
        self.fig.subplots_adjust(hspace=0.3)

        # Ajouter un titre et des labels pour les axes
        self.ax1.set_title("Évolution de la température aux thermistances et de la commande")
        self.ax1.set_xlabel("Temps (s)")
        self.ax1.set_ylabel("Températures (°C)")
        self.ax1.xaxis.set_tick_params(labelbottom=True)
        self.ax2.set_xlabel("Temps (s)")
        self.ax2.set_ylabel("Commande (V)")


        # Initialiser les courbes (ligne pour chaque paramètre)
        self.line_t0, = self.ax1.plot([], [], 'c-', label="Température t1 (°C)")
        self.line_t1, = self.ax1.plot([], [], 'b-', label="Température t2 (°C)")
        self.line_t2, = self.ax1.plot([], [], 'g-', label="Température t3 (°C)")
        self.line_pred_t2, = self.ax1.plot([], [], 'y-', label="Température prédite (°C)")
        self.line_commande, = self.ax2.plot([], [], 'r-')

        # Marquer la légende
        self.ax1.legend()

        # Intégrer le graphique Matplotlib sur la fenetre
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # Initialisation des listes de données du graphique
        self.x_data = []
        self.y_data_commande = []
        self.y_data_t0 = []
        self.y_data_t1 = []
        self.y_data_t2 = []
        self.y_data_pred_t2 = []
        self.start_time = 0.0
    
    def on_close(self):
        """Arrête la mise à jour du graphique et ferme proprement la fenêtre."""
        if self.en_marche:
            messagebox.showwarning("Warning", "Un travail est en cours!\nRassurez vous d'avoir arrêté pour fermer la fenêtre.")
        else:
            self.parent.deiconify()  # Restaurer la fenêtre principale
            plt.close(self.fig)  # Ferme la figure Matplotlib pour éviter l'erreur
            self.destroy()  # Détruit la fenêtre customTkinter
        

    def update_plot(self):
        """Mise à jour du graphique en temps réel."""
        if self.en_marche and self.FIFO_charge:
            data = self.FIFO.get_data().copy()
            if -10.0 not in data.values(): # On se rassure que les donnees sont deja toutes disponibles
                if self.previous_time_update != data["temps"]:
                    self.previous_time_update = data["temps"]
                    if self.first_update:
                        self.start_time = data["temps"]
                        self.first_update = False
                    
                    # Temps pour l'axe des temps
                    current_time = data["temps"] - self.start_time

                    # Mettre à jour les champs d'affichage des temperatures aux thermistances et la commande envoyée
                    self.scrollable_body_frame.dict_param_affichage["Commande [V]"].delete("0.0", "end")
                    self.scrollable_body_frame.dict_param_affichage["Commande [V]"].insert("0.0", f"{data['command']:.2f}")

                    self.scrollable_body_frame.dict_param_affichage["Thermistance 1 [°C]"].delete("0.0", "end")
                    self.scrollable_body_frame.dict_param_affichage["Thermistance 1 [°C]"].insert("0.0", f"{data['t0']:.2f}")

                    self.scrollable_body_frame.dict_param_affichage["Thermistance 2 [°C]"].delete("0.0", "end")
                    self.scrollable_body_frame.dict_param_affichage["Thermistance 2 [°C]"].insert("0.0", f"{data['t1']:.2f}")

                    self.scrollable_body_frame.dict_param_affichage["Thermistance 3 [°C]"].delete("0.0", "end")
                    self.scrollable_body_frame.dict_param_affichage["Thermistance 3 [°C]"].insert("0.0", f"{data['t2']:.2f}")

                    self.scrollable_body_frame.dict_param_affichage["Température prédite [°C]"].delete("0.0", "end")
                    self.scrollable_body_frame.dict_param_affichage["Température prédite [°C]"].insert("0.0", f"{data['pred_t2']:.2f}")

                    # Ajouter les nouvelles données à la liste
                    self.x_data.append(current_time)
                    self.y_data_commande.append(data["command"])
                    self.y_data_t0.append(data["t0"])
                    self.y_data_t1.append(data["t1"])
                    self.y_data_t2.append(data["t2"])
                    self.y_data_pred_t2.append(data["pred_t2"])

                    # Supprimer les anciennes valeurs pour rester dans le range de 2 minutes (courbe glissante)
                    if self.x_data and (self.x_data[-1] - self.x_data[0]) > self.range_time:
                        self.x_data.pop(0)
                        self.y_data_commande.pop(0)
                        self.y_data_t0.pop(0)
                        self.y_data_t1.pop(0)
                        self.y_data_t2.pop(0)
                        self.y_data_pred_t2.pop(0)

                    # Mettre à jour les courbes
                    self.line_commande.set_data(self.x_data, self.y_data_commande)
                    self.line_t0.set_data(self.x_data, self.y_data_t0)
                    self.line_t1.set_data(self.x_data, self.y_data_t1)
                    self.line_t2.set_data(self.x_data, self.y_data_t2)
                    self.line_pred_t2.set_data(self.x_data, self.y_data_pred_t2)

                    # Ajuster les limites du graphique
                    self.ax1.relim()
                    self.ax1.autoscale_view()
                    self.ax2.relim()
                    self.ax2.autoscale_view()
                    self.canvas.draw()

                    # Écriture des données dans le fichier CSV si on a cliqué sur le bouton exporter
                    if self.exporter:
                        if self.first_data_to_export:
                            self.start_export_time = data["temps"] # Pour ramener le debut du temps dans le fichier d'exportation à 0s
                            self.first_data_to_export = False
                        t = data["temps"] - self.start_export_time
                        with open(self.filename, mode="a", newline="") as file:
                            writer = csv.writer(file)
                            if self.prototype.mode == "COMMAND":
                                writer.writerow([round(t,ndigits=3), data["command"], data["t0"], data["t1"], data["t2"], data["pred_t2"]])
                            else:
                                writer.writerow([round(t,ndigits=3), data["consigne"], data["command"], data["t0"], data["t1"], data["t2"], data["pred_t2"]])
                        
    
    def update_stability(self):
        """Calcul de l'ecart-type et mise à jours du voyant de stabilité en temps réel."""
        if self.en_marche and self.FIFO_charge:
            if self.prototype.mode != "COMMAND": # Le calcul de stabilité ne se fait pas en mode commande
                data = self.FIFO.get_data().copy()
                if -10.0 != data["t2"]: # On se rassure que la donnée est deja disponible
                    if self.previous_time_stability != data["temps"]:
                        self.previous_time_stability = data["temps"]
                        self.echantillon[self.index_circulaire] = data["t2"] # On remplace l'ancienne valeur
                        self.index_circulaire = (self.index_circulaire + 1) % self.taille_echantillon

                        if not self.echantillon_full and self.index_circulaire == 0:
                            self.echantillon_full = True # Le tableau est plein (on a tout pour débuter le calcul)
                        
                        if self.echantillon_full:
                            ecart_type = np.std(self.echantillon, ddof=1) # Calcul de l'ecart-type echantillonnal
                            if ecart_type <= 0.1: # Spec du cahier des charges
                                self.indicateur_stabilite.configure(fg_color="#35cf30", hover_color="#35cf30") # Allumer le voyant de stabilité en vert
                            else:
                                self.indicateur_stabilite.configure(fg_color="#cc2328", hover_color="#cc2328") # Marquer le voyant en rouge
              

    def reset_plot(self):
        """Réinitialise le graphique pour un nouveau départ."""
        # Effacer les listes de données
        self.x_data.clear()
        self.y_data_commande.clear()
        self.y_data_t0.clear()
        self.y_data_t1.clear()
        self.y_data_t2.clear()
        self.y_data_pred_t2.clear()

        # Réinitialiser les courbes avec des listes vides
        self.line_commande.set_data([], [])
        self.line_t0.set_data([], [])
        self.line_t1.set_data([], [])
        self.line_t2.set_data([], [])
        self.line_pred_t2.set_data([], [])

        # Réinitialiser les axes et redessiner
        self.ax1.relim()
        self.ax1.autoscale_view()
        self.ax2.relim()
        self.ax2.autoscale_view()
        self.canvas.draw()

        # Réinitialiser le temps de départ
        self.start_time = 0.0
    
    def makeFileName(self):
        """Construit le nom du fichier d'enregistrement avec la date et l'heure actuelles"""
        home = Path.home()
        documents_dir = home / "Documents"
        dossier = documents_dir / "Prototype"
        dossier.mkdir(parents=True, exist_ok=True)  # Crée le dossier s'il n'existe pas

        temps_actuel = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        return dossier / f"proto_data {temps_actuel}.csv"
    
    def validate_consigne(self):
        """Permet de verifier que la commande saisie est correcte"""
        try:
            float(self.consigne.get())
        except ValueError:
            return False
        return True
    
    def validate_commande(self):
        """Permet de verifier que la commande saisie est correcte"""
        try:
            float(self.commande.get())
        except ValueError:
            return False
        return True
    