'''Simulation 3d'''

from datetime import datetime
from pathlib import Path
import threading
from functools import cached_property
from collections import namedtuple
from copy import deepcopy
from tkinter import messagebox
import numpy as np
# from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Vecteur, get_iterable, definir_region, echelon_unitaire
from backend.Simulateur3D.utils import Vecteur, get_iterable, definir_region, porte_unitaire
from backend.Simulateur3D.Plaque import Plaque
from backend.Simulateur3D.Composantes import Source, Thermistance
from backend.Simulateur3D.Algorithme import diffusion_matricielle

zZ
# a implementer
# traiter les cas limites, e.g. division par zero
# acceleration cython
class Simulation():
    '''Classe pour gerer les parametres, l'execution et l'affichage de la simulation'''
    Facteurs_thermiques = namedtuple('Facteurs_thermiques', ['conduction', 'convection', 'source'])
    Affichage = namedtuple('Affichage', ['fig', 'axs'])

    # tous les grandeurs spatiales sont en metre
    # tous les temperatures peuvent aussi etre exprimees en kelvin,
    # car la simulation utilise uniquement des differences de temperature
    params_defaut = {
        # sans unité
        'nb_elements': (116, 61),
        # seconde
        'duree': 500,
        # sans unité
        'facteur_temps': 8,
        # watt par metre carré degre celsius
        'coefficient_convection': 14,
        # degree celsius
        'temperature_ambiante': 23,
        'temperature_initiale': 23,
        # parametres de personnalisation
        'affiche_kelvin': False,
        'deux_dimensions': False,
        'afficher_plaque': True,
        'afficher_thermistances': True,
        'apparence_sombre': False,
        'exporter_reponses': True,
        }

    def __init__(self, plaque: Plaque=Plaque(),
                 sources: list[Source]=Source(),
                 thermistances: list[Thermistance]=Thermistance(),
                 params: dict=None):
        
        if params is None:
            params = {}

        for key, value in deepcopy(Simulation.params_defaut).items():
            # imposer les paramètres par défaut au besoin
            params[key] = params.get(key, value)

        self.plaque = plaque

        # personnalisation
        self.affichage_kelvin = params.get('affiche_kelvin')
        self.deux_dimensions = params.get('deux_dimensions')
        self.afficher_plaque = params.get('afficher_plaque')
        self.afficher_thermistances = params.get('afficher_thermistances')
        self.apparence_sombre = params.get('apparence_sombre')
        self.cmap = params.get('theme_temperature', 'coolwarm')

        # temporelles
        self.nb_elements = Vecteur(*params.get('nb_elements'))
        self.duree = params.get('duree')
        self.facteur_temps = params.get('facteur_temps')

        # composantes
        self.sources = {src.label:src for src in get_iterable(sources)}
        self.thermistances = {therm.label:therm for therm in get_iterable(thermistances)}

        # thermiques
        offset_kelvin = 273.15 if self.affichage_kelvin else 0

        self.coefficient_convection = params.get('coefficient_convection')
        self.temperature_ambiante = params.get('temperature_ambiante') + offset_kelvin
        self.temperature_initiale = params.get('temperature_initiale', self.temperature_ambiante)
        self.temperature = np.ones(self.nb_elements)*self.temperature_ambiante

        # affichage avec matplotlib
        self.surface_plaque = None
        self.courbes_thermistances = {}
        
        # attributs d'etat
        self.exporter_reponses = params.get('exporter_reponses')
        self.exec = True
        self.figure_initialisee = False
        self.iteration_diffusion = 0

        # attributs divers
        self.thread = None

        # bilan energetique
        # self.gains_energie = []
        # self.pertes_energie = []

    def redefinir_parametres(self, params):
        for key, value in params.items():
            self.__dict__[key] = value

    def initialiser_avec_defaut(self):
        for key, value in deepcopy(Simulation.params_defaut).items():
            self.__dict__[key] = value

    # proprietes spatiales
    @cached_property
    def dx(self):
        return self.plaque.longueur / self.nb_elements.x

    @cached_property
    def dy(self):
        return self.plaque.largeur / self.nb_elements.y

    @cached_property
    def dz(self):
        return self.plaque.epaisseur

    @cached_property
    def volumes_elements(self):
        return self.dx*self.dy*self.dz

    @cached_property
    def aires_elements(self):
        # contribution des surfaces xy
        aires = 2*self.dx*self.dy * np.ones(self.nb_elements)

        # contribution des surfaces xz
        aires[:, 0] += self.dx*self.dz
        aires[:, -1] += self.dx*self.dz

        # contribution des surfaces yz
        aires[0, :] += self.dy*self.dz
        aires[-1, :] += self.dy*self.dz
        return aires

    @cached_property
    def position_elements(self):
        positions_x = np.arange(0, self.nb_elements[0])*self.dx
        positions_y = np.arange(0, self.nb_elements[1])*self.dy
        mesh_x, mesh_y = np.meshgrid(positions_x, positions_y)

        return Vecteur(mesh_x.T, mesh_y.T)

    # proprietes temporelles
    @cached_property
    def dt(self):
        return pow(1/self.dx**2 + 1/self.dy**2, -1) / (self.facteur_temps*self.plaque.diffusivite)

    @cached_property
    def iterations(self):
        return round(self.duree/self.dt)

    @cached_property
    def temps(self):
        return np.arange(0, self.iterations)*self.dt

    # proprietes sources
    @cached_property
    def elements_sources(self):
        elements_sources = {}

        # aucune source
        if not self.sources:
            return np.zeros(self.nb_elements)

        for label, src in self.sources.items():
            region = definir_region(self.position_elements, src.coins)

            elements_sources[label] = np.where(region, 1., 0.)

            elements_effectifs = np.count_nonzero(elements_sources[label])
            if not elements_effectifs == 0:
                elements_sources[label] /= elements_effectifs

        return elements_sources
 
    @cached_property
    def source(self):
        '''dictionnaire des matrices de puissance de chaque source'''
        source = {}

        for label, src in self.sources.items():
            source[label] = self.elements_sources[label] * src.commande

        return source

    @cached_property
    def application_sources(self):
        '''dictionnaire des modulations des applications des puissances des sources'''
        application = {}

        for label, src in self.sources.items():
            # idealement pouvoir appliquer une fonction quelconque
            # qui serait un attribut de la classe source
            application[label] = porte_unitaire(self.temps, src.delais, src.duree)

        return application

    # proprietes thermistances
    @cached_property
    def indices_thermistances(self):
        indices_thermistances = {}

        for label, therm in self.thermistances.items():
            # arrondir a l'element le plus proche
            indice_x = round(therm.position.x / self.dx)
            indice_y = round(therm.position.y / self.dy)
            indices_thermistances[label] = (indice_x, indice_y)

        return indices_thermistances

    # facteurs et constantes equation diffusion
    @cached_property
    def ponderations_diffusion(self):
        x = np.ones(self.nb_elements)
        x[1:-1, :] += 1

        y = np.ones(self.nb_elements)
        y[:, 1:-1] += 1

        return Vecteur(x, y)

    @cached_property
    def facteurs_thermiques(self):
        # joule par metre degree celsius
        conduction = self.dt * self.plaque.diffusivite

        # sans unite
        convection = self.dt * self.coefficient_convection * self.aires_elements\
            / (self.plaque.densite*self.plaque.chaleur_specifique*self.volumes_elements)

        # degree celsius par watt
        source = self.dt\
            / (self.plaque.densite*self.plaque.chaleur_specifique*self.volumes_elements)

        return Simulation.Facteurs_thermiques(conduction, convection, source)

    @cached_property
    def differentiels(self):
        '''Pour alleger les arguments de l'algorithme'''
        dx = self.plaque.longueur / self.nb_elements.x
        dy = self.plaque.largeur / self.nb_elements.y
        return Vecteur(dx, dy)

    # methodes d'execution
    def executer_diffusion(self):
        # for i in tqdm(range(self.iterations)):
        while self.iteration_diffusion < self.iterations and self.exec:
            source_instantannee = np.zeros(self.nb_elements)
            # considerer tous les sources qui agissent a l'instant
            for label in self.sources.keys():
                source_instantannee += self.application_sources[label][self.iteration_diffusion] * self.source[label]

            self.temperature = diffusion_matricielle(self.temperature, self.temperature_ambiante, source_instantannee,
                                                     self.facteurs_thermiques, self.ponderations_diffusion, self.differentiels)
            
            self.sonder_temperature(self.iteration_diffusion)

            # verification bilan d'energie
            # self.gains_energie.append(np.sum(self.source)*self.dt)
            # self.pertes_energie.append(self.coefficient_convection*np.sum(self.aires_elements*(self.temperature - self.temperature_ambiante)*self.dt))

            self.iteration_diffusion += 1

        self.exec = False

    def sonder_temperature(self, iteration):
        for label, therm in self.thermistances.items():
            therm.echantillonner(self.temps[iteration],
                                 self.temperature[*self.indices_thermistances[label]])

    # methodes affichage de la simulation
    @cached_property
    def afficher(self):
        # appliquer le bon theme
        if self.apparence_sombre:
            plt.style.use('dark_background')
        else:
            plt.style.use('default')

        if self.affichage_kelvin:
            unites = '[K]'
        else:
            unites = r'[$\circ$C]'

        fig = plt.figure(figsize=(12, 5))
        axs = {}

        # wow j'ai appris que bool est une sous-classe de int!!!
        col_plq = self.afficher_plaque
        col_therm = self.afficher_thermistances
        ncols = col_plq + col_therm

        if self.afficher_plaque:
            if self.deux_dimensions:
                ax = fig.add_subplot(1, ncols, (col_plq, col_plq))
                self.surface_plaque = ax.imshow(self.temperature.T, cmap='coolwarm',
                                                origin='lower', extent=[0,self.plaque.longueur, 0, self.plaque.largeur])
            else:
                ax = fig.add_subplot(1, ncols, (col_plq, col_plq), projection='3d')
                self.surface_plaque = ax.plot_surface(*self.position_elements, self.temperature, cmap=self.cmap, antialiased=False)

                ax.set_zlabel(rf'Température {unites}')

            # formatage de l'axe
            ax.set_xlabel('Position en x [m]')
            ax.set_ylabel('Position en y [m]')
            ax.set_title('Température dans la plaque selon la position')

            axs['plaque'] = ax
            axs['colorbar'] = fig.colorbar(self.surface_plaque, ax=ax, cmap=self.cmap, orientation='horizontal', label=rf'Température {unites}')

        if self.afficher_thermistances:
            ax = fig.add_subplot(1, ncols, (ncols, ncols))
            axs['thermistances'] = ax
            courbes = {}

            for label, therm in self.thermistances.items():
                courbes[label], = ax.plot(therm.temps, therm.temperature, label=label)
                
            self.courbes_thermistances = courbes

            # formatage de l'axe
            ax.set_title('Température aux thermistances')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel(rf'Température {unites}')
            ax.legend()
        
        # pour assurer que le premier affichage est la temperature initiale
        if self.thread is not None: self.thread.start()

        return Simulation.Affichage(fig, axs)

    def mettre_figure_a_jour(self, iteration=0):
        # assurer la meme temperature pour tout l'affichage
        temperature = self.temperature

        # mettre a jour plaque
        if self.afficher_plaque:
            ax = self.afficher.axs['plaque']
            cb = self.afficher.axs['colorbar']

            if self.deux_dimensions:
                self.surface_plaque.set_array(temperature.T)
            else:
                for artist in ax.collections:
                    artist.remove()

                ax.plot_surface(*self.position_elements, temperature, cmap=self.cmap, antialiased=False)
            
            cb.mappable.set_clim(temperature.min(), temperature.max())
            cb.update_normal(self.surface_plaque)
                     
        # mettre a jour thermistances
        if self.afficher_thermistances:
            ax = self.afficher.axs['thermistances']
            iteration = self.iteration_diffusion

            for label, therm in self.thermistances.items():
                courbe = self.courbes_thermistances[label]

                # afficher selon les iterations de la diffusion et non l'animation
                courbe.set_data(therm.temps[:iteration], therm.temperature[:iteration])

            ax.relim()
            ax.autoscale_view()

    def exporter_resultats(self):
        home = Path.home()
        documents_dir = home / "Documents"
        dossier = documents_dir / "Simulation"
        dossier.mkdir(parents=True, exist_ok=True)  # cree le dossier s'il n'existe pas

        temps_actuel = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        fichier = dossier / f"sim_data {temps_actuel}.csv"

        # Création d'un DataFrame avec le temps
        df = pd.DataFrame({'temps': self.temps[:self.iteration_diffusion]})

        # ajout des puissances dissipees par chaque source
        for label, src in self.sources.items():
            df[label] = self.application_sources[label][:self.iteration_diffusion] * src.commande

        # ajout des temperatures mesurees par chaque thermistance
        for label, therm in self.thermistances.items():
            df[label] = therm.temperature[:self.iteration_diffusion]

        df.to_csv(fichier, index=False)
        messagebox.showinfo("Succès", f"Résultats exportés dans : {fichier}")

    def executer_simulation(self):
        self.thread = threading.Thread(target=self.executer_diffusion)
        # self.thread.start()

        animation = FuncAnimation(self.afficher.fig, self.mettre_figure_a_jour, range(0, self.iterations, 5), interval=1000)

        plt.show()

        # assure d'arreter la diffusion
        self.exec = False
        self.thread.join()
        
        if self.exporter_reponses:
            self.exporter_resultats()


