import pandas as pd
import numpy as np

__all__ = [
    "get_retorno_simple",
    "get_retorno_logaritmico",
    "get_retorno_acumulado_simple",
    "get_retorno_acumulado_logaritmico"
]

def get_retorno_simple(df: pd.DataFrame, fill_value: float = None) -> pd.DataFrame:
    """
    Calcula los retornos simples (porcentuales) de un DataFrame de precios.

    Args:
        df (pd.DataFrame): DataFrame con precios de activos. Las columnas representan activos,
                           las filas representan fechas u observaciones en el tiempo.
        fill_value (float, optional): Valor con el que se reemplazarán los NaN generados por
                                      el cálculo del retorno. Por defecto, no se reemplazan.

    Returns:
        pd.DataFrame: DataFrame con los retornos simples. Si no se especifica fill_value,
                      se excluye la primera fila con NaN.
    """
    returns = df.pct_change()

    if fill_value is not None:
        returns.fillna(fill_value, inplace=True)
    else:
        returns.dropna(inplace=True)

    return returns

def get_retorno_logaritmico(df: pd.DataFrame, fill_value: float = None) -> pd.DataFrame:
    """
    Calcula los retornos logarítmicos de un DataFrame de precios.

    Args:
        df (pd.DataFrame): DataFrame con precios de activos. Las columnas representan activos,
                           las filas representan fechas u observaciones en el tiempo.
        fill_value (float, optional): Valor con el que se reemplazarán los NaN generados por
                                      el cálculo del retorno logarítmico. Por defecto, no se reemplazan.

    Returns:
        pd.DataFrame: DataFrame con los retornos logarítmicos. Si no se especifica fill_value,
                      se excluye la primera fila con NaN.
    """
    returns = np.log(df / df.shift(1))

    if fill_value is not None:
        returns.fillna(fill_value, inplace=True)
    else:
        returns.dropna(inplace=True)

    return returns

def get_retorno_acumulado_simple(returns_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el retorno acumulado simple a partir de un DataFrame de retornos simples.

    Args:
        returns_df (pd.DataFrame): DataFrame con retornos simples (porcentuales) por periodo. 
                                   Las columnas representan activos, las filas el tiempo.

    Returns:
        pd.DataFrame: Retorno acumulado simple en cada periodo.
                      Representa el crecimiento del capital con reinversión de beneficios.
    """
    return (1 + returns_df).cumprod() - 1

def get_retorno_acumulado_logaritmico(log_returns_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el retorno acumulado logarítmico (log return compuesto).

    Args:
        log_returns_df (pd.DataFrame): DataFrame con retornos logarítmicos por periodo.

    Returns:
        pd.DataFrame: Retorno acumulado logarítmico en cada periodo.
                      Se calcula como la suma acumulada de los log-returns,
                      luego se convierte a retorno simple con exponenciación.
    """
    return np.exp(log_returns_df.cumsum()) - 1