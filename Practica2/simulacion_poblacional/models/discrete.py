"""Modelo discreto: P_{t+1} = P_t + r * P_t"""

import numpy as np
from models.base_model import BasePopulationModel


class DiscreteModel(BasePopulationModel):

    def _build_time_vector(self) -> np.ndarray:
        return np.arange(0, int(self.tiempo_total) + 1, dtype=float)

    def _update_population(self, population, t_index) -> float:
        actual = population[-1]
        return actual + self.r * actual