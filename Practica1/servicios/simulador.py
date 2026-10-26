"""
Servicios: cálculo del factor de temperatura, del índice y clasificación.
Aquí se aplica el patrón Strategy para el cálculo del índice.
"""
from abc import ABC, abstractmethod


# ---------- Patrón Strategy ----------
class EstrategiaIndice(ABC):
    """Interfaz común para calcular el índice de lluvia."""

    @abstractmethod
    def calcular(self, h, n, tr):
        ...


class IndiceBase(EstrategiaIndice):
    """Modelo original: I = 0.5H + 0.3N + 0.2Tr"""

    def calcular(self, h, n, tr):
        return 0.5 * h + 0.3 * n + 0.2 * tr


class IndiceAjustado(EstrategiaIndice):
    """Modelo ajustado: I = 0.55H + 0.30N + 0.15Tr"""

    def calcular(self, h, n, tr):
        return 0.55 * h + 0.30 * n + 0.15 * tr


# ---------- Factor de temperatura ----------
TABLA_TEMPERATURA = {
    10: 1.00, 12: 0.90, 14: 0.80, 16: 0.70, 18: 0.60,
    20: 0.50, 22: 0.40, 24: 0.30, 26: 0.20, 28: 0.10,
}


def factor_temperatura(temp):
    """Devuelve Tr según la tabla del modelo (con interpolación lineal)."""
    if temp <= 10:
        return TABLA_TEMPERATURA[10]
    if temp >= 28:
        return TABLA_TEMPERATURA[28]

    claves = sorted(TABLA_TEMPERATURA)
    inferior = max(t for t in claves if t <= temp)
    superior = min(t for t in claves if t >= temp)

    if inferior == superior:
        return TABLA_TEMPERATURA[inferior]

    t_inf = TABLA_TEMPERATURA[inferior]
    t_sup = TABLA_TEMPERATURA[superior]
    proporcion = (temp - inferior) / (superior - inferior)
    return round(t_inf + (t_sup - t_inf) * proporcion, 4)


# ---------- Clasificador ----------
def clasificar(indice):
    """Devuelve el estado de lluvia según el índice."""
    if indice < 0.40:
        return "Sin lluvia"
    if indice < 0.60:
        return "Baja posibilidad"
    if indice < 0.75:
        return "Lluvia probable"
    return "Lluvia"