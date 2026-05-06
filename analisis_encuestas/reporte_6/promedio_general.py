import csv

# columnas: id(0) carrera(1) semestre(2) jornada(3) trabaja(4) promedio_actual(5)
INDICE_PROMEDIO = 5

suma = 0
total = 0

with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiante:
    encuesta = csv.reader(estudiante)
    next(encuesta)

    for fila in encuesta:
        suma += float(fila[INDICE_PROMEDIO].strip())
        total += 1

promedio_general = suma / total

print(f"Total de encuestados : {total}")
print(f"Promedio general     : {round(promedio_general, 2)}")
