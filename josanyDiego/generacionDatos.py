

import pandas as pd
import numpy as np
import random
from gender_guesser.detector import Detector


import psycopg2
from faker import Faker
import random

# TABLA 1 AÑOS_ANT

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

# Generar datos aleatorios con Faker y Numpy
fake = Faker()

# Generar datos para la tabla "clientes" como ejemplo
for i in range(50000):  # ajusta el número de filas que deseas generar
    id_solicitante= i
    años_ant_viajado = np.random.randint(0,2)
    num_max_viaje_por_temp = np.random.randint(0,2)
    

    # Insertar datos en la tabla "clientes"
    cursor.execute(
        f"INSERT INTO años_ant (id_solicitante, años_ant_viajado, num_max_viaje_por_temp) VALUES (%s, %s, %s, %s)",
        (id_solicitante, años_ant_viajado, num_max_viaje_por_temp)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()


# TABLA2 caract


# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()


for i in range(50000):  # ajusta el número de filas que deseas generar
    id_solicitante="" # Revisar si tenemos que copiar en el init.sql los ides de la primera tabla
    años_ant_viajado = np.random.randint(60,90)
    num_max_viaje_por_temp = np.random.randint(0,2)
    sexo=np.random.choice('Hombre','Mujer')
    edad=np.random.randint(60,90)
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

    trabajo = random.choice(trabajos,size=len(df))
    años_trabajados=np.random.randint(0,45)
    tipo_movilidad=['Limitada','Media','Perfecta']
    movilidad=np.random.choice(tipo_movilidad)
    discapacidad= np.random.randint(0, 1)
    enfermedad = np.random.randint(0, 1, 50000) #0 terminal, 1 resto enfermedades
    

    # Insertar datos en la tabla "clientes"
    cursor.execute(
        f"INSERT INTO caract (id_solicitante,años_ant_viajado,num_max_por_temp,sexo,edad,trabajo,años_trabajados,movilidad,discapacidad,enfermedad) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)",
        (id_solicitante, años_ant_viajado, num_max_viaje_por_temp,sexo,edad,trabajo,años_trabajados,movilidad,discapacidad,enfermedad)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

#  TABLE3 datos

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

fake= Faker() #Revisar si funciona

for i in range(50000):  # ajusta el número de filas que deseas generar
    id_solicitante="" # Revisar si tenemos que copiar en el init.sql los ides de la primera tabla
    nombre=fake.name()
    apellido=fake.name() #Revisar si los apellidos se meten en juntos o separados en dos columnas
    # Insertar datos en la tabla "clientes"
    cursor.execute(
        f"INSERT INTO datos (id_solicitante,nombre,apellido) VALUES (%s, %s, %s)",
        (id_solicitante,nombre,apellido)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

# TABLE 4 destinos 
    
# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

fake= Faker() #Revisar si funciona

for i in range(50000):  
    id_destino="" 
    destino=""
    tipo_destino=""
    cursor.execute(
        f"INSERT INTO caract (id_destino,destino,tipo_destino) VALUES (%s, %s, %s)",
        (id_destino,destino,tipo_destino)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()




# TABLE5 5 IF NOT EXISTS fam_num 

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()



for i in range(50000):  
    
    id_solicitante=""#Revisar si nos lo traemos de otra tabla
    nombre=""#Revisar si nos lo traemos de otra tabla
    apellido=""#Revisar si nos lo traemos de otra tabla
    familia_numerosa=np.random.randint(0,1)
    edad_hijo=np.random.randint(15,26)
    trabaja_hijo=np.random.randint(0,1)

    id_destino="" 
    destino=""
    tipo_destino=""

    cursor.execute(
        f"INSERT INTO fam_num (id_solicitante,nombre,apellido,familia_numerosa,edad_hjo,trabaja_hijo) VALUES (%s, %s, %s,%s, %s, %s)",
        (id_solicitante,nombre,apellido,familia_numerosa,edad_hijo,trabaja_hijo)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()



#TABLE 6 habitacion 
# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()



for i in range(50000):  
    
    id_solicitante=""#Revisar si nos lo traemos de otra tabla
    hab_ind=np.random.randint(0,1)


    cursor.execute(
        f"INSERT INTO habitacion (id_solicitante,hab_ind) VALUES (%s, %s)",
        (id_solicitante,hab_ind)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

#TABLE 7 IF NOT EXISTS pensiones


# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()



for i in range(50000):  
    
    id_solicitante=""#Revisar si nos lo traemos de otra tabla
    renta=np.random.randint()
    pension= np.random.randint(6784.54, 42829.29, 50000)
    tipo_pension=np.random.choice('contributiva','no contributiva',p=[0.2,0.8])
    estado_civil=np.random.choice('Casado/a','Soltero/a',p=[0.2,0.8])
    pension_conyuge=np.random.randint(6784.54, 42829.29, 50000)


    cursor.execute(
        f"INSERT INTO pensiones (id_solicitante,renta,pension,tipo_pension,estado_civil,pension_conyuge) VALUES (%s, %s,%s, %s,%s, %s)",
        (id_solicitante,renta,pension,tipo_pension,estado_civil,pension_conyuge)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()


# TABLE 8 precios 

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

for i in range(50000): 

    id_precio =" "
    tipo_destino=""#revisar si ya está generado
    duracion=np.random.randint(3,9)
    transporte=np.random.randint(0,1)
    sup_hab_ind=" "
    precios_habitaciones=[]
    precio=np.random.choice(precios_habitaciones)

    cursor.execute(
        f"INSERT INTO precios (id_precio,tipo_destino,duracion,transporte,sup_hab_ind,precio) VALUES (%s, %s,%s, %s,%s, %s)",
        (id_precio,tipo_destino,duracion,transporte,sup_hab_ind,precio)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

# TABLE 9  solicitudes 

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

for i in range(50000): 
    id_solicitante = ''
    id_viaje =' '


    cursor.execute(
        f"INSERT INTO solicitudes (id_solicitante,id_viaje) VALUES (%s, %s)",
        (id_solicitante,id_viaje)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

# TABLE 10 viajero (

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

for i in range(50000): 
    id_solicitante=' '
    domicilio=' '
    vehiculo =np.random.randint(0,1)



    cursor.execute(
        f"INSERT INTO viajero (id_solicitante,domicilio,vehiculo) VALUES (%s, %s,(%s)",
        (id_solicitante,domicilio,vehiculo)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

# TABLE 11 viajes 

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

for i in range(50000): 

    id_viaje=" "
    id_destino =" "
    id_precio =" "

    cursor.execute(
        f"INSERT INTO viajes (id_viaje,id_destino,id_precio) VALUES (%s, %s,(%s)",
        (id_viaje,id_destino,id_precio)
    )

# Hacer commit para aplicar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
