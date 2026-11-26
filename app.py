
from pathlib import Path

import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parent

ARCHIVOS = {
    "BeautifulSoup": "resultados_beautifulsoup.csv",
    "Selenium": "resultados_selenium.csv",
    "Scrapy": "resultados_scrapy.csv",
}

COLUMNAS = [
    "Producto",
    "Precio_COP",
    "Vendedor",
    "Estado",
    "Disponibilidad",
    "URL",
]


@st.cache_data
def cargar_datos():
    resultados = {}

    for metodo, archivo in ARCHIVOS.items():
        ruta = BASE / archivo
        datos = pd.read_csv(ruta)

        faltantes = set(COLUMNAS) - set(datos.columns)
        if faltantes:
            raise ValueError(
                f"{archivo} no contiene: {sorted(faltantes)}"
            )

        resultados[metodo] = datos

    return resultados


st.set_page_config(
    page_title="Análisis Comercial | EA3",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Análisis de Información Comercial")
st.subheader("EA3 | Programación para Análisis de Datos")

st.info(
    "Los datos proceden de una copia HTML local de "
    "Mercado Libre Colombia utilizada en la EA1. "
    "No representan precios en tiempo real."
)

try:
    resultados = cargar_datos()
except (FileNotFoundError, ValueError) as error:
    st.error(f"No se pudieron cargar los datos: {error}")
    st.stop()

metodo = st.selectbox(
    "Selecciona el método de extracción",
    list(resultados.keys()),
)

datos = resultados[metodo]


DESCRIPCIONES = {
    "BeautifulSoup": (
        "Analiza la estructura HTML mediante selectores "
        "y permite extraer información de sus elementos."
    ),
    "Selenium": (
        "Automatiza la interacción con un navegador "
        "y permite trabajar con contenido web dinámico."
    ),
    "Scrapy": (
        "Framework especializado en extracción "
        "estructurada de información mediante spiders."
    ),
}

st.success(f"Método activo: {metodo}")
st.write(DESCRIPCIONES[metodo])


col1, col2, col3 = st.columns(3)

col1.metric("Método seleccionado", metodo)
col2.metric("Registros disponibles", len(datos))
col3.metric("Atributos comunes", len(COLUMNAS))

st.markdown("### Resultados del método seleccionado")
st.dataframe(
    datos[COLUMNAS],
    use_container_width=True,
    hide_index=True,
)

st.markdown("### Comparación entre métodos")

comparacion = []

for nombre, tabla in resultados.items():
    precios = pd.to_numeric(
        tabla["Precio_COP"]
        .astype(str)
        .str.replace(r"[^\d]", "", regex=True),
        errors="coerce",
    )

    comparacion.append({
        "Método": nombre,
        "Precio (COP)": precios.iloc[0] if len(precios) else None,
    })

tabla_comparacion = pd.DataFrame(comparacion)

st.dataframe(
    tabla_comparacion,
    use_container_width=True,
    hide_index=True,
)

st.bar_chart(
    tabla_comparacion.set_index("Método")["Precio (COP)"]
)

st.caption(
    "Proyecto académico desarrollado con Python, "
    "pandas y Streamlit."
)
