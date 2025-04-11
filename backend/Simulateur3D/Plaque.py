'''definition de la classe plaque pour la simulation 3d'''

from dataclasses import dataclass

from backend.Simulateur3D.utils import valider_positif


@dataclass(init=False)
class Plaque():
    '''
    classe pour definir la geometrie et les proprietes thermiques de la plaque

              +------------------+
             /    longueur      /|
            +--------x---------+ |
            |                  | |
    largeur y      (x, y)      | +
            |                  |z epaisseur
            o------------------+

    '''

    # tous les grandeurs spatiales sont en metre
    _longueur: float = 117.23e-3
    _largeur: float = 61.57e-3
    _epaisseur: float = 1.5e-3
    # joule par kilogramme degre celsius
    _chaleur_specifique: float = 903.
    # kilogramme par metre cube
    _densite: float = 2699.
    # watt par metre degree celsius
    _conductivite_thermique: float = 237.

    def __init__(self, **kwargs):
        valid_keys = {
            "longueur", "largeur", "epaisseur",
            "chaleur_specifique", "densite", "conductivite_thermique"
        }

        inattendu = set(kwargs) - valid_keys
        if inattendu:
            raise TypeError(f"Arguments inattendus: {inattendu}")
        
        self.longueur = kwargs.get("longueur", 117.23e-3)
        self.largeur = kwargs.get("largeur", 61.57e-3)
        self.epaisseur = kwargs.get("epaisseur", 1.5e-3)
        self.chaleur_specifique = kwargs.get("chaleur_specifique", 903.)
        self.densite = kwargs.get("densite", 2699.)
        self.conductivite_thermique = kwargs.get("conductivite_thermique", 237.)        

    @property
    def longueur(self):
        return self._longueur
    
    @longueur.setter
    @valider_positif
    def longueur(self, valeur: float):
        self._longueur = valeur

    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    @valider_positif
    def largeur(self, valeur: float):
        self._largeur = valeur

    @property
    def epaisseur(self):
        return self._epaisseur
    
    @epaisseur.setter
    @valider_positif
    def epaisseur(self, valeur: float):
        self._epaisseur = valeur

    @property
    def chaleur_specifique(self):
        return self._chaleur_specifique
    
    @chaleur_specifique.setter
    @valider_positif
    def chaleur_specifique(self, valeur: float):
        self._chaleur_specifique = valeur

    @property
    def densite(self):
        return self._densite
    
    @densite.setter
    @valider_positif
    def densite(self, valeur: float):
        self._densite = valeur

    @property
    def conductivite_thermique(self):
        return self._conductivite_thermique
    
    @conductivite_thermique.setter
    @valider_positif
    def conductivite_thermique(self, valeur: float):
        self._conductivite_thermique = valeur
            
    @property
    def volume(self):
        try:
            return self._volume
        except AttributeError:
            return self._longueur * self._largeur * self._epaisseur

    @property
    def diffusivite(self):
        try:
            return self._diffusivite
        except AttributeError:
            # metre carré par seconde
            diffusivite = self._conductivite_thermique /(self._densite * self._chaleur_specifique)
            return diffusivite

    def __str__(self):
        # idealement ces valeurs sont variables selon
        # la longueur des strings
        col1 = 25
        col2 = 15
        col3 = 10
        en_tete = col1 + col2 + col3

        str_plaque = (
            f"{self.__class__.__name__:<{en_tete}}\n"
            f"{'-'*en_tete}\n"
            f"{'longueur':<{col1}}{self._longueur:^{col2}}{'[m]':<{col3}}\n"
            f"{'largeur':<{col1}}{self._largeur:^{col2}}{'[m]':<{col3}}\n"
            f"{'epaisseur':<{col1}}{self._epaisseur:^{col2}}{'[m]':<{col3}}\n"
            f"{'chaleur specifique':<{col1}}{self._chaleur_specifique:^{col2}.2e}{'[J/kg degC]':<{col3}}\n"
            f"{'densite':<{col1}}{self.densite:^{col2}.2e}{'[kg/m^3]':<{col3}}\n"
            f"{'conductivite thermique':<{col1}}{self._conductivite_thermique:^{col2}.2e}{'[W/m degC]':<{col3}}\n"
            f"{'diffusivite thermique':<{col1}}{self.diffusivite:^{col2}.2e}{'[m^3/s]':<{col3}}\n"
            f"{'-'*en_tete}\n"
            )

        return str_plaque
