import csv

personas = []
with open('../dataset_10000_personas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        personas.append({"ciudad": fila["ciudad"]})

# Lógica del reporte
conteo_ciudades = {}
for p in personas:
    ciudad = p["ciudad"]
    if ciudad in conteo_ciudades:
        conteo_ciudades[ciudad] += 1
    else:
        conteo_ciudades[ciudad] = 1

# Encontrar el mayor usando items()
ciudad_top = ""
max_personas = 0

for ciudad, total in conteo_ciudades.items():
    if total > max_personas:
        max_personas = total
        ciudad_top = ciudad

print(f"--- Reporte 13 ---")
print(f"La ciudad con más personas es {ciudad_top} con {max_personas} registros.")