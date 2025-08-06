# pyfinquant/data_providers/base_provider.py

from abc import ABC, abstractmethod
import pandas as pd
from typing import List

class BaseDataProvider(ABC):
    """
    Clase Base Abstracta (ABC) para todos los proveedores de datos.
    """

    @abstractmethod
    def get_prices(self, tickers: List[str], start_date: str, end_date: str, **kwargs) -> pd.DataFrame:
        """
        Obtiene los precios de cierre ajustados para una lista de tickers en un rango de fechas.

        Args:
            tickers (List[str]): Lista de símbolos de los activos (ej: ['AAPL', 'GOOGL']).
            start_date (str): Fecha de inicio en formato 'YYYY-MM-DD'.
            end_date (str): Fecha de fin en formato 'YYYY-MM-DD'.

        Returns:
            pd.DataFrame: Un DataFrame donde el índice es un DatetimeIndex y
                          cada columna corresponde al precio de cierre ajustado de un ticker.
        """
        pass