# 🧾 fichaPax — Generador automático de fichas de pasajeros

Este proyecto automatiza la generación diaria de fichas de pasajeros a partir de un archivo CSV exportado por un sistema de gestión hotelera. El objetivo es reemplazar el proceso manual de completar formularios PDF, reduciendo errores, acelerando el check‑in y manteniendo un registro ordenado y estandarizado.

## 🎯 Objetivo del proyecto

En hotelería, cada ingreso de pasajeros requiere completar una ficha con datos personales, fechas de estadía y otra información relevante.  
Tradicionalmente, este proceso se realiza a mano, copiando datos desde el sistema de reservas hacia un formulario PDF o impreso.

Este proyecto busca:

* Automatizar la creación de fichas a partir de un CSV generado diariamente por el software de gestión.

* Completar automáticamente una plantilla PDF con los datos de cada pasajero.

* Generar una ficha por pasajero lista para:

* ser firmada en recepción, o

* ser completada parcialmente por el huésped si faltan datos.

## 🗂️ Cómo funciona

1. **Exportación diaria del CSV**

El sistema de gestión hotelera genera un archivo como:

´´´Code  
 	ingresos26\_12.csv  
Este archivo contiene las reservas del día: nombre, documento, fechas, nacionalidad, etc.

2. **Plantilla PDF**

El proyecto incluye una plantilla:

´´´Code  
plantilla\_formulario.pdf  
Esta plantilla fue adaptada para contener campos editables que coinciden con los nombres de las columnas del CSV.

3. **Script de Python**

El script:

´´´Code  
 	llenar\_fichas.py

realiza las siguientes tareas:

*  Lee el CSV.

*  Mapea cada columna del CSV a un campo del PDF.

* Genera un archivo FDF temporal.

* Completa la plantilla PDF con los datos del pasajero.

* Exporta una ficha por cada ingreso del día.

4.  **Salida**

El resultado es un conjunto de PDFs individuales, uno por pasajero, listos para imprimir o archivar digitalmente.

## 🔧 Tecnologías utilizadas

* Python 3

* csv para lectura de datos

*  pdftk o librerías equivalentes para completar PDFs

*  FDF como formato intermedio para rellenar campos

## 

## 📁 Estructura del repositorio

fichaPax/  
│  
├── ingresos26\_12.csv          \# Datos de ejemplo exportados del sistema hotelero  
├── plantilla\_formulario.pdf   \# Plantilla PDF con campos editables  
├── fichaPax.pdf               \# Ejemplo de ficha generada  
├── temp.fdf                   \# Archivo temporal usado para completar PDFs  
├── llenar\_fichas.py           \# Script principal  
└── README.md                  \# Este archivo

## 🚀 Próximos pasos

* Mejorar la detección de campos faltantes.  
* Generar logs diarios de fichas creadas.  
* Integrar un CLI simple para seleccionar fechas o archivos.  
* Exportar todas las fichas a una carpeta con fecha automática.  
  