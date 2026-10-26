"""Modelo estocástico: P_{t+1} = P_t + r*P_t + ε,  ε ~ N(0, σ²)"""

import numpy as np
from models.base_model import BasePopulationModel


class StochasticModel(BasePopulationModel):

    def __init__(self, P0, r, tiempo_total, sigma: float, semilla: int = 42):
        super().__init__(P0, r, tiempo_total)
        self.sigma = float(sigma)
        self.rng = np.random.default_rng(semilla)  # Reproducibilidad

    def _build_time_vector(self) -> np.ndarray:
        return np.arange(0, int(self.tiempo_total) + 1, dtype=float)

    def _update_population(self, population, t_index) -> float:
        actual = population[-1]
        ruido = self.rng.normal(0, self.sigma)
        nueva = actual + self.r * actual + ruido
        return max(nueva, 0.0)  # Población no negativa