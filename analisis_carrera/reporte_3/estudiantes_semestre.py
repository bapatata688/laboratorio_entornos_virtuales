import csv

# diccionario que almacenara el csv
dataset_10000_personas = {}

with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    # se recorre el csv, en la columna semestre
    for datos in lector_csv:
        semestre = datos["semestre"]

        # si el semestre no esta en el diccionario dataset, se crea como lista
        if semestre not in dataset_10000_personas:
            dataset_10000_personas[semestre] = []
        # si el semestre esta en el diccionario dataset, se agrega a la lista
        dataset_10000_personas[semestre].append(datos)
# se sortean los semestres, se recorren las llaves, ya que la estructura del dicionario es:
# "1":[...], "2":[...]} con las llaves como strings, convertimos esas llaves a ints
semestres_ordenados = sorted(dataset_10000_personas.keys(), key=int)
# se recorre el semetre ordenado y se imprime
for valores in semestres_ordenados:
    nombre_semestre = dataset_10000_personas[valores]
    total = len(nombre_semestre)
    print(f"{valores}: {total}")
