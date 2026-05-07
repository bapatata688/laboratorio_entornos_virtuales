#Reporte 17:Cantidad de personas por rango de edad


import csv

def cargar_datos(ruta):
    encuestados = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "edad": int(fila["edad"])
            }
            encuestados.append(persona)
    return encuestados

ruta = "dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("\nREPORTE 17")

rangos = {"18-25":0, "26-35":0, "36-50":0, "51+":0}

for p in datos:
    edad = p["edad"]

    if 18 <= edad <= 25:
        rangos["18-25"] += 1
    elif 26 <= edad <= 35:
        rangos["26-35"] += 1
    elif 36 <= edad <= 50:
        rangos["36-50"] += 1
    else:
        rangos["51+"] += 1

for r, c in rangos.items():
    print(r, ":", c)