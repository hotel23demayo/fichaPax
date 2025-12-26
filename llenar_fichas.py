import csv
import os


# Configuración
PDF_PLANTILLA = 'plantilla_formulario.pdf'
CSV_DATOS = 'ingresos26_12.csv'


def llenar_pdf(datos_huesped):
    # Nombre del archivo de salida (ej: Oporto_Jose.pdf)
    nombre_salida = f"fichas/ficha_{datos_huesped['Apellido y nombre'].replace(' ', '_')}.pdf"
    
    # Mapeo: 'NombreEnPDF': 'NombreEnCSV'
    # Ajusta los nombres de la izquierda a los que pusiste en LibreOffice
    mapeo = {
        'Nombre': datos_huesped['Apellido y nombre'],
        'dni': datos_huesped['Nro. doc.'],
        'Numero': datos_huesped['Nro. habitación'],
        'Voucher': datos_huesped['Voucher'],
        'ingreso': datos_huesped['Fecha de ingreso'],
        'egreso': datos_huesped['Fecha de egreso'],
        'seccional': datos_huesped['Sede']
    }


    # Generamos los argumentos para pdftk
    campos = ""
    for campo, valor in mapeo.items():
        campos += f"f {campo} {valor} " # Simplificado para el ejemplo


    # Usamos una técnica de pdftk para llenar sin crear archivos FDF intermedios
    # Si los nombres tienen espacios, se complica, por eso usamos FDF o librerías
    # Aquí te sugiero instalar fdfgen: pip install fdfgen
    from fdfgen import forge_fdf
    fields = [ (k, v) for k, v in mapeo.items() ]
    fdf = forge_fdf("", fields, [], [], [])
    
    with open("temp.fdf", "wb") as fdf_file:
        fdf_file.write(fdf)


    os.system(f"pdftk {PDF_PLANTILLA} fill_form temp.fdf output {nombre_salida} flatten")


# Crear carpeta de salida
if not os.path.exists('fichas'):
    os.makedirs('fichas')


with open(CSV_DATOS, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for fila in reader:
        print(f"Generando ficha para: {fila['Apellido y nombre']}")
        llenar_pdf(fila)


print("¡Proceso completado!")
