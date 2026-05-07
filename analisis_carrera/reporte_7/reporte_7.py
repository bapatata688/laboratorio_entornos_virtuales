# reporte 7: cantidad de personas con internet

import csv

# creamos una lista vacia donde guardaremos todas las personas
# cada elemento sera un diccionario con estructura organizada
personas = []

# abrimos el archivo csv en modo lectura
with open("dataset_10000_personas.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    # recorremos cada fila del archivo
    for fila in lector:

        # construimos un diccionario por cada persona
        # usamos diccionarios anidados para separar tipos de informacion
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
                # convertimos el texto a valor booleano
                "trabaja": fila["trabaja"] == "True",
                "ingreso_mensual": float(fila["ingreso_mensual"])
            },

            # subdiccionario con informacion tecnologica
            "datos_tecnologicos": {
                "internet": fila["internet"] == "True",
                "computadora": fila["computadora"] == "True"
            }
        }

        # agregamos la persona a la lista
        personas.append(persona)


# tomamos una persona como ejemplo para mostrar la estructura
prueba = personas[0]

print("\n==============================")
print("claves de una persona:")

# usamos keys() para recorrer todas las claves del diccionario
# esto nos ayuda a entender como esta organizada la informacion
for clave in prueba.keys():
    print("-", clave)

print("\n==============================")
print("valores de datos tecnologicos:")

# usamos values() para mostrar solo los valores del subdiccionario
for valor in prueba["datos_tecnologicos"].values():
    print("-", valor)


# iniciamos el contador de personas con internet
contador_internet = 0

# recorremos todas las personas almacenadas
for persona in personas:

    # verificamos que exista la clave datos_tecnologicos
    if "datos_tecnologicos" in persona:

        datos = persona["datos_tecnologicos"]

        # recorremos el subdiccionario usando items()
        # para que nos de acceso a clave y valor al mismo tiempo
        for clave, valor in datos.items():

            # buscamos especificamente la clave internet
            if clave == "internet":

                # verificamos que el valor sea booleano para que el dato sea vaido
                if isinstance(valor, bool):

                    # si el valor es true significa que la persona tiene internet
                    if valor:
                        contador_internet += 1


# mostramos los resultados finales

print("\n==============================")
print("resultados")

# usamos len para contar cuantas personas hay en total
print("total de registros:", len(personas))

# mostramos cuantas personas tienen acceso a internet
print("cantidad de personas con internet:", contador_internet)

print("\n==============================")