"""
Punto de entrada: ejecuta la simulación y muestra los resultados.
"""
from controladores.controlador import ControladorSimulacion
from servicios.simulador import IndiceBase, IndiceAjustado
from vistas.vista import VistaConsola


def main():
    vista = VistaConsola()

    # Modelo base
    controlador_base = ControladorSimulacion(IndiceBase())
    resultados_base = controlador_base.simular()
    vista.mostrar_tabla(resultados_base, "MODELO BASE: I = 0.5H + 0.3N + 0.2Tr")

    # Modelo ajustado
    controlador_ajustado = ControladorSimulacion(IndiceAjustado())
    resultados_ajustado = controlador_ajustado.simular()
    vista.mostrar_tabla(
        resultados_ajustado,
        "MODELO AJUSTADO: I = 0.55H + 0.30N + 0.15Tr",
    )

    # Gráfica comparativa
    vista.graficar(resultados_base, resultados_ajustado)


if __name__ == "__main__":
    main()