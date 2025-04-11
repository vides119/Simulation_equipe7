from pathlib import Path
from tkinter import messagebox
import customtkinter
from CTkToolTip import CTkToolTip
from PIL import Image
import backend.fileOperations as fileOperations
from backend.Simulateur3D.utils import Vecteur
from backend.Simulateur3D.Plaque import Plaque as Plq
import backend.Simulateur3D.Composantes as compt
from backend.Simulateur3D.Simulation import Simulation as Sim

class ScrollableBodyFrame(customtkinter.CTkScrollableFrame): # Corps de la page
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1) # Limite le cadran des boutons load et save

        # Les données à l'ecran
        self.data = {}

        # Bloc de l'actuateur
        self.actuateur_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.actuateur_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.actuateur_frame.grid_columnconfigure(0, weight=1)

        label_simulation = customtkinter.CTkLabel(
            self.actuateur_frame,
            text="Actuateur",
            font=("Aptos Serif", 16, "bold")
        )
        label_simulation.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc params simulation
        self.simulation_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.simulation_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.simulation_frame.grid_columnconfigure(0, weight=1)

        label_simulation = customtkinter.CTkLabel(
            self.simulation_frame,
            text="Paramètres de simulation",
            font=("Aptos Serif", 16, "bold")
        )
        label_simulation.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc de la pertubation
        self.pertubation_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.pertubation_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.pertubation_frame.grid_columnconfigure(0, weight=1)

        label_simulation = customtkinter.CTkLabel(
            self.pertubation_frame,
            text="Pertubation",
            font=("Aptos Serif", 16, "bold")
        )
        label_simulation.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc params de la plaque
        self.plaque_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.plaque_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.plaque_frame.grid_columnconfigure(0, weight=1)

        label_plaque = customtkinter.CTkLabel(
            self.plaque_frame,
            text="Plaque",
            font=("Aptos Serif", 16, "bold")
        )
        label_plaque.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc params thermistances
        self.thermistances_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.thermistances_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.thermistances_frame.grid_columnconfigure(0, weight=1)

        label_plaque = customtkinter.CTkLabel(
            self.thermistances_frame,
            text="Thermistances",
            font=("Aptos Serif", 16, "bold")
        )
        label_plaque.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Bloc des options
        self.options_frame = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#484a4a", border_width=1)
        self.options_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.options_frame.grid_columnconfigure(0, weight=1)

        label_plaque = customtkinter.CTkLabel(
            self.options_frame,
            text="Options",
            font=("Aptos Serif", 16, "bold")
        )
        label_plaque.grid(row=0, column=0, pady=(10,2), sticky="n")

        # Ajout des params de l'actuateur
        for i, value in enumerate(master.actuateur_values):
            label = customtkinter.CTkLabel(self.actuateur_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.grid(row=i*2 + 1, column=0, padx=20, pady=(10,0), sticky="w")

            if value == "Position : x [m] , y [m]" or value == "Dimension : x [m] , y [m]": # Champs avec 2 entry sur la meme ligne
                entry_frame = customtkinter.CTkFrame(self.actuateur_frame, fg_color="transparent")
                entry_frame.grid(row= i * 2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
                entry_frame.grid_columnconfigure((0, 1), weight=1)

                entry_x = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_x.grid(row=0, column=0, padx=(10, 5), sticky="ew")

                entry_y = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_y.grid(row=0, column=1, padx=(5, 10), sticky="ew")

                name_for_save = f"{value}".replace(" : x [m] , y [m]","")
                self.data[f"Actuateur {name_for_save}_x [m]"] = entry_x
                self.data[f"Actuateur {name_for_save}_y [m]"] = entry_y
            else:
                # Pour customiser les champs de saisie
                entry_frame = customtkinter.CTkFrame(self.actuateur_frame, fg_color="transparent")
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
                self.data[f"Actuateur {value}"] = entry
        
        # Ajout des params de la pertubation
        for i, value in enumerate(master.pertubation_values):
            label = customtkinter.CTkLabel(self.pertubation_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.grid(row=i*2 + 1, column=0, padx=20, pady=(10,0), sticky="w")

            if value == "Position : x [m] , y [m]": # Champs avec 2 entry sur la meme ligne
                entry_frame = customtkinter.CTkFrame(self.pertubation_frame, fg_color="transparent")
                entry_frame.grid(row= i * 2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
                entry_frame.grid_columnconfigure((0, 1), weight=1)

                entry_x = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_x.grid(row=0, column=0, padx=(10, 5), sticky="ew")

                entry_y = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_y.grid(row=0, column=1, padx=(5, 10), sticky="ew")

                name_for_save = f"{value}".replace(" : x [m] , y [m]","")
                self.data[f"Pertubation {name_for_save}_x [m]"] = entry_x
                self.data[f"Pertubation {name_for_save}_y [m]"] = entry_y
            else:
                # Pour customiser les champs de saisie
                entry_frame = customtkinter.CTkFrame(self.pertubation_frame, fg_color="transparent")
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
                self.data[f"Pertubation {value}"] = entry

        # Ajout des params de simulation
        for i, value in enumerate(master.simulation_values):
            label_frame = customtkinter.CTkFrame(self.simulation_frame, fg_color="transparent")
            label_frame.grid(row=i*2 + 1, column=0, columnspan=2, sticky="w", padx=20, pady=(10,0))

            label = customtkinter.CTkLabel(label_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.pack(side="left")

            if value == "Facteur de temps [-]": # Pour ajouter la bulle d'informations du facteur de temps
                question_mark = customtkinter.CTkLabel(
                    label_frame,
                    text="?",
                    width=22,
                    height=22,
                    font=("Aptos", 14, "bold"),
                    fg_color="#5a5a5a",
                    text_color="white",
                    corner_radius=12,
                )
                question_mark.pack(side="left", padx=(10, 0))

                CTkToolTip(
                    question_mark,
                    message="Le facteur de temps ajuste la vitesse de simulation.\nUne valeur plus petite = simulation plus rapide.\n Sa valeur est entre 3 et 10, en dessous de 3 la simulation devient instable.",
                    delay=0.2
                )

            if value == "Maillage : x [-] , y [-]": # Champs avec 2 entry sur la meme ligne
                entry_frame = customtkinter.CTkFrame(self.simulation_frame, fg_color="transparent")
                entry_frame.grid(row= i * 2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
                entry_frame.grid_columnconfigure((0, 1), weight=1)

                entry_x = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_x.grid(row=0, column=0, padx=(10, 5), sticky="ew")

                entry_y = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
                entry_y.grid(row=0, column=1, padx=(5, 10), sticky="ew")

                name_for_save = f"{value}".replace(" : x [-] , y [-]","")
                self.data[f"{name_for_save}_x [-]"] = entry_x
                self.data[f"{name_for_save}_y [-]"] = entry_y
            else:
                # Pour customiser les champs de saisie
                entry_frame = customtkinter.CTkFrame(self.simulation_frame, fg_color="transparent")
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

        # Ajout des params de la plaque
        for i, value in enumerate(master.plaque_values):
            label = customtkinter.CTkLabel(self.plaque_frame, text=value, font=("Aptos Serif", 14, "bold"))
            label.grid(row=i*2 + 1, column=0, padx=20, pady=(10,0), sticky="w")

            # Pour customiser les champs de saisie
            entry_frame = customtkinter.CTkFrame(self.plaque_frame, fg_color="transparent")
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
        
        # Ajout des params thermistances
        for i, param in enumerate(master.thermistances_values):
            label = customtkinter.CTkLabel(self.thermistances_frame, text=param, font=("Aptos Serif", 14, "bold"))
            label.grid(row= i * 2 + 1, column=0, padx=20, pady=(10, 0), sticky="w")

            entry_frame = customtkinter.CTkFrame(self.thermistances_frame, fg_color="transparent")
            entry_frame.grid(row= i * 2 + 2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
            entry_frame.grid_columnconfigure((0, 1), weight=1)

            entry_x = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
            entry_x.grid(row=0, column=0, padx=(10, 5), sticky="ew")

            entry_y = customtkinter.CTkEntry(entry_frame, height=35, border_width=0.5, bg_color="transparent", border_color="#484a4a", font=("Aptos Serif", 12), corner_radius=5, placeholder_text="...")
            entry_y.grid(row=0, column=1, padx=(5, 10), sticky="ew")

            name_for_save = f"{param}".replace(" : x [m] , y [m]","")
            self.data[f"{name_for_save}_x [m]"] = entry_x
            self.data[f"{name_for_save}_y [m]"] = entry_y
        
        # Valeurs par defaut du simulateur
        default ={
            "Actuateur Commande [W]": "1",
            "Actuateur Moment d'allumage [s]": "0",
            "Actuateur Durée [s]": "500",
            "Actuateur Position_x [m]": "15.58e-3",
            "Actuateur Position_y [m]": "29e-3",
            "Actuateur Dimension_x [m]": "14.84e-3",
            "Actuateur Dimension_y [m]": "15.8e-3",
            "Pertubation Valeur [W]": "0",
            "Pertubation Moment d'allumage [s]": "0",
            "Pertubation Durée [s]": "500",
            "Pertubation Position_x [m]": "36.58e-3",
            "Pertubation Position_y [m]": "32.12e-3",
            "Durée [s]": "500",
            "Température ambiante [°C]": "23",
            "Coefficient de convection [W.m⁻².°C⁻¹]": "14",
            "Maillage_x [-]": "116",
            "Maillage_y [-]": "61",
            "Facteur de temps [-]": "8",
            "Longueur [m]": "116e-3",
            "Largeur [m]": "61e-3",
            "Epaisseur [m]": "1.5e-3",
            "Chaleur spécifique [J.kg⁻¹.°C⁻¹]": "903",
            "Densité [kg/m³]": "2699",
            "Conductivité thermique [W.m⁻¹.°C⁻¹]": "237",
            "Thermistance 1_x [m]": "15.06e-3",
            "Thermistance 1_y [m]": "30.15e-3",
            "Thermistance 2_x [m]": "60.24e-3",
            "Thermistance 2_y [m]": "30.15e-3",
            "Thermistance 3_x [m]": "105.27e-3",
            "Thermistance 3_y [m]": "30.15e-3"
        }
        self.setEntries(default)
    
    def getData(self): # Retourne le dictionnaire label + entry
        return self.data

    def setEntries(self, data): # Permet de modifier chaque entry grace au fichier JSON
        for label, entry in self.data.items():
            entry.delete(0, customtkinter.END)
            entry.insert(0, data.get(label, ""))

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
                if v < 0 and label not in ("Actuateur Commande [W]", "Pertubation Valeur [W]"):
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
        
        # Verifier que les moments d'allumage sont corrects
        valeur_pertubation = float(self.data["Pertubation Valeur [W]"].get())
        duree_simulation = float(self.data["Durée [s]"].get())
        moment_actuateur = float(self.data["Actuateur Moment d'allumage [s]"].get())
        duree_actuateur = float(self.data["Actuateur Durée [s]"].get())
        moment_pertubation = float(self.data["Pertubation Moment d'allumage [s]"].get())
        duree_pertubation = float(self.data["Pertubation Durée [s]"].get())

        if moment_actuateur > duree_simulation:
            self.data["Actuateur Moment d'allumage [s]"].configure(border_color="red")
            messagebox.showerror("Erreur", "Le moment d'allumage de l'actuateur ne peut pas dépasser la durée de simulation!")
            return True
        if duree_simulation-moment_actuateur < duree_actuateur:
            self.data["Actuateur Durée [s]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La durée de l'actuateur dépasse le temps entre son allumage et la fin de la simulation!")
            return True
        
        if valeur_pertubation != 0:
            if moment_pertubation > duree_simulation:
                self.data["Pertubation Moment d'allumage [s]"].configure(border_color="red")
                messagebox.showerror("Erreur", "Le moment d'allumage de la pertubation ne peut pas dépasser la durée de simulation!")
                return True
            if duree_simulation-moment_pertubation < duree_pertubation:
                self.data["Pertubation Durée [s]"].configure(border_color="red")
                messagebox.showerror("Erreur", "La durée de la pertubation dépasse le temps entre son allumage et la fin de la simulation!")
                return True
            
        # Verifier qu'on a pas facteur de temps < 4 (instabilité) ou pas  facteur de temps > 10 (vitesse de simulation plus ou moins ralentie)
        facteur_temps = float(self.data["Facteur de temps [-]"].get())
        if facteur_temps < 4 or facteur_temps > 10:
            self.data["Facteur de temps [-]"].configure(border_color="red")
            messagebox.showerror("Erreur", "Le facteur de temps doit être choisi entre 4 et 10 pour que le simulateur soit rapide et stable!")
            return True
        
        # Verifier que les positions de l'actuateur, la pertubation et les thermistances sont dans la plaque ainsi que les dims de l'actuateur
        longueur = float(self.data["Longueur [m]"].get())
        largeur = float(self.data["Largeur [m]"].get())
        
        if float(self.data["Actuateur Position_x [m]"].get()) > longueur:
            self.data["Actuateur Position_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de l'actuateur dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Actuateur Position_y [m]"].get()) > largeur:
            self.data["Actuateur Position_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de l'actuateur dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Actuateur Dimension_x [m]"].get()) > longueur:
            self.data["Actuateur Dimension_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "Les dimensions de l'actuateur dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Actuateur Dimension_y [m]"].get()) > largeur:
            self.data["Actuateur Dimension_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "Les dimensions de l'actuateur dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Pertubation Position_x [m]"].get()) > longueur:
            self.data["Pertubation Position_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la pertubation dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Pertubation Position_y [m]"].get()) > largeur:
            self.data["Pertubation Position_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la pertubation dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 1_x [m]"].get()) > longueur:
            self.data["Thermistance 1_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 1 dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 1_y [m]"].get()) > largeur:
            self.data["Thermistance 1_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 1 dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 2_x [m]"].get()) > longueur:
            self.data["Thermistance 2_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 2 dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 2_y [m]"].get()) > largeur:
            self.data["Thermistance 2_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 2 dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 3_x [m]"].get()) > longueur:
            self.data["Thermistance 3_x [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 3 dépasse les dimensions de la plaque!")
            return True
        if float(self.data["Thermistance 3_y [m]"].get()) > largeur:
            self.data["Thermistance 3_y [m]"].configure(border_color="red")
            messagebox.showerror("Erreur", "La position de la thermistance 3 dépasse les dimensions de la plaque!")
            return True
        return False



class SimulationGUI(customtkinter.CTkToplevel):
    """Classe representant l'interface graphique pour le simulateur"""
    def __init__(self, parent, theme, title, simulation_values, plaque_values, actuateur_values, pertubation_values, thermistances_values):
        super().__init__(parent)
        self.parent = parent  # Stocke la référence à la fenêtre principale
        self.current_theme = theme  # Stocker le thème actuel
        self.title_header = title # Stocker le texte d'entete de la fenetre
        self.simulation_values = simulation_values
        self.plaque_values = plaque_values
        self.actuateur_values = actuateur_values
        self.pertubation_values = pertubation_values
        self.thermistances_values = thermistances_values
        self.protocol("WM_DELETE_WINDOW", self.on_close) # Détection de la fermeture de la fenêtre
        self.simulation_en_cours = False


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
        self.scrollable_body_frame = ScrollableBodyFrame(self) # Instance du corps de la page
        self.scrollable_body_frame.grid(row=1, column=0, padx=10, pady=(10,0), sticky="nsew", columnspan=2)

        # Les options
        self.exporter_reponses = customtkinter.StringVar(value="on")
        self.checkBox_exporter_reponses = customtkinter.CTkCheckBox(self.scrollable_body_frame.options_frame, text=f"\nExporter les réponses à l'échelon\n({Path.home() / 'Documents' / 'Simulation'})", command=self.exporter_reponses_callback, variable=self.exporter_reponses, onvalue="on", offvalue="off", fg_color="#3d7cf2")
        self.checkBox_exporter_reponses.grid(row=1, column=0, padx=25, pady=10, sticky="w")

        self.en_kelvin = customtkinter.StringVar(value="off")
        self.checkBox_en_kelvin = customtkinter.CTkCheckBox(self.scrollable_body_frame.options_frame, text="Température en Kelvin", command=self.en_kelvin_callback, variable=self.en_kelvin, onvalue="on", offvalue="off", fg_color="#3d7cf2")
        self.checkBox_en_kelvin.grid(row=2, column=0, padx=25, pady=10, sticky="w")

        self.afficher_thermistances = customtkinter.StringVar(value="on")
        self.checkBox_afficher_thermistances = customtkinter.CTkCheckBox(self.scrollable_body_frame.options_frame, text="Afficher les réponses à l'échelon", command=self.afficher_thermistances_callback, variable=self.afficher_thermistances, onvalue="on", offvalue="off", fg_color="#3d7cf2")
        self.checkBox_afficher_thermistances.grid(row=3, column=0, padx=25, pady=10, sticky="w")

        self.afficher_plaque = customtkinter.StringVar(value="on")
        self.checkBox_afficher_plaque = customtkinter.CTkCheckBox(self.scrollable_body_frame.options_frame, text="Afficher le graphique de la plaque", command=self.afficher_plaque_callback, variable=self.afficher_plaque, onvalue="on", offvalue="off", fg_color="#3d7cf2")
        self.checkBox_afficher_plaque.grid(row=4, column=0, padx=25, pady=10, sticky="w")

        save_load_button_frame = customtkinter.CTkFrame(self.scrollable_body_frame.options_frame, fg_color="transparent")
        save_load_button_frame.grid(row=5, column=0, padx=(10,10) , pady=10, sticky="nsew")
        save_load_button_frame.grid_columnconfigure(0, weight=1)
        save_load_button_frame.grid_columnconfigure(1, weight=1)
        
        self.load_button = customtkinter.CTkButton(save_load_button_frame, text="Charger", command=self.load_file, height=35, fg_color="#3d7cf2")
        self.load_button.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.save_button = customtkinter.CTkButton(save_load_button_frame, text="Enregistrer", command=self.save_file, height=35, fg_color="#3d7cf2")
        self.save_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Conteneur bouton simuler et type de simulation
        self.run_button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.run_button_frame.grid(row=2, column=0, pady=10, sticky="ew", columnspan=2)
        self.run_button_frame.grid_columnconfigure(0, weight=1)

        # Sous-frame bouton simuler et type de simulation
        self.button_container = customtkinter.CTkFrame(self.run_button_frame, fg_color="transparent")
        self.button_container.grid(row=0, column=0, sticky="e", padx=(0,35),pady=10)
        self.button_container.grid_columnconfigure((0, 1), weight=1)

        # Choix du type de simulation 2D ou 3D
        self.type_simulation = customtkinter.CTkSegmentedButton(self.button_container, values=["2D", "3D"], command=self.type_simulation_callback, height=40, selected_color="#3d7cf2")
        self.type_simulation.grid(row=0, column=0, padx=10, pady=10)
        self.type_simulation.set("3D")

        # Bouton Simuler
        self.run_button = customtkinter.CTkButton(self.button_container, text="Simuler", command=self.simulate, height=40, fg_color="#1160f2",)
        self.run_button.grid(row=0, column=1, padx=(10,0), pady=10)

    
    def set_theme(self, theme):
        """Permet de changer le thème des fenetres"""
        self.current_theme = theme
        customtkinter.set_appearance_mode(theme)
        self.update_theme_buttons(theme)

        # Changer aussi chez le parent
        if hasattr(self.parent, 'set_theme'):
            self.parent.set_theme(theme)
    
    def update_theme_buttons(self, active_theme):
        """ Gère l'effet visuel des boutons si le thème change """
        default_fg = "transparent"
        black_fg = "#303030"
        light_fg = "#918d8d"
        
        self.light_theme_button.configure(
            fg_color=light_fg if active_theme == "Light" else default_fg,
            hover_color="#484a4a" if active_theme == "Light" else "#1f1d1d"
        )
        self.dark_theme_button.configure(
            fg_color=black_fg if active_theme == "Dark" else default_fg,
            hover_color="#484a4a" if active_theme == "Light" else "#1f1d1d"
        )
        self.auto_theme_button.configure(
            fg_color=black_fg if active_theme == "system" else default_fg,
            hover_color="#484a4a" if active_theme == "Light" else "#1f1d1d"
        )
        self.label_title.configure(text_color="#2b2a2a" if active_theme == "Light" else "white")
        self.header_frame.configure(fg_color="#c7c1c1" if active_theme == "Light" else "#484a4a")

    def save_file(self):
        """Permet de sauvegarder les paramètres dans un fichier JSON"""
        self.parent.iconify()
        fileOperations.save_file(data_owner=self.scrollable_body_frame)

    def load_file(self):
        """Permet d'ouvir le fichier JSON et charger les données"""
        self.parent.iconify()
        fileOperations.load_file(data_owner=self.scrollable_body_frame)
    
    def simulate(self):
        """ Permet de lancer la simulation"""
        self.parent.iconify()
        if self.simulation_en_cours:
            messagebox.showinfo("Info", "Une simulation est déjà en cours!")
        elif self.scrollable_body_frame.invalid_or_empty():
            pass # Tous les warnin concernant les champs incorrects sont directement faits dans la méthode invalid_or_empty()
        elif self.checkBox_afficher_thermistances.get() == "off" and self.checkBox_afficher_plaque.get() == "off":
            messagebox.showwarning("Warning", "Choisir au moins une option d'affichage parmi plaque et réponses à l'échelon)")
        else:
            self.simulation_en_cours = True
            data = self.scrollable_body_frame.getData()

            # Collecte des paramètres pour la simulation
            plq_params = {
                'longueur': float(data["Longueur [m]"].get()),
                'largeur': float(data["Largeur [m]"].get()),
                'epaisseur': float(data["Epaisseur [m]"].get()),
                'chaleur_specifique': float(data["Chaleur spécifique [J.kg⁻¹.°C⁻¹]"].get()),
                'densite': float(data["Densité [kg/m³]"].get()),
                'conductivite_thermique': float(data["Conductivité thermique [W.m⁻¹.°C⁻¹]"].get())
            }
            actuateur_params = {
                'position': Vecteur(float(data["Actuateur Position_x [m]"].get()), float(data["Actuateur Position_y [m]"].get())),
                'dimensions': Vecteur(float(data["Actuateur Dimension_x [m]"].get()), float(data["Actuateur Dimension_y [m]"].get())),
                'commande': float(data["Actuateur Commande [W]"].get()),
                'delais': float(data["Actuateur Moment d'allumage [s]"].get()),
                'duree': float(data["Actuateur Durée [s]"].get()),
                'label': 'actuateur'
            }
            perturbation_params = {
                'position': Vecteur(float(data["Pertubation Position_x [m]"].get()), float(data["Pertubation Position_y [m]"].get())),
                'dimensions': Vecteur(6.45e-3, 3.17e-3), # Selon les specs
                'commande': float(data["Pertubation Valeur [W]"].get()),
                'delais': float(data["Pertubation Moment d'allumage [s]"].get()),
                'duree':float(data["Pertubation Durée [s]"].get()),
                'label': 'Perturbation'
            }
            therm1_params = {
                'label': 't1',
                'position': Vecteur(float(data[ "Thermistance 1_x [m]"].get()), float(data[ "Thermistance 1_y [m]"].get()))
            }
            therm2_params = {
                'label': 't2',
                'position': Vecteur(float(data["Thermistance 2_x [m]"].get()), float(data["Thermistance 2_y [m]"].get()))
            }
            therm3_params = {
                'label': 't3',
                'position': Vecteur(float(data["Thermistance 3_x [m]"].get()), float(data["Thermistance 3_y [m]"].get()))
            }
            sim_params = {
                'nb_elements': Vecteur(int(data["Maillage_x [-]"].get()), int(data["Maillage_y [-]"].get())),
                'duree': float(data["Durée [s]"].get()),
                'facteur_temps': float(data["Facteur de temps [-]"].get()),
                'temperature_ambiante': float(data["Température ambiante [°C]"].get()),
                'coefficient_convection': float(data["Coefficient de convection [W.m⁻².°C⁻¹]"].get()),
                'affiche_kelvin': True if self.checkBox_en_kelvin.get() == "on" else False,
                'deux_dimensions': True if self.type_simulation.get() == "2D" else False,
                'apparence_sombre': True if customtkinter.get_appearance_mode() == "Dark" else False,
                'afficher_thermistances': True if self.checkBox_afficher_thermistances.get() == "on" else False,
                'afficher_plaque': True if self.checkBox_afficher_plaque.get() == "on" else False,
                'exporter_reponses': True if self.checkBox_exporter_reponses.get() == "on" else False
            }

            # Instanciation des objets pour nécessaires pour la simulation
            plaque = Plq(**plq_params)
            actuateur = compt.Source(**actuateur_params)
            perturbation = compt.Source(**perturbation_params)
            trm1 = compt.Thermistance(**therm1_params)
            trm2 = compt.Thermistance(**therm2_params)
            trm3 = compt.Thermistance(**therm3_params)

            # Lancement de la simulation
            simulation = Sim(plaque=plaque, thermistances=[trm1, trm2, trm3], sources=[actuateur, perturbation], params=sim_params)
            simulation.executer_simulation()

            # On check pour voir si le thread a fini avec l'update de la courbe
            self.simulation_en_cours =  simulation.thread.is_alive()

    def type_simulation_callback(self,value):
        """Montre dans le terminal le type de simulation en cours"""
        print("Type simulation:", value)
    
    def exporter_reponses_callback(self):
        """Montre dans le terminal si on exporte les reponses à l'échelon"""
        print("Exportation des réponses à l'échelon:", self.checkBox_exporter_reponses.get())
    
    def en_kelvin_callback(self):
        """Montre dans le terminal si on est en kelvin"""
        print("En Kelvin:", self.checkBox_en_kelvin.get())
    
    def afficher_thermistances_callback(self):
        """Montre dans le terminal si l'option afficher le graphe des thermistances en choisie"""
        print("Affichage du graphique des thermistances:", self.checkBox_afficher_thermistances.get())
    
    def afficher_plaque_callback(self):
        """Montre dans le terminal si l'option afficher le graphe de la temperature dans la plaque en choisie"""
        print("Affichage du graphique de la temperature de la plaque:", self.checkBox_afficher_plaque.get())
    
    def on_close(self):
        """Ferme proprement la fenêtre et restaure la principale."""
        if not self.simulation_en_cours:
            self.parent.deiconify()  # Restaurer la fenêtre principale
            self.destroy()  # Détruit la fenêtre customTkinter
        else:
            messagebox.showerror("Error", "Veuillez d'abord fermer la simulation.")