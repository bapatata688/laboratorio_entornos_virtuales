import csv

# diccionario con llave id_trabajadores que sera una lista
encuestas = {"si_trabaja": [], "no_trabaja": []}
with open("../dataset_10000_personas.csv", "r", encoding="utf-8") as encuesta:
    lector = csv.DictReader(encuesta)
    for dato in lector:
        trabajador = dato["trabaja"]
        if trabajador == "True":
            encuestas["si_trabaja"].append(trabajador)
        if trabajador == "False":
            encuestas["no_trabaja"].append(trabajador)
total_trabajadores = len(encuestas["si_trabaja"])
total_no_trabajadores = len(encuestas["no_trabaja"])
total_datos = total_no_trabajadores + total_trabajadores
porcentaje_trabajadores = (total_trabajadores / total_datos) * 100
porcentaje_no_trabajadores = (total_no_trabajadores / total_datos) * 100
print(f"no trabajan: {total_no_trabajadores} trabajan:{total_trabajadores}")
print(
    f"porcentaje no trabajan: {porcentaje_no_trabajadores}% porcentaje si trabajan:{porcentaje_trabajadores}%"
)
