import csv

personas = []
with open('../dataset_10000_personas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        persona = {
            "datos_academicos": {
                "carrera": fila["carrera"],
                "promedio": int(fila["promedio"])
            }
        }
        personas.append(persona)

# Lógica: Acumular sumas y conteos por carrera
sumas_carreras = {}
conteos_carreras = {}

for p in personas:
    carr = p["datos_academicos"]["carrera"]
    prom = p["datos_academicos"]["promedio"]
    
    if carr in sumas_carreras:
        sumas_carreras[carr] += prom
        conteos_carreras[carr] += 1
    else:
        sumas_carreras[carr] = prom
        conteos_carreras[carr] = 1

# Calcular promedios y buscar el mayor
mejor_carrera = ""
mejor_promedio = 0

for carrera in sumas_carreras.keys():
    promedio_actual = sumas_carreras[carrera] / conteos_carreras[carrera]
    if promedio_actual > mejor_promedio:
        mejor_promedio = promedio_actual
        mejor_carrera = carrera

print(f"--- Reporte 14 ---")
print(f"La carrera con el promedio más alto es {mejor_carrera} con {mejor_promedio:.2f}")