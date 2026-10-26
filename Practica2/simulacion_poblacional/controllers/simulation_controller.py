"""Controlador: orquesta el flujo Vista ↔ Servicio."""

from config.settings import SimulationConfig
from services.simulation_service import SimulationService
from services.comparison_service import (
    StatisticalComparison, GrowthRateComparison,
)
from utils.data_loader import DataLoader
from views.console_view import ConsoleView


class SimulationController:

    def __init__(self, config: SimulationConfig, view: ConsoleView):
        self.config = config
        self.view = view
        self.service = SimulationService(config)

    def run(self):
        self.view.show_header(self.config)

        try:
            if not DataLoader.validate(self.config.datos_entrada):
                raise ValueError("Datos de entrada inválidos.")

            P0 = DataLoader.extract_P0(self.config.datos_entrada)

            # Ejecuta los 4 modelos
            results = self.service.run_all(P0)

            # Muestra resultados individuales
            for name, (t, p) in results.items():
                self.view.show_result(name, t, p)

            # Estrategia de comparación
            stats = StatisticalComparison().compare(results)
            growth = GrowthRateComparison().compare(results)
            self.view.show_comparison(stats)
            self.view.show_comparison(growth)

            # Gráfica comparativa
            self.view.plot_all(results, show=True)

        except Exception as e:
            self.view.show_error(str(e))