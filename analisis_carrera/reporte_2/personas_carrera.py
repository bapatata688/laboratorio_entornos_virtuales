import csv

encuestas = {}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    lector = csv.DictReader(encuesta)
    # si la carrera no esta en el diccionario encuestas se crea como lista
    for datos in lector:
        carrera = datos["carrera"]
        if carrera not in encuestas:
            encuestas[carrera] = []
            # se agrega a la lista
        encuestas[carrera].append(datos)
# se recorre llave y valor de encuestas y se muestra
for llave, valor in encuestas.items():
    total_estudiantes = len(valor)
    print(f"{llave}: {total_estudiantes}")
