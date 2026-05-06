import csv

# columnas: id(0) carrera(1) semestre(2) jornada(3) trabaja(4) promedio_actual(5)
INDICE_CARRERA = 1
INDICE_PROMEDIO = 5

# estructura: [nombre_carrera, suma_promedios, cantidad_estudiantes]
prom_carrera = []

with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiante:
    encuesta = csv.reader(estudiante)
    next(encuesta)

    for fila in encuesta:
        carrera = fila[INDICE_CARRERA].strip()
        promedio = float(fila[INDICE_PROMEDIO].strip())
        encontrado = False

        for c in prom_carrera:
            if c[0] == carrera:
                c[1] += promedio
                c[2] += 1
                encontrado = True
                break

        if not encontrado:
            prom_carrera.append([carrera, promedio, 1])

for c in prom_carrera:
    prom = c[1] / c[2]
    print(f"{c[0]}: {round(prom, 2)}")
