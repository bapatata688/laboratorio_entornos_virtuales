import csv

encuesta = []

with open("../encuesta_ingenieria_10000_respuestas.csv", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)

    for fila in lector:

        estudiante = [
            fila[0],  # ID

            [fila[1], fila[2], fila[3]],  # datos generales
            # carrera, semestre, jornada

            [fila[4], fila[5]],  # datos academicos
            # trabaja, promedio

            [fila[6], fila[7]],  # datos tecnologicos

            fila[8:]  # otros 
        ]

        encuesta.append(estudiante)



suma_si = 0
contador_si = 0

suma_no = 0
contador_no = 0

for estudiante in encuesta:

    trabaja = estudiante[2][0]
    promedio = float(estudiante[2][1])

    if trabaja in ["Si", "SI", "Sí"]:
        suma_si += promedio
        contador_si += 1

    elif trabaja in ["No", "NO"]:
        suma_no += promedio
        contador_no += 1


if contador_si > 0:
    promedio_si = suma_si / contador_si
else:
    promedio_si = 0

if contador_no > 0:
    promedio_no = suma_no / contador_no
else:
    promedio_no = 0


print("Promedio estudiantes que trabajan:", round(promedio_si, 2))
print("Promedio estudiantes que NO trabajan:", round(promedio_no, 2))