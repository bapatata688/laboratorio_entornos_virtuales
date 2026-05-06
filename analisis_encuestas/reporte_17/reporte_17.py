# Reporte 17: Relación entre acceso a internet y promedio académico
import csv

# lista en donde guardaremos los datos
encuesta = []

with open("../encuesta_ingenieria_10000_respuestas.csv", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)

    for fila in lector:

        estudiante = [
            fila[0],  # ID

            [fila[1], fila[2], fila[3]],  # datos generales

            [fila[4], fila[5]],  # datos academicos 

            [fila[6], fila[7]],  # tecnologicos

            fila[8:]  # otros 
        ]

        encuesta.append(estudiante)



suma_bueno = 0
contador_bueno = 0

suma_malo = 0
contador_malo = 0

for estudiante in encuesta:

    # promedio 
    promedio = float(estudiante[2][1])

    # internet esta en otros
    internet = int(estudiante[4][7])  

    if internet >= 3:
        suma_bueno += promedio
        contador_bueno += 1

    else:
        suma_malo += promedio
        contador_malo += 1


# calcular promedios
if contador_bueno > 0:
    promedio_bueno = suma_bueno / contador_bueno
else:
    promedio_bueno = 0

if contador_malo > 0:
    promedio_malo = suma_malo / contador_malo
else:
    promedio_malo = 0


# mostrar resultados
print("Promedio teniendo buen internet:", round(promedio_bueno, 2))
print("Promedio teniendo mal internet:", round(promedio_malo, 2))