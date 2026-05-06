# Reporte 20: Listado del perfil predominante del encuestado según las respuestas más frecuentes. 

import csv

encuesta = []

with open("../encuesta_ingenieria_10000_respuestas.csv", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)

    for fila in lector:

        estudiante = [
            fila[0],
            [fila[1], fila[2], fila[3]],  # generales
            [fila[4], fila[5]],           # académicos
            [fila[6], fila[7]],           # tecnológicos
            fila[8:]
        ]

        encuesta.append(estudiante)



# Contadores de carrera
sistemas = 0
electronica = 0
electrica = 0

# Contadores de semestre
sem_5 = 0
sem_6 = 0
sem_7 = 0

# Contadores de jornada
matutina = 0
vespertina = 0
nocturna = 0

# Contadores de trabajo
trabaja_si = 0
trabaja_no = 0

# Internet
internet_bueno = 0
internet_malo = 0

# Estres
estres_bajo = 0
estres_medio = 0
estres_alto = 0

# Satisfaccion
satis_baja = 0
satis_media = 0
satis_alta = 0

# Recorrido de estudiantes
for estudiante in encuesta:

    # Carrera
    carrera = estudiante[1][0]
    if carrera == "Ingenieria de Sistemas":
        sistemas += 1
    elif carrera == "Ingenieria Electronica":
        electronica += 1
    else:
        electrica += 1

    # Semestre
    semestre = int(estudiante[1][1])
    if semestre == 5:
        sem_5 += 1
    elif semestre == 6:
        sem_6 += 1
    else:
        sem_7 += 1

    # Jornada
    jornada = estudiante[1][2]
    if jornada == "Matutina":
        matutina += 1
    elif jornada == "Vespertina":
        vespertina += 1
    elif jornada == "Nocturna":
        nocturna += 1

    # Trabajo
    trabaja = estudiante[2][0]
    if trabaja == "Sí":
        trabaja_si += 1
    else:
        trabaja_no += 1

     # Internet 
    internet = int(estudiante[4][7])
    if internet >= 3:
        internet_bueno += 1
    else:
        internet_malo += 1

    # Estres 
    estres = int(estudiante[4][13])
    if estres <= 2:
        estres_bajo += 1
    elif estres == 3:
        estres_medio += 1
    else:
        estres_alto += 1

    # Satisfaccion 
    satisfaccion = int(estudiante[4][15])
    if satisfaccion <= 2:
        satis_baja += 1
    elif satisfaccion == 3:
        satis_media += 1
    else:
        satis_alta += 1

# Carrera 
if sistemas >= electronica and sistemas >= electrica:
    carrera_pred = "Ingenieria de Sistemas"
elif electronica >= sistemas and electronica >= electrica:
    carrera_pred = "Ingenieria Electronica"
else:
    carrera_pred = "Ingenieria Electrica"

# Semestre 
if sem_5 >= sem_6 and sem_5 >= sem_7:
    semestre_pred = "5"
elif sem_6 >= sem_5 and sem_6 >= sem_7:
    semestre_pred = "6"
else:
    semestre_pred = "7"

# Jornada 
if matutina >= vespertina and matutina >= nocturna:
    jornada_pred = "Matutina"
elif vespertina >= matutina and vespertina >= nocturna:
    jornada_pred = "Vespertina"
else:
    jornada_pred = "Nocturna"

# Trabajo 
if trabaja_si >= trabaja_no:
    trabajo_pred = "Trabaja"
else:
    trabajo_pred = "No trabaja"

# Internet
if internet_bueno >= internet_malo:
    internet_pred = "Buen acceso a internet"
else:
    internet_pred = "Mal acceso a internet"

# Estres
if estres_alto >= estres_medio and estres_alto >= estres_bajo:
    estres_pred = "Alto"
elif estres_medio >= estres_bajo:
    estres_pred = "Medio"
else:
    estres_pred = "Bajo"

# Satisfacción
if satis_alta >= satis_media and satis_alta >= satis_baja:
    satis_pred = "Alta"
elif satis_media >= satis_baja:
    satis_pred = "Media"
else:
    satis_pred = "Baja"


# Mostrar resultados
print("\nPerfil predominante del encuestado\n")
print("Carrera:", carrera_pred)
print("Semestre:", semestre_pred)
print("Jornada:", jornada_pred)
print("Situacion laboral:", trabajo_pred)
print("Acceso a internet:", internet_pred)
print("Nivel de estres:", estres_pred)
print("Satisfaccion con la carrera:", satis_pred)