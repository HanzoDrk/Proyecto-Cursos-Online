import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos
from evaluaciones.evaluaciones import Evaluacion, Tarea, Examen

RUTA_ARCHIVO = os.path.join("data_manager", "evaluacion.json")

class GestorEvaluaciones:
    def __init__(self):
        self.evaluaciones = []
        self.cargar()

    def crear_evaluacion(self, tipo, titulo, descripcion, fecha_entrega):
        if tipo.lower() == "examen":
            nueva_evaluacion = Examen(titulo, descripcion, fecha_entrega)
        elif tipo.lower() == "tarea":
            nueva_evaluacion = Tarea(titulo, descripcion, fecha_entrega)
        else:
            raise ValueError("Tipo de evaluación no válido.")

        self.evaluaciones.append(nueva_evaluacion.to_dict())
        self.cargar()
        print(f"Evaluación {nueva_evaluacion.titulo} Creada. Tipo: {nueva_evaluacion.tipo()}")
        return nueva_evaluacion

    def registrar_calificacion(evaluacion, estudiante, calificacion):
        evaluacion.regitrar_calificacion(estudiante, calificacion)

    def mostrar_evaluaciones(self):
        if not self.evaluaciones:
            return "No hay evaluaciones registradas."
        lineas = []
        for evaluacion in self.evaluaciones:
            lineas.append(evaluacion.mostrar_informacion())
        return "\n".join(lineas)

    def eliminar_evaluacion(self,titulo):
        for evaluacion in self.evaluaciones:
            if evaluacion.titulo == titulo:
                self.evaluaciones.remove(evaluacion)
                print(f"Evaluación {evaluacion.titulo} se eliminó correctamente.")
                return
        print(f"No se encontró una evaluación con el título {titulo}.")

    def guardar(self):
        guardar_datos(RUTA_ARCHIVO, self.evaluaciones)

    def cargar(self):
        self.evaluaciones = cargar_datos(RUTA_ARCHIVO)