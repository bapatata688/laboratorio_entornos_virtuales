# laboratorio_entornos_virtuales

Repositorio de proyectos de analisis de datos con Python.  
`git@github.com:bapatata688/laboratorio_entornos_virtuales.git`

---

## Integrantes

| Nombre                             | Rol              |
| ---------------------------------- | ---------------- |
| Daniella Marissa Navarro Araniva   | Reportes         |
| Cristian Francisco Pérez Hernández | Estudiantes      |
| Erick Xavier Maldonado Caballero   | Notas            |
| Diego Alejandro Escobar Barahona   | Exámenes y notas |

---

## Proyectos

| Carpeta                  | Dataset                                    |
| ------------------------ | ------------------------------------------ |
| `analisis_carrera/`      | dataset_10000_personas.csv                 |
| `analisis_encuestas/`    | encuesta_ingenieria_10000_respuestas.csv   |
| `analisis_evaluacion/`   | examenes, notas, estudiantes               |
| `analisis_restaurantes/` | encuesta_restaurantes_10000.csv            |
| `sistema_modular/`       | encuesta_restaurantes_20000_respuestas.csv |

---

## Entornos virtuales

### Conda — desde `environment.yml`

```bash
# Crear
conda env create -f environment.yml

# Activar
conda activate <nombre_entorno>

# Desactivar
conda deactivate

# Eliminar
conda env remove -n <nombre_entorno>

# Ver entornos
conda env list
```

### venv — sin archivo yml

```bash
# Crear
python -m venv .venv

# Activar
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# Instalar dependencias
pip install pandas matplotlib seaborn jupyter

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde archivo
pip install -r requirements.txt

# Desactivar
deactivate
```

---

## Entornos por proyecto

| Proyecto              | Nombre entorno          | Comando activar                        |
| --------------------- | ----------------------- | -------------------------------------- |
| analisis_carrera      | `analisis_carrera`      | `conda activate analisis_carrera`      |
| analisis_encuestas    | `analisis_encuestas`    | `conda activate analisis_encuestas`    |
| analisis_evaluacion   | `analisis_evaluacion`   | `conda activate analisis_evaluacion`   |
| analisis_restaurantes | `analisis_restaurantes` | `conda activate analisis_restaurantes` |
| sistema_modular       | `sistema_modular`       | `conda activate sistema_modular`       |

---

## Ejecutar

```bash
# Activar entorno del proyecto
conda activate <nombre_entorno>

# Correr script
python reporte_X/reporte_X.py

# Abrir notebook
jupyter notebook
```

---

## Dependencias comunes

```
jupyter
```
