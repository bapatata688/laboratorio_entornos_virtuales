# Reporte 19: Porcentaje de estudiantes interesados en cursos virtuales.

import csv

encuesta = []

with open("../encuesta_ingenieria_10000_respuestas.csv", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)

    for fila in lector:

        estudiante = [
            fila[0],
            [fila[1], fila[2], fila[3]],
            [fila[4], fila[5]],
            [fila[6], fila[7]],
            fila[8:]
        ]

        encuesta.append(estudiante)


total = 0
interesados = 0

for estudiante in encuesta:

    total += 1

    interes = int(estudiante[4][16])  # q19_intencion_continuar

    if interes >= 4:
        interesados += 1


# porcentaje
if total > 0:
    porcentaje = (interesados / total) * 100
else:
    porcentaje = 0


print("Porcentaje de estudiantes interesados en cursos virtuales:", round(porcentaje, 2), "%")

