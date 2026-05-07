# reporte 8: cantidad de personas con computadora

import csv

# lista donde almacenaremos todos los registros del csv
# cada elemento sera un diccionario que representa una persona
personas = []

# abrimos el archivo csv en modo lectura
with open("dataset_10000_personas.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    # recorremos cada fila del archivo
    for fila in lector:

        # construimos un diccionario anidado por cada persona
        persona = {
            "id": int(fila["id"]),
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
                # convertimos string a booleano comparando con "True"
                "trabaja": fila["trabaja"] == "True",
                "ingreso_mensual": float(fila["ingreso_mensual"])
            },

            # subdiccionario con informacion tecnologica
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True",
                "computadora": fila["computadora"] == "True"
            }
        }

        # agregamos cada persona a la lista
        personas.append(persona)


# tomamos el primer registro como ejemplo para mostrar estructura
prueba = personas[0]

print("\n==============================")
print("claves de una persona:")

# usamos keys() para ver las claves principales del diccionario
for clave in prueba.keys():
    print("-", clave)

print("\n==============================")
print("valores de datos tecnologicos:")

# accedemos al subdiccionario y usamos values() para ver sus valores
for valor in prueba["datos_tecnologicos"].values():
    print("-", valor)


# iniciamos contador para personas con computadora
contador_computadora = 0

# recorremos toda la lista de personas
for persona in personas:

    # verificamos que exista la clave datos_tecnologicos
    if "datos_tecnologicos" in persona:

        datos = persona["datos_tecnologicos"]

        # recorremos clave y valor usando items()
        for clave, valor in datos.items():

            # buscamos especificamente la clave computadora
            if clave == "computadora":

                # validamos que el valor sea booleano
                if isinstance(valor, bool):

                    # si es true significa que tiene computadora
                    if valor:
                        contador_computadora += 1


# mostramos resultados finales

print("\n==============================")
print("resultados")

# usamos len() para contar total de registros
print("total de registros:", len(personas))

# mostramos cantidad de personas con computadora
print("cantidad de personas con computadora:", contador_computadora)

print("==============================")

