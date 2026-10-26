"""Carga y valida los datos de entrada (arreglo de la guía)."""

from typing import List


class DataLoader:

    @staticmethod
    def extract_P0(datos: List[float]) -> float:
        if not datos:
            raise ValueError("El arreglo de datos no puede estar vacío.")
        if datos[0] <= 0:
            raise ValueError("La población inicial debe ser > 0.")
        return float(datos[0])

    @staticmethod
    def validate(datos: List[float]) -> bool:
        return all(isinstance(x, (int, float)) and x >= 0 for x in datos)