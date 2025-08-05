"""Mide el rendimiento de una inversión a lo largo del tiempo
"""

def RentabilidadMinima(Infacion: float, Impuestos: float) -> float:
    """
    Calcula la rentabilidad mínima necesaria para igualar la pérdida del poder adquisitivo
    debido a la inflación, considerando el efecto de los impuestos.

    La fórmula utilizada es: Rentabilidad = Inflación / (1 - Impuestos)

    Args:
        Infacion (float): Tasa de inflación esperada (por ejemplo, 0.05 para 5%).
        Impuestos (float): Tasa impositiva sobre las ganancias (por ejemplo, 0.25 para 25%).

    Returns:
        float: Rentabilidad mínima necesaria para no perder poder adquisitivo después de impuestos.
    """
    return Infacion / (1 - Impuestos)

def RentabilidadReal(RentabilidadBruta: float, Inflacion: float) -> float:
    """
    Calcula la rentabilidad real de una inversión, descontando el efecto de la inflación.

    Args:
        RentabilidadBruta (float): Rentabilidad nominal o bruta obtenida por la inversión (en decimal, ej: 0.08 para 8%).
        Inflacion (float): Tasa de inflación en el mismo período (en decimal, ej: 0.03 para 3%).

    Returns:
        float: Rentabilidad real (en decimal), que representa el aumento del poder adquisitivo.
    """
    return ((1 + RentabilidadBruta) / (1 + Inflacion)) - 1


def CAGR(ValorInicial: float, ValorFinal: float, Years: float) -> float:
    """
    Calcula la Tasa de Crecimiento Anual Compuesta (CAGR).

    Args:
        ValorInicial (float): Valor inicial de la inversión o activo.
        ValorFinal (float): Valor final de la inversión o activo después del período.
        Years (int): Número de años del período considerado.

    Returns:
        float: CAGR expresado como porcentaje. Representa el crecimiento promedio anual de una inversión.
    """
    Ratio = ValorFinal / ValorInicial
    return (Ratio ** (1 / Years) - 1) * 100

