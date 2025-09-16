from abc import ABC, abstractclassmethod

class Usuario(ABC):
    _contadores = {"U": 1, "E": 1, "I": 1} 
     
    def __init__(self, nombre, correo, rol, contrasenia, prefijo="U"):
        self.__nombre = None
        self.__correo = None
        self.__rol = None
        self.__contrasenia = None
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.contrasenia = contrasenia
        self.id_usuario = self._generar_id(prefijo)
 
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor):
            raise ValueError("EL nombre no puede estar vacío.")
        else:
            self.__nombre = str(valor)

    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, valor):
        if not valor or not str(valor):
            raise ValueError("El correo no puede estar vacío.")
        else:
            self.__correo = str(valor)

    @property
    def rol(self):
        return self.__rol
    
    @rol.setter
    def rol(self, valor):
        if not valor or not str(valor):
            raise ValueError("El rol no puede estar vacío.")
        else:
            self.__rol = str(valor)

    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @contrasenia.setter
    def contrasenia(self, valor):
        if not valor or not str(valor):
            raise ValueError("La contraseña no puede estar vacía.")
        else:
            self.__contrasenia = str(valor)

    @abstractclassmethod
    def mostrar_informacion(self):
         pass
    
    @classmethod
    def _generar_id(cls, prefijo):
        nuevo_id = f"{prefijo}{cls._contadores[prefijo.upper()]:03d}"
        cls._contadores[prefijo.upper()] += 1
        return nuevo_id
    
    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasenia": self.contrasenia,
            "rol": self.rol
        }

class Estudiante(Usuario):
    def __init__(self, nombre, correo, contrasenia):
        super().__init__(nombre, correo, "Estudiante", contrasenia, prefijo="E")
    
    def mostrar_informacion(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}"
    
    def inscribir_curso(self, curso):
        curso.agregar_estudiante(self)
        print(f"Estudiante {self.nombre} inscrito en el curso {curso.nombre}.")

    
class Instructor(Usuario):
    def __init__(self, nombre, correo, contrasenia):
        super().__init__(nombre, correo, "Instructor", contrasenia, prefijo="I")

    def mostrar_informacion(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}"
    
