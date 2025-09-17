class Reportes: 

    @staticmethod
    def promedio_por_estudiante(curso):
        promedios = {}
        if not curso.evaluaciones:
            print(f"Error: EL curso no tiene evaliaciones para calcular.")
            return promedios
        
        for estudiantes in curso.estuduantes:
            total_calificiones = 0
            num_calificaciones = 0
            for evalu in curso.evaluaciones:
                for calificacion in evalu.calificaciones:
                    if calificacion["estudiante_id"] == estudiantes.id_usuario:
                        total_calificiones += calificacion["nota"]
                        num_calificaciones += 1
                        break

            promedio = total_calificiones / num_calificaciones if num_calificaciones > 0 else 0
            promedios[estudiantes.id_usuario] = round(promedio , 2)
        return promedios 
    
    @staticmethod
    def promedios_bajo(gesotr_usuarios, promedios, limite = 65):
        estudiante_prom_bajo = []
        for estudiante_id, promedio in promedios.items():
            if promedio < limite:
                estudiante = gesotr_usuarios.buscar_usario_id(estudiante_id)
                if estudiante:
                    reporte_info = f"- {estudiante.nombre} (ID: {estudiante_id}): Promedio {promedio}"
                    estudiante_prom_bajo.append(reporte_info)
        return estudiante_prom_bajo
    
