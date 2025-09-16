class Curso:
    def __init__(self, nombre, descripcion, instructor, codigo):
        self.__nombre = None
        self.__descripcion = None
        self.__instructor = None
        self.__codigo = None
        self.nombre = nombre
        self.descripcion = descripcion
        self.instructor = instructor
        self.codigo = codigo
        self.estudiantes = []
        self.evaluaciones = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor):
            raise ValueError("El nombre del curso no puede estar vacío.")
        else:
            self.__nombre = str(valor)
            
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        if not valor or not str(valor.strip()):
            print("No hay descripcion del curso, se agregara sin-descripcion.")
            self.__descripcion = "Sin-descripcion"
        else:
            self.__descripcion = str(valor.strip())

    @property
    def instructor(self):
        return self.__instructor
    
    @instructor.setter
    def instructor(self, valor):
        if not valor or not str(valor):
            raise ValueError("El instructor no puede estar vacío.")
        else:
            self.__instructor = valor

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor or not str(valor):
            raise ValueError("El codigo del curso no puede estar vacio.")
        else:
            self.__codigo = str(valor)

    def mostrar_informacion(self):
        info = f"Curso: {self.nombre}\n"
        info += f"Descripción: {self.descripcion}\n"
        info += f"Instructor: {self.instructor.nombre}\n"
        info += f"Código: {self.codigo}\n"
        info += f"Número de estudiantes inscritos: {len(self.estudiantes)}\n"
        return info 
    
    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}.")
        else:
            raise Exception(f"El estudiante {estudiante.nombre} ya esta en el curso {self.nombre}")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            return "No hay estudiantes inscritos en este curso."
        linea = []
        for estudiante in self.estudiantes:
            lineas = f"- {estudiante.nombre} (ID: {estudiante.id_usuario}, Correo: {estudiante.correo})"
            linea.append(lineas)
        return "\n".join(linea)
    
    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def to_dict(self):
        return {
            "nombre" : self.nombre,
            "descripcion" : self.descripcion,
            "instructor" : self.instructor,
            "codigo" : self.codigo,
            "estudiantes" : self.estudiantes,
            "evaluaciones" : self.evaluaciones
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            instructor=data["instructor"],
            codigo=data["codigo"],
            estudiantes=data["estudiantes"],
            evaluaciones=data["evaluacioens"]
        )
