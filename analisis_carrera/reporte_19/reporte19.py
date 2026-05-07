#Reperote 19: Porcentaje de personas que trabajan

import csv

def cargar_datos(ruta):
    encuestados = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "trabaja": fila["trabaja"].lower() == "true"
            }
            encuestados.append(persona)
    return encuestados

ruta = "dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("\nREPORTE 19")

total = len(datos)
trabajan = 0

for p in datos:
    if p["trabaja"]:
        trabajan += 1

print("Porcentaje:", round((trabajan/total)*100,2), "%")