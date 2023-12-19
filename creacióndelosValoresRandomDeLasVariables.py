import csv
import pandas as pd
import numpy as np

nombres="nombres_españoles.csv"

df=pd.read_csv(nombres)
# Creación calumna edad y valores random entre 60 y 100
df["Edad"]=np.random.randint(60, 101, size=len(df))

# Creo la columna Discapacidad, dejo estos porcentajes por si los queremos modificar
porcentajeTrue=87
porcentajeFalse=13
df["Discapacidad"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrue/100, porcentajeFalse/100])

# Creación columna renta y valores (tomo la renta media del ine 14762 https://ine.es/jaxiT3/Datos.htm?t=9942)
rentaMedia=14762
df["IRPF"]=np.random.randint(rentaMedia-5000,rentaMedia+5000, size=len(df))

# Creación columna pension y valores (tendremos que revisar los datos)
pensionMedia=1197.87
df["Pension"]=np.random.randint(pensionMedia-300,pensionMedia+300, size=len(df))

# Creación columna familia numerosa:
porcentajeTrueFN=87
porcentajeFalseFN=13
df["Familia_numerosa"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueFN/100, porcentajeFalseFN/100])

# Creación columna lista de espera:
porcentajeTrueLE=87
porcentajeFalseLE=13
df["Lista espera"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueLE/100, porcentajeFalseLE/100])

# Creación columna Repetición de destinos:
porcentajeTrueRd=87
porcentajeFalseRd=13
df["Repetición destinos"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueRd/100, porcentajeFalseRd/100])

# Creación columna Estado Civil (True=Casado/False=Soltero)
porcentajeTrueEc=87
porcentajeFalseEc=13
df["Estado civil"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueEc/100, porcentajeFalseEc/100])

# Creación columna Pensión Contributiva (True=Pension Contributiva/ False=Pension No Contributiva)
porcentajeTruePc=65
porcentajeFalsePc=35
df["P.Contributiva"]=np.random.choice([True, False], size=len(df), p=[porcentajeTruePc/100, porcentajeFalsePc/100])


# Creación columna Participación ultimos años:
porcentajeTruePuañ=10
porcentajeFalsePuañ=90
df["Participación últimos dos años"]=np.random.choice([True, False], size=len(df), p=[porcentajeTruePuañ/100, porcentajeFalsePuañ/100])


# Creación columna Vehículo propio (T/F)
porcentajeTrueVp=60
porcentajeFalseVp=40
df["Vehiculo (S/N)"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueVp/100, porcentajeFalseVp/100])

# Creación columna Coste Viaje:
costeViajeMedio=210
df["Coste Viaje"]=np.random.randint(costeViajeMedio-85,costeViajeMedio+125, size=len(df))


# Creación Columna Huella Generada de Carbono:
maxHuella=100
minHuella=0
df["Huella CO2 generada"]=np.random.randint(minHuella,maxHuella, size=len(df))

# Creación columna Habitación Individual:
porcentajeTrueHi=60
porcentajeFalseHi=40
df["Habitacion Individual"]=np.random.choice([True, False], size=len(df), p=[porcentajeTrueHi/100, porcentajeFalseHi/100])

# Creación columna Mobilidad (30-100%):
maxMobilidad=100
minMobilidad=0
df["Mobilidad"]=np.random.randint(minMobilidad,maxMobilidad, size=len(df))

# Creación Columna Estado de salud (30-100%)
maxSalud=100
minSalud=0
df["Estado de salud"]=np.random.randint(minSalud,maxSalud, size=len(df))

# Creación Columna Score:
df["Score"]=0

print(df.columns)
print(df)



