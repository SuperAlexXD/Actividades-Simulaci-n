"""Vista: toda la interacción con el usuario (consola + gráficas)."""

import matplotlib.pyplot as plt
import numpy as np


class ConsoleView:

    def show_header(self, config):
        print("=" * 60)
        print(" SIMULACIÓN POBLACIONAL - COMPARACIÓN DE MODELOS")
        print("=" * 60)
        print(f" Datos entrada : {config.datos_entrada}")
        print(f" r (tasa)      : {config.r}")
        print(f" sigma (ruido) : {config.sigma}")
        print(f" dt (paso)     : {config.dt}")
        print(f" tiempo total  : {config.tiempo_total}")
        print("=" * 60)

    def show_result(self, name, t, p):
        print(f"\n▶ {name}: P0={p[0]:.2f} → Pf={p[-1]:.2f} "
              f"(pasos={len(t)})")

    def show_comparison(self, text: str):
        print("\n" + text)

    def plot_all(self, results, show: bool = True):
        plt.figure(figsize=(12, 7))
        styles = {
            "DeterministicModel": ("-", 2.0),
            "DiscreteModel": ("--", 1.8),
            "StochasticModel": ("-", 1.2),
            "ContinuousModel": (":", 2.0),
        }
        for name, (t, p) in results.items():
            ls, lw = styles.get(name, ("-", 1.5))
            plt.plot(t, p, ls, linewidth=lw, label=name)

        plt.title("Comparación: modelos determinístico, discreto, "
                  "estocástico y continuo")
        plt.xlabel("Tiempo")
        plt.ylabel("Población")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("comparacion_modelos.png", dpi=120)
        if show:
            plt.show()
        print("\n📊 Gráfica guardada como 'comparacion_modelos.png'")

    def show_error(self, msg: str):
        print(f"❌ ERROR: {msg}")