from abc import ABC, abstractclassmethod

class Usuari(ABC):
    def __init__(self, nombre, correo, rol, contrasenia, id_usuario):
        self.__nombre = None
        self.__correo = None
        self.__rol = None
        self.__contrasenia = None
        self.__id_usuario = None
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.contrasenia = contrasenia
        self.id_usuario = id_usuario
        
    @abstractclassmethod
    def mostrar_informacion(self):
        pass
    
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @contrasenia.setter
    def contrasenia(self, valor):
        if not valor or not str(valor):
            raise ValueError("La contraseña no puede estar vacía.")
        else:
            self.__contrasenia = str(valor)

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor):
            print("Nombre no valido.")
    