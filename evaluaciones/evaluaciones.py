from abc import ABC, abstractclassmethod

class Evaluacion(ABC):
    def __init__(self, titulo, descripcion, fecha_entrega):
        self.__titulo = None
        self.__descripcion = None
        self.__fecha_entrega = None
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.calificacion = []

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not valor or not str(valor):
            raise ValueError("El título no puede estar vacío.")
        else:
            self.__titulo = str(valor)

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        if not valor or not str(valor):
            raise ValueError("La descripción no puede estar vacía.")
        else:
            self.__descripcion = str(valor)

    @property
    def fecha_entrega(self):
        return self.__fecha_entrega
    
    @fecha_entrega.setter
    def fecha_entrega(self, valor):
        if not valor or not str(valor):
            raise ValueError("La fecha de entrega no puede estar vacía.")
        else:
            self.__fecha_entrega = str(valor)

    @abstractclassmethod
    def tipo(self):
        pass

    def regitrar_calificacion(self, estudiante, calificacion):
        if calificacion < 0 or calificacion > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")
        self.calificacion.append((estudiante, calificacion))
        print(f"Calificación {calificacion} registrada para el estudiante {estudiante.nombre} en la evaluación {self.titulo}.")

    def mostrar_informacion(self):
        info = f"Título: {self.titulo}\nDescripción: {self.descripcion}\nFecha de Entrega: {self.fecha_entrega}\nTipo: {self.tipo()}\n"
        if self.calificacion:
            info += "Calificaciones:\n"
            for estudiante, calificacion in self.calificacion:
                info += f"- {estudiante.nombre}: {calificacion}\n"
        else:
            info += "No hay calificaciones registradas.\n"
        return info
    
    def to_dict(self):
        return {
            "titulo" : self.titulo,
            "descripcion" : self.descripcion,
            "fecha_entrega" : self.fecha_entrega,
            "calificacion" : self.calificacion
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            fecha_entrega=data["fecha_entrega"],
            calificacion=data["calificacion"]
        )

class Tarea(Evaluacion):
    def __init__(self, titulo, descripcion, fecha_entrega):
        super().__init__(titulo, descripcion, fecha_entrega)

    def tipo(self):
        return "Tarea"
    
    def __str__(self):
        return f"Tarea: {self.titulo}, Fecha de Entrega: {self.fecha_entrega}"
    
class Examen(Evaluacion):
    def __init__(self, titulo, descripcion, fecha_entrega):
        super().__init__(titulo, descripcion, fecha_entrega)

    def tipo(self):
        return "Examen" 
    
    def __str__(self):
        return f"Examen: {self.titulo}, Fecha de Entrega: {self.fecha_entrega}"

