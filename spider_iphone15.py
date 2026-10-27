
from pathlib import Path
import scrapy


class Iphone15Spider(scrapy.Spider):
    """Extrae información comercial del iPhone 15 desde un HTML local."""

    name = "iphone15"

    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "LOG_LEVEL": "INFO"
    }

    async def start(self):
        """Genera la solicitud inicial para procesar el HTML local."""

        ruta_html = Path("iphone15_mercadolibre.html").resolve()

        yield scrapy.Request(
            url=ruta_html.as_uri(),
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        """Extrae los atributos comerciales mediante selectores CSS."""

        # Nombre del producto
        nombre = response.css("h1::text").get()

        if nombre:
            nombre = nombre.strip()

        # Precio principal
        precio_texto = response.css(
            '[itemprop="price"]::attr(content)'
        ).get()

        precio = int(precio_texto) if precio_texto else None

        # Vendedor de la oferta seleccionada
        textos_vendedor = response.css(
            ".ui-seller-data-header__title"
        ).xpath(".//text()").getall()

        vendedor = " ".join(
            texto.strip()
            for texto in textos_vendedor
            if texto.strip()
        )

        if vendedor:
            vendedor = vendedor.replace("Vendido por", "").strip()
        else:
            vendedor = None

        # Estado del producto
        subtitulo = response.css(
            ".ui-pdp-subtitle::text"
        ).get()

        estado = (
            subtitulo.split("|")[0].strip()
            if subtitulo
            else None
        )

        # Disponibilidad
        disponibilidad = response.xpath(
            '//span[normalize-space(.)="¡Última en Stock!"]'
            '/text() | '
            '//p[normalize-space(.)="¡Última en Stock!"]/text()'
        ).get()

        if disponibilidad:
            disponibilidad = disponibilidad.strip()

        # URL original de la publicación
        url = response.css(
            'link[rel="canonical"]::attr(href)'
        ).get()

        # Entregar el registro estructurado
        yield {
            "Producto": nombre,
            "Precio_COP": precio,
            "Vendedor": vendedor,
            "Estado": estado,
            "Disponibilidad": disponibilidad,
            "URL": url
        }
