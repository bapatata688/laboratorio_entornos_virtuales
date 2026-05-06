# funcion para calcular promedio de una lista de numeros
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0  # evita division por cero si la lista esta vacia


# funcion para agrupar objetos segun un atributo
def agrupar_por(encuestados, atributo):
    grupos = {}  # diccionario donde se almacenan los grupos

    for e in encuestados:
        valor = getattr(e, atributo)  # obtiene el valor del atributo del objeto

        if valor not in grupos:
            grupos[valor] = []  # crea lista si la categoria no existe

        grupos[valor].append(e)  # agrega el objeto al grupo correspondiente

    return grupos


# =========================
# reporte 6 promedio gasto por comida
def promedio_gasto_por_comida(encuestados):
    grupos = agrupar_por(encuestados, "comida_preferida")  # agrupa por tipo de comida

    print("\nreporte 6 promedio gasto por comida:")

    resultados = {}  # guarda promedios por cada comida

    for comida, lista_objetos in grupos.items():
        gastos = [e.gasto_promedio for e in lista_objetos]  # extrae gastos de cada grupo
        resultados[comida] = promedio(gastos)  # calcula promedio

    ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)  # ordena de mayor a menor

    for comida, valor in ordenados:
        print(f"{comida} {valor:.2f}")  # imprime resultado formateado

    print("el mayor gasto indica mayor consumo y preferencia del cliente")


# =========================
# reporte 7 satisfaccion promedio del producto 

def satisfaccion_producto(encuestados):
    valores = [e.satisfaccion_producto for e in encuestados]  # extrae calificaciones del producto

    print(f"\nreporte 7 satisfaccion producto: {promedio(valores):.2f}")  # promedio final

    print("refleja la calidad percibida del producto")


# =========================
# reporte 8 satisfaccion promedio del servicio

def satisfaccion_servicio(encuestados):
    valores = [e.satisfaccion_servicio for e in encuestados]  # extrae calificaciones del servicio

    print(f"\nreporte 8 satisfaccion servicio: {promedio(valores):.2f}")  # promedio final

    print("muestra la calidad de atencion al cliente")


# =========================
# reporte 9 calificacion general promedio

def calificacion_general(encuestados):
    valores = [e.calificacion_general for e in encuestados]  # extrae calificacion general

    print(f"\nreporte 9 calificacion general: {promedio(valores):.2f}")  # promedio final

    print("resume la experiencia general del cliente")


# =========================
# reporte 10 distribucion de percepcion de precios

def distribucion_precios(encuestados):
    conteo = agrupar_por(encuestados, "precio_percepcion")  # agrupa por percepcion de precio

    total = len(encuestados)  # total de encuestados

    print("\nreporte 10 distribucion de precios")

    for categoria, lista in conteo.items():
        porcentaje = (len(lista) / total) * 100  # calcula porcentaje por categoria
        print(f"{categoria} {len(lista)} {porcentaje:.1f}%")  # imprime cantidad y porcentaje

    print("muestra como los clientes perciben los precios del restaurante")