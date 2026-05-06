import csv

# lista de encuestados
encuestados = []
# contador de encuestados
encuestado = 0
# abrir las encuestas
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf_8"
) as encuestas:
    # asignar la variable encuesta leyendo las encuestas
    encuesta = csv.reader(encuestas)
    # salto de la primera linea
    next(encuesta)
    # recorrer las filas de el csv, asignando la primera columna a la variable id_encuestado
    for encuesta in encuesta:
        id_encuestado = encuesta[0]
        # si es la primera columna de la encuesta, se agrega el id de encuestado a la lst
        if id_encuestado:
            encuestados.append(id_encuestado)
            # aumentar el contador
            encuestado += 1
# el total de encuestados sera igual a la longitud de la lista
total_encuestados = len(encuestados)
# imprimir el total de encuestados
print(f"Total de encuestados: {total_encuestados}")
