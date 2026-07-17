import sys
import os
from pathlib import Path

DAG_DIR = Path(__file__).resolve().parent

SRC_PATH = DAG_DIR.parent / "src"  

sys.path.append(str(SRC_PATH))
os.chdir(str(SRC_PATH))

from extract import extract
from transform import transform
from load import load

from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="dag_clima",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    catchup=False,
    tags=["clima"],    
)

def dag_clima():

    @task
    def extraer():
        return extract()
    
    @task
    def transformar(datos_curdos):
        return transform(datos_curdos)
    
    @task
    def cargar(filas):
        load(filas)

    cargar(transformar(extraer()))

dag_clima()    