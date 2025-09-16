import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos

RUTA_ARCHIVO = os.path.join("data_manager", "reportes.json")

class Repotes:
    def __init__(self):
        self.promedios = {}
        self.estudiantes_bajo = []
        self.cargar()

def promedio_por_estudiante(self, curso):

    for estudiante in curso.estudiantes:
        total = 0
        for evaluacion in curso.evaluaciones:
            if estudiante.id_usuario in evaluacion.calificaciones:
                total += evaluacion.calificaciones[estudiante.id_usuario]
        promedio = total / len(curso.evaluaciones) if curso.evaluaciones else 0
        self.promedios[estudiante.nombre] = promedio
    return self.promedios

def estudiantes_promedio_bajo(self,curso, limite=60):
    promedio = promedio_por_estudiante(curso)
    
    for nombre, promedio in self.promedios.items():
        if promedio < limite:
            self.estudiantes_bajo.append(nombre)
    return self.estudiantes_bajo

def guardar(self):
        guardar_datos(RUTA_ARCHIVO, self.promedios, self.estudiantes_bajo)

def cargar(self):
        promedio_por_estudiante = cargar_datos(RUTA_ARCHIVO)