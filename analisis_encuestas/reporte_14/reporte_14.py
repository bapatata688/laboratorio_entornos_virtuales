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
                    percepcion = [int(x) for x in datos[20:26]] # q15 está aquí
                    encuestado = [int(datos[0]), generales, academicas, tecnologicas, economicas, percepcion]
                    encuestas.append(encuestado)
    except FileNotFoundError:
        print("Error: No se encontró 'encuesta_ingenieria_10000_respuestas.csv' en la carpeta.")
    return encuestas

def generar_reporte_14():
    datos = procesar_datos_encuesta()
    if not datos: return
    
    stats_carreras = [
        ["Ingeniería de Sistemas", 0, 0],
        ["Ingeniería Electrónica", 0, 0],
        ["Ingeniería Eléctrica", 0, 0]
    ]
    
    for encuestado in datos:
        carrera = encuestado[1][0]
        dificultad = encuestado[5][0]
        
        for i in range(len(stats_carreras)):
            if stats_carreras[i][0] == carrera:
                stats_carreras[i][1] += dificultad
                stats_carreras[i][2] += 1
                break
                
    max_promedio = 0
    carrera_top = ""
    
    print("--- Reporte 14: Carrera percibida como más difícil (Basado en q15) ---")
    for item in stats_carreras:
        if item[2] > 0:
            promedio = item[1] / item[2]
            print(f"{item[0]}: Nivel promedio de dificultad = {promedio:.2f}")
            if promedio > max_promedio:
                max_promedio = promedio
                carrera_top = item[0]
                
    print("-" * 65)
    print(f"RESULTADO: La carrera percibida como más difícil es '{carrera_top}' con un promedio de {max_promedio:.2f}")

if __name__ == "__main__":
    generar_reporte_14()