import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos
from cursos.cursos import Curso

RUTA_ARCHIVO = os.path.join("almacenamiento", "cursos.json")

class GestorCursos:
    def __init__(self, gestor_usuarios):
        self.cursos = []
        self.gestor_usuarios = gestor_usuarios
        self.cargar()

    def crear_curso(self, nombre, descripcion, codigo, instructor_id):
        if self.buscar_curso(codigo):
            print(f"Error: Ya existe un curso con el codigo: {codigo}")
            return None
        
        instructor = self.gestor_usuarios.buscar_usuario_id(instructor_id)
        if not instructor or instructor.rol.lower() != "instructor":
            print(f"Error: No se encontro ningun instructor con el id {instructor_id}")
            return None
        
        nuevo_curso = Curso(nombre, descripcion, instructor, codigo)
        self.cursos.append(nuevo_curso)
        self.guardar()
        print(f"Curso '{nuevo_curso.nombre}' creado. Código: {nuevo_curso.codigo}")
        return nuevo_curso

    def buscar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def mostrar_cursos(self):
        if not self.cursos:
            return "No Hay cursos registrados."
        
        lineas = []
        for curso in self.cursos:
            lineas.append(str(curso))
        return "\n".join(lineas)

    def eliminar_curso(self, codigo):
        curso_eliminar = self.buscar_curso(codigo)
        if curso_eliminar:
            self.cursos.remove(curso_eliminar)
            self.guardar()
            print(f"Curso {curso_eliminar.nombre} se elimino correctamente.")
        else:
            print(f"Error: No se encontro un curso con el codigo {codigo}")

    def inscribir_estudiante(self, codigo_curso, id_estudiante): # Cambio de nombre de la variable para ser consistente
        curso = self.buscar_curso(codigo_curso)
        if not curso:
            print(f"Error: No existe un curso con el codigo {codigo_curso}")
            return None
        
        estudiante = self.gestor_usuarios.buscar_usuario_id(id_estudiante) # Cambiado: No existe la funcion buscar_usuario_id, se asume que se llama buscar_usuario_por_id
        if not estudiante or estudiante.rol != "Estudiante":
            print(f"Error: No se encontró un estudiante con el ID '{id_estudiante}'.")
            return 

        try:
            curso.agregar_estudiante(estudiante)
            self.guardar() # Guardamos el estado actualizado del curso
            print(f"Estudiante '{estudiante.nombre}' inscrito en el curso '{curso.nombre}'.")
        except ValueError as e:
            print(f"Error al inscribir: {e}")
    
    def guardar(self):
        cursos_dict = [curso.to_dict() for curso in self.cursos]
        guardar_datos(RUTA_ARCHIVO, cursos_dict)

    def cargar(self):
        try:
            datos_curso = cargar_datos(RUTA_ARCHIVO)
            self.cursos = []
            for data in datos_curso:
                instructor = self.gestor_usuarios.buscar_usuario_por_id(data["instructor_id"])
                curso = Curso(data["nombre"], data["descripcion"], instructor, data["codigo"])

                if "estudiante_ids" in data:
                    for estu_id in data["estudiante_ids"]:
                        estudiante = self.gestor_usuarios.buscar_usuario_por_id(estu_id) # Error con buscar usuario
                        if estudiante:
                            try:
                                curso.agregar_estudiante(estudiante)
                            except ValueError:
                                pass
                
                # Falta la logica para cargar evaluaciones

                self.cursos.append(curso)

        except FileNotFoundError:
            self.cursos = []
        except Exception as e:
            print(f"Ocurrió un error al cargar los cursos: {e}")
            self.cursos = []