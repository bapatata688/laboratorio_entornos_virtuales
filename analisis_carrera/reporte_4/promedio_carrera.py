import csv

# diccionario con llave id_trabajadores que sera una lista
encuestas = {}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    lector = csv.DictReader(encuesta)
    for dato in lector:
        promedio = float(dato["promedio"])
        carrera = dato["carrera"]
        if carrera not in encuestas:
            encuestas[carrera] = []
        encuestas[carrera].append(promedio)
for llave, valor in encuestas.items():
    promedio_carrera = sum(valor) / len(valor)
    print(f"carrera: {llave} tiene {promedio_carrera:.2f} de promedio")
