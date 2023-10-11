def planificacion_prioridad():
    num_procesos = int(input("Ingrese el número de procesos: "))

    # Crear listas separadas para procesos con tiempo de llegada 0 y otros procesos
    procesos_llegada_cero = []
    procesos_prioridad = []

    # Solicitar información de cada proceso al usuario
    for i in range(num_procesos):
        nombre = input(f"Ingrese el nombre del proceso {i + 1}: ")
        rafaga = int(input(f"Ingrese la Rafaga de CPU del proceso {i + 1}: "))
        tiempoLlegada = int(input(f"Ingrese el tiempo de llegada del proceso {i + 1}: "))
        prioridad = int(input(f"Ingrese la prioridad del proceso {i + 1}: "))

        proceso = {"nombre": nombre, "rafaga": rafaga, "tiempoLlegada": tiempoLlegada, "prioridad": prioridad}

        if tiempoLlegada == 0:
            procesos_llegada_cero.append(proceso)
        else:
            procesos_prioridad.append(proceso)

    # Ordenar los procesos de llegada cero por duración y luego por prioridad
    procesos_llegada_cero.sort(key=lambda x: (x["tiempoLlegada"], x["prioridad"]))

    # Inicializar la variable tiempo_total
    tiempo_total = 0

    # Inicializar el tiempo de espera total
    tiempos_espera = []

    # Inicializar el tiempo de retorno total
    tiempos_retorno = []

    # Si solo hay un proceso con tiempo de llegada igual a 0, ejecutarlo de inmediato
    if len(procesos_llegada_cero) == 1:
        proceso_unico = procesos_llegada_cero.pop(0)
        print(f"Ejecutando {proceso_unico['nombre']} (Rafaga: {proceso_unico['rafaga']}, Tiempo de llegada: {proceso_unico['tiempoLlegada']}, Prioridad: {proceso_unico['prioridad']})")
        tiempo_total += proceso_unico['rafaga']
        tiempos_espera.append(0)
        tiempos_retorno.append(tiempo_total)

    # Si hay más de un proceso con llegada igual a 0, tomar el de menor duración
    if len(procesos_llegada_cero) > 1:
        # Ordenar los procesos de llegada cero por prioridad
        procesos_llegada_cero.sort(key=lambda x: x["prioridad"])
        # Tomar el proceso de menor prioridad
        proceso_elegido = procesos_llegada_cero.pop(0)
        print(f"Ejecutando {proceso_elegido['nombre']} (Rafaga: {proceso_elegido['rafaga']}, Tiempo de llegada: {proceso_elegido['tiempoLlegada']}, Prioridad: {proceso_elegido['prioridad']})")
        tiempo_total += proceso_elegido['rafaga']
        tiempos_espera.append(0)
        tiempos_retorno.append(tiempo_total)

        # Insertar los demás procesos de llegada cero en la lista ordenada
        for proceso in procesos_llegada_cero:
            procesos_prioridad.insert(0, proceso)

    # Ordenar los otros procesos por prioridad y luego por duración
    procesos_prioridad.sort(key=lambda x: (x["prioridad"], x["tiempoLlegada"]))

    # Ejecutar los demás procesos por prioridad y duración
    for proceso in procesos_prioridad:
        print(f"Ejecutando {proceso['nombre']} (Rafaga: {proceso['rafaga']}, Tiempo de llegada: {proceso['tiempoLlegada']}, Prioridad: {proceso['prioridad']})")
        tiempo_total += proceso['rafaga']
        tiempos_espera.append(tiempo_total - (proceso['rafaga'] + proceso['tiempoLlegada']))
        tiempos_retorno.append(tiempo_total)

    print(f"Tiempo total de ejecución: {tiempo_total}")
    print(f"Tiempos de espera: {tiempos_espera}")
    print(f"Tiempos de retorno: {tiempos_retorno}")

    # Calcular el tiempo total de espera
    tiempo_total_espera = sum(tiempos_espera)
    # Calcular el tiemmpo total de retorno
    tiempo_total_retorno = sum(tiempos_retorno)

    # Calcular el promedio del tiempo de espera
    promedio_espera = tiempo_total_espera / num_procesos
    print(f"Tiempo total de espera: {tiempo_total_espera}")
    print(f"Promedio del tiempo de espera: {promedio_espera}")

    promedio_retorno = tiempo_total_retorno / num_procesos
    print(f"Tiempo total de retorno: {tiempo_total_retorno}")
    print(f"Promedio del tiempo de espera: {promedio_retorno}")


if __name__ == "__main__":
    planificacion_prioridad()

























