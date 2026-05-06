import csv

# lista con dos valores, si y no.
estudiante_trabaja = ["Sí", "No"]
# contadores de trabajadores y no trabajadores
trabajador = 0
no_trabajador = 0
# lista anidada de estudiantes, se almacenara los contadores de trabajadores
estudiantes = [[], []]

# abrir el csv
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiante:
    # variable encuesta para leer el csv
    encuesta = csv.reader(estudiante)
    # salto de linea
    next(encuesta)
    # bucle que lee la columna N5 del csv, donde se veran los estudiantes trabajadores y
    # no trabajadores, si el estudiante trabaja, se aumenta el contador de estudiantes
    # trabajadores y se almacenara en la primera lista, si no trabaja, el contador de no
    # trabajadores aumenta y se agrega a la segunda lista
    for trabajadores in encuesta:
        trabaja = trabajadores[4].strip()
        if trabaja == estudiante_trabaja[0]:
            trabajador += 1
            estudiantes[0].append(trabajador)
        if trabaja == estudiante_trabaja[1]:
            no_trabajador += 1
            estudiantes[1].append(trabajador)
# suma ambas listas de trabajadores y no trabajadores
total_trabajador = len(estudiantes[0]) + len(estudiantes[1])
# estudiantes trabajadores es la primera lista de la lista anidada de estudiantes
estudiantes_trabajadores = len(estudiantes[0])
# estudiantes no trabajadores es la segunda lista de la lista anidada de estudiantes
estudiantes_no_trabajadores = len(estudiantes[1])
# se calcula el porcentaje de estudiantes trabajadores dividiendo los estudiantes trabajadores por el total de estudiantes multiplicado por 100
porcentaje_estudiantes_trabajadores = (
    estudiantes_trabajadores / total_trabajador
) * 100
# se calcula el porcentaje de estudiantes no trabajadores dividiendo los estudiantes trabajadores por el total de estudiantes por 100
porcentaje_estudiantes_no_trabajadores = (
    estudiantes_no_trabajadores / total_trabajador
) * 100
# se imprimen los porcentajes
print(
    f"porcentaje de estudiantes trabajadores: {porcentaje_estudiantes_trabajadores:.2f}% porcentaje de estudiantes que no trabajan:{porcentaje_estudiantes_no_trabajadores:.2f}%"
)
