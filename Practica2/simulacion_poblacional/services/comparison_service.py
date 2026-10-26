"""Strategy Pattern: distintas estrategias de comparación entre modelos."""

from abc import ABC, abstractmethod
from typing import Dict, Tuple
import numpy as np


class ComparisonStrategy(ABC):
    @abstractmethod
    def compare(self, results: Dict[str, Tuple[np.ndarray, np.ndarray]]) -> str:
        ...


class StatisticalComparison(ComparisonStrategy):
    """Compara valor final y media de cada modelo."""

    def compare(self, results):
        lines = ["=" * 60, "COMPARACIÓN ESTADÍSTICA", "=" * 60]
        for name, (t, p) in results.items():
            lines.append(
                f"{name:<15} | final={p[-1]:>10.2f} | "
                f"media={p.mean():>10.2f} | máx={p.max():>10.2f}"
            )
        return "\n".join(lines)


class GrowthRateComparison(ComparisonStrategy):
    """Compara la tasa de crecimiento observada."""

    def compare(self, results):
        lines = ["=" * 60, "TASAS DE CRECIMIENTO OBSERVADAS", "=" * 60]
        for name, (t, p) in results.items():
            if len(p) > 1 and p[0] > 0:
                tasa = (p[-1] - p[0]) / p[0] * 100
                lines.append(f"{name:<15} | crecimiento total: {tasa:>8.2f}%")
        return "\n".join(lines)