!pip install gender_guesser

import pandas as pd
import numpy as np
import random
from gender_guesser.detector import Detector

df_datos = pd.read_csv('nombres_españoles.csv', sep = ';', header = None)
df_datos = df_datos.rename(columns={0: 'nombre', 1: 'apellido'})
df_datos['id_solicitante'] = df_datos.index + 1
df_datos = df_datos[['id_solicitante', 'nombre', 'apellido']]
df_datos['nombre'] = df_datos['nombre'].astype('str')
df_datos['nombre'] = df_datos['nombre'].apply(lambda x: x.title())
df_datos['apellido'] = df_datos['apellido'].astype('str')
df_datos['apellido'] = df_datos['apellido'].apply(lambda x: x.title())

df_datos

df_datos.to_csv('datos.csv')

df_caract = df_datos.copy()
df_caract['sexo'] = None
gender_detector = Detector()
df_caract['edad'] = np.random.randint(65, 100, 50000)
df_caract['trabajo'] = None
df_caract['mobilidad'] = None
df_caract['discapacidad'] = None
df_caract['enfermedad'] = None
df_caract['años_trabajados'] = None
enfermedad = ['None', 'terminal']
enfermedad = ['None'] * 99 + ['terminal'] * 1
años = list(range(15,41))

trabajos = [
    "Médico",
    "Enfermero/a",
    "Profesor/a",
    "Ingeniero/a",
    "Abogado/a",
    "Arquitecto/a",
    "Administrativo/a",
    "Comercial/Vendedor/a",
    "Electricista",
    "Fontanero/a",
    "Programador/a informático/a",
    "Diseñador/a gráfico/a",
    "Carpintero/a",
    "Fontanero/a",
    "Cocinero/a",
    "Camarero/a",
    "Agricultor/a",
    "Peluquero/a",
    "Fontanero/a",
    "Operario/a de fábrica"
]

mobilidad = ['perfecta', 'media', 'limitada']

for i in (df_caract.index):
    df_caract['sexo'][i] = gender_detector.get_gender(df_caract['nombre'][i])
    df_caract['trabajo'][i] = random.choice(trabajos)
    df_caract['años_trabajados'][i] = random.choice(años)
    df_caract['mobilidad'][i] = random.choice(mobilidad)
    df_caract['discapacidad'][i] = np.random.choice([True, False])
    df_caract['enfermedad'][i] = random.choice(enfermedad)

df_caract = df_caract[['id_solicitante', 'sexo', 'edad', 'trabajo', 'años_trabajados',
       'mobilidad', 'discapacidad', 'enfermedad']]

df_caract

df_caract.to_csv('caract.csv')

df_viajero = df_datos.copy()

destinos_cap = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia",
    "Palma de Mallorca", "Las Palmas de Gran Canaria", "Bilbao", "Alicante", "Córdoba",
    "Valladolid", "Vigo", "Girona", "Lugo", "León", "Toledo", "Santander", "Pamplona",
    "Logroño", "Badajoz", "Huesca", "Castellón de la Plana", "Tarragona", "Lleida",
    "Ourense", "Cáceres", "Jaén", "Almería", "Ciudad Real", "Huelva", "Cuenca", "Ávila",
    "Segovia", "Soria", "Teruel", "Cuenca", "Zamora", "Guadalajara", "Palencia", "Huesca"]
dest1 = destinos_cap * 80

destinos_nocap = ["Ávila", "Salamanca", "Cáceres", "Oviedo", "Soria", "Girona", "Pontevedra", "Ronda", "Cudillero", 
    "Albarracín", "Cudillero", "Alcalá del Júcar", "Combarro", 
    "Frigiliana", "Aínsa", "Peñíscola", "Trujillo", "Besalú", "Valderrobres", 
    "Almagro", "Ujué", "Mirambel", "Morella", "La Alberca", "Chinchón", 
    "Sepúlveda", "Calaceite", "Albarracín", "Mogarraz", "Frias", 
    "Poza de la Sal", "Valverde de los Arroyos", "Santillana del Mar", 
    "Bárcena Mayor", "Vilafamés", "Medinaceli", "Alquézar", "Yanguas", 
    "Monteagudo de las Vicarías", "Ujue", "Candelario", "Fornalutx", 
    "Cadaqués", "Valldemossa", "Aínsa", "Pals", "Mogarraz", "Pedraza", 
    "Lerma", "Peñalba de Santiago", "Almagro", "Frias", "Valldemossa", 
    "Alcalá del Júcar", "Aracena", "Chinchón", "Caleruega"]
dest2 = destinos_nocap * 20
domicilio = dest1 + dest2

df_viajero['vehiculo'] = None
df_viajero['domicilio'] = None
for i in df_viajero.index:
    df_viajero['domicilio'][i] = random.choice(domicilio)
    df_viajero['vehiculo'][i] = np.random.choice([True, False])

df_viajero = df_viajero[['id_solicitante', 'domicilio', 'vehiculo']]

df_viajero

df_viajero.to_csv('viajero.csv')

df_fam_num = df_datos.copy()

df_fam_num['familia_numerosa'] = None
df_fam_num['edad_hijo'] = None
df_fam_num['trabaja_hijo'] = None

for i in df_fam_num.index:
    df_fam_num['familia_numerosa'][i] = np.random.choice([True, False])
    
fam_num_index = df_fam_num[df_fam_num['familia_numerosa'] == True].index
for i in (fam_num_index):
    df_fam_num['edad_hijo'][i] = np.random.randint(15, 26)

hijo_mayor_index = df_fam_num[df_fam_num['edad_hijo'] > 20].index
for i in (hijo_mayor_index):
    df_fam_num['trabaja_hijo'][i] = np.random.choice([True, False])

df_fam_num

df_fam_num.to_csv('fam_num.csv')

df = df_datos.copy()
df = df[['id_solicitante']]

df_pensiones = df.copy()

df_pensiones['renta'] = None
rentas = [0, 8400, 12000, 15000, 18000, 21000]
for i in df_pensiones.index:
    df_pensiones['renta'][i] = random.choice(rentas)
    
df_pensiones['pension'] = np.random.randint(6784.54, 42830.29, 50000)

bins = [6774.54, 12600, 14700, 16800, 18900, 21000, 23100, 25200, 27300, 29400, float('inf')]
etiquetas = ['tipo_1', 'tipo_2', 'tipo_3', 'tipo_4', 'tipo_5', 'tipo_6', 'tipo_7', 'tipo_8', 'tipo_9', 'tipo_10']
df_pensiones['tipo_pension'] = pd.cut(df_pensiones['pension'], bins=bins, labels=etiquetas)

df_pensiones['estado_civil'] = None
estados = ['soltero/a', 'casado/a', 'viudo/a']
df_pensiones['pension_conyuge'] = None
for i in (df_pensiones.index):
    df_pensiones['estado_civil'][i] = random.choice(estados)
    
casados_index = df_pensiones[df_pensiones['estado_civil'] == 'casado/a'].index
for i in (casados_index):
    df_pensiones['pension_conyuge'][i] = np.random.randint(6784.54, 42830.29)

df_pensiones

df_pensiones.to_csv('pensiones.csv')

df_años_ant = df.copy()
df_años_ant['lista_espera'] = None
df_años_ant['años_ant_viajado'] = None

años = ['None', '2021/2022', '2022/2023', '2021/2022 y 2022/2023']
for i in df_años_ant.index:
    df_años_ant['lista_espera'][i] = np.random.choice([True, False])
    df_años_ant['años_ant_viajado'][i] = random.choice(años)

df_años_ant['num_max_viaje_por_temp'] = None
doble_index = df_años_ant[df_años_ant['años_ant_viajado'] == '2021/2022 y 2022/2023'].index
for i in doble_index:
    df_años_ant['num_max_viaje_por_temp'][i] = np.random.randint(1, 4)

df_años_ant

df_años_ant.to_csv('años_ant.csv')

df_habitacion = df.copy()
df_habitacion['hab_ind'] = None
habitacion = ([True] * 25) + ([False] * 75)

for i in df_habitacion.index:
    df_habitacion['hab_ind'][i] = random.choice(habitacion)

df_habitacion

df_habitacion.to_csv('habitacion.csv')

df_solicitantes = df.copy()

df_solicitudes

df_viajes = pd.read_csv('viajes2.csv')

df_viaje

def obtener_4_viajes():
    return np.random.choice(df_viajes['id_viaje'], size=4, replace=True)

df_solicitantes['ids_viajes'] = df_solicitantes.apply(lambda x: obtener_4_viajes(), axis=1)
df_solicitantes = df_solicitantes.explode('ids_viajes')
df_final = pd.merge(df_solicitantes, df_viajes, left_on='ids_viajes', right_on='id_viaje')

df_final = df_final[['id_solicitante', 'id_viaje']]

df_final = df_final.sort_values(by='id_solicitante')