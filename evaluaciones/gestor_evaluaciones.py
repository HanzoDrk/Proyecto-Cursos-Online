from evaluaciones.evaluaciones import Tarea, Examen

class GestorEvaluaciones:
    def __init__(self, gestor_curso, gestor_evaluaciones):
        self.gestor_curso = gestor_curso
        self.gestor_evaluaciones = gestor_evaluaciones

    def crear_evaluacion(self, codigo_curso, tipo, titulo, descripcion, fecha_entrega):
        curso = self.gestor_curso.buscar_curso(codigo_curso)
        if not curso:
            print(f"Error, no se encontro ningun curso con el codigo: {codigo_curso}")
            return
        

        if tipo.lower() == "tarea":
            nueva_evaluacion = Tarea(titulo, descripcion, fecha_entrega)
        elif tipo.lower() == "examen":
            nueva_evaluacion = Examen(titulo, descripcion, fecha_entrega)
        else:
            print(f"Error: tipo de evaluacion no valido")

        self.agregar_evaluacion.append(nueva_evaluacion)
        self.gestor_curso.guardar()
        print(f"Evaluación '{titulo}' agregada al curso '{curso.nombre}'.")

    def registrar_calificacio(self, codigo_curso, titulo_evaluacion, id_estudiate, nota):
        curso = self.gestor_curso.buscar_curso(codigo_curso)
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
            return None
        
        try:
            evaluacion_encontrada.registrar_calificacion(id_estudiate, nota)
            self.gestor_evaluaciones.guardar()
        except ValueError as e:
            print(f"Error en el registro de la nota: {e}")