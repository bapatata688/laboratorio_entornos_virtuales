def procesar_datos_encuesta():
    encuestas = []
    try:
        with open('encuesta_ingenieria_10000_respuestas.csv', 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(',')
                if len(datos) == 26:
                    generales = [datos[1], int(datos[2]), datos[3], int(datos[5])]
                    academicas = [int(x) for x in datos[6:15] + datos[16:20]]
                    tecnologicas = [int(datos[15])]
                    economicas = [datos[4]]
                    percepcion = [int(x) for x in datos[20:26]] # q16 está aquí
                    encuestado = [int(datos[0]), generales, academicas, tecnologicas, economicas, percepcion]
                    encuestas.append(encuestado)
    except FileNotFoundError:
        print("Error: No se encontró 'encuesta_ingenieria_10000_respuestas.csv' en la carpeta.")
    return encuestas

def generar_reporte_13():
    datos = procesar_datos_encuesta()
    if not datos: return
    
    suma_estres = 0
    total_estudiantes = len(datos)
    
    for encuestado in datos:
        suma_estres += encuestado[5][1]
        
    promedio = suma_estres / total_estudiantes
    
    print("--- Reporte 13: Nivel de estrés académico general ---")
    print(f"Total de respuestas evaluadas: {total_estudiantes}")
    print(f"Promedio general de estrés (Escala 1-5): {promedio:.2f}")

if __name__ == "__main__":
    generar_reporte_13()