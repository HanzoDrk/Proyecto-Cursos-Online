import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos
from usuarios.usuario import Usuario, Estudiante, Instructor

RUTA_ARCHIVO = os.path.join("data_manager", "usuarios.json")

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.cargar()

    def crear_usuario(self,tipo, nombre, correo, contrasenia):
        if tipo.lower() == "estudiante":
            nuevo_usuario = Estudiante(nombre, correo, contrasenia)
        elif tipo.lower() == "instructor":
            nuevo_usuario = Instructor(nombre, correo, contrasenia)
        else:
            raise ValueError("Tipo de usuario no válido.")
            
        self.usuarios.append(nuevo_usuario.to_dict())
        print(f"Usuario {nuevo_usuario.nombre} Creado. Id: {nuevo_usuario.id_usuario}")
            
    def buscar_usuario(self,correo):
        for usuario in self.usuarios:
            if usuario.correo == correo:
                return usuario
        return None

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        lineas = []
        for usuario in self.usuarios:
            lineas.append(f"- {usuario.nombre} (ID: {usuario.id_usuario}, Correo: {usuario.correo}, Rol: {usuario.rol})")
        return "\n".join(lineas)

    def eliminar_usuario(self,correo):
        usuario = buscar_usuario(self,correo)
        if usuario:
            self.usuarios.remove(usuario.to_dict())
            print(f"Usuario {usuario.nombre} se eliminó correctamente.")

    def guardar(self):
        guardar_datos(RUTA_ARCHIVO, self.usuarios)

    def cargar(self):
        self.usuarios = cargar_datos(RUTA_ARCHIVO)
