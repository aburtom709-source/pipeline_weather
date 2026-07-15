import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

def load(lista):
    conexion = psycopg2.connect(host=HOST, port=PORT, dbname=DBNAME, user=USER, password=PASSWORD)
    cursor = conexion.cursor()

    for l in lista:
        cursor.execute("INSERT INTO clima (time, temperature_2m, relative_humidity_2m) VALUES (%s, %s, %s) ON CONFLICT (time) DO NOTHING", (l['time'], l['temperature_2m'], l['relative_humidity_2m']))
        conexion.commit()

    cursor.close()
    conexion.close()