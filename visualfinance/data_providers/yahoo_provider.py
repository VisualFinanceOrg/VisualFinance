from .base_provider import BaseDataProvider
import yfinance as yf
from typing import List
import pandas as pd

class YahooFinanceDataProvider(BaseDataProvider):
    """
    Proveedor de datos basado en Yahoo Finance usando yfinance.

    Implementa el método `get_prices` requerido por la clase base.
    """

    def get_prices(self, tickers: List[str], start_date: str, end_date: str, **kwargs) -> pd.DataFrame:
        """
        Obtiene precios ajustados de cierre desde Yahoo Finance.

        Args:
            tickers (List[str]): Lista de símbolos (e.g., ['AAPL', 'MSFT']).
            start_date (str): Fecha inicial en formato 'YYYY-MM-DD'.
            end_date (str): Fecha final en formato 'YYYY-MM-DD'.

        Returns:
            pd.DataFrame: DataFrame con índice de fechas y columnas por ticker.
        """
        data = yf.download(
            tickers=tickers,
            start=start_date,
            end=end_date,
            auto_adjust=kwargs.get("auto_adjust", False),
            interval=kwargs.get("interval", "1d"),
            prepost=kwargs.get("prepost", False),
            progress=kwargs.get("progress", False)
        )

        # Si se solicitan múltiples tickers, 'Adj Close' será un DataFrame
        if len(tickers) == 1:
            adj_close = data['Adj Close'].to_frame(name=tickers[0])
        else:
            adj_close = data['Adj Close']

        # Asegurar que el índice es datetime
        adj_close.index = pd.to_datetime(adj_close.index)

        return adj_close