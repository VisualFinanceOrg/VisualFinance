def ROI(Beneficio:float,Inversion:float)->float:
    """
    Retorno sobre una inversión, puede ser un proyecto, empresa, producto, etc. Es una metrica general.

    Args:
        Beneficio (float): Beneficio obtenido sobre la inversión
        Inversion (float): Dinero aportado para un producto/proyecto

    Returns:
        float: ROI (Return on Investment) --> Mide la ganancia obtenida respecto al coste de inversión
    """
    return (Beneficio/Inversion)*100

def ROIC(Nopat:float,CapitalInvertido:float)->float:
    """
    Rentabilidad de una empresas sobre un capital que ha sido efectivamente invertido, se centra en el capital operativo total.
    El ROIC es más efectivo al evaluar una empresa porque excluye inversiones no relacionadas con el negocio

    Args:
        Nopat (float): Beneficio operativo despues de impuestos (Net Operating Profit After Taxes)
        CapitalInvertido (float): Capital invertido

    Returns:
        float: ROIC (Return on Invested Capital) --> Evalúa eficiencia operativa con el capital efectivamente invertido
    """
    return (Nopat/CapitalInvertido) * 100

def ROE(BeneficioNeto: float, PatrimonioNeto: float) -> float:
    """
    Beneficio neto sobre el patrimonio neto. Mide la rentabilidad para el accionista.

    Args:
        BeneficioNeto (float): Beneficio neto obtenido por la empresa en un período determinado.
        PatrimonioNeto (float): Capital contable o recursos propios aportados por los accionistas.

    Returns:
        float: ROE (Return on Equity) --> Cuánto gana la empresa por el dinero de los accionistas, expresado en porcentaje.
    """
    return (BeneficioNeto / PatrimonioNeto) * 100

def ROA(BeneficioNeto: float, ActivosTotales: float) -> float:
    """
    Calcula el ROA (Return on Assets), que mide la rentabilidad sobre los activos totales.

    Args:
        BeneficioNeto (float): Beneficio neto generado por la empresa durante un período determinado.
        ActivosTotales (float): Total de activos que posee la empresa, incluyendo activos corrientes y no corrientes.

    Returns:
        float: ROA expresado como porcentaje. Indica cuánta rentabilidad genera la empresa por cada unidad de activo.
    """
    return (BeneficioNeto / ActivosTotales) * 100

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

def InterestCoverageRatio(Ebit: float, Intereses: float) -> float:
    """
    Calcula la cobertura de intereses (Interest Coverage Ratio).

    Args:
        Ebit (float): Beneficio antes de intereses e impuestos.
        Intereses (float): Gastos por intereses.

    Returns:
        float: Ratio --> Muestra cuántas veces se pueden cubrir los intereses con el Ebit.
    """
    return Ebit / Intereses

def DeudaSobreEBITDA(DeudaNeta: float, Ebitda: float) -> float:
    """
    Calcula el ratio Deuda / Ebitda.

    Args:
        DeudaNeta (float): Total de deuda menos caja disponible.
        Ebitda (float): Ganancia operativa antes de depreciaciones e impuestos.

    Returns:
        float: Años necesarios para repagar la deuda usando el Ebitda.
    """
    return DeudaNeta / Ebitda

def MargenOperativo(Ebit: float, Ventas: float) -> float:
    """
    Calcula el margen operativo de una empresa.

    Args:
        Ebit (float): Beneficio antes de intereses e impuestos.
        Ventas (float): Ingresos totales por ventas.

    Returns:
        float: Margen operativo (%) --> Indica cuánto beneficio operativo se genera por cada unidad de venta.
    """
    return (Ebit / Ventas) * 100

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