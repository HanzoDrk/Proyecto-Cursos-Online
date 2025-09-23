from evaluaciones.evaluaciones import Tarea, Examen

class GestorEvaluaciones:
    def __init__(self, gestor_cursos, gestor_evaluaciones):
        # CORREGIDO: Usamos un nombre consistente (en plural) para el atributo.
        self.gestor_cursos = gestor_cursos
        self.gestor_evaluaciones = gestor_evaluaciones

    def crear_evaluacion(self, codigo_curso, tipo, titulo, descripcion, fecha_entrega):
        # CORREGIDO: Ahora se usa el nombre consistente, self.gestor_cursos.
        curso = self.gestor_cursos.buscar_curso(codigo_curso)
        if not curso:
            print(f"Error, no se encontro ningun curso con el codigo: {codigo_curso}")
            return

        if tipo.lower() == "tarea":
            nueva_evaluacion = Tarea(titulo, descripcion, fecha_entrega)
        elif tipo.lower() == "examen":
            nueva_evaluacion = Examen(titulo, descripcion, fecha_entrega)
        else:
            print(f"Error: tipo de evaluacion no valido")
            return

        curso.agregar_evaluacion(nueva_evaluacion)
        # CORREGIDO: Usamos el nombre consistente, self.gestor_cursos.
        self.gestor_cursos.guardar()
        print(f"Evaluación '{titulo}' agregada al curso '{curso.nombre}'.")

    # CORREGIDO: Se corrigió el nombre del método y el parámetro.
    def registrar_calificacion(self, codigo_curso, titulo_evaluacion, id_estudiante, nota):
        # Ahora se usa el nombre consistente, self.gestor_cursos.
        curso = self.gestor_cursos.buscar_curso(codigo_curso)
        if not curso:
            print(f"Error: No hay curso con el codigo, {codigo_curso}")
            return

        evaluacion_encontrada = None
        for evalu in curso.evaluaciones:
            if evalu.titulo.lower() == titulo_evaluacion.lower():
                evaluacion_encontrada = evalu
                break

        if not evaluacion_encontrada:
            print(f"Error: No se encontro ninguna evaluacion en el curso con el nombre {titulo_evaluacion}")
            return

        try:
            # CORREGIDO: El parámetro ahora está escrito correctamente.
            evaluacion_encontrada.registrar_calificacion(id_estudiante, nota)
            self.gestor_cursos.guardar()
        except ValueError as e:
            print(f"Error en el registro de la nota: {e}")