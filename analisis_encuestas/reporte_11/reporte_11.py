def procesar_datos_encuesta():
    encuestas = []
    try:
        with open('encuesta_ingenieria_10000_respuestas.csv', 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(',')
                if len(datos) == 26:
                    generales = [datos[1], int(datos[2]), datos[3], int(datos[5])]
                    academicas = [int(x) for x in datos[6:15] + datos[16:20]] # q01 está aquí
                    tecnologicas = [int(datos[15])]
                    economicas = [datos[4]]
                    percepcion = [int(x) for x in datos[20:26]]
                    encuestado = [int(datos[0]), generales, academicas, tecnologicas, economicas, percepcion]
                    encuestas.append(encuestado)
    except FileNotFoundError:
        print("Error: No se encontró 'encuesta_ingenieria_10000_respuestas.csv' en la carpeta.")
    return encuestas

def generar_reporte_11():
    datos = procesar_datos_encuesta()
    if not datos: return
    
    horas_estudio = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
    
    for encuestado in datos:
        respuesta_horas = encuestado[2][0]
        for i in range(len(horas_estudio)):
            if horas_estudio[i][0] == respuesta_horas:
                horas_estudio[i][1] += 1
                break
                
    print("--- Reporte 11: Cantidad de estudiantes según horas de estudio (q01) ---")
    print("Codificación de Horas (1 a 5) | Estudiantes")
    print("-" * 45)
    for item in horas_estudio:
        print(f" Opción {item[0]} {' ' * 21} | {item[1]}")

if __name__ == "__main__":
    generar_reporte_11()