"""Facade: coordina Factory + modelos + comparación."""

from typing import Dict, Tuple
import numpy as np

from config.settings import SimulationConfig
from services.model_factory import ModelFactory


class SimulationService:

    def __init__(self, config: SimulationConfig):
        self.config = config
        self.results: Dict[str, Tuple[np.ndarray, np.ndarray]] = {}

    def run(self, model_type: str, P0: float):
        model = ModelFactory.create(model_type, P0, self.config)
        t, p = model.simulate()
        self.results[model.name()] = (t, p)
        return t, p

    def run_all(self, P0: float) -> Dict[str, Tuple[np.ndarray, np.ndarray]]:
        for mtype in ModelFactory.available():
            self.run(mtype, P0)
        return self.results