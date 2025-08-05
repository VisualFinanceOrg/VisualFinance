import pandas as pd
from pydantic import BaseModel, field_validator
import numpy as np
from typing import Dict

class ModelParameters(BaseModel):
    """
    Contrato de datos para los parámetros de entrada del optimizador.
    Cualquier estimador debe devolver un objeto con esta estructura.
    """
    mean_returns: pd.Series
    covariance_matrix: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True


class OptimalWeights(BaseModel):
    """
    Contrato de datos para los pesos de una cartera optimizada.
    Cualquier optimizador debe devolver un objeto con esta estructura.
    """
    weights: Dict[str, float]

    @field_validator('weights')
    def weights_must_sum_to_one(cls, v: Dict[str, float]) -> Dict[str, float]:
        """Valida que la suma de los pesos sea aproximadamente 1."""
        if not np.isclose(sum(v.values()), 1.0):
            raise ValueError(f"La suma de los pesos debe ser 1, pero es {sum(v.values())}")
        return v