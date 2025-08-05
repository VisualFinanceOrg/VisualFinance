def ValorFuturo(ValorActual: float, Inflacion: float, Years: float) -> float:
    """
    Calcula el valor futuro de una cantidad de dinero ajustado por inflación.

    Args:
        ValorActual (float): Monto actual de dinero.
        Inflacion (float): Tasa de inflación anual (en decimal, ej: 0.05 para 5%).
        Years (float): Número de años en el futuro.

    Returns:
        float: Valor futuro esperado, ajustado por la inflación acumulada.
    """
    return ValorActual * ((1 + Inflacion) ** Years)

def ValorPresente(ValorFuturo: float, Inflacion: float, Years: float) -> float:
    """
    Calcula el valor presente de una cantidad futura ajustada por inflación.

    Args:
        ValorFuturo (float): Monto proyectado en el futuro.
        Inflacion (float): Tasa de inflación anual (en decimal, ej: 0.05 para 5%).
        Years (float): Número de años en el futuro.

    Returns:
        float: Valor presente ajustado a inflación, es decir, cuánto equivale hoy ese monto futuro.
    """
    return ValorFuturo / ((1 + Inflacion) ** Years)
