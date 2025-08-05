"""Métricas para decidir si un proyecto de inversión es viable."""

def VAN(Flujos: list[float], TasaDescuento: float) -> float:
    """
    Calcula el Valor Actual Neto (VAN) de una inversión.

    Args:
        Flujos (list[float]): Lista de flujos de caja (el primer valor suele ser negativo e indica la inversión inicial).
        TasaDescuento (float): Tasa de descuento o WACC (porcentaje en decimal, ej: 0.1 para 10%).

    Returns:
        float: Valor Actual Neto (VAN) --> Si el VAN > 0, la inversión es rentable.
    """
    return sum(f / (1 + TasaDescuento) ** t for t, f in enumerate(Flujos))

def TIR(Flujos: list[float], precision: float = 1e-6, max_iter: int = 1000) -> float:
    """
    Calcula la Tasa Interna de Retorno (TIR) usando el método de búsqueda incremental.

    Args:
        Flujos (list[float]): Lista de flujos de caja.
        precision (float): Precisión para la aproximación.
        max_iter (int): Iteraciones máximas.

    Returns:
        float: TIR (Tasa Interna de Retorno) expresada como decimal.
    """
    tasa = 0.1
    for _ in range(max_iter):
        van = sum(f / (1 + tasa) ** t for t, f in enumerate(Flujos))
        if abs(van) < precision:
            return tasa * 100  # TIR como porcentaje
        tasa += 0.0001
    raise ValueError("No se encontró una TIR con la precisión deseada.")

def WACC(Ke: float, E: float, Kd: float, D: float, Tc: float) -> float:
    """
    Calcula el WACC (Weighted Average Cost of Capital)

    Args:
        Ke (float): Coste del capital propio (en decimal, ej: 0.1 para 10%)
        E (float): Valor del capital propio
        Kd (float): Coste de la deuda (en decimal)
        D (float): Valor de la deuda
        Tc (float): Tasa impositiva (en decimal)

    Returns:
        float: WACC expresado como porcentaje
    """
    V = E + D
    return ((E / V) * Ke + (D / V) * Kd * (1 - Tc)) * 100

def PAYBACK(InversionInicial: float, FlujoCajaAnual: float) -> float:
    """
    Calcula el período de recuperación (Payback) de una inversión.

    Args:
        InversionInicial (float): Monto total invertido al inicio del proyecto.
        FlujoCajaAnual (float): Flujo de caja generado por año.

    Returns:
        float: Años necesarios para recuperar la inversión inicial. No tiene en cuenta el valor del dinero en el tiempo.
    """
    return InversionInicial / FlujoCajaAnual