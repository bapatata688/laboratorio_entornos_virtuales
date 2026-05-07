# Análisis de Carreras — dataset_10000_personas

Análisis exploratorio de un dataset de 10,000 personas usando Python y pandas.  
Cada reporte es un script independiente enfocado en un aspecto del dataset.

---

## Estructura del proyecto

```
analisis_carreras/
├── dataset_10000_personas.csv
├── reporte_1/   → personas por ciudad
├── reporte_2/   → estudiantes y personas por carrera
├── reporte_3/   → estudiantes por semestre y promedio académico
├── reporte_4/   → promedio por carrera
├── reporte_5/   → personas que trabajan
├── reporte_6/   → reporte_6
├── reporte_7/   → reporte_7
├── reporte_8/   → reporte_8
├── reporte_9/   → reporte_9
├── reporte_10/  → reporte_10
├── reporte_11/  → reporte_11
├── reporte_12/  → reporte_12
├── reporte_13/  → reporte_13
├── reporte_14/  → reporte_14
├── reporte_15/  → reporte_15
├── reporte_16/  → reporte_16
├── reporte_17/  → reporte_17
├── reporte_18/  → reporte_18
├── reporte_19/  → reporte_19
└── reporte_20/  → reporte_20
```

---

## 🐍 Entorno virtual con Conda

### Crear el entorno

```bash
conda create -n analisis_carreras python=3.11
```

### Activar el entorno

```bash
conda activate analisis_carreras
```

### Instalar dependencias

```bash
pip install  jupyter
```

### Desactivar el entorno

```bash
conda deactivate
```

### Eliminar el entorno (si es necesario)

```bash
conda env remove -n analisis_carreras
```

### Ver entornos disponibles

```bash
conda env list
```

---

## Ejecutar un reporte

```bash
# Activar entorno primero
conda activate analisis_carreras

# Ejecutar cualquier reporte
python reporte_1/personas_por_ciudad.py
python reporte_2/estudiantes_carrera.py
# ...
python reporte_20/reporte20.py
```

## 📓 Ejecutar el notebook

```bash
conda activate analisis_carreras
jupyter notebook analisis_general.ipynb
```

---

## Dependencias principales

| Librería  | Uso                    |
| --------- | ---------------------- |
|           |
|           |
|           |
| `jupyter` | Notebooks interactivos |

---

## Dataset

**Archivo:** `dataset_10000_personas.csv`  
**Registros:** 10,000 personas  
**Campos relevantes:** ciudad, carrera, semestre, promedio, trabajo, etc.
