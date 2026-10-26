"""Clase base abstracta para todos los modelos de simulación."""

from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np


class BasePopulationModel(ABC):
    """
    Template Method Pattern: define el esqueleto del algoritmo de simulación.
    Cada subclase implementa `_update_population` y `_build_time_vector`.
    """

    def __init__(self, P0: float, r: float, tiempo_total: float):
        self.P0 = float(P0)
        self.r = float(r)
        self.tiempo_total = float(tiempo_total)

    # ---------- Métodos que las subclases DEBEN implementar ----------
    @abstractmethod
    def _build_time_vector(self) -> np.ndarray:
        """Construye el vector de tiempo propio del modelo."""
        ...

    @abstractmethod
    def _update_population(self, population: List[float], t_index: int) -> float:
        """Calcula la nueva población en el paso t_index."""
        ...

    # ---------- Template Method ----------
    def simulate(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Esqueleto del algoritmo: construye tiempo, itera, retorna resultados.
        Subclases NO deben sobrescribir este método.
        """
        time_vector = self._build_time_vector()
        populations = [self.P0]
        for i in range(1, len(time_vector)):
            populations.append(self._update_population(populations, i))
        return time_vector, np.array(populations, dtype=float)

    # ---------- Método común ----------
    def name(self) -> str:
        return self.__class__.__name__