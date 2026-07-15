CREATE TABLE clima (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP UNIQUE,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT
)