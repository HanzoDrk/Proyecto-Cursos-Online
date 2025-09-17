from abc import ABC, abstractclassmethod

class Evaluacion(ABC):
    def __init__(self, titulo, descripcion, fecha_entrega):
        self.__titulo = None
        self.__descripcion = None
        self.__fecha_entrega = None

        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.calificaciones = []

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El título no puede estar vacío.")
        self.__titulo = str(valor)

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self.__descripcion = str(valor)

    @property
    def fecha_entrega(self):
        return self.__fecha_entrega
    
    @fecha_entrega.setter
    def fecha_entrega(self, valor):
        if not valor or not valor.strip(): 
            raise ValueError("La fecha de entrega no puede estar vacía.")
        self.__fecha_entrega = str(valor)

    @abstractclassmethod
    def tipo(self):
        pass

    def registrar_calificacion(self, estudiante_id, nota):
        if not ( 0 <= nota <= 100):
            raise ValueError("La calificación debe estar entre 0 y 100.")
        
        for cali in self.calificaciones:
            if cali["estudiantes_id"] == estudiante_id:
                cali["nota"] == nota
                print(f"Calificación del estudiante ID {estudiante_id} actualizada a {nota}.")
                return
            
        self.calificaciones.append({"estudiante_id": estudiante_id, "nota": nota})
        print(f"Calificación {nota} registrada para el estudiante ID {estudiante_id}.")


    def mostrar_informacion(self):
        info =(f"Título: {self.titulo} (Tipo: {self.tipo()})\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Fecha de Entrega: {self.fecha_entrega}\n")
        
        if self.calificaciones:
            info += "Calificaciones:\n"
            for cali in self.calificaciones:
                info += f"- Estudiante ID {cali['estudiante_id']}: {cali['nota']}\n"
        else:
            info += "No hay calificaciones registradas.\n"
        return info
    
    def to_dict(self):
        return {
            "tipo": self.tipo(), 
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_entrega": self.fecha_entrega,
            "calificaciones": self.calificaciones
        }
    
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