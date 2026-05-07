import csv

personas = []
with open('../dataset_10000_personas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        persona = {
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True"
            }
        }
        personas.append(persona)

# Lógica del reporte
sin_internet = 0
for p in personas:
    # Validando si el valor de internet es False
    if p["datos_tecnologicos"]["internet"] == False:
        sin_internet += 1

print(f"--- Reporte 15 ---")
print(f"Cantidad total de personas que no cuentan con internet: {sin_internet}")