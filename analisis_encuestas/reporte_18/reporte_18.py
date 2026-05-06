# 18. Relación entre horas de estudio y rendimiento académico. 

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


suma_1 = 0
cont_1 = 0

suma_2 = 0
cont_2 = 0

suma_3 = 0
cont_3 = 0

suma_4 = 0
cont_4 = 0

suma_5 = 0
cont_5 = 0


for estudiante in encuesta:

    horas = int(estudiante[3][0])      # q01_horas_estudio
    promedio = float(estudiante[2][1])  # promedio

    if horas == 1:
        suma_1 += promedio
        cont_1 += 1

    elif horas == 2:
        suma_2 += promedio
        cont_2 += 1

    elif horas == 3:
        suma_3 += promedio
        cont_3 += 1

    elif horas == 4:
        suma_4 += promedio
        cont_4 += 1

    elif horas == 5:
        suma_5 += promedio
        cont_5 += 1


# promedios
prom_1 = suma_1 / cont_1 if cont_1 > 0 else 0
prom_2 = suma_2 / cont_2 if cont_2 > 0 else 0
prom_3 = suma_3 / cont_3 if cont_3 > 0 else 0
prom_4 = suma_4 / cont_4 if cont_4 > 0 else 0
prom_5 = suma_5 / cont_5 if cont_5 > 0 else 0


# resultados
print("Promedio con 1 hora de estudio:", round(prom_1, 2))
print("Promedio con 2 horas de estudio:", round(prom_2, 2))
print("Promedio con 3 horas de estudio:", round(prom_3, 2))
print("Promedio con 4 horas de estudio:", round(prom_4, 2))
print("Promedio con 5 horas de estudio:", round(prom_5, 2))

# Cual tiene el mejor promedio
mejor_promedio = prom_1
mejor_horas = 1

if prom_2 > mejor_promedio:
    mejor_promedio = prom_2
    mejor_horas = 2

if prom_3 > mejor_promedio:
    mejor_promedio = prom_3
    mejor_horas = 3

if prom_4 > mejor_promedio:
    mejor_promedio = prom_4
    mejor_horas = 4

if prom_5 > mejor_promedio:
    mejor_promedio = prom_5
    mejor_horas = 5


print("El mejor promedio lo obtienen los estudiantes que estudian", mejor_horas, "horas")