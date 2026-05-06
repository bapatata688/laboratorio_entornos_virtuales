import csv

# se enlistan las carreras
carreras = ["Ingeniería Eléctrica", "Ingeniería de Sistemas", "Ingeniería Electrónica"]
# se agregan contadores de las carreras
ing_electrica = 0
ing_sistemas = 0
ing_electronica = 0
# se crea una lista anidada con las carreras
estudiantes_ingienerias = [[], [], []]
# se abre el documento de encuestas en modo lectura
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiantes:
    # se lee el documento con csv
    encuesta = csv.reader(estudiantes)
    # se hace un salto de linea
    next(encuesta)
    # se crea un bucle que recorra en las columnas de las carreras
    for encuestado in encuesta:
        # se define la variable carrera, que es la columna de carreras
        carrera = encuestado[1]
        # si la carrera es igual a la primera carrera, se agrega un 1 a la primera lista
        if carrera == carreras[0]:
            estudiantes_ingienerias[1].append(ing_electrica)
        # si la carrera es igual a la segunda carrera, se agrega un 1 a la segunda lista
        elif carrera == carreras[1]:
            estudiantes_ingienerias[0].append(ing_sistemas)
        # si la carrera es igual a la tercera carrera, se agrega un 1 a la tercera lista
        elif carrera == carreras[2]:
            estudiantes_ingienerias[2].append(ing_electronica)
# se cuantifica la cantidad de estudiantes por carrera con la funcion len
total_estudiantes_electricos = len(estudiantes_ingienerias[0])
total_estudiantes_sistemas = len(estudiantes_ingienerias[1])
total_estudiantes_electronicos = len(estudiantes_ingienerias[2])
# se imprime la cantidad de estudiantes por carrera
print(
    f"Ingenieros electricos: {total_estudiantes_electricos} Ingenieros de sistemas: {total_estudiantes_sistemas} total electronicos: {total_estudiantes_electronicos}"
)
# fin del algoritmo
