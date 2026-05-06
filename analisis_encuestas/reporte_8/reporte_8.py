import csv

# columnas: id(0) carrera(1) semestre(2) jornada(3) trabaja(4) promedio_actual(5)
INDICE_SEMESTRE = 2
INDICE_PROMEDIO = 5

# estructura: [semestre, suma_promedios, cantidad_estudiantes]
prom_semestre = []

with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiante:
    encuesta = csv.reader(estudiante)
    next(encuesta)

    for fila in encuesta:
        semestre = int(fila[INDICE_SEMESTRE].strip())
        promedio = float(fila[INDICE_PROMEDIO].strip())
        encontrado = False

        for s in prom_semestre:
            if s[0] == semestre:
                s[1] += promedio
                s[2] += 1
                encontrado = True
                break

        if not encontrado:
            prom_semestre.append([semestre, promedio, 1])

prom_semestre.sort(key=lambda s: s[0])

for s in prom_semestre:
    prom = s[1] / s[2]
    print(f"Semestre {s[0]}: {round(prom, 2)}")
