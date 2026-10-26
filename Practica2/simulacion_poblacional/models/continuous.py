"""Modelo continuo: dP/dt = r*P  →  Euler: P_{t+dt} = P_t + dt*r*P_t"""

import numpy as np
from models.base_model import BasePopulationModel


class ContinuousModel(BasePopulationModel):

    def __init__(self, P0, r, tiempo_total, dt: float = 0.1):
        super().__init__(P0, r, tiempo_total)
        self.dt = float(dt)

    def _build_time_vector(self) -> np.ndarray:
        return np.arange(0, self.tiempo_total + self.dt, self.dt)

    def _update_population(self, population, t_index) -> float:
        actual = population[-1]
        cambio = self.r * actual
        return actual + self.dt * cambio