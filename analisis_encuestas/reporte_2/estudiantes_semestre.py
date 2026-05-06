import csv

semestre_5 = 5
semestre_6 = 6
semestre_7 = 7
estudiantes_semestre_5 = 0
estudiantes_semestre_6 = 0
estudiantes_semestre_7 = 0
estudiante_semestre = [[], [], []]

with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiantes:
    encuesta = csv.reader(estudiantes)
    next(encuesta)
    for semestre in encuesta:
        estudiantes_semestre = int(semestre[2].strip())
        if estudiantes_semestre == semestre_5:
            estudiantes_semestre_5 += 1
            estudiante_semestre[0].append(estudiantes_semestre_5)
        if estudiantes_semestre == semestre_6:
            estudiantes_semestre_6 += 1
            estudiante_semestre[1].append(estudiantes_semestre_6)
        if estudiantes_semestre == semestre_6:
            estudiantes_semestre_7 += 1
            estudiante_semestre[2].append(estudiantes_semestre_7)
total_semestre_5 = len(estudiante_semestre[0])
total_semestre_6 = len(estudiante_semestre[1])
total_semestre_7 = len(estudiante_semestre[2])
print(
    f"Total estudiantes semestre 5: {total_semestre_5} Total estudiantes semestre 6: {total_semestre_6} Total estudiantes semestre 7: {total_semestre_7}"
)
