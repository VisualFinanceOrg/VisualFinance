""" Contiene ratios para analizar la salud financiera de una 
empresa (analisis fundamental)
"""

def SHARP(RentabilidadActivo: float, RentabilidadLibreRiesgo: float, Volatilidad: float) -> float:
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