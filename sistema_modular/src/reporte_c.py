# Agrupa los encuestados según el tiempo de entrega y calcula la distribución
def distribucion_tiempo_entrega(encuestados):
    # Diccionario para contar cuántas veces aparece cada categoría de tiempo
    conteo = {}
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Obtiene el tiempo de entrega del encuestado
        tiempo = e.tiempo_entrega
        # Suma 1 al conteo de ese tiempo (si no existe, empieza en 0)
        conteo[tiempo] = conteo.get(tiempo, 0) + 1
    # Obtiene el total de encuestados para calcular porcentajes
    total = len(encuestados)
    print("\nReporte 11 - Distribución de tiempo de entrega:")
    # Recorre cada categoría y su cantidad
    for categoria, cantidad in conteo.items():
        # Calcula qué porcentaje del total representa esa categoría
        porcentaje = (cantidad / total) * 100
        print(f"  {categoria}: {cantidad} ({porcentaje:.1f}%)")


# Calcula el porcentaje de encuestados que volverían a comprar
def porcentaje_volveria_comprar(encuestados):
    # Cuenta los encuestados que respondieron sí
    si = sum(
        1 for e in encuestados if e.volveria_comprar.strip().lower() in ["sí", "si"]
    )
    # Obtiene el total de encuestados
    total = len(encuestados)
    # Calcula el porcentaje
    porcentaje = (si / total) * 100
    print(f"\nReporte 12 - Porcentaje que volvería a comprar: {porcentaje:.1f}%")


# Calcula el NPS general clasificando encuestados en promotores, pasivos y detractores
def nps_general(encuestados):
    # Cuenta promotores (puntaje >= 9), detractores (<= 6) y pasivos (el resto)
    promotores = sum(1 for e in encuestados if e.recomendaria >= 9)
    detractores = sum(1 for e in encuestados if e.recomendaria <= 6)
    pasivos = len(encuestados) - promotores - detractores
    total = len(encuestados)
    # Calcula el NPS: (promotores - detractores) / total * 100
    nps = ((promotores - detractores) / total) * 100
    print(f"\nReporte 13 - NPS General: {nps:.1f}")
    print(
        f"Reporte 14 - Promotores: {promotores} | Pasivos: {pasivos} | Detractores: {detractores}"
    )


# Calcula el NPS agrupado por tipo de comida preferida
def nps_por_comida(encuestados):
    # Diccionario para acumular promotores, detractores y total por comida
    datos = {}
    # Recorre cada encuestado en la lista
    for e in encuestados:
        # Obtiene la comida preferida del encuestado
        comida = e.comida_preferida
        # Si esa comida no existe en el diccionario, la inicializa
        if comida not in datos:
            datos[comida] = {"promotores": 0, "detractores": 0, "total": 0}
        # Suma al total de esa comida
        datos[comida]["total"] += 1
        # Clasifica al encuestado según su puntaje de recomendación
        if e.recomendaria >= 9:
            datos[comida]["promotores"] += 1
        elif e.recomendaria <= 6:
            datos[comida]["detractores"] += 1
    print("\nReporte 15 - NPS por tipo de comida:")
    # Recorre cada comida y calcula su NPS
    for comida, valores in datos.items():
        nps = (
            (valores["promotores"] - valores["detractores"]) / valores["total"]
        ) * 100
        print(f"  {comida}: {abs(nps):.1f}")
