"""
Modelo: representa una observación climática y el resultado de la simulación.
"""


class Clima:
    """Datos climáticos de una hora."""

    def __init__(self, hora, humedad, nubosidad, temperatura):
        self.hora = hora
        self.humedad = humedad          # %
        self.nubosidad = nubosidad      # %
        self.temperatura = temperatura  # °C

    @property
    def h(self):
        """Humedad normalizada (0 a 1)."""
        return self.humedad / 100

    @property
    def n(self):
        """Nubosidad normalizada (0 a 1)."""
        return self.nubosidad / 100

    def __repr__(self):
        return (f"Clima(hora='{self.hora}', humedad={self.humedad}, "
                f"nubosidad={self.nubosidad}, temperatura={self.temperatura})")


class Resultado:
    """Resultado de la simulación para una hora."""

    def __init__(self, hora, tr, indice, estado):
        self.hora = hora
        self.tr = tr
        self.indice = indice
        self.estado = estado

    def __repr__(self):
        return (f"Resultado(hora='{self.hora}', tr={self.tr}, "
                f"indice={self.indice:.4f}, estado='{self.estado}')")