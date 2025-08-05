from abc import ABC, abstractmethod
import pandas as pd
from visualfinance.utils.models import ModelParameters

class BaseEstimator(ABC):
    """
    Clase Base Abstracta (ABC) para todos los estimadores de parámetros.

    Esta clase define el contrato que debe seguir cualquier método de estimación
    (histórico, GARCH, Black-Litterman, etc.). Obliga a que cada estimador
    implemente un método `estimate` que reciba un DataFrame de precios y devuelva
    un objeto `ModelParameters`.

    Esto desacopla completamente la optimización de la estimación, permitiendo
    inyectar parámetros de cualquier fuente en el optimizador.
    """

    @abstractmethod
    def estimate(self, prices_df: pd.DataFrame) -> ModelParameters:
        """
        Estima la media de retornos esperados y la matriz de covarianza a partir
        de una serie temporal de precios.

        Args:
            prices_df (pd.DataFrame): Un DataFrame de precios, como el devuelto
                                      por un `BaseDataProvider`.

        Returns:
            ModelParameters: Una instancia del modelo Pydantic que contiene
                             la media de retornos y la matriz de covarianza,
                             listas para ser usadas por un optimizador.
        """
        pass