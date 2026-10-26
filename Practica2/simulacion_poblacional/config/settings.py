"""Configuración global de la simulación."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class SimulationConfig:
    """Parámetros de entrada para la simulación (datos de la guía)."""
    datos_entrada: List[float] = field(
        default_factory=lambda: [1000, 1100, 1250, 1400, 1600, 1850, 2100]
    )
    r: float = 0.05              # Tasa de crecimiento
    sigma: float = 50.0          # Nivel de ruido (desviación estándar)
    dt: float = 0.1              # Paso para Euler
    tiempo_total: float = 10.0   # Horizonte temporal
    semilla: int = 42            # Reproducibilidad del modelo estocástico