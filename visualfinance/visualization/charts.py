import plotly.express as px
import pandas as pd

__all__ = [
    "plot_histogram",
    "plot_timeline"
]

def plot_histogram(df: pd.DataFrame,value_name="Value",nbins=30):
    df_melted = df.melt(var_name="Ticker", value_name=value_name)
    
    fig = px.histogram(df_melted, x=value_name, color="Ticker", nbins=nbins,
                       title=f"Distribución de {value_name} por activo",
                       opacity=0.5)
    fig.update_layout(template="plotly_white",barmode='overlay')
    fig.show()
    
def plot_timeline(df: pd.DataFrame, value_name="Value"):
    df_reset = df.copy()
    df_reset.index.name = "Date"
    df_reset = df_reset.reset_index().melt(id_vars="Date", var_name="Ticker", value_name=value_name)

    fig = px.line(df_reset, x="Date", y=value_name, color="Ticker", title=f"{value_name} de activos en el tiempo")
    fig.update_layout(template="plotly_white")
    fig.show()