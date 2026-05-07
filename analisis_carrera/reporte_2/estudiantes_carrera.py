import csv

# diccionario estudiantes, contiene carreras, contadores,
encuestados = {
    "carrera": ["Ing. Eléctrica", "Ing. Sistemas", "Ing. Electrónica"],
    "estudiantes_carrera": {
        "estudiantes_electrica": 0,
        "estudiantes_sistemas": 0,
        "estudiantes_electronica": 0,
    },
    "estudiantes_por_carrera": {
        "ingeneria_electrica": [],
        "ingeneria_sistemas": [],
        "ingeneria_electronica": [],
    },
}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    encuestas = csv.DictReader(encuesta)
    for estudiante in encuestas:
        # si la columna contiene una de las carreras, aumentar contador y guardarlo en la lista
        carrera = estudiante["carrera"]
        if carrera == encuestados["carrera"][0]:
            encuestados["estudiantes_carrera"]["estudiantes_electrica"] += 1
            encuestados["estudiantes_por_carrera"]["ingeneria_electrica"].append(
                encuestados["estudiantes_carrera"]["estudiantes_electrica"]
            )
        if carrera == encuestados["carrera"][1]:
            encuestados["estudiantes_carrera"]["estudiantes_sistemas"] += 1
            encuestados["estudiantes_por_carrera"]["ingeneria_sistemas"].append(
                encuestados["estudiantes_carrera"]["estudiantes_sistemas"]
            )
        if carrera == encuestados["carrera"][2]:
            encuestados["estudiantes_carrera"]["estudiantes_electronica"] += 1
            encuestados["estudiantes_por_carrera"]["ingeneria_electronica"].append(
                encuestados["estudiantes_carrera"]["estudiantes_electronica"]
            )


total_ing_electricos = len(
    encuestados["estudiantes_por_carrera"]["ingeneria_electrica"]
)
total_ing_sistemas = len(encuestados["estudiantes_por_carrera"]["ingeneria_sistemas"])
total_ing_electronicos = len(
    encuestados["estudiantes_por_carrera"]["ingeneria_electronica"]
)
print(
    f"Total de estudiantes de Ing. Eléctrica: {total_ing_electricos}, total de estudiantes de Ing. sistemas: {total_ing_sistemas}, total de ing electronicos: {total_ing_electronicos}"
)
