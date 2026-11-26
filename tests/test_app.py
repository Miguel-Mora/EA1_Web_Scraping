
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parents[1] / "app.py"

METODOS = ("BeautifulSoup", "Selenium", "Scrapy")

COLUMNAS = {
    "Producto",
    "Precio_COP",
    "Vendedor",
    "Estado",
    "Disponibilidad",
    "URL",
}


def iniciar_app():
    app = AppTest.from_file(str(APP), default_timeout=15)
    app.run()
    assert not app.exception, "La aplicación produjo una excepción"
    return app


def test_aplicacion_inicia_sin_errores():
    app = iniciar_app()

    assert len(app.selectbox) == 1
    assert app.selectbox[0].value == "BeautifulSoup"


def test_selector_contiene_tres_metodos():
    app = iniciar_app()

    assert list(app.selectbox[0].options) == list(METODOS)


@pytest.mark.parametrize("metodo", METODOS)
def test_cambio_de_metodo(metodo):
    app = iniciar_app()

    app.selectbox[0].set_value(metodo).run()

    assert not app.exception
    assert app.selectbox[0].value == metodo
    assert any(
        f"Método activo: {metodo}" in elemento.value
        for elemento in app.success
    )


def test_tabla_muestra_atributos_comerciales():
    app = iniciar_app()

    assert len(app.dataframe) >= 1

    tabla = app.dataframe[0].value

    assert COLUMNAS.issubset(set(tabla.columns))
    assert len(tabla) > 0


def test_comparacion_incluye_tres_metodos():
    app = iniciar_app()

    assert len(app.dataframe) >= 2

    comparacion = app.dataframe[1].value

    assert set(comparacion["Método"]) == set(METODOS)
    assert comparacion["Precio (COP)"].notna().all()
    assert (comparacion["Precio (COP)"] > 0).all()
