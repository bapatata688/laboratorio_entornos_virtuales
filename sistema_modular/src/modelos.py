# clase padre
class Encuestado:
    # van a ir agregando self.(nombre_columna)
    def __init__(self, datos_diccionario):
        self.id = datos_diccionario.get("id")
        self.comida_preferida = datos_diccionario.get("comida_preferida")
        self.frecuencia_consumo = datos_diccionario.get("frecuencia_consumo")
        self.gasto_promedio = float(datos_diccionario.get("gasto_promedio", 0))
        self.satisfaccion_producto = int(
            datos_diccionario.get("satisfaccion_producto", 0)
        )
        self.satisfaccion_servicio = int(
            datos_diccionario.get("satisfaccion_servicio", 0)
        )
        self.tiempo_entrega = datos_diccionario.get("tiempo_entrega")
        self.precio_percepcion = datos_diccionario.get("precio_percepcion")
        self.recomendaria = int(datos_diccionario.get("recomendaria_nps", 0))
        self.volveria_comprar = datos_diccionario.get("volveria_comprar")
        self.calificacion_general = int(
            datos_diccionario.get("calificacion_general", 0)
        )
