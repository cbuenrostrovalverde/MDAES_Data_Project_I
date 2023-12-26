import numpy as np
import pandas as pd
import psycopg2
import time

for i in range(1,2):
    time.sleep(10)

conn = psycopg2.connect(host='postgres', dbname='example', user='example', password ='example')
cur = conn.cursor()

# Crear un DataFrame de ejemplo
data = {
    'Edad': [25, 30, 22, 28],
    'Ciudad': [1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Realizar la operación de suma
df['Suma'] = df['Edad'] + df['Ciudad']

for index, row in df.iterrows():
    print("INSERT INTO test (Edad, Ciudad, Suma) VALUES ("+str(row['Edad'])+","+str(row['Ciudad'])+","+str(row['Suma'])+");")
    cur.execute("INSERT INTO test (Edad, Ciudad, Suma) VALUES ("+str(row['Edad'])+","+str(row['Ciudad'])+","+str(row['Suma'])+");")


# Confirmar y cerrar la conexión
conn.commit()
conn.close()
