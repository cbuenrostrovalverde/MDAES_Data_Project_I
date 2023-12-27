import pandas as pd
import numpy as np
import random
import psycopg2
import csv

# Parámetros de conexión a PostgreSQL
connection_params = {
    'host': 'postgres',
    'port': '5480',
    'database': 'tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
}

# Conectar a PostgreSQL
conn = psycopg2.connect(**connection_params)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

df = pd.read_csv('nombres_españoles.csv', sep = ';', header = None)

# Tabla Viajes:
df_viajes = pd.DataFrame({
    "id_destino": "" ,#revisar que valor le asignamos,
    "id_destino": "" #revisar que valor le asignamos
    })
for index, row in df.iterrows():
    cursor.execute("INSERT INTO viajes destino (id_precio, id_destino) VALUES ("+str(row['id_precio'])+","+str(row['id_destino'])+");")
# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()



