def FCF(Nopat: float, Depreciacion: float, Amortizacion: float,
        Capex: float, VariacionCapitalTrabajo: float) -> float:
    """
    Calcula el Flujo de Caja Libre (Free Cash Flow, FCF).

    Args:
        Nopat (float): Beneficio operativo despues de impuestos (Net Operating Profit After Taxes).
        Depreciacion (float): Depreciación contable del periodo.
        Amortizacion (float): Amortización contable del periodo.
        Capex (float): Gastos de capital (inversiones en activos).
        VariacionCapitalTrabajo (float): Cambios en capital de trabajo operativo.

    Returns:
        float: FCF --> Efectivo disponible para accionistas y acreedores.
    """

    return Nopat + Depreciacion + Amortizacion - Capex - VariacionCapitalTrabajo

def NOPAT(Ebit:float,TasaImpositiva:float)->float:
    """
    Beneficio operativo despues de impuestos (Net Operating Profit After Taxes)

    Args:
        Ebit (float): Beneficio antes de intereses e impuestos (Earnings Before Interest and Taxes)
        TasaImpositiva (float): Tasa de deducciones fiscales (impuestos)

    Returns:
        float: NOPAT (Net Operating Profit After Taxes) --> Mide el rendimiento operativo real descontando impuestos, pero sin tener en cuenta la deuda
    """
    return Ebit/(1-TasaImpositiva)

def EBIT(Ingresos:float,CostosOperativos:float,GastosGenerales:float)->float:
    """
    Beneficio antes de intereses e impuestos (Earnings Before Interest and Taxes)

    Args:
        Ingresos (float): Ingresos totales de la empresa
        CostosOperativos (float): Costos operacionales de la empresa para producir sus ingresos
        GastosGenerales (float): Gastos generales que no necesariamente son operativos (Excluye intereses e impuestos)

    Returns:
        float: Evalúa la rentabilidad operativa pura, sin considerar la deuda ni los impuestos
    """
    return Ingresos-(CostosOperativos+GastosGenerales)

def EBITDA(Ebit:float,Depreciacion:float,Amortizacion:float)->float:
    """Beneficio antes de intereses, impuestos, depreciaciones y amortizaciones.

    Args:
        Ebit (float): Beneficio antes de intereses e impuestos (Earnings Before Interest and Taxes)
        Depreciacion (float): Asignación contable que refleja la pérdida de valor de activos físicos (como maquinaria) por uso o tiempo
        Amortizacion (float): Similar a la depreciación, pero para activos intangibles (como licencias o software)

    Returns:
        float: Mide la rentabilidad operativa antes de impactos contables y financieros. Ideal para comparar empresas con diferentes estructuras financieras
    """
    return Ebit+Depreciacion+Amortizacion