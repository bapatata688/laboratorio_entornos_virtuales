# reporte 10: promedio academico de personas que no trabajan

import csv

# lista donde almacenaremos todas las personas
# cada elemento sera un diccionario con datos organizados
personas = []

# abrimos el archivo csv
with open("dataset_10000_personas.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    # recorremos cada fila del archivo
    for fila in lector:

        # construimos un diccionario anidado por persona
        persona = {
            "id": int(fila["id"]),
            "nombre": fila["nombre"],
            "edad": int(fila["edad"]),
            "ciudad": fila["ciudad"],

            # subdiccionario con datos academicos
            "datos_academicos": {
                "carrera": fila["carrera"],
                "semestre": int(fila["semestre"]),
                "promedio": float(fila["promedio"])
            },

            # subdiccionario con datos laborales
            "datos_laborales": {
                # convertimos string a booleano
                "trabaja": fila["trabaja"] == "True",
                "ingreso_mensual": float(fila["ingreso_mensual"])
            },

            # subdiccionario con datos tecnologicos
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True",
                "computadora": fila["computadora"] == "True"
            }
        }

        # agregamos la persona a la lista
        personas.append(persona)


# usamos un ejemplo para mostrar la estructura del diccionario
prueba = personas[0]

print("\n==============================")
print("claves de una persona:")

# usamos keys() para ver las claves principales
for clave in prueba.keys():
    print("-", clave)


# variables para calcular el promedio
suma_promedios = 0

# lista donde guardamos promedios validos
promedios_validos = []

# recorremos todas las personas
for persona in personas:

    # verificamos que exista datos laborales
    if "datos_laborales" in persona:

        datos_lab = persona["datos_laborales"]

        # filtramos personas que no trabajan (false)
        if "trabaja" in datos_lab and datos_lab["trabaja"] == False:

            # accedemos a los datos academicos
            if "datos_academicos" in persona:

                datos_acad = persona["datos_academicos"]

                # recorremos el subdiccionario con items()
                for clave, valor in datos_acad.items():

                    # buscamos el promedio
                    if clave == "promedio":

                        # validamos que sea numerico
                        if isinstance(valor, (int, float)):

                            # acumulamos la suma
                            suma_promedios += valor

                            # guardamos el valor para conteo
                            promedios_validos.append(valor)


# calculamos el promedio final
if len(promedios_validos) > 0:
    promedio_final = suma_promedios / len(promedios_validos)
else:
    promedio_final = 0

# mostramos resultados

print("\n==============================")
print("resultados")

# total de registros en la base
print("total de registros:", len(personas))

# cantidad de personas que no trabajan
print("cantidad de personas que no trabajan:", len(promedios_validos))

# promedio academico calculado
print("promedio academico de personas que no trabajan:", round(promedio_final, 2))

print("==============================")