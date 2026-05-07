# reporte 6: promedio de ingresos

import csv

# creamos una lista vacia donde vamos a guardar a todas las personas
# cada elemento de la lista sera un diccionario con informacion estructurada
personas = []

# abrimos el archivo csv en modo lectura
with open("dataset_10000_personas.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    # recorremos cada fila del archivo
    for fila in lector:

        # construimos un diccionario por cada persona
        # agregando tambien diccionarios anidados 
        persona = {
            "id": int(fila["id"]),  # convertimos a entero
            "nombre": fila["nombre"],
            "edad": int(fila["edad"]),
            "ciudad": fila["ciudad"],

            # subdiccionario con informacion academica
            "datos_academicos": {
                "carrera": fila["carrera"],
                "semestre": int(fila["semestre"]),
                "promedio": float(fila["promedio"])
            },

            # subdiccionario con informacion laboral
            "datos_laborales": {
                # convertimos el texto "True" o "False" a booleano
                "trabaja": fila["trabaja"] == "True",
                "ingreso_mensual": float(fila["ingreso_mensual"])
            },

            # subdiccionario con informacion tecnologica
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True",
                "computadora": fila["computadora"] == "True"
            }
        }

        # agregamos el diccionario de la persona a la lista
        personas.append(persona)


# tomamos una persona como ejemplo para mostrar estructura
prueba = personas[0]

print("\n==============================")
print("claves de una persona:")

# usamos keys() para recorrer las claves del diccionario
# esto nos permite ver la estructura general de los datos
for clave in prueba.keys():
    print("-", clave)


# iniciamos variables para el calculo
suma_ingresos = 0
contador = 0

# recorremos todas las personas de la lista
for persona in personas:

    # verificamos que la clave datos_laborales exista en el diccionario
    if "datos_laborales" in persona:

        datos = persona["datos_laborales"]

        # verificamos que exista la clave ingreso_mensual
        if "ingreso_mensual" in datos:

            ingreso = datos["ingreso_mensual"]

            # usamos isinstance para validar que el valor sea numerico
            if isinstance(ingreso, (int, float)):

                # acumulamos los ingresos
                suma_ingresos += ingreso

                # contamos cuantas personas tienen ingreso valido
                contador += 1


# calculamos el promedio
# evitamos division entre cero verificando el contador
if contador > 0:
    promedio = suma_ingresos / contador
else:
    promedio = 0


# mostramos resultados finales

print("\n==============================")
print("resultados")

# usamos len para contar total de registros en la lista
print("total de registros en la base:", len(personas))

# mostramos cuantas personas fueron consideradas en el calculo
print("cantidad de personas analizadas:", contador)

# mostramos el promedio con 2 decimales
print("promedio de ingresos:", round(promedio, 2))

print("\n==============================")