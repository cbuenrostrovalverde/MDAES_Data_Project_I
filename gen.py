import pandas as pd
import numpy as np
import random
import psycopg2
import time
from gender_guesser.detector import Detector
from faker import Faker

for i in range(1,2):
    time.sleep(10)

conn = psycopg2.connect(host='postgres', dbname='project', user='project', password ='project')
cur = conn.cursor()

fake = Faker('es_ES')
nombres = [fake.first_name() for _ in range(50000)]
apellidos = [fake.last_name() for _ in range(50000)]
data = {'nombre': nombres, 'apellido': apellidos}
df_datos = pd.DataFrame(data)
df_datos['id_solicitante'] = df_datos.index + 1
df_datos = df_datos[['id_solicitante','nombre','apellido']]

for index, row in df_datos.iterrows():
    cur.execute(
        "INSERT INTO datos (id_solicitante, nombre, apellido) VALUES (%s, %s, %s)",
        (int(row['id_solicitante']), row['nombre'], row['apellido'])
    )

df_caract = df_datos.copy()
df_caract['sexo'] = None
df_caract['edad'] = np.random.randint(65, 100, len(df_caract))
df_caract['trabajo'] = None
df_caract['movilidad'] = np.random.choice(['perfecta', 'media', 'limitada'], len(df_caract))
df_caract['discapacidad'] = np.random.choice([True, False], len(df_caract))
df_caract['enfermedad'] = np.random.choice([False] * 99 + [True], len(df_caract))
df_caract['años_trabajados'] = np.random.randint(15, 41, len(df_caract))

gender_detector = Detector()
def get_gender(name):
    return gender_detector.get_gender(name)
df_caract['sexo'] = df_caract['nombre'].apply(get_gender)

trabajos = [
    "Medico", "Enfermero", "Profesor", "Ingeniero", "Abogado", "Arquitecto", "Administrativo",
    "Comercial/Vendedor", "Electricista", "Fontanero", "Programador_informatico", "Diseñador_grafico",
    "Carpintero", "Cocinero", "Camarero", "Agricultor", "Peluquero", "Fontanero",
    "Operario_de_fabrica"
]

df_caract['trabajo'] = np.random.choice(trabajos, len(df_caract))
df_caract['id_caract'] = df_caract['id_solicitante']

df_caract['discapacidad'] = np.random.choice([True, False], len(df_caract))
df_caract['discapacidad'].fillna(False, inplace=True)
df_caract['discapacidad'] = df_caract['discapacidad'].astype(bool)

df_caract['enfermedad'] = np.random.choice([True, False], len(df_caract))
df_caract['enfermedad'].fillna(False, inplace=True)
df_caract['enfermedad'] = df_caract['enfermedad'].astype(bool)

df_caract = df_caract[['id_caract','id_solicitante', 'sexo', 'edad', 'trabajo', 'años_trabajados',
       'movilidad', 'discapacidad', 'enfermedad']]

for index, row in df_caract.iterrows():
    cur.execute(
        "INSERT INTO caract (id_caract, id_solicitante, sexo, edad, trabajo, años_trabajados, movilidad, discapacidad, enfermedad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (int(row['id_caract']), int(row['id_solicitante']), row['sexo'], int(row['edad']), row['trabajo'], 
         int(row['años_trabajados']), row['movilidad'], row['discapacidad'], row['enfermedad'])
    )

df_viajero = df_datos.copy()
destinos_cap = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Malaga", "Murcia",
    "Palma de Mallorca", "Las Palmas de Gran Canaria", "Bilbao", "Alicante", "Córdoba",
    "Valladolid", "Vigo", "Girona", "Lugo", "León", "Toledo", "Santander", "Pamplona",
    "Logrono", "Badajoz", "Huesca", "Castellon de la Plana", "Tarragona", "Lleida",
    "Ourense", "Caceres", "Jaen", "Almeria", "Ciudad Real", "Huelva", "Cuenca", "Avila",
    "Segovia", "Soria", "Teruel", "Cuenca", "Zamora", "Guadalajara", "Palencia", "Huesca"]
dest1 = destinos_cap * 80

destinos_nocap = ["Avila", "Salamanca", "Caceres", "Oviedo", "Soria", "Girona", "Pontevedra", "Ronda", "Cudillero", 
    "Albarracin", "Cudillero", "Alcala del Jucar", "Combarro", 
    "Frigiliana", "Ainsa", "Peniscola", "Trujillo", "Besalu", "Valderrobres", 
    "Almagro", "Ujue", "Mirambel", "Morella", "La Alberca", "Chinchon", 
    "Sepulveda", "Calaceite", "Albarracin", "Mogarraz", "Frias", 
    "Poza de la Sal", "Valverde de los Arroyos", "Santillana del Mar", 
    "Barcena Mayor", "Vilafames", "Medinaceli", "Alquezar", "Yanguas", 
    "Monteagudo de las Vicarias", "Ujue", "Candelario", "Fornalutx", 
    "Cadaques", "Valldemossa", "Ainsa", "Pals", "Mogarraz", "Pedraza", 
    "Lerma", "Penalba de Santiago", "Almagro", "Frias", "Valldemossa", 
    "Alcala del Júcar", "Aracena", "Chinchon", "Caleruega"]
dest2 = destinos_nocap * 20
domicilio = dest1 + dest2

df_viajero['domicilio'] = np.random.choice(domicilio, len(df_viajero))
df_viajero['vehiculo'] = np.random.choice([True, False], len(df_viajero))
df_viajero['vehiculo'].fillna(False, inplace=True)
df_viajero['vehiculo'] = df_viajero['vehiculo'].astype(bool)
df_viajero = df_viajero[['id_solicitante', 'domicilio', 'vehiculo']]

for index, row in df_viajero.iterrows():
    cur.execute(
        "INSERT INTO viajero (id_solicitante, domicilio, vehiculo) VALUES (%s, %s, %s)",
        (int(row['id_solicitante']), row['domicilio'], row['vehiculo'])
    )

df_fam_num = df_datos.copy()
df_fam_num['familia_numerosa'] = np.random.choice([True, False], size=len(df_fam_num))
df_fam_num['edad_hijo'] = np.where(df_fam_num['familia_numerosa'], np.random.randint(15, 26, size=len(df_fam_num)), None)
df_fam_num['trabaja_hijo'] = np.where((df_fam_num['familia_numerosa']) & (df_fam_num['edad_hijo'] > 20), True, None)
df_fam_num['edad_hijo'].fillna(False, inplace=True)
df_fam_num['trabaja_hijo'].fillna(False, inplace=True)
df_fam_num['edad_hijo'] = df_fam_num['edad_hijo'].replace(False, 0)
df_fam_num['edad_hijo'] = pd.to_numeric(df_fam_num['edad_hijo'], errors='coerce')
df_fam_num['trabaja_hijo'] = df_fam_num['trabaja_hijo'].astype(bool)

for index, row in df_fam_num.iterrows():
    cur.execute(
        "INSERT INTO fam_num (id_solicitante, familia_numerosa, edad_hijo, trabaja_hijo) VALUES (%s, %s, %s, %s)",
        (int(row['id_solicitante']), row['familia_numerosa'], row['edad_hijo'], row['trabaja_hijo'])
    )

df = df_datos.copy()
df_pensiones = df[['id_solicitante']].copy()
rentas = [0, 8400, 12000, 15000, 18000, 21000]
df_pensiones['renta'] = np.random.choices(rentas, k = len(df_pensiones))
df_pensiones['pension'] = np.random.randint(6784.54, 42830.29, len(df_pensiones))

bins = [6774.54, 12600, 14700, 16800, 18900, 21000, 23100, 25200, 27300, 29400, float('inf')]
etiquetas = ['tipo_1', 'tipo_2', 'tipo_3', 'tipo_4', 'tipo_5', 'tipo_6', 'tipo_7', 'tipo_8', 'tipo_9', 'tipo_10']
df_pensiones['tipo_pension'] = pd.cut(df_pensiones['pension'], bins=bins, labels=etiquetas)

estados = ['soltero/a', 'casado/a', 'viudo/a']
df_pensiones['estado_civil'] = np.random.choice(estados, k=len(df_pensiones))
df_pensiones.loc[df_pensiones['estado_civil'] == 'casado/a', 'pension_conyuge'] = np.random.randint(6784.54, 42830.29, df_pensiones['estado_civil'].eq('casado/a').sum())
df_pensiones['pension_conyuge'] .fillna(0, inplace=True)
df_pensiones['pension_conyuge'] = df_pensiones['pension_conyuge'].astype(float)
df_pensiones['pension_conyuge'] = df_pensiones['pension_conyuge'].astype(int)

for index, row in df_pensiones.iterrows():
    cur.execute(
        "INSERT INTO pensiones (id_solicitante, renta, pension, tipo_pension, estado_civil, pension_conyuge) VALUES (%s, %s, %s, %s, %s, %s)",
        (int(row['id_solicitante']), int(row['renta']) ,int(row['pension']), row['tipo_pension'], row['estado_civil'], int(row['pension_conyuge']))
    )

df_años_ant = df.copy()
df_años_ant['lista_espera'] = np.random.choice([True, False], len(df_años_ant))
df_años_ant['viaje_2021'] = np.random.choice([True, False], len(df_años_ant))
df_años_ant['viaje_2022'] = np.random.choice([True, False], len(df_años_ant))
df_años_ant['num_max_viaje_por_temp'] = np.random.randint( 1, 4, len(df_años_ant))
df_años_ant

for index, row in df_años_ant.iterrows():
    cur.execute(
        "INSERT INTO años_ant (id_solicitante, lista_espera, viaje_2021, viaje_2022, num_max_viaje_por_temp) VALUES (%s, %s, %s, %s, %s)",
        (int(row['id_solicitante']), row['lista_espera'] , row['viaje_2021'], row['viaje_2022'], row['num_max_viaje_por_temp'])
    )

df_habitacion = df.copy()
df_habitacion['hab_ind'] = np.random.choice(([True] * 25 + [False] * 75), k=len(df_habitacion))
df_habitacion['hab_ind'].fillna(False, inplace=True)
df_habitacion['hab_ind'] = df_habitacion['hab_ind'].astype(bool)
df_habitacion = df_habitacion[['id_solicitante', 'hab_ind']]

for index, row in df_habitacion.iterrows():
    cur.execute(
        "INSERT INTO habitacion (id_solicitante, hab_ind) VALUES (%s, %s)",
        (int(row['id_solicitante']), row['hab_ind'])
    )

conn.commit()
conn.close()