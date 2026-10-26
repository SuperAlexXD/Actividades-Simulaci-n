"""Modelo determinístico: P(t) = P0 * e^(r*t)"""

import numpy as np
from models.base_model import BasePopulationModel


class DeterministicModel(BasePopulationModel):

    def _build_time_vector(self) -> np.ndarray:
        return np.linspace(0, self.tiempo_total, 200)

    def _update_population(self, population, t_index) -> float:
        # El determinístico se recalcula directo desde la fórmula
        t = self._time_vector[t_index]
        return self.P0 * np.exp(self.r * t)

    def simulate(self):
        # Sobrescribe porque el determinístico es analítico, no iterativo
        self._time_vector = self._build_time_vector()
        return self._time_vector, self.P0 * np.exp(self.r * self._time_vector)