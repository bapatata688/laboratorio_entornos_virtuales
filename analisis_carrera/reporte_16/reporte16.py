#REPORTE 16:Relacion entre ingreso y promedio 


import csv                                                                   # Esta es la libreria csv que nos permite leer archivos csv

def cargar_datos(ruta):                                                      # Esta funcion se utiliza para reutilizar el codigo de lectura del archivo csv, recibe como parametro la ruta del archivo
    encuestados = []                                                         # Creamos una lista vacia para almacenar los datos de los encuestados
    with open(ruta, newline='', encoding='utf-8') as archivo:                # Abrimos el archivo csv utilizando la funcion open, especificamos la ruta, el modo de apertura, el tipo de salto de linea y la codificacion, ademas with se asegura que se cierre el archivo al finalizar
        lector = csv.DictReader(archivo)                                     # Creamos un objeto lector utilizando csv.DictReader, que nos permite leer el archivo csv como un diccionario, donde las claves son los nombres de las columnas o en este caso "id"
        for fila in lector:                                                  # Utilizamos un bucle for para recorrer las 10,00 personas una por una
            persona = {                                                      # Empezamos a crear una estructura mas ordenada de diccionarios 
                "id": int(fila["id"]),                                       # Convertimos el valor de "id" a un numero entero y lo asignamos a la clave "id" del diccionario persona
                "nombre": fila["nombre"],                                    # Asignamos el valor de "nombre" a la clave "nombre" del diccionario persona  
                "edad": int(fila["edad"]),                                   # Convertimos el valor de "edad" a un numero entero y lo asignamos a la clave "edad" del diccionario persona
                "ciudad": fila["ciudad"],                                    # Asignamos el valor de "ciudad" a la clave "ciudad" del diccionario persona
                "datos_academicos": {                                        # En esta seccion un diccionario dentro de otro esto es un diccionario anidado, donde "datos_academicos" es la clave del diccionario persona
                    "promedio": float(fila["promedio"])                      # y su valor es otro diccionario con las claves "carrera", "semestre" y "promedio"
                    "carrera": fila["carrera"],
                    "semestre": int(fila["semestre"]),
                },
                "datos_laborales": {
                    "trabaja": fila["trabaja"].lower() == "true",            # Convertimos el valor de "trabaja" a un booleano, primero lo convertimos a minusculas con lower() y luego comparamos si es igual a "true", esto nos dara True o False dependiendo del valor original    
                    "ingreso_mensual": float(fila["ingreso_mensual"])
                },
                "datos_tecnologicos": {
                    "internet": fila["internet"].lower() == "true",
                    "computadora": fila["computadora"].lower() == "true"
                }
            }
            encuestados.append(persona)
    return encuestados

ruta = "dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("\nREPORTE 16")

suma_ingresos = 0
suma_promedios = 0
contador = 0

for p in datos:
    ingreso = p["datos_laborales"]["ingreso_mensual"]
    promedio = p["datos_academicos"]["promedio"]

    if ingreso > 0:
        suma_ingresos += ingreso
        suma_promedios += promedio
        contador += 1

print("Promedio ingreso:", round(suma_ingresos/contador,2))
print("Promedio académico:", round(suma_promedios/contador,2))