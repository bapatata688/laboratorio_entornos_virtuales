# Sistema de Análisis de Encuesta de Ingeniería

Análisis exploratorio de datos sobre 10,000 estudiantes de ingeniería, organizado en 20 reportes individuales y un reporte general consolidado.

---

## Estructura del repositorio

```
.
├── diccionario_variables_encuesta.csv
├── encuesta_ingenieria_10000_respuestas.csv
├── preguntas_encuesta.csv
├── README.md
├── reporte_1
│   ├── encuestados.py
│   └── total_encuestados.ipynb
├── reporte_11
│   ├── reporte_11.ipynb
│   └── reporte_11.py
├── reporte_12
│   ├── reporte_12.ipynb
│   └── reporte_12.py
├── reporte_13
│   ├── reporte_13.ipynb
│   └── reporte_13.py
├── reporte_14
│   ├── reporte_14.ipynb
│   └── reporte_14.py
├── reporte_15
│   ├── reporte_15.ipynb
│   └── reporte_15.py
├── reporte_16
│   ├── reporte_16.ipynb
│   └── reporte_16.py
├── reporte_17
│   ├── Reporte_17.ipynb
│   └── reporte_17.py
├── reporte_18
│   ├── reporte_18.ipynb
│   └── reporte_18.py
├── reporte_19
│   ├── reporte_19.ipynb
│   └── reporte_19.py
├── reporte_2
│   ├── estudiantes_semestre.py
│   └── estudiantes_semestres.ipynb
├── reporte_20
│   ├── reporte_20.ipynb
│   └── reporte_20.py
├── reporte_3
│   ├── estudiantes_carrera.py
│   └── estudiantes_carreras.ipynb
├── reporte_4
│   ├── estudiante_jornada.py
│   └── estudiantes_jornadas.ipynb
├── reporte_5
│   ├── estudiantes_trabajadora.ipynb
│   └── estudiantes_trabajadores.py
├── reporte_6
│   ├── promedio_general.py
│   └── reporte_promedio.ipynb
├── reporte_7
│   ├── reporte_7.ipynb
│   └── reporte_7.py
├── reporte_8
│   ├── reporte_8.ipynb
│   └── reporte_8.py
├── reporte_9
│   ├── reporte_9.ipynb
│   └── reporte_9.py
└── reporte_general.ipynb

```

---

## Reportes

| #   | Descripción                                                        | Estado     |
| --- | ------------------------------------------------------------------ | ---------- |
| 1   | Total de encuestados                                               | Completado |
| 2   | Cantidad de estudiantes por carrera                                | Completado |
| 3   | Cantidad de estudiantes por semestre                               | Completado |
| 4   | Cantidad de estudiantes por jornada                                | Completado |
| 5   | Porcentaje de estudiantes que trabajan y que no trabajan           | Completado |
| 6   | Promedio general del promedio académico reportado                  | Completado |
| 7   | Promedio académico por carrera                                     | Completado |
| 8   | Promedio académico por semestre                                    | Completado |
| 9   | Cantidad de estudiantes con acceso a internet en casa              | Incompleto |
| 10  | Cantidad de estudiantes con computadora propia                     | Completado |
| 11  | Cantidad de estudiantes según horas de estudio semanal             | Completado |
| 12  | Nivel de satisfacción general con la carrera                       | Completado |
| 13  | Nivel de estrés académico general                                  | Completado |
| 14  | Curso percibido como más difícil                                   | Completado |
| 15  | Carrera con mayor nivel promedio de estrés                         | Completado |
| 16  | Relación entre trabajar y promedio académico                       | Completado |
| 17  | Relación entre acceso a internet y promedio académico              | Completado |
| 18  | Relación entre horas de estudio y rendimiento académico            | Completado |
| 19  | Porcentaje de estudiantes interesados en cursos virtuales          | Completado |
| 20  | Perfil predominante del encuestado según respuestas más frecuentes | Completado |

---

## Requisitos

- Python 3.10 o superior
- Jupyter Notebook o JupyterLab
- Librería estándar `csv` (incluida en Python)

Para los reportes interactivos:

```bash
pip install pandas ipywidgets
```

---

## Uso

1. Clonar el repositorio y ubicarse en la carpeta del proyecto.
2. Asegurarse de que el archivo `encuesta_ingenieria_10000_respuestas.csv` esté en la raíz.
3. Abrir cualquier notebook con Jupyter y ejecutar las celdas en orden.

```bash
jupyter notebook reporte_general.ipynb
```

---

## Dataset

El archivo `encuesta_ingenieria_10000_respuestas.csv` contiene 10,000 registros de estudiantes de las carreras de Ingeniería Eléctrica, Ingeniería de Sistemas e Ingeniería Electrónica. La descripción completa de cada columna se encuentra en `diccionario_variables_encuesta.csv`.
