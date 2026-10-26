"""Punto de entrada de la aplicación (MVC)."""

from config.settings import SimulationConfig
from controllers.simulation_controller import SimulationController
from views.console_view import ConsoleView


def main():
    config = SimulationConfig()
    view = ConsoleView()
    controller = SimulationController(config, view)
    controller.run()


if __name__ == "__main__":
    main()