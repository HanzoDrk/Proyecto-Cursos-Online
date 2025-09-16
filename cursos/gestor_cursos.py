import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos
from cursos.cursos import Curso

RUTA_ARCHIVO = os.path.join("data_manager", "cursos.json")

class GestorCursos:
    def __init__(self):
        self.cursos = []
        self.cargar()

    def crear_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        descripcion = input("Ingrese la descripcion del curso: ")
        instructor = input("Ingrese el nombre del instructor: ")
        codigo = input("Ingrese el codigo del curso: ")

        nuevo_curso = Curso(nombre, descripcion, instructor, codigo)
        self.cursos.append(nuevo_curso.to_dict())
        self.guardar()
        print(f"Curso: {nuevo_curso.nombre} Creado. Codigo: {nuevo_curso.codigo}")

    def buscar_curso(self, nombre, codigo):
        for i in self.cursos:
            if i.nombre == nombre and i.codigo == codigo:
                return i
        return None

    def mostrar_cursos(self):
        if not self.cursos:
            return "No Hay cursos registrados."
        lineas = []
        for curso in self.cursos:
            lineas.append(f"Curso: {curso.nombre} Codigo: {curso.codigo} Instructor: {curso.instructor.nombre}")
        return "\n".join(lineas)

    def eliminar_curso(self, nombre, codigo):
        curso = buscar_curso(nombre, codigo)
        if curso:
            self.cursos.remove(curso.to_dict())
            self.guardar()
            print(f"Curso {curso.nombre} se elimino correctamente.")

    def incribir_estudiante_a_curso(curso, estudiante):
        curso.agregar_estudiante(estudiante)
        print(f"Estudiante {estudiante.nombre} inscrito en el curso {curso.nombre}.")
    
    def guardar(self):
        guardar_datos(RUTA_ARCHIVO, self.cursos)

    def cargar(self):
        self.cursos = cargar_datos(RUTA_ARCHIVO)


