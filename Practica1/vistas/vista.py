"""
Vista: muestra la tabla de resultados y las gráficas.
"""
import matplotlib.pyplot as plt


class VistaConsola:
    """Presenta los resultados por consola y en gráficas."""

    def mostrar_tabla(self, resultados, titulo):
        print("\n" + "=" * 65)
        print(titulo)
        print("=" * 65)
        print(f"{'Hora':<8}{'Tr':<8}{'Índice':<10}{'Estado'}")
        print("-" * 65)
        for r in resultados:
            print(f"{r.hora:<8}{r.tr:<8.2f}{r.indice:<10.4f}{r.estado}")
        print("=" * 65)

    def graficar(self, resultados_base, resultados_ajustado):
        horas = [r.hora for r in resultados_base]
        indices_base = [r.indice for r in resultados_base]
        indices_ajustado = [r.indice for r in resultados_ajustado]

        plt.figure(figsize=(10, 5))
        plt.plot(horas, indices_base, marker="o", label="Modelo base")
        plt.plot(horas, indices_ajustado, marker="s", label="Modelo ajustado")

        # Líneas de umbral
        plt.axhline(0.40, color="gray", linestyle="--")
        plt.text(8.1, 0.41, "Umbral 0.40", color="gray", fontsize=9)
        
        plt.axhline(0.60, color="orange", linestyle="--")
        plt.text(8.1, 0.61, "Umbral 0.60", color="orange", fontsize=9)
        
        plt.axhline(0.75, color="red", linestyle="--")
        plt.text(8.1, 0.76, "Umbral 0.75", color="red", fontsize=9)

        plt.title("Índice de lluvia durante 24 horas")
        plt.xlabel("Hora")
        plt.ylabel("Índice I")
        plt.ylim(0, 1)
        plt.grid(True, alpha=0.3)
        
        plt.text(0.1, 0.95, "● Modelo base   ■ Modelo ajustado", fontsize=10)

        # Quitamos plt.tight_layout() porque tiene un bug con Python 3.14
        # En su lugar, ajustamos los márgenes manualmente
        plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

        # Guardar la imagen
        plt.savefig("grafica_lluvia.png", dpi=120)
        print("\n✅ Gráfica guardada como 'grafica_lluvia.png' en la carpeta del proyecto.")
        
        # Intentar mostrar (si no se abre en WSL, no pasa nada)
        try:
            plt.show()
        except Exception:
            pass