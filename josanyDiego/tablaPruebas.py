import numpy as np
import csv
import pandas as pd 

ruta='C:\\Users\\josan\\Documents\\GitHub\\MDAES_Data_Project_I\\datos_previos_old\\solicitantes.csv'

df=pd.read_csv(ruta)
df['edad']=np.random.randint(60,90)
condiciones_movilidad= [0,1,2]
        # (row['movilidad']==0),#'Limitada'
        # (row['movilidad']==1),#'Media'
        # (row['movilidad']==2) #'Perfecta'

df['mobilidad']=np.random.choice(condiciones_movilidad)
df['discapacidad']=np.random.randint(0, 2, size=len(df)) #1 discapacidad
df['enfermedad']=np.random.randint(0, 2, size=len(df)) #1 enfermedad
df['vehiculo']=np.random.randint(0, 2, size=len(df)) #1 tiene vehiculo
df['familiaNumerosa']=np.random.randint(0, 2, size=len(df))# uno famiia numerosa
df['habitacion_individual']=np.random.randint(0, 2, size=len(df))
df['renta']=np.random.randint(6000, 50000, size=len(df))
condiciones_anyos_anteriores=['2022/2023','2021/2022']
df['anyosAnterioresViajando']=np.random.choice(condiciones_anyos_anteriores)

print(df)




