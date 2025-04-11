'''Utilites pour les modules backend'''

import collections
from itertools import starmap

import numpy as np

# types
Vecteur = collections.namedtuple('Vecteur', ['x', 'y'])

# conventions des coins d'un rectangle:
# A: en haut a gauche, B: en bas a droite
#
#     A------x------+
#     |             |
#     y      .      |
#     |             |
#     +-------------B
#
Rectangle = collections.namedtuple('Rectangle', ['A', 'B'])

# fonctions
def get_iterable(x):
    if isinstance(x, collections.abc.Iterable):
        return x
    else:
        return (x,)
    
def definir_region(referentiel: np.meshgrid, rectangle: Rectangle):
    region = (referentiel.x>rectangle.A.x) & (referentiel.y>rectangle.A.y) &\
            (referentiel.x<rectangle.B.x) & (referentiel.y<rectangle.B.y)
    return region

def porte_unitaire(temps: float, delais: float, duree=0.):
    if duree <= 0:
        # echelon
        reponse = temps>delais
    else:
        reponse = (temps>delais) & (temps<delais+duree)
    return np.where(reponse, 1., 0.)

def trouver_coin(centre: Vecteur, dimensions: Vecteur, indice: str):
    '''conventions utilisees pour le type Rectangle'''
    if indice == 'A':
        return starmap(lambda a, b: a - b/2, zip(centre, dimensions))
    elif indice == 'B':
        return starmap(lambda a, b: a + b/2, zip(centre, dimensions))
    
    raise IndexError('Choisir le coin A ou B.')

# decorateurs
def valider_positif(f):
    def wrapper(self, valeur):
        if valeur < 0:
            raise ValueError(f"{f.__name__} doit être > 0")
        return f(self, valeur)
    return wrapper

def valider_vecteur(f):
    def wrapper(self, valeur):
        if valeur.x < 0:
            raise ValueError(f"{f.__name__} x doit être > 0")
        if valeur.y < 0:
            raise ValueError(f"{f.__name__} y doit être > 0")
        return f(self, valeur)
    return wrapper
