"""Starter code para Visualização de Dados em Python

Este script fornece exemplos básicos de como carregar o arquivo `data.csv`
e gerar gráficos com `matplotlib`. Também inclui um exemplo opcional com
`plotly` se estiver instalado.

Instruções rápidas:
- Rode: `python3 starter-code.py` para gerar arquivos PNG com os gráficos.
- Para funcionalidades avançadas, instale dependências: `pip install pandas matplotlib plotly`
"""
import csv
import os
from datetime import datetime

try:
    import pandas as pd
except Exception:
    pd = None

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None

try:
    import plotly.express as px
except Exception:
    px = None


DATA_PATH = os.path.join(os.path.dirname(__file__), "data.csv")


def load_data(path=DATA_PATH):
    if pd:
        df = pd.read_csv(path, parse_dates=["date"]) if "date" in open(path).read() else pd.read_csv(path)
        return df

    # fallback: simple csv reader returning list of dicts
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def example_matplotlib(df):
    if plt is None:
        print("matplotlib não está instalado. Instale com: pip install matplotlib")
        return

    # Se df for lista de dicts, convertendo rapidamente para colunas simples
    if not hasattr(df, "plot"):
        # converte para colunas simples
        categories = [r.get("category") for r in df]
        values = [float(r.get("value", 0)) for r in df]
    else:
        categories = df["category"] if "category" in df else df.iloc[:, 0]
        values = df["value"] if "value" in df else df.iloc[:, 1]

    # Gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color="C0")
    plt.title("Exemplo: Gráfico de Barras")
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.savefig("bar_plot.png")
    print("Salvou bar_plot.png")

    # Gráfico de linha (se houver coluna date ou índice ordenável)
    try:
        if hasattr(df, "plot") and "date" in df:
            plt.figure(figsize=(6, 4))
            plt.plot(df["date"], df["value"], marker="o")
            plt.title("Exemplo: Série Temporal")
            plt.xlabel("Date")
            plt.ylabel("Value")
            plt.tight_layout()
            plt.savefig("line_plot.png")
            print("Salvou line_plot.png")
    except Exception:
        pass


def example_plotly(df):
    if px is None:
        print("plotly não está instalado. Para instalar: pip install plotly")
        return

    # Exemplo rápido com plotly express
    try:
        if hasattr(df, "plot"):
            fig = px.bar(df, x="category", y="value", title="Bar com Plotly")
        else:
            # converter lista de dicts em lists para plotly
            cats = [r.get("category") for r in df]
            vals = [float(r.get("value", 0)) for r in df]
            fig = px.bar(x=cats, y=vals, labels={"x": "category", "y": "value"}, title="Bar com Plotly")

        fig.write_html("plotly_bar.html")
        print("Salvou plotly_bar.html")
    except Exception as e:
        print("Erro ao criar gráfico plotly:", e)


def main():
    data = load_data()
    print("Dados carregados:")
    if hasattr(data, "head"):
        print(data.head())
        print(data.describe())
    else:
        print(data[:5])

    example_matplotlib(data)
    # Executar plotly se desejar
    example_plotly(data)


if __name__ == "__main__":
    main()
