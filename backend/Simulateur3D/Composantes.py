'''Classes des composantes pour interagir avec un plaque'''

from dataclasses import dataclass, field

from backend.Simulateur3D.utils import (Vecteur, Rectangle,
                           trouver_coin, valider_positif, valider_vecteur)


@dataclass(init=False)
class Source():
    '''
    Classe pour appliquer une puissance a une plaque
    
    Le montage du client (prototype):
    Actuateur: position=(15.58e-3, 29e-3), dimensions=(14.84e-3, 15.8e-3)
    Perturbation: position=(36.58e-3, 32.12e-3), dimensions=(6.45e-3, 3.17e-3)
    '''
    
    # tous les grandeurs spatiales sont en metre
    _position: Vecteur[float] = Vecteur(15.58e-3, 29e-3)
    _dimensions: Vecteur[float] = Vecteur(14.84e-3, 15.8e-3)
    # watt
    commande: float = 5.
    # seconde
    _delais: float = 0.
    # si <= 0 -> echelon
    duree: float = -1.
    label: str = ''
    
    nombre_sources = 0

    def __init__(self, **kwargs):
        valid_keys = {
            "position", "dimensions", "commande",
            "delais", "duree", 'label'
        }

        inattendu = set(kwargs) - valid_keys
        if inattendu:
            raise TypeError(f"Arguments inattendus: {inattendu}")
        
        self.position = kwargs.get("position", Vecteur(15.58e-3, 29e-3))
        self.dimensions = kwargs.get("dimensions", Vecteur(14.84e-3, 15.8e-3))
        self.commande = kwargs.get("commande", 5.)
        self.delais = kwargs.get("delais",0.)
        self.duree = kwargs.get("duree", -1.)
        
        if not kwargs.get('label'):
            self.label = f'source_{Source.nombre_sources}'
        else:
            self.label = kwargs.get('label')

        Source.nombre_sources += 1

    @property
    def position(self):
        return self._position
    
    @position.setter
    @valider_vecteur
    def position(self, valeur: Vecteur):
        self._position = valeur

    @property
    def dimensions(self):
        return self._dimensions
    
    @dimensions.setter
    @valider_vecteur
    def dimensions(self, valeur: Vecteur):
        self._dimensions = valeur

    @property
    def delais(self):
        return self._delais
    
    @delais.setter
    @valider_positif
    def delais(self, valeur: Vecteur):
        self._delais = valeur

    @property
    def surface(self):
        try:
            return self._surface
        except AttributeError:
            return self._dimensions.x * self._dimensions.y

    @property
    def coins(self):
        try:
            return self._coins
        except AttributeError:
            coin_A = Vecteur(*trouver_coin(self._position, self._dimensions, 'A'))
            coin_B = Vecteur(*trouver_coin(self._position, self._dimensions, 'B'))
            return Rectangle(coin_A, coin_B)

@dataclass(init=False)
class Thermistance():
    '''
    Classe pour sonder la temperature a un point sur une plaque

    Le montage du client (prototype):
    Thermistance 1: position=(15.06e-3, 30.15e-3)
    Thermistance 2: position=(60.24e-3, 30.15e-3)
    Thermistance 3: position=(105.27e-3, 30.15e-3)
    '''

    # tous les grandeurs spatiales sont en metre
    _position: Vecteur[float] = Vecteur(15.06e-3, 30.15e-3)
    # seconde
    _temps: list[float] = field(default_factory=lambda: [])
    # degree celsius
    _temperature: list[float] = field(default_factory=lambda: [])
    label: str = ''

    nombre_thermistances = 0

    def __init__(self, **kwargs):
        valid_keys = {
            "position", 'label'
        }

        inattendu = set(kwargs) - valid_keys
        if inattendu:
            raise TypeError(f"Arguments inattendus: {inattendu}")
        
        self._position = kwargs.get("position", Vecteur(15.06e-3, 30.15e-3))

        self._temps = []
        self._temperature = []

        if not kwargs.get("label"):
            self.label = f'thermistance_{Thermistance.nombre_thermistances}'
        else:
            self.label = kwargs.get("label")

        Thermistance.nombre_thermistances += 1

    @property
    def position(self):
        return self._position
    
    @position.setter
    @valider_vecteur
    def position(self, valeur: Vecteur):
        self._position = valeur

    @property
    def temps(self):
        return self._temps
    
    @property
    def temperature(self):
        return self._temperature

    def echantillonner(self, temps, temperature):
        self.temps.append(temps)
        self.temperature.append(temperature)
        
