from src.lector import leer_datos
from src.modelos import Encuestado
from src.reportes import AnalizarEncuestados

datos_crudos = leer_datos("encuestas.csv")
encuestados = [Encuestado(dato) for dato in datos_crudos]
analizador = AnalizarEncuestados(encuestados)

# reportes diego
analizador.total_encuestados()
analizador.comida_mas_preferida()
analizador.encuestados_por_comida()
analizador.frecuencia_consumo_comun()
analizador.promedio_gasto_general()

# reportes Daniella
analizador.promedio_gasto_por_comida()
analizador.satisfaccion_producto()
analizador.satisfaccion_servicio()
analizador.calificacion_general()
analizador.distribucion_precios()

# Reportes del 11 al 15
analizador.distribucion_tiempo_entrega()
analizador.porcentaje_volveria_comprar()
analizador.nps_general()
analizador.nps_por_comida()

# Reporte 16: comida con mayor nivel de satisfacción promedio
analizador.comida_mejor_satisfaccion()

# Reporte 17: comida con menor satisfacción promedio
analizador.comida_peor_satisfaccion()

# Reporte 18: relación entre percepción de precios y nivel de recomendación
analizador.relacion_precio_recomendacion()

# Reporte 19: influencia del tiempo de entrega en la satisfacción del producto
analizador.relacion_tiempo_satisfaccion()

# Reporte 20: perfil predominante del consumidor
analizador.perfil_predominante()
