from usuarios.usuario import Usuario, Estudiante, Instructor

usuarios = []

def crear_usuario(tipo, nombre, correo, contrasenia):
    if tipo.lower() == "estudiante":
        nuevo_usuario = Estudiante(nombre, correo, contrasenia)
    elif tipo.lower() == "instructor":
        nuevo_usuario = Instructor(nombre, correo, contrasenia)
    else:
        raise ValueError("Tipo de usuario no válido.")
        
    usuarios.append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario.nombre} Creado. Id: {nuevo_usuario.id_usuario}")
        
def buscar_usuario(correo):
    for usuario in usuarios:
        if usuario.correo == correo:
            return usuario
    return None

def mostrar_usuarios():
    if not usuarios:
        return "No hay usuarios registrados."
    lineas = []
    for usuario in usuarios:
        lineas.append(f"- {usuario.nombre} (ID: {usuario.id_usuario}, Correo: {usuario.correo}, Rol: {usuario.rol})")
    return "\n".join(lineas)

def eliminar_usuario(correo):
    usuario = buscar_usuario(correo)
    if usuario:
        usuarios.remove(usuario)
        print(f"Usuario {usuario.nombre} se eliminó correctamente.")
