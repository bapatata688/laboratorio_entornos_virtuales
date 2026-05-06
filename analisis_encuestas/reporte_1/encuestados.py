import csv

# programa que calcula el total de encuestados en un csv.
# pre: encuestados siendo el primer valor del csv.
# post: mostrar el total de encuestados

# lista de encuestados en la encuesta
# pre: la lista esta vacia
# post: la lista contiene los id de los encuestados
encuestados = []
# contador de encuestados
# pre: empieza por cero
# post: contiene la id_encuestado
encuestado = 0
# abrir el csv como encuestas
# pre: el csv esta una carpeta arriba respecto al script actual
# post: lectura del csv
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf_8"
) as encuestas:
    # lectura de encuestas con la libreria csv
    encuesta = csv.reader(encuestas)
    # salto de primera linea
    next(encuesta)
    # recorrer la primera columna de las encuestas
    # pre: las id de encuestados son la primera columna en las encuestas
    # post: encuestados contiene los id de los encuestados
    for encuesta in encuesta:
        id_encuestado = encuesta[0]
        if id_encuestado:
            encuestados.append(id_encuestado)
            encuestado += 1
# longitud de la lista de encuestados
# pre: encuestados contiene solamente id de los encuestados
# post: longitud de encuestados
total_encuestados = len(encuestados)
print(f"Total de encuestados: {total_encuestados}")
