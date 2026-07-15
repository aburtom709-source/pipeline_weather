import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=-53.79&longitude=-67.7&hourly=temperature_2m,relative_humidity_2m"

def extract():
    res = requests.get(URL).json()
    return res
