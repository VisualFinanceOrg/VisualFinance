import pandas as pd
import numpy as np

__all__ = [
    "portfolio_returns"
]

def portfolio_returns(df: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    """
    Calcula los retornos ponderados de un portafolio dado un DataFrame de retornos por activo
    y un diccionario de pesos asignados a cada activo.

    Args:
        df (pd.DataFrame): DataFrame con retornos de activos. Las columnas deben coincidir con los nombres en `weights`.
                           Las filas representan periodos de tiempo (diarios, mensuales, etc.).
        weights (dict[str, float]): Diccionario con los pesos de cada activo. Las claves deben coincidir con las columnas del DataFrame.
                                    No es necesario que los pesos estén normalizados (la función lo hará automáticamente).

    Returns:
        pd.Series: Serie con los retornos del portafolio en cada periodo, calculados como la combinación lineal ponderada
                   de los retornos individuales.

    Raises:
        ValueError: Si hay columnas en `weights` que no existen en `df`, o si no hay correspondencia total.
    """
    # Validación de columnas
    if not set(weights.keys()).issubset(set(df.columns)):
        raise ValueError("Las claves de `weights` deben coincidir con columnas del DataFrame de retornos.")

    # Extraer y normalizar pesos
    weights_vec = np.array([weights[col] for col in df.columns])
    total_weight = weights_vec.sum()
    if total_weight == 0:
        raise ValueError("La suma de los pesos no puede ser cero.")

    weights_vec_norm = weights_vec / total_weight

    # Retornos del portafolio
    return df @ weights_vec_norm
