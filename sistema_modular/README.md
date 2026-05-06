# Sistema Modular - Analisis de Encuestas
Sistema modular desarrollado en Python para el analisis de encuestas de consumo en restaurantes.
El proyecto procesa datos desde archivos CSV, modela encuestados y genera reportes estadisticos.

## Creacion del entorno
conda create -n sistema_modular python=3.10
conda activate sistema_modular

## Instalacion desde archivo de entorno
conda env create -f environment.yml

## Estructura del proyecto

sistema_modular/
├── src/                         Codigo fuente
├── prueba/                      Validacion del entorno
├── encuestas.csv               Datos de prueba
├── encuesta_restaurantes_20000_respuestas.csv  Datos de encuesta
├── environment.yml             Dependencias
├── main.py                     Ejecucion principal
└── README.md

## Ejecucion del proyecto
python main.py

## Validacion del entorno
python prueba/validacion_entorno.py

## Reproducibilidad
El entorno puede replicarse en otra maquina con:
conda env create -f environment.yml