from cursos.cursos import Curso

cursos = []

def crear_curso():
    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripcion del curso: ")
    instructor = input("Ingrese el nombre del instructor: ")
    codigo = input("Ingrese el codigo del curso: ")

    nuevo_curso = Curso(nombre, descripcion, instructor, codigo)
    cursos.append(nuevo_curso)
    print(f"Curso: {nuevo_curso.nombre} Creado. Codigo: {nuevo_curso.codigo}")

def buscar_curso(nombre, codigo):
    for i in cursos:
        if i.nombre == nombre and i.codigo == codigo:
            return i
    return None

def mostrar_cursos():
    if not cursos:
        return "No Hay cursos registrados."
    lineas = []
    for curso in cursos:
        lineas.append(f"Curso: {curso.nombre} Codigo: {curso.codigo} Instructor: {curso.instructor.nombre}")
    return "\n".join(lineas)

def eliminar_curso(nombre, codigo):
    curso = buscar_curso(nombre, codigo)
    if curso:
        cursos.remove(curso)
        print(f"Curso {curso.nombre} se elimino correctamente.")

def incribir_estudiante_a_curso(curso, estudiante):
    curso.agregar_estudiante(estudiante)
    print(f"Estudiante {estudiante.nombre} inscrito en el curso {curso.nombre}.")


