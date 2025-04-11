from tkinter import filedialog, messagebox
import json

def save_file(data_owner):
    """Fonction pour sauvegarder les paramètres dans un fichier JSON"""
    if data_owner.invalid_or_empty():
        pass # Toutes les actions sont faites dans la fonction du if
    else:
        file_path = filedialog.asksaveasfilename(
            filetypes=[("Fichiers JSON", "*.json")],
            title="Enregistrer le fichier"
            )
        
        if file_path and not file_path.endswith(".json"): # Si oublie de l'extension
            file_path += ".json"

        if file_path:
            data = {}
            for label, entry in data_owner.getData().items():
                data[label] = entry.get()
            
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                    messagebox.showinfo("Succès", f"fichier enregistré: {file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", "Impossible d'enregistrer le fichier.")
                print(f"Impossible d'enregistrer le fichier: {e}")
    

def load_file(data_owner):
    """Fonction pour ouvir le fichier JSON et charger les données"""
    file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier JSON",
        filetypes=[("Fichiers JSON", "*.json")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                data_owner.setEntries(data=data)

                # Remettre la couleur si c'etait en rouge
                entries = data_owner.getData().values()
                for entry in entries:
                    entry.configure(border_color="#616161") 

                messagebox.showinfo("Succès", "Les paramètres ont été correctemement chargés.")
        except Exception as e:
            messagebox.showerror("Erreur", "Impossible de lire le fichier de configuration" )
            print(f"Impossible de lire le fichier de configuration : {e}")