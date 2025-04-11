# [Simulateur équipe 7]

Dépôt officiel du logiciel incluant l'interface pour la simulation3D et l'interface Simulink.

## Étapes pour initialiser le dépot:
- Installer le dépôt: `git clone https://github.com/Equipe7Design2/Simulation_equipe7.git`
- Changer le dossier de travail pour celui du dépôt:`cd Simulation_equipe7`
- Créer environnement virtuel: `python -m venv venv`
- Activer l'environnement virtuel:
	+ pour Windows: `./venv/Scripts/Activate.ps1`
	+ pour Mac: `source ./venv/bin/activate`
- Installer la version la plus récente de pip: `python -m pip install --upgrade pip`
- Installer les requis: `pip install -r ./requirements.txt`

Sanity test: Si nécéssaire, entrer dans l'interface ligne de commande python and exécuter

```python
from backend.Simulateur3D.Plaque import Plaque
print(Plaque())
```
## Étapes pour exécuter la simulation 3D:

- Activer l'environnement virtuel:
	+ pour Windows: `./venv/Scripts/Activate.ps1`
	+ pour Mac: `source ./venv/bin/activate`
- Exécuter la commande dans le terminal

```bash
python main.py
```

## Étapes pour excécuter l'interface simulink
- Ouvrir le dépot dans Matlab
- Ouvrir le fichier Asservissement_2023a.slx
- Exécuter le fichier main.m

## Contact

Pour toutes questions, écrire à equipe7.design2@gmail.com ou soulever un Issue.
