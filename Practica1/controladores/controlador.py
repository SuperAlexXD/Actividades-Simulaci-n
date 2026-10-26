"""
Controlador: orquesta el modelo y los servicios de la simulación.
"""
from modelos.clima import Clima, Resultado
from servicios.simulador import factor_temperatura, clasificar


class ControladorSimulacion:
    """Ejecuta la simulación sobre los datos fijos de la práctica."""

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def datos_por_defecto(self):
        # (hora, humedad %, nubosidad %, temperatura °C)
        crudos = [
            ("06:00", 65, 40, 14),
            ("08:00", 70, 50, 16),
            ("10:00", 68, 45, 18),
            ("12:00", 60, 30, 22),
            ("14:00", 75, 70, 20),
            ("16:00", 85, 85, 18),
            ("18:00", 92, 95, 16),
            ("20:00", 88, 90, 17),
            ("22:00", 80, 75, 15),
        ]
        return [Clima(*fila) for fila in crudos]

    def simular(self):
        resultados = []
        for clima in self.datos_por_defecto():
            tr = factor_temperatura(clima.temperatura)
            indice = self.estrategia.calcular(clima.h, clima.n, tr)
            estado = clasificar(indice)
            resultados.append(Resultado(clima.hora, tr, indice, estado))
        return resultados