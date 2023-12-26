import pandas as pd
import numpy as np
import random
from gender_guesser.detector import Detector
#En este archivo lo que vamos hacer es valorizar las variables.

# Crear un DataFrame de ejemplo

# Variables definidas en funciones:
# -Pension
# -discapacidad
# -familianumerosa?? (falta edad hijo y trabaja hijo)
# -funcioedad
# -Lista Espera
# -Vehiculo
# -movilidad
# -Estado de salud
# -lista espera
# -años Viajando(Hay que revisar si dividimos la columna o hay otra alternativa
# -num_max_viaje_por_temp. Queda pendiente revisar si la dejamos, la quitamos o que Nacho nos la explique
import psycopg2

# Parámetros de conexión a PostgreSQL
connection_params = {
    'host': 'tu_host',
    'port': 'tu_puerto',
    'database': 'tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
}

# Conectar a PostgreSQL
conn = psycopg2.connect(**connection_params)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejemplo de inserción de datos en una tabla existente
cursor.execute('INSERT INTO personas (nombre, edad, ciudad) VALUES (%s, %s, %s)', ('María', 30, 'Madrid'))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()


df = pd.read_csv('nombres_españoles.csv', sep = ';', header = None)

# Tabla sexo:

df['sexo'] = None
gender_detector = Detector()
df['nombre'] = df['nombre'].astype('str')
df['nombre'] = df['nombre'].apply(lambda x: x.title())
df['apellido'] = df['apellido'].astype('str')
df['apellido'] = df['apellido'].apply(lambda x: x.title())
for i in (df.index):
    df['sexo'][i] = gender_detector.get_gender(df['nombre'][i])

# Tabla Trabajo:
    
df['trabajo'] = None
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
for i in (df.index):
    df['trabajo'][i] = random.choice(trabajos)

# Tabla domicilio:
    
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

df['domicilio'] = None
for i in df.index:
    df['domicilio'][i] = random.choice(domicilio)

# Tabla Edad:
df['edad'] = np.random.randint(65, 100, 50000)

# Tabla discapacidad:
df['discapacidad'] = np.random.randint(0, 2, 50000)

# Tabla pension:
df['pension'] = np.random.randint(6784.54, 42830.29, 50000)

# Este no creo que nos sirva: lo dejo aquí comentado:
# bins = [6774.54, 12600, 14700, 16800, 18900, 21000, 23100, 25200, 27300, 29400, float('inf')]
# etiquetas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# df['tipo_pension'] = pd.cut(df['pension'], bins=bins, labels=etiquetas)

# Tabla Rentas:
df['renta'] = None
rentas = [0, 8400, 12000, 15000, 18000, 21000]
for i in df.index:
    df['renta'][i] = random.choice(rentas)

# Tabla familia numerosa:
    
df['familia_numerosa'] = np.random.randint(0, 2, 50000)
df['edad_hijo'] = None

fam_num_index = df[df['familia_numerosa'] == 1].index
for i in (fam_num_index):
    df['edad_hijo'][i] = np.random.randint(15, 26)

df['trabaja_hijo'] = None

hijo_mayor_index = df[df['edad_hijo'] > 20].index
for i in (hijo_mayor_index):
    df['trabaja_hijo'][i] = np.random.randint(0, 2)

# Tabla estado civil:
    
df['estado_civil'] = None
estados = ['soltero/a', 'casado/a', 'viudo/a']
for i in (df.index):
    df['estado_civil'][i] = random.choice(estados)

# Tabla Vehículo:
df['vehiculo'] = np.random.randint(0, 2, 50000)

# Tabla Habitación Individual:
df['hab_individual'] = np.random.randint(0, 2, 50000)

# Tabla lista espera:
df['lista_espera'] = np.random.randint(0, 2, 50000)

# Tabla años viajando:
df['años_ant_viajado'] = None
años = ['None', '2021/2022', '2022/2023', '2021/2022 y 2022/2023']
for i in df.index:
    df['años_ant_viajado'][i] = random.choice(años)

# Tabla numero máximo de viajes por temporada:
df['num_max_viaje_por_temp'] = None
doble_index = df[df['años_ant_viajado'] == '2021/2022 y 2022/2023'].index
for i in doble_index:
    df['num_max_viaje_por_temp'][i] = np.random.randint(1, 4)

# Tabla mobilidad:
df['mobilidad'] = None
mobilidad = ['perfecta', 'media', 'limitada']
for i in (df.index):
    df['mobilidad'][i] = random.choice(mobilidad)

# Tabla enfermedad:
    
df['enfermedad'] = None
enfermedad = ['None', 'terminal']
enfermedad = ['None'] * 99 + ['terminal'] * 1
for i in (df.index):
    df['enfermedad'][i] = random.choice(enfermedad)

df[df['enfermedad'] == 'terminal']

# Tabla Viajes:
df_viajes = pd.DataFrame({
   "destino": np.random.randint(10, size=500),
   "plazas": np.random.randint(20, size=500),
    "duracion_dias": np.random.randint(1, 10, size = 500),
   "coste_viaje_dia": np.random.randint(5, size=500),
   "huella_carbono": np.random.randint(30, size=500),
    "plazas_provincia": np.random.randint(30, size=500)
})
df_viajes

# Tabla Viajes:

destinos_cap = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia",
    "Palma de Mallorca", "Las Palmas de Gran Canaria", "Bilbao", "Alicante", "Córdoba",
    "Valladolid", "Vigo", "Girona", "Lugo", "León", "Toledo", "Santander", "Pamplona",
    "Logroño", "Badajoz", "Huesca", "Castellón de la Plana", "Tarragona", "Lleida",
    "Ourense", "Cáceres", "Jaén", "Almería", "Ciudad Real", "Huelva", "Cuenca", "Ávila",
    "Segovia", "Soria", "Teruel", "Cuenca", "Zamora", "Guadalajara", "Palencia", "Huesca"]

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

destinos = destinos_cap + destinos_nocap


for i in df_viajes.index:
    df_viajes['destino'][i] = random.choice(destinos)


# Tabla coste viaje:

coste_viajes_cap = [75,80,90,100,110,130]
coste_viajes_nocap = [30,40,50,60,70]

for i in df_viajes.index:
    if df_viajes['destino'][i] in destinos_cap:
        df_viajes['coste_viaje_dia'][i] = random.choice(coste_viajes_cap)
    else:
        df_viajes['coste_viaje_dia'][i] = random.choice(coste_viajes_nocap)


