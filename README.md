
# Análisis de información comercial mediante Web Scraping

## Evidencias de Aprendizaje 1, 2 y 3

**Asignatura:** Programación para Análisis de Datos  
**Institución:** Institución Universitaria Digital de Antioquia  
**Producto:** Apple iPhone 15 de 128 GB  
**Plataforma de origen:** Mercado Libre Colombia

## 1. Introducción

Este proyecto académico aplica técnicas de extracción de información
comercial, control de versiones, pruebas automatizadas e integración
y despliegue continuo mediante herramientas de desarrollo de software.

El proyecto se desarrolla progresivamente:

- **EA1:** extracción de datos mediante BeautifulSoup, Selenium y Scrapy.
- **EA2:** control de versiones, pruebas automatizadas, GitHub Actions
  y publicación de un reporte HTML en GitHub Pages.
- **EA3:** aplicación web interactiva desarrollada con Streamlit,
  pruebas adicionales y despliegue mediante Streamlit Community Cloud.

Los datos proceden de una copia HTML local de una publicación comercial.
No corresponden a precios actualizados en tiempo real.

## 2. Objetivo

Implementar un proyecto reproducible de análisis de información comercial,
incorporando control de versiones, pruebas automatizadas, integración
continua y publicación de resultados mediante servicios en la nube.

## 3. Datos y metodología

La fuente utilizada es `iphone15_mercadolibre.html`, almacenada durante
la EA1.

Se analizan seis atributos comerciales:

1. Producto.
2. Precio en pesos colombianos.
3. Vendedor.
4. Estado.
5. Disponibilidad.
6. URL de la publicación.

Las herramientas BeautifulSoup, Selenium y Scrapy generaron los
archivos CSV utilizados por la aplicación.

El trabajo toma como referencia la metodología CRISP-DM para organizar
la comprensión, preparación y análisis de los datos.

## 4. Tecnologías utilizadas

- Python 3.11 para el desarrollo y las pruebas locales.
- BeautifulSoup, Selenium y Scrapy.
- pandas.
- Streamlit.
- pytest.
- Git y GitHub.
- GitHub Actions.
- GitHub Pages.
- Streamlit Community Cloud.
- Visual Studio Code y Jupyter Notebook.

## 5. Estructura del proyecto

```text
EA1_Web_Scraping/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   ├── test_resultados.py
│   └── test_app.py
├── .gitignore
├── app.py
├── generar_reporte.py
├── iphone15_mercadolibre.html
├── Morales_Miguel_Analizando_EA1.ipynb
├── README.md
├── requirements.txt
├── resultados_beautifulsoup.csv
├── resultados_selenium.csv
├── resultados_scrapy.csv
└── spider_iphone15.py
```

La carpeta `.venv/`, las cachés y los archivos HTML generados
localmente no se incluyen en el repositorio.

## 6. Instalación

Clonar el repositorio:

```powershell
git clone https://github.com/Miguel-Mora/EA1_Web_Scraping.git
cd EA1_Web_Scraping
```

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Instalar las dependencias principales de EA3:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Los comandos anteriores están preparados para PowerShell en Windows.

Para reproducir el notebook y los procesos originales de extracción
pueden requerirse otras bibliotecas, como BeautifulSoup, Selenium,
Scrapy y lxml, según el procedimiento ejecutado.

## 7. Ejecutar la aplicación

Desde la carpeta principal del proyecto:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Abrir la dirección indicada por Streamlit, normalmente:

http://localhost:8501

La aplicación permite:

- Seleccionar BeautifulSoup, Selenium o Scrapy.
- Consultar los datos comerciales almacenados.
- Visualizar indicadores y tablas.
- Comparar los precios obtenidos por cada método.

## 8. Pruebas automatizadas

El proyecto utiliza pytest para validar los resultados y la
aplicación web.

Ejecutar todas las pruebas:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

Se implementaron **20 pruebas automatizadas**:

- 13 pruebas de la EA2 sobre los archivos CSV.
- 7 pruebas de la EA3 sobre la aplicación Streamlit.

Las pruebas verifican la estructura y consistencia de los datos,
así como el inicio de la aplicación, el selector y las tablas.

No vuelven a ejecutar los procesos de scraping en Internet.

## 9. Control de versiones

Se utiliza Git para mantener el historial del proyecto.

- `main`: rama principal.
- `feature/ea2-devops`: desarrollo realizado durante EA2.
- `feature/ea3-app`: desarrollo de la aplicación Streamlit durante EA3.

Las mejoras se incorporan mediante commits y pull requests.

## 10. Automatización con GitHub Actions

El archivo `.github/workflows/ci.yml` define el pipeline.

El workflow se ejecuta ante:

- Eventos `push` en las ramas configuradas.
- Eventos `pull_request` dirigidos a `main`.

El trabajo de validación realiza las siguientes operaciones:

1. Descarga el repositorio.
2. Configura Python 3.11.
3. Instala las dependencias desde `requirements.txt`.
4. Ejecuta las pruebas automatizadas con pytest.
5. Genera el reporte HTML mediante `generar_reporte.py`.
6. Verifica la existencia de `site/index.html`.

Cuando se ejecuta un `push` sobre `main`, el workflow también
prepara y publica el reporte HTML mediante GitHub Pages.

Los trabajos de despliegue dependen de la finalización satisfactoria
de las validaciones anteriores.

## 11. Despliegue de servicios

### GitHub Pages — EA2

El reporte HTML generado automáticamente se publica en:

https://miguel-mora.github.io/EA1_Web_Scraping/

Su publicación se realiza mediante GitHub Actions después de
integrar cambios en la rama `main`.

### Streamlit Community Cloud — EA3

La aplicación interactiva está disponible en:

https://ea1webscraping-jkjjq2ayqrjxjhhcebtjsf.streamlit.app/

Configuración utilizada:

- Repositorio: `Miguel-Mora/EA1_Web_Scraping`.
- Rama de despliegue: `feature/ea3-app`.
- Archivo principal: `app.py`.
- Dependencias: `requirements.txt`.
- Servicio: Streamlit Community Cloud.

Streamlit Community Cloud gestiona la construcción y publicación
de la aplicación desde la rama conectada.

Es importante distinguir este mecanismo del despliegue de
GitHub Pages ejecutado directamente por GitHub Actions.

## 12. Resultados

Durante la EA1 se obtuvo un registro comercial por herramienta,
con consistencia en los seis atributos seleccionados.

La EA2 incorporó pruebas y automatización del reporte HTML.

La EA3 amplió la solución mediante una interfaz interactiva y siete
pruebas adicionales.

La ejecución del pipeline de EA3 en GitHub Actions finalizó
satisfactoriamente con **20 pruebas aprobadas**.

## 13. Limitaciones

El proyecto utiliza una sola publicación comercial y archivos CSV
generados a partir de una copia HTML local.

No realiza monitoreo continuo del mercado, scraping periódico ni
actualización automática de precios.

La aplicación representa los resultados históricos del ejercicio.

## 14. Finalidad académica

Proyecto desarrollado para la asignatura Programación para
Análisis de Datos de la Institución Universitaria Digital
de Antioquia.
