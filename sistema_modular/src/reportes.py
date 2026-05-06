# aca solo se llaman las funciones declaradas en sus reportes
from src.reporte_a import (
    total_encuestados,
    comida_mas_preferida,
    encuestados_por_comida,
    frecuencia_consumo_comun,
    promedio_gasto_general,
)
from src.reporte_b import (
    promedio_gasto_por_comida,
    satisfaccion_producto,
    satisfaccion_servicio,
    calificacion_general,
    distribucion_precios,
)

# 11 al 15
from src.reporte_c import (
    distribucion_tiempo_entrega,
    porcentaje_volveria_comprar,
    nps_general,
    nps_por_comida,
)

# 16 al 20
from src.reporte_e import (
    comida_mejor_satisfaccion,
    comida_peor_satisfaccion,
    relacion_precio_recomendacion,
    relacion_tiempo_satisfaccion,
    perfil_predominante,
)


class AnalizarEncuestados:
    def __init__(self, lista_objetos):
        self.encuestados = lista_objetos

    def total_encuestados(self):
        total_encuestados(self.encuestados)

    def comida_mas_preferida(self):
        comida_mas_preferida(self.encuestados)

    def encuestados_por_comida(self):
        encuestados_por_comida(self.encuestados)

    def frecuencia_consumo_comun(self):
        frecuencia_consumo_comun(self.encuestados)

    def promedio_gasto_general(self):
        promedio_gasto_general(self.encuestados)

    def promedio_gasto_por_comida(self):
        promedio_gasto_por_comida(self.encuestados)

    def satisfaccion_producto(self):
        satisfaccion_producto(self.encuestados)

    def satisfaccion_servicio(self):
        satisfaccion_servicio(self.encuestados)

    def calificacion_general(self):
        calificacion_general(self.encuestados)

    def distribucion_precios(self):
        distribucion_precios(self.encuestados)

    # 11-15
    def distribucion_tiempo_entrega(self):
        distribucion_tiempo_entrega(self.encuestados)

    def porcentaje_volveria_comprar(self):
        porcentaje_volveria_comprar(self.encuestados)

    def nps_general(self):
        nps_general(self.encuestados)

    def nps_por_comida(self):
        nps_por_comida(self.encuestados)

    # 16-20
    def comida_mejor_satisfaccion(self):
        comida_mejor_satisfaccion(self.encuestados)

    def comida_peor_satisfaccion(self):
        comida_peor_satisfaccion(self.encuestados)

    def relacion_precio_recomendacion(self):
        relacion_precio_recomendacion(self.encuestados)

    def relacion_tiempo_satisfaccion(self):
        relacion_tiempo_satisfaccion(self.encuestados)

    def perfil_predominante(self):
        perfil_predominante(self.encuestados)
