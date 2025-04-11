# [Simulateur équipe 7]

Dépôt officiel du logiciel incluant l'interface pour la simulation3D et l'interface Simulink.

## Étapes pour initialser le repo:
- Installer le dépôt: `git clone https://github.com/Equipe7Design2/Simulation3D.git`
- Changer le dossier de travail pour celui du dépôt:`cd Simulation_equipe7`
- Créer environnement virtuel: `python -m venv venv`
- Activer l'environnement virtuel:
	+ pour Windows: `./venv/Scripts/Activate.ps1`
	+ pour Mac: `./venv/bin/activate`
- Installer la version la plus récente de pip: `python.exe -m pip install --upgrade pip`
- Installer les requis: `pip install -r ./requirements.txt`

Sanity test: Entrer dans l'interface ligne de commande python and exécuter

```bash
from backend.Simulation import simulation
from backend.Plaque import plaque
```
## Étapes pour exécuter la simulation 3D:

- Activer l'environnement virtuel:
	+ pour Windows: `./venv/Scripts/Activate.ps1`
	+ pour Mac: `./venv/bin/activate`
- Exécuter la commande dans le terminal

```bash
python main.py
```

## Étapes pour excécuter l'interface simulink
- Ouvrir le dossier dans matlab
- Ouvrir le fichier Asservissement_2023a.slx
- Exécuter le fichier main.m

## Contact

Pour toutes questions, écrire à equipe7.design2@gmail.com ou soulever un Issue.

<!---
Si jamais le remote n'est pas set-up:
- "git remote add origin https://github.com/Equipe7Design2/Simulation3D.git"

## Si vous ajoutez un package avec pip, faire la commande suivante pour updater le requirements.txt:
- "pip freeze > requirements.txt"
-->

