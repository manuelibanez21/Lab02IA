# 📘 Proyecto – Agentes Inteligentes y Visualización de Datos  

Este repositorio contiene el desarrollo de dos puntos principales relacionados con:  

1. El ecosistema de visualización con **hvPlot** y su integración con diferentes librerías.  
2. Conceptos fundamentales de agentes inteligentes, campos de potencial artificial y el modelo **BDI (Belief–Desire–Intention)**.  

---

## 📑 Índice  

1. [Primer Punto – Ecosistema de hvPlot y Visualización en Python](#-primer-punto--ecosistema-de-hvplot-y-visualización-en-python)  
   - [Librerías de Datos](#-1-librerías-de-datos)  
   - [hvPlot (.plot API)](#-2-hvplot-plot-api)  
   - [Representación Intermedia](#-3-representación-intermedia)  
   - [Salida de Visualización](#-4-salida-de-visualización-backends)  
   - [Integración con Streamlit](#-5-integración-con-streamlit)  
   - [Conclusión](#-conclusión)  

2. [Segundo Punto – Agentes Inteligentes y Planificación de Trayectorias](#-segundo-punto--agentes-inteligentes-y-planificación-de-trayectorias)  
   - [Agente Inteligente](#-1-qué-es-un-agente-inteligente)  
   - [Campo de Potencial Artificial](#-2-campo-de-potencial-artificial-cpa)  
   - [Algoritmo BDI](#-3-algoritmo-bdi-beliefdesireintention)  
   - [Conclusión](#-conclusión-1)  

---

# 📌 Primer Punto – Ecosistema de hvPlot y Visualización en Python  

Este apartado explica cómo funcionan las librerías de datos y visualización que aparecen en el ecosistema de **hvPlot** y cómo se integran con otras herramientas.  

---

## 🔹 1. Librerías de Datos  

Son las fuentes donde se cargan, transforman o manipulan los datos antes de graficarlos. Algunas de las más destacadas son:  

- 🐼 **pandas** → Manejo de datos tabulares (DataFrames).  
- 🦕 **dask** → Procesamiento de grandes volúmenes de datos en paralelo.  
- 🌍 **GeoPandas** → Datos espaciales y mapas.  
- 📊 **xarray** → Datos multidimensionales (clima, simulaciones).  
- 🚀 **RAPIDS** → Procesamiento acelerado en GPU.  
- 🦆 **DuckDB** → Consultas SQL en archivos locales.  
- 🔗 **NetworkX** → Análisis de grafos y redes.  
- 📚 **Intake** → Carga estructurada de datasets.  
- 🐍 **Polars** → Manejo eficiente de datos columnar.  
- 🪶 **Ibis** → Lenguaje unificado para bases de datos.  

---

## 🔹 2. hvPlot (`.plot()` API)  

**hvPlot** es una extensión que unifica la forma de graficar datos.  
- Permite usar `.hvplot()` en lugar de `.plot()`.  
- Convierte los datos en **gráficos interactivos** con solo una línea de código.  

📍 Ejemplo:  

```python
import pandas as pd
import hvplot.pandas  

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})  
df.hvplot.line(x="x", y="y")  

