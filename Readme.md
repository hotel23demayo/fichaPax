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

El proyecto utiliza la plantilla oficial del hotel:

´´´Code  
fichaPax.pdf  
Esta es la ficha original en formato PDF del Hotel 23 de Mayo.

3. **Script de Python**

El script:

´´´Code  
 	llenar\_fichas.py

realiza las siguientes tareas:

*  Lee el CSV y agrupa los registros por número de **voucher**.

*  De cada grupo de pasajeros con el mismo voucher, **selecciona al titular** (persona de mayor edad).

*  Extrae los **acompañantes** (hasta 3) con nombre y DNI.

*  Identifica todas las **habitaciones** que ocupa el grupo familiar.

*  Mapea solo los campos necesarios del CSV a posiciones específicas del PDF.

*  Los campos vacíos o con "No informado" se dejan en **blanco** para completar a mano.

* Sobrepone los datos sobre el PDF original sin modificar su diseño.

* Exporta **una ficha por voucher** (no por pasajero individual).

4.  **Salida**

El resultado es un conjunto de PDFs individuales en la carpeta `fichas/`, uno por cada **número de voucher**, con los datos del titular y acompañantes, listos para imprimir, firmar o completar en recepción.

## 🔧 Tecnologías utilizadas

* Python 3
* **csv** para lectura de datos
* **reportlab** para generar overlays de texto sobre PDFs
* **pypdf** para manipular y combinar PDFs
* Sistema de agrupación por voucher y selección automática de titular

## 📁 Estructura del repositorio

fichaPax/  
│  
├── ingresos26\_12.csv          \# Datos de ejemplo exportados del sistema hotelero  
├── fichaPax.pdf               \# Plantilla PDF oficial del Hotel 23 de Mayo  
├── llenar\_fichas.py           \# Script principal para generar fichas  
├── generar\_con\_overlay.py     \# Función que sobrepone datos al PDF  
├── previsualizar\_fichas.py    \# Script para previsualizar datos antes de generar  
├── fichas/                    \# Carpeta donde se guardan las fichas generadas  
└── README.md                  \# Este archivo

## 🚀 Uso

### Instalación de dependencias

```bash
pip install reportlab pypdf
```

### Generar fichas

```bash
python3 llenar_fichas.py
```

Las fichas se generarán en la carpeta `fichas/` con el formato:  
`ficha_voucher_XXXXXXXX.pdf`

### Previsualizar datos (opcional)

Para ver qué datos se van a rellenar antes de generar los PDFs:

```bash
python3 previsualizar_fichas.py
```

## ✨ Características principales

* ✅ **Una ficha por voucher** - Agrupa automáticamente por número de reserva
* ✅ **Titular automático** - Selecciona la persona de mayor edad del grupo
* ✅ **Acompañantes** - Incluye hasta 3 acompañantes con nombre y DNI
* ✅ **Múltiples habitaciones** - Si el grupo ocupa varias habitaciones, las muestra todas
* ✅ **Campos inteligentes** - Deja en blanco campos sin información para completar a mano
* ✅ **Diseño original** - Preserva el formato oficial del Hotel 23 de Mayo

## 🚀 Próximos pasos (ideas futuras)

* Generar logs diarios de fichas creadas con timestamp.
* Integrar un CLI interactivo para seleccionar fechas específicas.
* Exportar automáticamente a una carpeta con fecha del día.
* Enviar fichas por email a los huéspedes antes del check-in.  
  