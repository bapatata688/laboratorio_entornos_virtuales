# La longitud de encuestados es el total de encuestados
def total_encuestados(encuestados):
    # Obtiene el total contando todos los elementos de la lista
    total = len(encuestados)
    print(f"Reporte 1 - Total de encuestados: {total}")


# Contea las coincidencias de la comida favorita,
# la comida con mayor coincidencia es la que tiene mas votos
def comida_mas_preferida(encuestados):
    # Diccionario para contar cuántas veces aparece cada comida
    conteo = {}
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida
        # Suma 1 al conteo de esa comida (si no existe, empieza en 0)
        conteo[comida] = conteo.get(comida, 0) + 1
    # Encuentra la comida con mayor cantidad de votos
    mas_preferida = max(conteo, key=lambda c: conteo[c])
    print(
        f"Reporte 2 - Comida rápida más preferida: {mas_preferida} ({conteo[mas_preferida]} votos)"
    )


def encuestados_por_comida(encuestados):
    # Diccionario para contar cuántos encuestados prefieren cada comida
    conteo = {}
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida
        # Suma 1 al conteo de esa comida (si no existe, empieza en 0)
        conteo[comida] = conteo.get(comida, 0) + 1
    # Obtiene el total de encuestados para calcular porcentajes
    total = len(encuestados)
    print("\nReporte 3 - Cantidad de encuestados por tipo de comida:")
    # Recorre cada comida y su cantidad
    for comida, cantidad in conteo.items():
        # Calcula qué porcentaje del total representa esa comida
        porcentaje = (cantidad / total) * 100
        print(f"  {comida}: {cantidad} ({porcentaje:.1f}%)")


def frecuencia_consumo_comun(encuestados):
    # Diccionario para contar cuántas veces aparece cada frecuencia de consumo
    conteo = {}
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Obtiene la frecuencia de consumo del encuestado
        frecuencia = e.frecuencia_consumo
        # Suma 1 al conteo de esa frecuencia (si no existe, empieza en 0)
        conteo[frecuencia] = conteo.get(frecuencia, 0) + 1
    # Encuentra la frecuencia con mayor cantidad de personas
    mas_comun = max(conteo, key=lambda f: conteo[f])
    print(
        f"Reporte 4 - Frecuencia de consumo más común: {mas_comun} ({conteo[mas_comun]} personas)"
    )


def promedio_gasto_general(encuestados):
    # Acumulador para sumar el gasto de todos los encuestados
    total_gasto = 0.0
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Suma el gasto promedio del encuestado al acumulador
        total_gasto += e.gasto_promedio
    # Divide el gasto total entre la cantidad de encuestados
    promedio = total_gasto / len(encuestados)
    print(f"Reporte 5 - Promedio de gasto general: ${promedio:.2f}")
