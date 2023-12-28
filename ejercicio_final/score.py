import psycopg2
import pandas as pd
import numpy as np

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="project",
    user="project",
    password="project",
    host="localhost",
    port="5432"
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar las consultas
queries = [
"""CREATE TABLE query1 AS (
select d.id_solicitante, d.nombre, d.apellido, c.sexo, c.edad, c.trabajo, c.anyos_trabajados, c.movilidad, c.discapacidad, c.enfermedad,
f.familia_numerosa, f.edad_hijo, f.trabaja_hijo, h.hab_ind, p.renta, p.pension, p.tipo_pension, p.estado_civil, p.pension_conyuge, v.domicilio,
v.vehiculo, a.lista_espera, a.viaje_2021, a.viaje_2022, a.num_max_viaje_por_temp
from datos d, anyos_ant a, caract c, fam_num f, habitacion h, pensiones p, viajero v
where d.id_solicitante = a.id_solicitante and d.id_solicitante = c.id_solicitante and d.id_solicitante = f.id_solicitante 
and d.id_solicitante = h.id_solicitante and d.id_solicitante = p.id_solicitante  and d.id_solicitante = v.id_solicitante
);""",
    """CREATE TABLE query3 AS (
select v.id_viaje , v.id_destino, d.destino, d.tipo_destino,  v.id_precio, pr.duracion, pr.transporte, pr.sup_hab_ind, pr.precio, s.id_solicitante, m.mes, s.solicita_menu
from viajes v, destinos d, precios pr, solicitudes s, mes m 
where v.id_destino = d.id_destino and pr.id_precio = v.id_precio and s.id_viaje = v.id_viaje and m.id_viaje = v.id_viaje 
);""",
    """select q1.id_solicitante, q1.nombre, q1.apellido, q1.sexo, q1.edad, q1.trabajo, q1.anyos_trabajados, q1.movilidad, q1.discapacidad, q1.enfermedad,
q1.familia_numerosa, q1.edad_hijo, q1.trabaja_hijo, q1.hab_ind, q1.renta, q1.pension, q1.tipo_pension, q1.estado_civil, q1.pension_conyuge, q1.domicilio,
q1.vehiculo, q1.lista_espera, q1.viaje_2021, q1.viaje_2022, q1.num_max_viaje_por_temp, q3.id_viaje, q3.id_destino, q3.destino, q3.tipo_destino, q3.mes, q3.solicita_menu, q3.id_precio,
q3.duracion, q3.transporte, q3.sup_hab_ind, q3.precio
from query1 q1, query3 q3
where q1.id_solicitante = q3.id_solicitante;"""
]

for query in queries:
    cur.execute(query)

data = cur.fetchall()
columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(data, columns=columns)

cur.close()
conn.close()

def asignacionPuntos(row):
    condiciones_edad = [
        (row['edad'] < 60),
        (row['edad'] == 60),
        ((61 < row['edad']) & (row['edad'] < 78)),
        (row['edad'] >= 78)
    ]

    scoresEdad = [1, 2,2+row['edad']-60, 20]
    score_edad = np.select(condiciones_edad, scoresEdad, default=0)
    
    condiciones_años_trab = [
        (row['anyos_trabajados'] < 20),
        (20 < row['anyos_trabajados']) & (row['anyos_trabajados'] < 25),
        ((26 < row['anyos_trabajados']) & (row['anyos_trabajados'] < 30)),
        (row['anyos_trabajados'] >= 30)
    ]

    scoresAños_trab=[10,20,30,40]
    score_años_trab=np.select(condiciones_años_trab,scoresAños_trab,default=0)

    condiciones_movilidad= [
        (row['movilidad']=='limitada'),
        (row['movilidad']=='media'),
        (row['movilidad']=='perfecta')
    ]
    scoresMovilidad=[10,20,30]
    score_movilidad=np.select(condiciones_movilidad,scoresMovilidad,default=0)
    
    condiciones_discapacidad=[
        (row['discapacidad']==False),
        (row['discapacidad']==True)
    ]
    scoresDiscapacidad=[0,25]
    score_discapacidad=np.select(condiciones_discapacidad,scoresDiscapacidad,default=0)

    condiciones_enfermedad=[
        (row['enfermedad']==False),
        (row['enfermedad']==True)
    ]
    scoresEnfermedad=[50,0]
    score_enfermedad=np.select(condiciones_enfermedad,scoresEnfermedad,default=0)

    condiciones_familia_numerosa=[
        (row['familia_numerosa']==False),#No es familia numerosa
        (row['familia_numerosa']==True) & (row['edad_hijo']<26) & (row['edad_hijo']>0) & (row['trabaja_hijo']==False), #familia numerosa con menor de 26 que no trabaja
        (row['familia_numerosa']==True) & (row['edad_hijo']<26) & (row['edad_hijo']>0) & (row['trabaja_hijo']==True), #familia numerosa con menor de 26 que trabaja
    ]

    scoresFamiliaNumerosa=[0,50,15]
    score_familia_numerosa=np.select(condiciones_familia_numerosa,scoresFamiliaNumerosa,default=0)

    condiciones_habitacion=[
        (row['hab_ind']==False), #Habitacion doble
        (row['hab_ind']==True) #habitacion individual
    ]

    scoresHabitacion=[20,0]
    score_habitacion_individual=np.select(condiciones_habitacion,scoresHabitacion,default=0)

    condiciones_renta=[
        (row['renta']<1),
        ((row['renta']<8500) & (row['renta']>1)),
        ((row['renta']<13000) & (row['renta']>8500)),
        ((row['renta']<16000) & (row['renta']>13000)),
        ((row['renta']<19000) & (row['renta']>16000)),
        ((row['renta']<22000) & (row['renta']>19000))
    ]
    scoresRenta=[50,40,30,20,10,0]
    score_renta=np.select(condiciones_renta,scoresRenta,default=0)

    condiciones_vehiculo=[
        (row['vehiculo']==False), #Habitacion doble
        (row['vehiculo']==True) #habitacion individual
    ]

    scores_vehiculo=[20,0]
    score_vehiculo_ind=np.select(condiciones_vehiculo,scores_vehiculo,default=0)
    
    condiciones_años_ant=[
        ((row['lista_espera']==True) & (row['viaje_2021']==True) & (row['viaje_2022']==True) & (row['num_max_viaje_por_temp']<2)),
        ((row['lista_espera']==True) & (row['viaje_2021']==False) & (row['viaje_2022']==False) & (row['num_max_viaje_por_temp']<2)),
        ((row['lista_espera']==True) & (row['viaje_2021']==False) & (row['viaje_2022']==True) & (row['num_max_viaje_por_temp']<2)),
        ((row['lista_espera']==True) & (row['viaje_2021']==True) & (row['viaje_2022']==False) & (row['num_max_viaje_por_temp']<2)),
        ((row['lista_espera']==True) & (row['viaje_2021']==True) & (row['viaje_2022']==True) & (row['num_max_viaje_por_temp']>1)),
        ((row['lista_espera']==True) & (row['viaje_2021']==False) & (row['viaje_2022']==True) & (row['num_max_viaje_por_temp']>1)),
        ((row['lista_espera']==True) & (row['viaje_2021']==True) & (row['viaje_2022']==False) & (row['num_max_viaje_por_temp']>1)),
        (row['lista_espera']==False)
    ]

    scores_años_ant=[40,70,50,60,5,10,15,0]
    score_años_ant=np.select(condiciones_años_ant,scores_años_ant,default=0)

    condiciones_destino=[
        (row['tipo_destino']=='circuitos_culturales'),
        (row['tipo_destino']=='turismo_naturaleza'),
        (row['tipo_destino']=='zona_baleares'),
        (row['tipo_destino']=='capitales_provincia'),
        (row['tipo_destino']=='zona_costera'),
        (row['tipo_destino']=='viaje_ceuta_melilla'),
        (row['tipo_destino']=='zona_canarias')
    ]

    scores_destinos=[50,35,20,0,10,70,30]
    score_destino=np.select(condiciones_destino,scores_destinos,default=0)


    condiciones_precio=[
        (row['id_precio']==1),
        (row['id_precio']==2),
        (row['id_precio']==3),
        (row['id_precio']==4),
        (row['id_precio']==5),
        (row['id_precio']==6),
        (row['id_precio']==7),
        (row['id_precio']==8),
        (row['id_precio']==9),
        (row['id_precio']==10),
        (row['id_precio']==11),
        (row['id_precio']==12),
        (row['id_precio']==13),
        (row['id_precio']==14),
        (row['id_precio']==15),
        (row['id_precio']==16),
        
    ]
    
    scores_precios=[12,11,13,5,8,9,14,3,2,10,15,1,4,7,16,6]
    score_precio=np.select(condiciones_precio,scores_precios,default=0)   

    totalScore= score_edad + score_años_trab+ score_movilidad+score_discapacidad+score_enfermedad +score_familia_numerosa+score_habitacion_individual+score_renta +score_vehiculo_ind+score_años_ant+score_destino+score_precio
    return totalScore

df['Score_Total'] = df.apply(asignacionPuntos, axis=1)

df_aux = df.copy()
df_aux['pension'] = np.where(df_aux['estado_civil'] == 'casado/a',
                             (df_aux['pension'] + df_aux['pension_conyuge']) / 1.33,
                             df_aux['pension'])

def asignacionPuntosPension(row):
    condiciones_pensiones=[
        ((row['pension']<13076) & (row['pension']>6786)),
        ((row['pension']<19365) & (row['pension']>13075)),
        ((row['pension']<25654) & (row['pension']>19364)),
        ((row['pension']<31943) & (row['pension']>25653)),
        (row['pension']>31942)
    ]
    scores_pension=[10,20,30,40,50]
    score_pension=np.select(condiciones_pensiones,scores_pension,default=0)
    return score_pension

df_aux['score_pension'] = df_aux.apply(asignacionPuntosPension, axis=1)
df_aux['score_total'] = df_aux['Score_Total'] + df_aux['score_pension']
df['Score_Total'] = df_aux['score_total']
