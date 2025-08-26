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
# 📌 Segundo Punto – Agentes Inteligentes y Planificación de Trayectorias  

En este apartado se revisan los conceptos fundamentales relacionados con agentes inteligentes y un modelo de toma de decisiones denominado **BDI (Belief–Desire–Intention)**, el cual se aplica en la planificación de trayectorias.  

---

## 🔹 1. ¿Qué es un Agente Inteligente?  

Un **agente inteligente** es una entidad (software, robot o sistema) capaz de percibir su entorno mediante sensores y actuar sobre él a través de actuadores, con el fin de alcanzar objetivos definidos.  
Se caracteriza por:  
- **Autonomía** → Decide y actúa sin intervención constante.  
- **Adaptabilidad** → Aprende o ajusta su comportamiento ante cambios en el entorno.  
- **Racionalidad** → Selecciona acciones que maximizan sus posibilidades de éxito.  
- **Interactividad** → Puede comunicarse y cooperar con otros agentes o usuarios.  

---

## 🔹 2. Campo de Potencial Artificial (CPA)  

El **campo de potencial artificial** es una técnica utilizada en planificación de trayectorias y control de robots móviles.  
La idea central es modelar el espacio de navegación como un campo de fuerzas:  

- ⚡ **Campo de atracción** → El objetivo ejerce una fuerza atractiva que guía al agente hacia la meta.  
- ⚡ **Campo de repulsión** → Los obstáculos generan una fuerza repulsiva que evita colisiones.  

De esta manera, el movimiento del agente surge como resultado de la suma vectorial de ambas fuerzas.  
✔️ Ventaja: método simple y rápido de implementar.  
❌ Limitación: puede presentar **mínimos locales**, atrapando al agente en posiciones no deseadas.  

---

## 🔹 3. Algoritmo BDI (Belief–Desire–Intention)  

El modelo **BDI** es un enfoque clásico de razonamiento para agentes inteligentes que imita la toma de decisiones humana.  

- **Beliefs (Creencias)** → Información que el agente tiene sobre el mundo y su estado actual.  
- **Desires (Deseos)** → Objetivos o estados finales que el agente quisiera alcanzar.  
- **Intentions (Intenciones)** → Conjunto de planes y acciones que el agente elige ejecutar para cumplir sus deseos, dadas sus creencias.  

Este modelo permite que un agente no solo reaccione a estímulos, sino que **planifique, seleccione y ejecute acciones de manera deliberativa**.  
Se utiliza en **planificación de trayectorias**, sistemas multiagente, robótica autónoma y simulaciones de comportamiento.  

---

## 🔹 Conclusión  

Los agentes inteligentes, en combinación con técnicas como el **campo de potencial artificial** y el **modelo BDI**, proporcionan un marco sólido para diseñar sistemas autónomos capaces de **navegar, tomar decisiones y adaptarse dinámicamente** a su entorno.  

