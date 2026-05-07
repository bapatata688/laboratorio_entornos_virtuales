#Reporte 20: Perfil promedio del encuestado
import csv

def cargar_datos(ruta):
    encuestados = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "edad": int(fila["edad"]),
                "ingreso": float(fila["ingreso_mensual"]),
                "promedio": float(fila["promedio"]),
                "trabaja": fila["trabaja"].lower() == "true"
            }
            encuestados.append(persona)
    return encuestados

ruta = "dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("\nREPORTE 20: Perfil promedio del encuestado")

total = len(datos)

suma_edad = 0
suma_ingreso = 0
suma_promedio = 0
trabajan = 0

for p in datos:
    suma_edad += p["edad"]
    suma_ingreso += p["ingreso"]
    suma_promedio += p["promedio"]

    if p["trabaja"]:
        trabajan += 1

# Promedios
prom_edad = suma_edad / total
prom_ingreso = suma_ingreso / total
prom_promedio = suma_promedio / total
porcentaje_trabaja = (trabajan / total) * 100

print("Edad promedio:", round(prom_edad, 2))
print("Ingreso mensual promedio:", round(prom_ingreso, 2))
print("Promedio académico:", round(prom_promedio, 2))
print("Porcentaje que trabaja:", round(porcentaje_trabaja, 2), "%")
