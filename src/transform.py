def transform(data):
    tiempo = data["hourly"]["time"]
    temperatura = data["hourly"]["temperature_2m"]
    humedad = data["hourly"]["relative_humidity_2m"]

    filas = []

    for tiem, temp, hume in zip(tiempo, temperatura, humedad):
        filas.append({"time": tiem, "temperature_2m": temp, "relative_humidity_2m": hume})
    
    return filas