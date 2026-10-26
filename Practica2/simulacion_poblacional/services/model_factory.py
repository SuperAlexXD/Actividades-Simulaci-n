"""Factory Pattern: crea instancias de modelos según su tipo."""

from models.deterministic import DeterministicModel
from models.discrete import DiscreteModel
from models.stochastic import StochasticModel
from models.continuous import ContinuousModel
from config.settings import SimulationConfig


class ModelFactory:
    """Registro centralizado de modelos disponibles."""

    _REGISTRY = {
        "deterministic": DeterministicModel,
        "discrete": DiscreteModel,
        "stochastic": StochasticModel,
        "continuous": ContinuousModel,
    }

    @classmethod
    def create(cls, model_type: str, P0: float, config: SimulationConfig):
        model_type = model_type.lower()
        if model_type not in cls._REGISTRY:
            raise ValueError(
                f"Modelo '{model_type}' no reconocido. "
                f"Opciones: {list(cls._REGISTRY.keys())}"
            )

        if model_type == "stochastic":
            return StochasticModel(
                P0=P0, r=config.r, tiempo_total=config.tiempo_total,
                sigma=config.sigma, semilla=config.semilla,
            )
        if model_type == "continuous":
            return ContinuousModel(
                P0=P0, r=config.r, tiempo_total=config.tiempo_total,
                dt=config.dt,
            )
        return cls._REGISTRY[model_type](
            P0=P0, r=config.r, tiempo_total=config.tiempo_total,
        )

    @classmethod
    def available(cls):
        return list(cls._REGISTRY.keys())