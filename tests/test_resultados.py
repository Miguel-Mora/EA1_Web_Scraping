import pandas as pd
import pytest
from pathlib import Path

# Directorio principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

ARCHIVOS_CSV = [
    "resultados_beautifulsoup.csv",
    "resultados_selenium.csv",
    "resultados_scrapy.csv",
]

# Seis atributos comerciales comunes a los tres métodos
COLUMNAS_REQUERIDAS = [
    "Producto",
    "Precio_COP",
    "Vendedor",
    "Estado",
    "Disponibilidad",
    "URL",
]


@pytest.mark.parametrize("archivo", ARCHIVOS_CSV)
def test_archivos_csv_existen(archivo):
    """Verifica que los archivos CSV estén presentes."""
    assert (BASE_DIR / archivo).is_file()


@pytest.mark.parametrize("archivo", ARCHIVOS_CSV)
def test_columnas_requeridas(archivo):
    """Verifica que cada CSV contenga las columnas esperadas."""
    df = pd.read_csv(BASE_DIR / archivo, encoding="utf-8-sig")

    assert all(columna in df.columns for columna in COLUMNAS_REQUERIDAS)


@pytest.mark.parametrize("archivo", ARCHIVOS_CSV)
def test_datos_no_vacios(archivo):
    """Verifica que existan registros y que no tengan valores nulos."""
    df = pd.read_csv(BASE_DIR / archivo, encoding="utf-8-sig")

    assert not df.empty
    assert df[COLUMNAS_REQUERIDAS].notna().all().all()


@pytest.mark.parametrize("archivo", ARCHIVOS_CSV)
def test_precio_valido(archivo):
    """Verifica que los precios registrados sean positivos."""
    df = pd.read_csv(BASE_DIR / archivo, encoding="utf-8-sig")

    precios = pd.to_numeric(df["Precio_COP"], errors="coerce")

    assert precios.notna().all()
    assert (precios > 0).all()


def test_consistencia_entre_metodos():
    """Compara los seis atributos comerciales entre las herramientas."""
    columnas_comparacion = [
        "Producto",
        "Precio_COP",
        "Vendedor",
        "Estado",
        "Disponibilidad",
        "URL",
    ]

    resultados = [
        pd.read_csv(BASE_DIR / archivo, encoding="utf-8-sig")[
            columnas_comparacion
        ].reset_index(drop=True)
        for archivo in ARCHIVOS_CSV
    ]

    assert resultados[0].equals(resultados[1])
    assert resultados[1].equals(resultados[2])