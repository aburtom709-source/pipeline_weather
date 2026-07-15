from extract import extract
from transform import transform
from load import load

if __name__ == "__main__":
    datos_crudos = extract()
    filas = transform(datos_crudos)
    load(filas)
    print("Listo, cargado en psql")