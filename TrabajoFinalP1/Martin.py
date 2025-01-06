def ingresar_equipos():
    equipos = []
    puntos = []
    while True:
        equipo = input("Ingrese el nombre del equipo (o 'listo' para terminar): ")
        if equipo.lower() == 'listo':
            break
        punto = int(input(f"Ingrese los puntos obtenidos por {equipo}: "))
        equipos.append(equipo)
        puntos.append(punto)
    return equipos, puntos

def calcular_porcentajes(equipos, puntos):
    total_puntos = sum(puntos)
    porcentajes = [(equipos[i], puntos[i], puntos[i] / total_puntos * 100) for i in range(len(equipos))]
    return porcentajes

def ordenar_por_puntos(porcentajes):
    return sorted(porcentajes, key=lambda x: x[1], reverse=True)

def mostrar_posiciones(porcentajes_ordenados):
    print("Posiciones de equipos por puntos:")
    for equipo, punto, porcentaje in porcentajes_ordenados:
        print(f"{equipo}: {punto} puntos ({porcentaje:.2f}%)")

def actualizar_puntos(equipos, puntos):
    equipo = input("Ingrese el nombre del equipo a actualizar: ")
    if equipo in equipos:
        nuevo_punto = int(input(f"Ingrese los nuevos puntos para {equipo}: "))
        indice = equipos.index(equipo)
        puntos[indice] = nuevo_punto
    else:
        print("Equipo no encontrado.")

def eliminar_equipo(equipos, puntos):
    equipo = input("Ingrese el nombre del equipo a eliminar: ")
    if equipo in equipos:
        indice = equipos.index(equipo)
        equipos.pop(indice)
        puntos.pop(indice)
    else:
        print("Equipo no encontrado.")

def mostrar_estadisticas(porcentajes):
    if porcentajes:
        equipo_max = max(porcentajes, key=lambda x: x[1])
        equipo_min = min(porcentajes, key=lambda x: x[1])
        print(f"Equipo con mayor puntaje: {equipo_max[0]} con {equipo_max[1]} puntos.")
        print(f"Equipo con menor puntaje: {equipo_min[0]} con {equipo_min[1]} puntos.")
    else:
        print("No hay equipos en el listado.")

# Menu
equipos, puntos = ingresar_equipos()
while True:
    print("\n1. Mostrar posiciones de equipos")
    print("2. Actualizar puntos de un equipo")
    print("3. Eliminar un equipo")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        porcentajes = calcular_porcentajes(equipos, puntos)
        porcentajes_ordenados = ordenar_por_puntos(porcentajes)
        mostrar_posiciones(porcentajes_ordenados)
    elif opcion == 2:
        actualizar_puntos(equipos, puntos)
    elif opcion == 3:
        eliminar_equipo(equipos, puntos)
    elif opcion == 4:
        porcentajes = calcular_porcentajes(equipos, puntos)
        mostrar_estadisticas(porcentajes)
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Intente nuevamente.")
