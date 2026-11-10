# Análisis de información comercial mediante Web Scraping

## Evidencias de aprendizaje 1 y 2

**Asignatura:** Programación para Análisis de Datos  
**Institución:** Institución Universitaria Digital de Antioquia  
**Producto analizado:** Apple iPhone 15 de 128 GB  
**Plataforma:** Mercado Libre Colombia

## 1. Descripción del proyecto

Este proyecto académico implementa técnicas de extracción y análisis
de información comercial utilizando Python.

La Evidencia de Aprendizaje 1 desarrolló un ejercicio de Web Scraping
sobre una publicación del Apple iPhone 15 de 128 GB en Mercado Libre
Colombia.

Se utilizaron tres herramientas:

- BeautifulSoup.
- Selenium.
- Scrapy.

Las tres implementaciones procesan información a partir de un documento
HTML almacenado localmente.

La Evidencia de Aprendizaje 2 continúa este proyecto mediante el uso
de Git, GitHub y prácticas de DevOps.

## 2. Objetivo general

Aplicar técnicas de extracción de datos y prácticas de control de
versiones, documentación y automatización para fortalecer la
reproducibilidad y mantenibilidad de un proyecto de software.

## 3. Datos analizados

Se extraen los siguientes atributos comerciales:

1. Nombre del producto.
2. Precio en pesos colombianos.
3. Vendedor.
4. Estado del producto.
5. Disponibilidad.
6. URL de la publicación.

Adicionalmente, los archivos CSV incluyen la fecha de procesamiento.

## 4. Herramientas utilizadas

- Python 3.11.
- BeautifulSoup.
- Selenium.
- Scrapy.
- pandas.
- Git.
- GitHub.
- Visual Studio Code.
- Jupyter Notebook.

## 5. Estructura del proyecto

```text
EA1_Web_Scraping/
├── .gitignore
├── iphone15_mercadolibre.html
├── Morales_Miguel_Analizando_EA1.ipynb
├── spider_iphone15.py
├── resultados_beautifulsoup.csv
├── resultados_selenium.csv
├── resultados_scrapy.csv
└── README.md
```

## 6. Preparación del entorno

### Crear un entorno virtual en Windows

```powershell
python -m venv .venv
```

### Activar el entorno

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar las dependencias

```powershell
python -m pip install requests beautifulsoup4 selenium scrapy pandas lxml ipykernel
```

### Abrir el notebook

Abrir `Morales_Miguel_Analizando_EA1.ipynb` en Visual Studio Code
y seleccionar el intérprete del entorno virtual `.venv`.

El archivo `iphone15_mercadolibre.html` debe encontrarse en la
carpeta principal del proyecto.

## 7. Metodología

El proyecto toma como referencia la metodología CRISP-DM para
organizar la comprensión de los datos, su preparación y la
evaluación descriptiva de los resultados.

La extracción se realiza sobre una copia HTML local de la publicación.

Este enfoque permite reproducir el ejercicio sin depender de
consultas en tiempo real a Mercado Libre.

## 8. Resultados de la Evidencia 1

Se obtuvo un registro comercial mediante cada herramienta.

En el análisis realizado se reportó:

- Completitud de los atributos seleccionados: 100 %.
- Consistencia entre los tres métodos: 100 %.
- Registros obtenidos: uno por herramienta.

Estos resultados corresponden a la publicación analizada y al
archivo HTML utilizado.

No deben interpretarse como una evaluación del comportamiento de
las herramientas en grandes volúmenes de datos o en navegación
web en tiempo real.

## 9. Control de versiones

El proyecto utiliza Git y GitHub para registrar los cambios.

La rama `main` conserva la versión principal del proyecto.

La rama `feature/ea2-devops` se utiliza para desarrollar las
mejoras correspondientes a la Evidencia de Aprendizaje 2.

Los cambios se documentan mediante commits y se integrarán
utilizando pull requests.

## 10. Automatización y DevOps

La Evidencia de Aprendizaje 2 contempla la incorporación de:

- Pruebas automatizadas.
- Integración continua mediante GitHub Actions.
- Documentación del flujo de trabajo.
- Un mecanismo de despliegue continuo apropiado para el proyecto.

Estas funcionalidades se documentarán conforme se implementen
y verifiquen.

## 11. Limitaciones

El ejercicio utiliza una única publicación comercial y un
documento HTML almacenado localmente.

Los resultados no representan un estudio estadístico del mercado
de teléfonos móviles ni permiten evaluar variaciones de precios
en tiempo real.

## 12. Finalidad académica

Proyecto desarrollado con fines de aprendizaje en la asignatura
Programación para Análisis de Datos de la IU Digital.