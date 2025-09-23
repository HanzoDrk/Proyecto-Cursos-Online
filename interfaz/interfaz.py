from usuarios.gestor_usuario import GestorUsuarios
from cursos.gestor_cursos import GestorCursos
from evaluaciones.gestor_evaluaciones import GestorEvaluaciones
from reportes.reporte import Reportes
import os

class Sistema:
    def __init__(self):
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_cursos = GestorCursos(self.gestor_usuarios) #error al momento de iniciar el programa, faltaba lo que esta adentro del parentesis.
        self.gestor_evaluaciones = GestorEvaluaciones(self.gestor_cursos, self.gestor_usuarios) #Error al incicar el programa, faltaban lo que esta adentro del parentesis.
        self.usuario_actual = None

    def limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def menu_principal(self):
        print("\n=-=-= Cursos Online =-=-=\n1. Iniciar sesion\n2. Registrarse\n3. Salir")
        return input("seleccione una opccion: ")
    
    def registrar_usuario(self):
        self.limpiar()
        print(" Registro de nuevo usuario ^-^ ")
        
        while True:
            tipo = input(f"Sellecione el tipo de usuario (Estudiante | 'Instructor): ").lower()
            if tipo in ["estudiante", "instructor"]:
                break
            else:
                print("Tipo de usuario no valido. Intente otra vez")

        nombre = input("Ingrese su nombre: ")

        while True:
            correo = input("Ingrese su correo electronico: ")
            if "@" not in correo and "." not in correo: #Se agrega otro tipo de variacion

                print("Correo no reconocido")
            elif self.gestor_usuarios.buscar_usuario(correo):
                print("Ya existe una cuenta con ese correo")
            else:
                break

        contrasenia = input("Ingrese su contraseña: ")

        try:
            nuevo_usuario = self.gestor_usuarios.crear_usuario(tipo, nombre, correo, contrasenia)
            if nuevo_usuario:
                print(f"\n¡Registro exitoso! El ID de usuario '{nuevo_usuario.id_usuario}' ha sido creado.")
        except ValueError as e:
            print(f"\nError en el registro: {e}")
        
        input("\nPresione Enter para volver al menú principal.")


    def iniciar_sesion(self):
        self.limpiar()
        print("=-=-= Inicio de sesion =-=-=")
        correo = input("Ingrese su correo electrónico: ")
        contrasenia = input("Ingrese su contraseña: ")

        usuario_encontrado = self.gestor_usuarios.buscar_usuario(correo)
        if usuario_encontrado and usuario_encontrado.contrasenia == contrasenia:
            self.usuario_actual = usuario_encontrado
            print(f"\n¡Bienvenido, {self.usuario_actual.nombre} :D!")
            self.mostrar_menu()
            input("Presione Enter para continuar.")
            
        else:
            print("\nError: Correo o contraseña incorrectos.")
            input("Presione Enter para volver al menú principal.")

    def cerrar_sesion(self):
        print(f"\nCerrando sesión de {self.usuario_actual.nombre}. ¡Hasta pronto!")
        self.usuario_actual = None
        input("Presione Enter para volver al menú principal.")

    def mostrar_menu(self):
        if not self.usuario_actual:
            print("Error: No hay ningún usuario logueado.")
            return

        if self.usuario_actual.rol.lower() == "estudiante":
            self.menu_estudiante()
        elif self.usuario_actual.rol.lower() == "instructor":
            self.menu_instructor()

    def menu_estudiante(self):
        while self.usuario_actual:
            self.limpiar()
            print(f"\n=-=-= Menú del Estudiante: {self.usuario_actual.nombre} =-=-=\n1. Inscribirse a un curso\n2. Ver mis cursos y notas\n3. Cerrar sesion")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.inscribir_estudiante_curso()
            elif opcion == "2":
                self.ver_cursos_notas()
            elif opcion == "3":
                self.cerrar_sesion()
                break
            else:
                input("Opción no válida. Presione Enter para continuar.")

    def inscribir_estudiante_curso(self):
        self.limpiar()
        print("\n--- Inscribirse a un Curso ---")
        print("Cursos disponibles:")
        lista_cursos = self.gestor_cursos.mostrar_cursos()
        if "No hay cursos registrados." in lista_cursos:
            print("\nActualmente no hay cursos disponibles para inscripción.")
            input("\nPresione Enter para volver al menú.")
            return
        
        print(lista_cursos)
        codigo_curso = input("\nIngrese el código del curso al que desea inscribirse: ")
        self.gestor_cursos.inscribir_estudiante(codigo_curso, self.usuario_actual.id_usuario)
        input("\nPresione Enter para volver al menú.")
    
    def ver_cursos_notas(self):
        self.limpiar()
        print(f"\n--- Cursos y Notas de: {self.usuario_actual.nombre} ---")
        
        cursos_del_estudiante = []
        for curso in self.gestor_cursos.cursos:
            if self.usuario_actual in curso.estudiantes:
                cursos_del_estudiante.append(curso)

        if not cursos_del_estudiante:
            print("\nNo estás inscrito en ningún curso todavía.")
            input("\nPresione Enter para volver al menú.")
            return

        for curso in cursos_del_estudiante:
            print("\n----------------------------------------")
            print(curso.mostrar_informacion())
            
            if not curso.evaluaciones:
                print("  Este curso aún no tiene evaluaciones.")
            else:
                print("  Calificaciones:")
                for evaluacion in curso.evaluaciones:
                    nota_encontrada = "Sin calificar"
                    for calificacion in evaluacion.calificaciones:
                        if calificacion["estudiante_id"] == self.usuario_actual.id_usuario:
                            nota_encontrada = calificacion["nota"]
                            break
                    print(f"    - {evaluacion.titulo}: {nota_encontrada}")

        print("\n----------------------------------------")
        input("\nPresione Enter para volver al menú.")

    def menu_instructor(self):
        while self.usuario_actual:
            self.limpiar()  #Cambio de variables debido a que no existia limpiar pantalla
            print(f"\n=-=-= Menú del Instructor: {self.usuario_actual.nombre} =-=-=\n1. Crear un nuevo curso\n2. Ver mis cursos\n3. Agregar evaluación a un curso")
            print("4. Registrar calificación de un estudiante\n5. Generar reporte de estudiantes con promedio bajo\n6. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.crear_nuevo_curso()
            elif opcion == "2":
                self.ver_mis_cursos_instructor()    #Cambio de variables para llamar a la correcta
            elif opcion == "3":
                self.agregar_evaluacion_a_curso()
            elif opcion == "4":
                self.registrar_calificacion_menu()
            elif opcion == "5":
                self.generar_reporte_promedio_bajo()
            elif opcion == "6":
                self.cerrar_sesion()
                break
            else:     
                print("Opcion no valida. Presione Enter para continuar.")

    def crear_nuevo_curso(self):
        self.limpiar()
        print("\n--- Crear un Nuevo Curso ---")

        nombre = input("Ingrese el nombre del curso: ")
        descripcion = input("Ingrese la descripción del curso: ")
        codigo = input("Ingrese un código único para el curso (ej. PROG-101): ")

        self.gestor_cursos.crear_curso(
            nombre,
            descripcion,
            codigo,
            self.usuario_actual.id_usuario
        )

        input("\nPresione Enter para volver al menú.")
    
    def ver_mis_cursos_instructor(self):
        self.limpiar()
        print(f"\n--- Cursos a cargo de: {self.usuario_actual.nombre} ---")

        cursos_del_instructor = []
        for curso in self.gestor_cursos.cursos:
            if curso.instructor and curso.instructor.id_usuario == self.usuario_actual.id_usuario:
                cursos_del_instructor.append(curso)

        if not cursos_del_instructor:
            print("\nAún no has creado ningún curso.")
            input("\nPresione Enter para volver al menú.")
            return

        for curso in cursos_del_instructor:
            print("\n=====================================")
            print(curso.mostrar_informacion())
            print("\n  Estudiantes Inscritos:")
            print(curso.mostrar_estudiantes()) 

        print("\n=====================================")
        input("\nPresione Enter para volver al menú.")
    

    def agregar_evaluacion_a_curso(self):
        self.limpiar()
        print("\n--- Agregar evaluacion al curso ---")
        self.ver_mis_cursos_instructor()
        
        self.limpiar()  #Se agrega una linea de codigo para limpiar los cursos
        codigo_curso = input("\nIngrese el codigo del curso para poder crear la evaluacion: ")

        while True:
            tipo = input("Ingrese el tipo de evaluacion (Tarea | Examen): ").lower()
            if tipo in ["tarea", "examen"]:
                break
            else:
                print("Error: tipo invalido. Intente de nuevo")
        
        titulo = input("Introduzca el titulo para la evaluacion: ")
        descripcion = input("Introduzca la descripcion para la evaluacion: ")
        fecha_entrega = input("Ingrese la fecha (e.j., YYYY-MM-DD): ")


        self.gestor_evaluaciones.crear_evaluacion(
            codigo_curso,
            tipo,
            titulo,
            descripcion,
            fecha_entrega
        )
        
        input("\nPresione Enter para volver al menu.")
    
    def registrar_calificacion_menu(self):
        self.limpiar()
        print("\n--- Registrar Calificación de un Estudiante ---")
        self.ver_mis_cursos_instructor()
        codigo_curso = input("\nIngrese el código del curso para registrar calificaciones: ")
        
        curso = self.gestor_cursos.buscar_curso(codigo_curso)
        if not curso or curso.instructor.id_usuario != self.usuario_actual.id_usuario:
            print("\nError: Código de curso no válido o no te pertenece.")
            input("Presione Enter para continuar.")
            return

        if not curso.estudiantes or not curso.evaluaciones:
            print("\nEste curso no tiene estudiantes o evaluaciones registradas todavía.")
            input("Presione Enter para continuar.")
            return

        print("\nEstudiantes en este curso:")
        print(curso.mostrar_estudiantes())
        
        print("\nEvaluaciones en este curso:")
        for ev in curso.evaluaciones:
            print(f"- {ev.titulo}")

        titulo_evaluacion = input("\nIngrese el título de la evaluación a calificar: ")
        id_estudiante = input("Ingrese el ID del estudiante a calificar: ")
        
        while True:
            try:
                nota_str = input(f"Ingrese la nota (0-100) para {id_estudiante}: ")
                nota = int(nota_str)
                if 0 <= nota <= 100:
                    break
                else:
                    print("Error: La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        
        self.gestor_evaluaciones.registrar_calificacion(
            codigo_curso,
            titulo_evaluacion,
            id_estudiante,
            nota
        )
        
        input("\nPresione Enter para volver al menú.")

    def generar_reporte_promedio_bajo(self):
        self.limpiar()
        print("\n--- Generar Reporte de Estudiantes con Promedio Bajo ---")

        self.ver_mis_cursos_instructor()
        codigo_curso = input("\nIngrese el código del curso para generar el reporte: ")

        curso = self.gestor_cursos.buscar_curso(codigo_curso)
        if not curso or curso.instructor.id_usuario != self.usuario_actual.id_usuario:
            print("\nError: Código de curso no válido o no te pertenece.")
            input("Presione Enter para continuar.")
            return

        try:
            limite = int(input("Ingrese el promedio límite (ej. 61): "))
        except ValueError:
            print("\nError: Límite no válido.")
            input("Presione Enter para continuar.")
            return
        
        print("\nGenerando reporte...")
        promedios = Reportes.promedio_por_estudiante(curso)
        estudiantes_bajos = Reportes.promedios_bajo(self.gestor_usuarios, promedios, limite)

        self.limpiar()  #Habia un error de atribute error, en donde no existia la funcion limpiar pantalla.

        print(f"--- Reporte para el curso: {curso.nombre} ---")
        if estudiantes_bajos:
            print(f"Estudiantes con promedio por debajo de {limite}:")
            for linea in estudiantes_bajos:
                print(linea)
        else:
            print(f"¡Buenas noticias! Ningún estudiante tiene un promedio por debajo de {limite}.")

        input("\nPresione Enter para volver al menú.")

    def ejecutar(self): # Bucle principal de la aplicación
        while True:
            self.limpiar()
            opcion = self.menu_principal()

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("¡Hasta pronto!")
                self.gestor_usuarios.guardar()
                self.gestor_cursos.guardar()
                break
            else:
                input("Opción no válida. Presione Enter para continuar.")
