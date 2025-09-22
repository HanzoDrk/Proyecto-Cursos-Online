import os
from almacenamiento.json_almacenamiento import guardar_datos, cargar_datos
from usuarios.usuario import Estudiante, Instructor

RUTA_ARCHIVO = os.path.join("almacenamiento", "usuarios.json")

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.cargar()

    def crear_usuario(self, tipo, nombre, correo, contrasenia):
        if self.buscar_usuario(correo):
            print(f"Error: el correo: {correo}, ya esta registrado")
            return None

        if tipo.lower() == "estudiante":
            nuevo_usuario = Estudiante(nombre, correo, contrasenia)
        elif tipo.lower() == "instructor":
            nuevo_usuario = Instructor(nombre, correo, contrasenia)
        else:
            raise ValueError("Tipo de usuario no válido.")
            
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nuevo_usuario.nombre} Creado. Id: {nuevo_usuario.id_usuario}")
        return nuevo_usuario
            
    def buscar_usuario(self,correo):
        for usuario in self.usuarios:
            if usuario.correo == correo:
                return usuario
        return None
    
    def buscar_usuario_id(self, usuario_id):    #En este bloque de codigo la funcion usuarios no existe debe ser usuario.
        for usuario in self.usuarios:
            if usuario.id_usuario == usuario_id:   #Se cambia usuario.id_usuarios por usuario
                return usuario   #Se regresa solo el usuario no el id
        return None

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        lineas = []
        for usuario in self.usuarios:
            lineas.append(f"- {usuario.nombre} (ID: {usuario.id_usuario}, Correo: {usuario.correo}, Rol: {usuario.rol})")
        return "\n".join(lineas)

    def eliminar_usuario(self,correo):
        usuario_eliminar = self.buscar_usuario(correo)
        if usuario_eliminar:
            self.usuarios.remove(usuario_eliminar)
            print(f"Usuario {usuario_eliminar.nombre} se eliminó correctamente.")
        else:
            print(f"Error: No se encontro un usuario con el correo proporcionado")

    def guardar(self):
        usuarios_dict = [usuario.to_dict() for usuario in self.usuarios]
        guardar_datos(RUTA_ARCHIVO, usuarios_dict)
        print("Datos guardados correctamente")

    def cargar(self):
        try:
            datos_cargados = cargar_datos(RUTA_ARCHIVO)
            self.usuarios = []
            for data in datos_cargados:
                if data["rol"].lower() == "estudiante":
                    usuario = Estudiante(data["nombre"], data["correo"], data["contrasenia"])
                elif data["rol"].lower() == "instructor":
                    usuario = Instructor(data["nombre"], data["correo"], data["contrasenia"])
                else:
                    continue

                usuario.id_usuario = data ["id_usuario"]
                self.usuarios.append(usuario)
        except FileNotFoundError:
            print("no se encontro el archivo, se creara una lista vacia.")
            self.usuarios = []
