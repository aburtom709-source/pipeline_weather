# 🌦️ Weather Data Pipeline

ETL que extrae el pronóstico de clima (hora, temperatura y humedad) desde la API pública de Open-Meteo, lo transforma y lo carga en una base de datos PostgreSQL corriendo en Docker.

## ⚙️ Funcionamiento

### 🔌 Extracción (Extract): 
Pide a la API de Open-Meteo el pronóstico, asi como el horario, la temperatura y la humedad para una ubicación fija.

### 🧹 Transformación (Transform): 
Convierte la respuesta de la API (tres listas paralelas: horas, temperaturas, humedades) en una lista de filas, una por hora.

### 📥 Carga (Load): 
Inserta esas filas en una tabla clima de PostgreSQL. Si una fila para ese horario ya existe, no la duplica.

## 🏗️ Arquitectura

```
API Open-Meteo → extract.py → transform.py → load.py → PostgreSQL (Docker)
```
 
- `src/extract.py` → solo habla con la API, devuelve el JSON crudo.
- `src/transform.py` → solo transforma datos en memoria, no sabe que existe una base de datos.
- `src/load.py` → solo habla con la base de datos, no sabe nada de la API.
- `src/main.py` → orquesta las tres funciones en orden.


## 🐋 Docker

PostgreSQL corre containerizado con Docker Compose para que el proyecto sea reproducible en cualquier máquina con un solo comando, sin depender de una instalación local de Postgres.

## 🔁 Idempotencia

La columna `time` tiene una restricción `UNIQUE`, y el `INSERT` usa `ON CONFLICT (time) DO NOTHING`. Esto permite correr el pipeline varias veces sin generar filas duplicadas para un mismo horario.

## 🚀 Cómo correr el proyecto
 
Seguí estos pasos en tu terminal:
 
### 1. Clonar el repositorio
```bash
git clone https://github.com/aburtom709-source/pipeline_weather.git
cd pipeline_weather
```
 
### 2. Configurar variables de entorno
Copiá `.env.example` a `.env` y completá tus credenciales:
```bash
cp .env.example .env
```
 
### 3. Levantar la base de datos
```bash
docker compose up -d
```
 
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
 
### 5. Correr el pipeline
```bash
python src/main.py
```
## 🌪️ Orquestación con Airflow

El pipeline también puede correr automáticamente cada hora usando Apache Airflow, 
en vez de ejecutarlo a mano con `python src/main.py`.

El DAG (`dags/dag_clima.py`) no reescribe la lógica: solo importa y encadena las 
funciones `extract()`, `transform()` y `load()` ya existentes en `src/`.

## 🚀 Cómo correrlo
```bash
export AIRFLOW_HOME=~/airflow
airflow db migrate
cp dags/dag_clima.py ~/airflow/dags/
airflow scheduler
airflow dag-processor
airflow api-server --port 8080
```

Con Postgres levantado (`docker compose up -d`), entrá a `http://localhost:8080`, 
buscá `dag_clima` y activá el toggle para que corra según el schedule (`@hourly`).
