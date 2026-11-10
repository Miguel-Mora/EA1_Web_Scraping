from pathlib import Path
from html import escape

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DIRECTORIO_SALIDA = BASE_DIR / "site"

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


def generar_tabla(nombre, archivo):
    """Genera una tabla HTML a partir de un CSV."""

    ruta = BASE_DIR / archivo

    datos = pd.read_csv(ruta, encoding="utf-8-sig")

    if datos.empty:
        raise ValueError(f"El archivo {archivo} no contiene registros")

    faltantes = set(COLUMNAS) - set(datos.columns)

    if faltantes:
        raise ValueError(
            f"Faltan columnas en {archivo}: {sorted(faltantes)}"
        )

    datos = datos[COLUMNAS].copy()

    datos["Precio_COP"] = datos["Precio_COP"].apply(
        lambda precio: f"${int(precio):,} COP"
    )

    tabla = datos.to_html(
        index=False,
        escape=True,
        classes="tabla-resultados",
        border=0,
    )

    return f"""
    <section class="tarjeta">
        <h2>{escape(nombre)}</h2>
        <p>Resultados obtenidos mediante {escape(nombre)}.</p>
        <div class="tabla-contenedor">
            {tabla}
        </div>
    </section>
    """


def generar_reporte():
    """Construye la página web de resultados."""

    DIRECTORIO_SALIDA.mkdir(
        parents=True,
        exist_ok=True,
    )

    secciones = []

    for nombre, archivo in ARCHIVOS.items():
        secciones.append(
            generar_tabla(nombre, archivo)
        )

    contenido = "\n".join(secciones)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>EA2 | Resultados de Web Scraping</title>

    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f5f9;
            color: #243247;
        }}

        header {{
            background: #17365d;
            color: white;
            padding: 45px 24px;
            text-align: center;
        }}

        header h1 {{
            margin-bottom: 12px;
        }}

        main {{
            max-width: 1100px;
            margin: 30px auto;
            padding: 0 20px;
        }}

        .tarjeta {{
            background: white;
            margin-bottom: 25px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 12px #00000012;
        }}

        .tabla-contenedor {{
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}

        th, td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
            text-align: left;
            overflow-wrap: anywhere;
        }}

        th {{
            background: #e9eff7;
        }}

        footer {{
            text-align: center;
            padding: 25px;
            color: #607086;
        }}
    </style>
</head>

<body>

    <header>
        <h1>Análisis de Información Comercial</h1>

        <p>
            Evidencia de Aprendizaje 2 |
            Programación para Análisis de Datos
        </p>

        <p>
            Apple iPhone 15 de 128 GB |
            Mercado Libre Colombia
        </p>
    </header>

    <main>

        <section class="tarjeta">
            <h2>Descripción del proyecto</h2>

            <p>
                Este proyecto académico presenta resultados
                de extracción de información comercial
                mediante BeautifulSoup, Selenium y Scrapy.
            </p>

            <p>
                Los datos proceden de una copia HTML
                almacenada localmente durante la EA1.
                No representan información en tiempo real.
            </p>
        </section>

        {contenido}

        <section class="tarjeta">
            <h2>Metodología</h2>

            <p>
                Se aplicaron técnicas de Web Scraping
                sobre una publicación comercial y
                se compararon seis atributos:
                producto, precio, vendedor, estado,
                disponibilidad y URL.
            </p>

            <p>
                Los archivos CSV fueron validados
                mediante pruebas automatizadas con pytest.
            </p>
        </section>

    </main>

    <footer>
        <p>
            Proyecto académico |
            Institución Universitaria Digital de Antioquia
        </p>

        <p>
            Página generada automáticamente con Python.
        </p>
    </footer>

</body>
</html>
"""

    destino = DIRECTORIO_SALIDA / "index.html"

    destino.write_text(
        html,
        encoding="utf-8",
    )

    print(f"Reporte generado correctamente: {destino}")


if __name__ == "__main__":
    generar_reporte()