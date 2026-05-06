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

def generar_reporte_15():
    datos = procesar_datos_encuesta()
    if not datos: return
    
    stats_estres = [
        ["Ingeniería de Sistemas", 0, 0],
        ["Ingeniería Electrónica", 0, 0],
        ["Ingeniería Eléctrica", 0, 0]
    ]
    
    for encuestado in datos:
        carrera = encuestado[1][0]
        estres = encuestado[5][1]
        
        for i in range(len(stats_estres)):
            if stats_estres[i][0] == carrera:
                stats_estres[i][1] += estres
                stats_estres[i][2] += 1
                break
                
    max_promedio = 0
    carrera_top = ""
    
    print("--- Reporte 15: Carrera con mayor nivel promedio de estrés (Basado en q16) ---")
    for item in stats_estres:
        if item[2] > 0:
            promedio = item[1] / item[2]
            print(f"{item[0]}: Nivel promedio de estrés = {promedio:.2f}")
            if promedio > max_promedio:
                max_promedio = promedio
                carrera_top = item[0]
                
    print("-" * 70)
    print(f"RESULTADO: La carrera con mayor estrés es '{carrera_top}' con un promedio de {max_promedio:.2f}")

if __name__ == "__main__":
    generar_reporte_15()