import numpy as np
import pandas as pd
from typing import Union, List
from scipy.stats import norm
from arch import arch_model


__all__ = [
    "value_at_risk_historical",
    "value_at_risk_parametric",
    "expected_shortfall",
    "sharpe_ratio"
]


def value_at_risk_historical(df: pd.DataFrame, alpha: Union[float, List[float]] = 0.05, method:str="lower") -> pd.DataFrame:
    """
    Calcula el Valor en Riesgo (VaR) utilizando simulación histórica.

    Args:
        df (pd.DataFrame): Serie de retornos históricos (puede ser una columna o más).
        alpha (float or list): Nivel(es) de confianza (por ejemplo, 0.05 para 95%).

    Returns:
        pd.DataFrame: DataFrame con los valores de VaR para cada alpha y cada activo.
    """
    alphas = [alpha] if isinstance(alpha, float) else alpha
    result = {
        a: df.apply(lambda x: np.percentile(x, a, method=method))
        for a in alphas
    }
    result = pd.DataFrame(result)
    result.columns.name = "Alpha"
    return (result*(-100)).T


def value_at_risk_parametric(
    df: pd.DataFrame,
    alpha: Union[float, List[float]] = 0.05,
    garch: tuple | None = None
) -> pd.DataFrame:
    """
    Calcula el VaR (Valor en Riesgo) usando una aproximación paramétrica normal.
    Opcionalmente ajusta un modelo GARCH(1,1).

    Args:
        df (pd.DataFrame): Serie de retornos por activo.
        alpha (float or list): Nivel(es) de confianza.
        garch (tuple, optional): Si se especifica, aplica GARCH(1,1) para estimar la volatilidad.

    Returns:
        pd.DataFrame: DataFrame con los valores de VaR para cada alpha y cada activo.
    """
    if garch is not None:
        scaled_port_ret = df * 100
        results = {}
        for col in scaled_port_ret.columns:
            series = scaled_port_ret[col].dropna()  # Quita NaNs si hay
            model = arch_model(series, vol='Garch', p=1, q=1)
            res = model.fit(disp="off")
            sigma_scaled = np.sqrt(res.forecast(horizon=1).variance.values[-1][0])
            results[col] = sigma_scaled/100  # 
        sigma = pd.Series(results)
    else:
        sigma = df.std()

    mu = df.mean()
    alphas = [alpha] if isinstance(alpha, float) else alpha
    result = {
        a: mu + norm.ppf(a) * sigma
        for a in alphas
    }

    result = pd.DataFrame(result)
    result.columns.name = "Alpha"
    return (result*(-100)).T


def expected_shortfall(df: pd.DataFrame, alpha: Union[float, List[float]] = 0.05) -> pd.DataFrame:
    """
    Calcula el Expected Shortfall (también conocido como CVaR).

    Args:
        df (pd.DataFrame): Serie de retornos por activo.
        alpha (float or list): Nivel(es) de confianza.

    Returns:
        pd.DataFrame: DataFrame con el Expected Shortfall para cada alpha y cada activo.
    """
    alphas = [alpha] if isinstance(alpha, float) else alpha
    result = {}

    for a in alphas:
        var = df.apply(lambda x: np.percentile(x, a * 100))
        es = df.apply(lambda x: x[x <= np.percentile(x, a * 100)].mean())
        result[a] = es

    result = pd.DataFrame(result)
    result.columns.name = "Alpha"
    return (result*(-100)).T


def sharpe_ratio(RentabilidadActivo: float, RentabilidadLibreRiesgo: float, Volatilidad: float) -> float:
    """
    Calcula el índice de Sharpe, una medida de rentabilidad ajustada al riesgo.

    Args:
        RentabilidadActivo (float): Rentabilidad esperada del activo o portafolio (en decimal, ej: 0.12 para 12%).
        RentabilidadLibreRiesgo (float): Rentabilidad de un activo sin riesgo (ej. bono soberano).
        Volatilidad (float): Desviación estándar de los retornos del activo (en decimal).

    Returns:
        float: Índice de Sharpe --> Mide cuánta rentabilidad adicional se obtiene por cada unidad de riesgo asumido.
    """
    return (RentabilidadActivo - RentabilidadLibreRiesgo) / Volatilidad