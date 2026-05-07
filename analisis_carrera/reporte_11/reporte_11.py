import csv

personas = []
# 1. Leer CSV y crear estructura de diccionarios
with open("../dataset_10000_personas.csv", mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        persona = {
            "id": int(fila["id"]),
            "nombre": fila["nombre"],
            "edad": int(fila["edad"]),
            "ciudad": fila["ciudad"],
            "datos_academicos": {
                "carrera": fila["carrera"],
                "semestre": int(fila["semestre"]),
                "promedio": int(fila["promedio"])
            },
            "datos_laborales": {
                "trabaja": fila["trabaja"] == "True",
                "ingreso_mensual": int(fila["ingreso_mensual"])
            },
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True",
                "computadora": fila["computadora"] == "True"
            }
        }
        personas.append(persona)

# 2. Lógica del reporte
conteo_semestres = {}

for p in personas:
    semestre = p["datos_academicos"]["semestre"]
    if semestre in conteo_semestres:
        conteo_semestres[semestre] += 1
    else:
        conteo_semestres[semestre] = 1

print("--- Reporte 11: Cantidad de personas por semestre ---")
for sem, total in conteo_semestres.items():
    print(f"Semestre {sem}: {total} personas")