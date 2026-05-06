# Define una función que recibe la lista de encuestados
def comida_mejor_satisfaccion(encuestados):

    # Diccionario para acumular la suma de satisfacción por comida
    suma = {}

    # Diccionario para contar cuántas veces aparece cada comida
    conteo = {}

    # Recorre cada encuestado en la lista
    for e in encuestados:

        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida

        # Obtiene el nivel de satisfacción del producto
        satisfaccion = e.satisfaccion_producto

        # Suma la satisfacción para esa comida (si no existe, empieza en 0)
        suma[comida] = suma.get(comida, 0) + satisfaccion

        # Cuenta cuántas veces aparece esa comida
        conteo[comida] = conteo.get(comida, 0) + 1

    # Diccionario para guardar los promedios de satisfacción por comida
    promedios = {}

    # Recorre cada tipo de comida registrada
    for comida in suma:

        # Calcula el promedio: suma total / cantidad
        promedios[comida] = suma[comida] / conteo[comida]

    # Encuentra la comida con el mayor promedio de satisfacción
    mejor = max(promedios, key=lambda comida: promedios[comida])

    # Imprime el resultado con el nombre de la comida y su promedio
    print(
        f"Reporte 16 - Comida con mejor satisfacción: {mejor} ({promedios[mejor]:.2f})"
    )


# ==============================================================================================
# REPORTE 17
# Define una función que recibe la lista de encuestados
def comida_peor_satisfaccion(encuestados):

    # Diccionario para acumular la suma de satisfacción por comida
    suma = {}

    # Diccionario para contar cuántas veces aparece cada comida
    conteo = {}

    # Recorre cada encuestado en la lista
    for e in encuestados:

        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida

        # Obtiene el nivel de satisfacción del producto
        satisfaccion = e.satisfaccion_producto

        # Suma la satisfacción para esa comida (si no existe, empieza en 0)
        suma[comida] = suma.get(comida, 0) + satisfaccion

        # Cuenta cuántas veces aparece esa comida
        conteo[comida] = conteo.get(comida, 0) + 1

    # Diccionario para guardar los promedios de satisfacción por comida
    promedios = {}

    # Recorre cada tipo de comida registrada
    for comida in suma:

        # Calcula el promedio: suma total / cantidad
        promedios[comida] = suma[comida] / conteo[comida]

    # Encuentra la comida con el menor promedio de satisfacción
    peor = min(promedios, key=lambda comida: promedios[comida])

    # Imprime el resultado con el nombre de la comida y su promedio
    print(f"Reporte 17 - Comida con menor satisfacción: {peor} ({promedios[peor]:.2f})")


# ==============================================================================================
# REPORTE 18
# Define una función que recibe la lista de encuestados
def relacion_precio_recomendacion(encuestados):

    # Diccionario para agrupar las recomendaciones según el precio percibido
    datos = {}

    # Recorre cada encuestado en la lista
    for e in encuestados:

        # Obtiene cómo percibe el precio (alto, medio, bajo)
        precio = e.precio_percepcion

        # Obtiene la puntuación de recomendación (NPS)
        recomendacion = e.recomendaria

        # Si ese tipo de precio no existe en el diccionario, lo crea con una lista vacía
        if precio not in datos:
            datos[precio] = []

        # Agrega la recomendación a la lista correspondiente a ese precio
        datos[precio].append(recomendacion)

    # Imprime el título del reporte
    print("\nReporte 18 - Relación entre precio y recomendación:")

    # Recorre cada tipo de precio y su lista de recomendaciones
    for precio, lista in datos.items():

        # Calcula el promedio de recomendación para ese grupo
        promedio = sum(lista) / len(lista)

        # Imprime el resultado con el promedio formateado a 2 decimales
        print(f"  {precio}: promedio recomendación = {promedio:.2f}")


# ==============================================================================================
# REPORTE 19
# Define una función que recibe la lista de encuestados
def relacion_tiempo_satisfaccion(encuestados):

    # Diccionario para agrupar la satisfacción según el tiempo de entrega
    datos = {}

    # Recorre cada encuestado en la lista
    for e in encuestados:

        # Obtiene el tiempo de entrega (rápido, normal, lento)
        tiempo = e.tiempo_entrega

        # Obtiene la satisfacción del producto
        satisfaccion = e.satisfaccion_producto

        # Si ese tiempo no existe en el diccionario, lo crea con una lista vacía
        if tiempo not in datos:
            datos[tiempo] = []

        # Agrega la satisfacción a la lista correspondiente a ese tiempo
        datos[tiempo].append(satisfaccion)

    # Imprime el título del reporte
    print("\nReporte 19 - Relación entre tiempo de entrega y satisfacción:")

    # Recorre cada tipo de tiempo y su lista de satisfacciones
    for tiempo, lista in datos.items():

        # Calcula el promedio de satisfacción para ese grupo
        promedio = sum(lista) / len(lista)

        # Imprime el resultado con el promedio formateado a 2 decimales
        print(f"  {tiempo}: satisfacción promedio = {promedio:.2f}")


# ==============================================================================================
# REPORTE 20
# Define una función que recibe la lista de encuestados
def perfil_predominante(encuestados):

    # Diccionario para contar cuántas veces se repite cada tipo de comida
    conteo_comida = {}

    # Diccionario para contar cuántas veces se repite cada frecuencia de consumo
    conteo_frecuencia = {}

    # Recorre cada encuestado en la lista
    for e in encuestados:

        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida

        # Obtiene la frecuencia de consumo (diario, semanal, etc.)
        frecuencia = e.frecuencia_consumo

        # Suma 1 al conteo de esa comida (si no existe, empieza en 0)
        conteo_comida[comida] = conteo_comida.get(comida, 0) + 1

        # Suma 1 al conteo de esa frecuencia
        conteo_frecuencia[frecuencia] = conteo_frecuencia.get(frecuencia, 0) + 1

    # Obtiene la comida más repetida (la más popular)
    comida_top = max(conteo_comida, key=lambda comida: conteo_comida[comida])

    # Obtiene la frecuencia más repetida
    frecuencia_top = max(
        conteo_frecuencia, key=lambda frecuencia: conteo_frecuencia[frecuencia]
    )

    # Imprime el título del reporte
    print("\nReporte 20 - Perfil predominante del consumidor:")

    # Imprime la comida más preferida
    print(f"  Comida favorita: {comida_top}")

    # Imprime la frecuencia de consumo más común
    print(f"  Frecuencia de consumo: {frecuencia_top}")
