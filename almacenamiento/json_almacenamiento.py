import json 
import os

def guardar_datos(ruta_archivo, datos): 
    directorio = os.path.dirname(ruta_archivo)
    # Extrae el nombre de la carpeta (directorio) de la ruta completa del archivo. 
    # Por ejemplo, si la ruta es 'almacenamiento/cursos.json', 'directorio' será 'almacenamiento'.
    if directorio and not os.path.exists(directorio):
    # aqui se verifica si se extrajo un nombre de directorio 
    # comprueba si esa carpeta no existe.
        os.makedirs(directorio)
        # Si la carpeta no existe, 'os.makedirs' la crea.
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos(ruta_archivo): 
    if not os.path.exists(ruta_archivo):
        return []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
