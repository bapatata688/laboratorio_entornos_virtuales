#Reporte 18: Promedio académico por ciudad

import csv

def cargar_datos(ruta):
    encuestados = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "ciudad": fila["ciudad"],
                "promedio": float(fila["promedio"])
            }
            encuestados.append(persona)
    return encuestados

ruta = "dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("\nREPORTE 18")

ciudades = {}

for p in datos:
    ciudad = p["ciudad"]
    prom = p["promedio"]

    if ciudad not in ciudades:
        ciudades[ciudad] = {"suma":0, "cantidad":0}

    ciudades[ciudad]["suma"] += prom
    ciudades[ciudad]["cantidad"] += 1

for ciudad, info in ciudades.items():
    promedio = info["suma"] / info["cantidad"]
    print(ciudad, ":", round(promedio,2))