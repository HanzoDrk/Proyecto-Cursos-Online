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
    def nombre(self):   #Variable nombre
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre del curso no puede estar vacío.")
        self.__nombre = str(valor)
            
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        if not valor or not str(valor.strip()):
            self.__descripcion = "Sin-descripcion"
        else:
            self.__descripcion = str(valor.strip())

    @property
    def instructor(self):
        return self.__instructor
    
    @instructor.setter
    def instructor(self, valor):
        if valor is None:
            self.__instructor = valor
            return
        self.__instructor = valor

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor or not str(valor):
            raise ValueError("El codigo del curso no puede estar vacio.")
        self.__codigo = str(valor)

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}.")
        else:
            raise ValueError(f"El estudiante {estudiante.nombre} ya esta en el curso {self.nombre}")
        
    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)
        print(f"Evaluacion {evaluacion.titulo}, agregada al curso {self.nombre}") #Cambio de una variable

        
    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"El estudiante {estudiante.nombre} se elimino correctamente")
        else:
            raise ValueError(f"El estudainte {estudiante.nombre} no se encuentra en este curso")

    def mostrar_informacion(self):  #Nombre de la variable corregida
        nombre_instructor = self.instructor.nombre if self.instructor else "no asignado"
        info = (f"Curso: {self.nombre} (Código: {self.codigo})\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Instructor: {nombre_instructor}\n"
                f"  Estudiantes inscritos: {len(self.estudiantes)}")
        return info 

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            return "No hay estudiantes inscritos en este curso."
        
        linea = []
        for estudiante in self.estudiantes:
            estudiantes_info = f"- {estudiante.nombre} (ID: {estudiante.id_usuario}, Correo: {estudiante.correo})"
            linea.append(estudiantes_info)
        return "\n".join(linea)
    
    def __str__(self):
        return self.mostrar_informacion()   #Nombre de la variable erroneo


    
    def to_dict(self):
        return {
            "nombre" : self.nombre,
            "descripcion" : self.descripcion,
            "codigo" : self.codigo,
            "instructor_id" : self.instructor.id_usuario if self.instructor else None,
            "estudiante_ids" : [est.id_usuario for est in self.estudiantes],
            "evaluaciones" : [eval.to_dict() for eval in self.evaluaciones]
        }
    