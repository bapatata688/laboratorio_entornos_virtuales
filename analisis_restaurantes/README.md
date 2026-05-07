# 🍽️ Análisis de Restaurantes — encuesta_restaurantes_10000

Análisis exploratorio de una encuesta de 10,000 registros de restaurantes usando Python y pandas.

---

## Estructura del proyecto

```
.
├── encuesta_restaurantes_10000.csv   # Dataset principal
├── analisis_restaurante.py           # Script principal de análisis
├── Reporte_general.ipynb             # Notebook con el análisis completo
├── reporte_6_10_Diego_Escobar/
│   └── documentacion_reportes.ipynb  # Reportes 6 al 10 — Diego Escobar
└── reporte_daniela/
    └── Proyecto_Restaurante.ipynb    # Reporte — Daniela
```

---

## Entorno virtual con Conda

### Crear el entorno

```bash
conda create -n analisis_restaurante python=3.11
```

### Activar el entorno

```bash
conda activate analisis_restaurante
```

### Instalar dependencias

```bash
pip install pandas matplotlib seaborn jupyter
```

### Desactivar el entorno

```bash
conda deactivate
```

### Eliminar el entorno (si es necesario)

```bash
conda env remove -n analisis_restaurante
```

### Ver entornos disponibles

```bash
conda env list
```

---

## Ejecutar el análisis

```bash
conda activate analisis_restaurante

# Script principal
python analisis_restaurante.py

# Notebooks
jupyter notebook Reporte_general.ipynb
jupyter notebook reporte_6_10_Diego_Escobar/documentacion_reportes.ipynb
jupyter notebook reporte_daniela/Proyecto_Restaurante.ipynb
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

**Archivo:** `encuesta_restaurantes_10000.csv`  
**Registros:** 10,000 encuestas  
**Campos relevantes:** nombre restaurante, ciudad, calificación, tipo de cocina, precio, etc.

---

## Integrantes

| Nombre        | Reporte              |
| ------------- | -------------------- |
| Diego Escobar | Reportes 6 al 10     |
| Daniela       | Proyecto Restaurante |
