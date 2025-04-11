
from collections import namedtuple
import numpy as np


def diffusion_matricielle(temperature: np.array, temperature_ambiante: np.array, source: np.array,
                          facteurs_thermiques: namedtuple, ponderations: namedtuple, differentiels: namedtuple):
    padded = np.pad(temperature, 1)
    nouvelle_temperature = temperature.copy()

    # ajout source
    nouvelle_temperature += facteurs_thermiques.source * source

    # conduction/diffusion
    diffuse_x = (padded[:-2, 1:-1] + padded[2:, 1:-1] - ponderations.x*temperature)/differentiels.x**2
    diffuse_y = (padded[1:-1, 2:] + padded[1:-1, :-2] - ponderations.y*temperature)/differentiels.y**2
    nouvelle_temperature += facteurs_thermiques.conduction*(diffuse_x + diffuse_y)

    # perte convection
    difference_ambiante = temperature_ambiante - temperature
    nouvelle_temperature += facteurs_thermiques.convection * difference_ambiante

    return nouvelle_temperature
