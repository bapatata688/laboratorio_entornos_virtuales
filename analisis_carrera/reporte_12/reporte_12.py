import csv

personas = []
with open('../dataset_10000_personas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        persona = {
            "id": int(fila["id"]),
            "nombre": fila["nombre"],
            "edad": int(fila["edad"]),
            # ... (el resto de campos se pueden omitir o incluir según la estructura base)
        }
        personas.append(persona)

# Lógica del reporte
suma_edades = 0
for p in personas:
    suma_edades += p["edad"]

promedio = suma_edades / len(personas)

print(f"--- Reporte 12 ---")
print(f"La edad promedio de las 10,000 personas es: {promedio:.2f} años")