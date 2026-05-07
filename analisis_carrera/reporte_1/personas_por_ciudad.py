import csv

# diccionario con llave id_trabajadores que sera una lista
encuestas = {}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    lector = csv.DictReader(encuesta)
    # si la ciudad no esta en el diccionario encuestas se crea como lista
    for datos in lector:
        ciudad = datos["ciudad"]
        if ciudad not in encuestas:
            encuestas[ciudad] = []
        encuestas[ciudad].append(datos)
# se recorre llave y valor de encuestas y se muestra
for llave, valor in encuestas.items():
    print(f"{llave}: {len(valor)}")
