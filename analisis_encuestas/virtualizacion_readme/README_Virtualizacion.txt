reporte_encuesta - Entorno Virtual
====================================

Proyecto de analisis de encuesta de ingenieria (10,000 respuestas).
El entorno se gestiona con Conda usando el archivo environment.yml.

Configuracion
-------------
    conda env create -f environment.yml
    conda activate reporte_encuesta

Verificar paquetes
------------------
    conda list

Desactivar
----------
    conda deactivate

Estructura
----------
- environment.yml              Define el entorno y dependencias
- encuesta_ingenieria_*.csv    Datos de la encuesta
- diccionario_variables_*.csv  Descripcion de variables
- preguntas_encuesta.csv       Preguntas del instrumento
- reporte_1/ ... reporte_20/   Reportes individuales (.py + .ipynb)
- reporte_general.ipynb        Reporte consolidado
