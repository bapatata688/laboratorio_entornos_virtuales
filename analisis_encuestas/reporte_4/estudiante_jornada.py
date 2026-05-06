import csv

# se define una lista con las jornadas
jornada = ["Matutina", "Vespertina", "Nocturna"]
# se definen los contadores por jornada
turno_matutino = 0
turno_vespertino = 0
turno_nocturno = 0
# se define una lista anidada con las jornadas que almancenaran los contenedores
jornadas = [[], [], []]
# se abre el csv de encuesta
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as encuestas:
    # se lee el csv de encuesta y se asigna a la variable encuesta
    encuesta = csv.reader(encuestas)
    # salto de la primera linea del csv
    next(encuesta)

    # se itera sobre las columna de jornada, si hay coincidencia entre el valor de la fila y la jornada, se incrementa el contador y se agrega a la lista de jorandas
    for turno in encuesta:
        turno_jornada = turno[3].strip()
        if turno_jornada == jornada[0]:
            turno_matutino += 1
            jornadas[0].append(turno_matutino)
        if turno_jornada == jornada[1]:
            turno_vespertino += 1
            jornadas[1].append(turno_vespertino)
        if turno_jornada == jornada[2]:
            turno_nocturno += 1
            jornadas[2].append(turno_nocturno)
# se calcula la longitud de las listas
total_turno_matutino = len(jornadas[0])
total_turno_vespertino = len(jornadas[1])
total_turno_nocturno = len(jornadas[2])
# se imprimen
print(
    f"Matutino: {total_turno_matutino} Vespertino: {total_turno_vespertino} Nocturno: {total_turno_nocturno}"
)
