import numpy as np

def asignacionPuntos(row):
#Edad:
    condiciones_edad = [
        (row['Edad'] < 60),
        (row['Edad'] == 60),
        ((61 < row['Edad']) & (row['Edad'] < 78)),
        (row['Edad'] >= 78)
    ]

    scoresEdad = [1, 2,2+row['Edad']-60, 20] #Revisar: le resto 60 a la edad de la fila para sumar esos puntos.
    score_edad = np.select(condiciones_edad, scoresEdad, default=0)
#Movilidad
    condiciones_movilidad= [
        (row['Movilidad']==0),#'Limitada'
        (row['Movilidad']==1),#'Media'
        (row['Movilidad']==2) #'Perfecta'
    ]
    scoresMovilidad=[10,20,30]
    score_movilidad=np.select(condiciones_movilidad,scoresMovilidad,default=0)
    
    condiciones_discapacidad=[
        (row['Discapacidad']==0),
        (row['Discapacidad']==1)
    ]
    scoresDiscapacidad=[0,25]
    score_discapacidad=np.select(condiciones_discapacidad,scoresDiscapacidad,default=0)
#Enfermedad
    condiciones_enfermedad=[
        (row['Enfermedad']==0),
        (row['Enfermedad']==1)
    ]
    scoresEnfermedad=[50,0]
    score_enfermedad=np.select(condiciones_enfermedad,scoresEnfermedad,default=0)
#Vehiculo propio
    condiciones_vehiculoPropio=[
        (row['Vehiculo']==0),#No tiene vehiculo propio
        (row['Vehiculo']==1)#Tiene vehículo propio
    ]
    scoresVehiculoPropio=[0,20]
    score_vehiculo=np.select(condiciones_vehiculoPropio,scoresVehiculoPropio,default=0)

#Familia_numerosa: No puedo probarla porque me da un error al generar los datos
    condiciones_familia_numerosa=[
        (row['familia_numerosa']==0),#No es familia numerosa
        (row['familia_numerosa']==1) & (row['edad_hijo']<26) & (row['trabaja_hijo']==0), #familia numerosa con menor de 26 que no trabaja
        (row['familia_numerosa']==1) & (row['edad_hijo']<26) & (row['trabaja_hijo']==1), #familia numerosa con menor de 26 que trabaja
    ]

    scoresFamiliaNumerosa=[0,50,0]
    score_familia_numerosa=np.select(condiciones_familia_numerosa,scoresFamiliaNumerosa,default=0)

    # Falta añadirla a la suma totalScore

#Habitación individual:
    condiciones_habitacion=[
        (row['hab_individual']==0), #Habitacion doble
        (row['hab_individual']==1) #habitacion individual
    ]

    scoresHabitacion=[20,0]
    score_habitacion_individual=np.select(condiciones_habitacion,scoresHabitacion,default=0)

# Renta
    condiciones_renta=[
        (row['Renta']<14700),
        (row['Renta']<16800),
        (row['Renta']<18900),
        (row['Renta']<21000),
        (row['Renta']<23100),
        (row['Renta']<25200),
        (row['Renta']<23700),
        (row['Renta']<29400),
        (row['Renta']>29400)
    ]
    scoresRenta=[50,45,40,35,30,20,10,5,0]
    score_renta=np.select(condiciones_renta,scoresRenta,default=0)

#Años anteriores viajando:
#     Personas usuarias del programa con acreditación en fase de lista de espera en la temporada 2022/2023: 175 puntos.
# Personas usuarias que no hayan viajado en las 2 últimas temporadas: 50 puntos.
# Personas usuarias que no hayan viajado en la temporada 2022/2023 y sí en la 2021/2022: 40 puntos.
# Personas usuarias que sí hayan viajado en la temporada 2022/2023 y no en la 2021/2022: 20 puntos
# Personas usuarias que sí hayan viajado en las dos últimas temporadas, la puntuación máxima por este apartado será de 10 puntos, de acuerdo con el siguiente detalle:
# Si se han realizado 2 o más viajes en cualquiera de las dos temporadas 2022/2023 y 2021/2022: 0 puntos.
# Resto de casos: 10 puntos.
    condiciones_anyos_anteriores=[
        (row['Anyos_Anteriores1']=='2022/2023'),
        (row['Anyos_Anteriores1']==None) & (row['Anyos_Anteriores2']==None),
        (row['Anyos_Anteriores1']==None) & (row['Anyos_Anteriores2']=='2021/2022'),
        (row['Anyos_Anteriores1']=='2022/2023') & (row['Anyos_Anteriores2']==None),
        (row['Anyos_Anteriores1']=='2022/2023') & (row['Anyos_Anteriores2']=='2021/2022')&(row['Viajes_realizados']>2),
        #Habría que definir una columna viajes realizados las dos últimas temporadas para poder evaluar
        (row['Anyos_Anteriores1']=='2022/2023') & (row['Anyos_Anteriores2']=='2021/2022')&(row['Viajes_realizados']<2)
    ]
    score_anyos_anteriores=[175,50,40,20,0,10]

    #Revisar el tema del estado civil, casado etc...

    totalScore= score_edad + score_movilidad+score_discapacidad+score_enfermedad+score_vehiculo+score_habitacion_individual+score_renta+score_anyos_anteriores+score_familia_numerosa
    return totalScore


    


# Aplicar la función a cada fila y crear una nueva columna 'Score_Total'
df['Score_Total'] = df.apply(asignacionPuntos, axis=1)

# Mostrar el DataFrame resultante
print(df)


df['Score_Total']=asignacionPuntos(df)
print(df)
print(df.columns)