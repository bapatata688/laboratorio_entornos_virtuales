import csv

# diccionario con llave id_trabajadores que sera una lista
encuestas = {"promedio": []}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    lector = csv.DictReader(encuesta)
    # por cada dato de la columna de promedio, se agrega a la lista promedio del
    # diccionario
    for datos in lector:
        promedio = float(datos["promedio"])
        encuestas["promedio"].append(promedio)

# el total de notas es la suma de las notas divido entre la longitud de total de notas
notas = encuestas["promedio"]
total_notas = sum(notas) / len(notas)
print(f"promedio general:{total_notas:.2f}")
