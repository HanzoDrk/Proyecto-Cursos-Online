import json 
import os

def guardar_datos(ruta_archivo, datos): #Guardar datos en un archivo json
    with open(ruta_archivo, 'w', encoding='utf=8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos(ruta_archivo): #Cargar datos desde un archivo json
    if not os.path.exists(ruta_archivo):
        return []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)