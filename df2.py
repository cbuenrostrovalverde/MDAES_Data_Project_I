zona_costera = [
    "Ruta_Andalucia",
    "Ruta_Cataluña",
    "Ruta_Murcia",
    "Ruta_CV"
]

zona_baleares = [
    "Ruta_Baleares"
]

zona_canarias = [
    "Ruta_Canarias"
]

circuitos_culturales = [
    "Jerez de la Frontera", 
    "Cordoba", 
    "Albolote", 
    "Granada", 
    "Jaen", 
    "Benalmadena", 
    "Sevilla",
    "Huesca", 
    "Teruel", 
    "Zaragoza",
    "Gijon", 
    "Oviedo",
    "Palma de Mallorca",
    "Las Palmas de Gran Canaria",
    "Santander", 
    "Santoña", 
    "Suances", 
    "Torrelavega",
    "Ciudad Real", 
    "Cuenca", 
    "Guadalajara", 
    "Toledo",
    "Avila", 
    "Burgos", 
    "Leon", 
    "Palencia", 
    "Salamanca", 
    "Segovia", 
    "Soria", 
    "Valladolid", 
    "Zamora",
    "Barcelona", 
    "Tarragona",
    "Alicante", 
    "Castellon", 
    "Valencia",
    "Badajoz", 
    "Caceres",
    "A Coruña", 
    "Lugo", 
    "Ourense", 
    "Sanxenxo",
    "Haro", 
    "Logroño",
    "Aranjuez", 
    "Pinto", 
    "San Lorenzo del Escorial",
    "Aguilas", 
    "La Manga del Mar Menor",
    "Pamplona", 
    "Burguete",
    "Laguardia", 
    "Eibar", 
    "Sondika",
    "Ceuta", 
    "Melilla"
]


turismo_naturaleza = [
    "Aguadulce", 
    "Sanlucar de Barrameda", 
    "Islantilla y Punta Umbria", 
    "La Iruela y Villanueva del Arzobispo",
    "Barbastro",
    "Gijon_2",
    "Palma de Mallorca_2",
    "Las Palmas de Gran Canaria_2",
    "Puerto de la Cruz",
    "Cabuerniga",
    "Hellin", 
    "Cuenca_2",
    "Avila_2", 
    "Mogarraz", 
    "Soria_2",
    "Pont de Suert",
    "Peñiscola",
    "Trujillo",
    "Santiago de Compostela",
    "Haro_2",
    "San Lorenzo del Escorial_2",
    "Zarautz"
]


capitales_provincia = [
    "Cordoba_2", 
    "Granada_2", 
    "Sevilla_2",
    "Zaragoza_2",
    "Santander_2",
    "Toledo_2",
    "Burgos_2", 
    "Leon_2", 
    "Salamanca_2", 
    "Zamora_2",
    "Girona",
    "Valencia_2",
    "Caceres_2",
    "Ourense_2",
    "San Sebastian"]

ceuta_melilla = [
    "Ceuta_2", 
    "Melilla_2"
]

destinos = zona_costera + zona_baleares + zona_canarias + circuitos_culturales + turismo_naturaleza + capitales_provincia + ceuta_melilla
destinos = pd.Series(destinos)
df_destinos = pd.DataFrame(destinos, columns=['destino'])

df_destinos.index = range(1, len(df_destinos) + 1)
df_destinos['id_destino'] = df_destinos.index
df_destinos['tipo_destino'] = 'zona_costera'  

df_destinos.loc[:4, 'tipo_destino'] = 'zona_costera'
df_destinos.loc[5, 'tipo_destino'] = 'zona_baleares'
df_destinos.loc[6, 'tipo_destino'] = 'zona_canarias'
df_destinos.loc[7:62, 'tipo_destino'] = 'circuitos_culturales'
df_destinos.loc[63:84, 'tipo_destino'] = 'turismo_naturaleza'
df_destinos.loc[85:99, 'tipo_destino'] = 'capitales_provincia'
df_destinos.loc[100:, 'tipo_destino'] = 'viaje_ceuta_melilla'

df_destinos = df_destinos[['id_destino', 'destino', 'tipo_destino']]
df_destinos.loc[101]

df_destinos

df_precios = pd.DataFrame({
    'id_precio': np.random.randint(1,100,16)
})
df_precios.index = range(1, len(df_precios) + 1)
df_precios['id_precio'] = df_precios.index


df_precios.loc[:4, 'tipo_destino'] = 'zona_costera'
df_precios.loc[5:8, 'tipo_destino'] = 'zona_baleares'
df_precios.loc[9:12, 'tipo_destino'] = 'zona_canarias'
df_precios.loc[13, 'tipo_destino'] = 'circuitos_culturales'
df_precios.loc[14, 'tipo_destino'] = 'turismo_naturaleza'
df_precios.loc[15, 'tipo_destino'] = 'capitales_provincia'
df_precios.loc[16, 'tipo_destino'] = 'viaje_ceuta_melilla'

duraciones = [7,9,7,9,7,9,7,9,7,9,7,9,5,4,3,4]
df_precios['duracion'] = duraciones
df_precios['transporte'] = 1

for i in range(1, min(13, len(df_precios)), 2):
    df_precios.loc[i:i+1, 'transporte'] = 1

for i in range(2, min(13, len(df_precios)), 4):
    df_precios.loc[i:i+1, 'transporte'] = 0

suplemento_hab_indv = [22,22,22,22,22,22,22,22,24,24,24,24,26,26,26,26]
df_precios['sup_hab_ind'] = suplemento_hab_indv

precios = [228.93, 253.65, 210.72, 290.07, 267.63, 253.77, 210.47, 331.49,
           355.30, 253.65, 210.39, 435.95, 293.16, 286.82, 124.68, 286.82]

df_precios['precio'] = precios

df_precios

df_viajes = pd.DataFrame({
    'id_viaje': np.random.randint(1,5,5000)
})
df_viajes.index = range(1, len(df_viajes) + 1)
df_viajes['id_viaje'] = df_viajes.index

df_viajes['destino'] = None
for i in df_viajes.index:
    df_viajes['destino'][i] = random.choice(destinos)


mapeo_ids = df_destinos.set_index('destino')['id_destino']
df_viajes['id_destino'] = df_viajes['destino'].map(mapeo_ids)

mapeo_tipo = df_destinos.set_index('destino')['tipo_destino']
df_viajes['tipo_destino'] = df_viajes['destino'].map(mapeo_tipo)

df_viajes['id_precio'] = 1
for i in df_viajes.index:
    if df_viajes['tipo_destino'][i] == 'turismo_naturaleza':
        df_viajes['id_precio'][i] = 14
    elif df_viajes['tipo_destino'][i] == 'circuitos_culturales':
        df_viajes['id_precio'][i] = 13
    elif df_viajes['tipo_destino'][i] == 'capitales_provincia':
        df_viajes['id_precio'][i] = 15
    elif df_viajes['tipo_destino'][i] == 'viaje_ceuta_melilla':
        df_viajes['id_precio'][i] = 16
    elif df_viajes['tipo_destino'][i] == 'zona_canarias':
        df_viajes['id_precio'][i] = np.random.choice([9,10,11,12])
    elif df_viajes['tipo_destino'][i] == 'zona_baleares':
        df_viajes['id_precio'][i] = np.random.choice([5,6,7,8])
    elif df_viajes['tipo_destino'][i] == 'zona_costera':
        df_viajes['id_precio'][i] = np.random.choice([1,2,3,4])

df_viajes = df_viajes[['id_viaje', 'id_destino', 'id_precio']]

df_viajes

df_destinos.to_csv('destinos.csv')

df_precios.to_csv('precios.csv')

df_viajes.to_csv('viajes.csv')


zona_costera = [
    "Ruta_Andalucia",
    "Ruta_Cataluña",
    "Ruta_Murcia",
    "Ruta_CV"
]

zona_baleares = [
    "Ruta_Baleares"
]

zona_canarias = [
    "Ruta_Canarias"
]

circuitos_culturales = [
    "Jerez de la Frontera", 
    "Cordoba", 
    "Albolote", 
    "Granada", 
    "Jaen", 
    "Benalmadena", 
    "Sevilla",
    "Huesca", 
    "Teruel", 
    "Zaragoza",
    "Gijon", 
    "Oviedo",
    "Palma de Mallorca",
    "Las Palmas de Gran Canaria",
    "Santander", 
    "Santoña", 
    "Suances", 
    "Torrelavega",
    "Ciudad Real", 
    "Cuenca", 
    "Guadalajara", 
    "Toledo",
    "Avila", 
    "Burgos", 
    "Leon", 
    "Palencia", 
    "Salamanca", 
    "Segovia", 
    "Soria", 
    "Valladolid", 
    "Zamora",
    "Barcelona", 
    "Tarragona",
    "Alicante", 
    "Castellon", 
    "Valencia",
    "Badajoz", 
    "Caceres",
    "A Coruña", 
    "Lugo", 
    "Ourense", 
    "Sanxenxo",
    "Haro", 
    "Logroño",
    "Aranjuez", 
    "Pinto", 
    "San Lorenzo del Escorial",
    "Aguilas", 
    "La Manga del Mar Menor",
    "Pamplona", 
    "Burguete",
    "Laguardia", 
    "Eibar", 
    "Sondika",
    "Ceuta", 
    "Melilla"
]


turismo_naturaleza = [
    "Aguadulce", 
    "Sanlucar de Barrameda", 
    "Islantilla y Punta Umbria", 
    "La Iruela y Villanueva del Arzobispo",
    "Barbastro",
    "Gijon_2",
    "Palma de Mallorca_2",
    "Las Palmas de Gran Canaria_2",
    "Puerto de la Cruz",
    "Cabuerniga",
    "Hellin", 
    "Cuenca_2",
    "Avila_2", 
    "Mogarraz", 
    "Soria_2",
    "Pont de Suert",
    "Peñiscola",
    "Trujillo",
    "Santiago de Compostela",
    "Haro_2",
    "San Lorenzo del Escorial_2",
    "Zarautz"
]


capitales_provincia = [
    "Cordoba_2", 
    "Granada_2", 
    "Sevilla_2",
    "Zaragoza_2",
    "Santander_2",
    "Toledo_2",
    "Burgos_2", 
    "Leon_2", 
    "Salamanca_2", 
    "Zamora_2",
    "Girona",
    "Valencia_2",
    "Caceres_2",
    "Ourense_2",
    "San Sebastian"]

ceuta_melilla = [
    "Ceuta_2", 
    "Melilla_2"
]

destinos = zona_costera + zona_baleares + zona_canarias + circuitos_culturales + turismo_naturaleza + capitales_provincia + ceuta_melilla
destinos = pd.Series(destinos)
df_destinos = pd.DataFrame(destinos, columns=['destino'])

df_destinos.index = range(1, len(df_destinos) + 1)
df_destinos['id_destino'] = df_destinos.index
df_destinos['tipo_destino'] = 'zona_costera'  

df_destinos.loc[:4, 'tipo_destino'] = 'zona_costera'
df_destinos.loc[5, 'tipo_destino'] = 'zona_baleares'
df_destinos.loc[6, 'tipo_destino'] = 'zona_canarias'
df_destinos.loc[7:62, 'tipo_destino'] = 'circuitos_culturales'
df_destinos.loc[63:84, 'tipo_destino'] = 'turismo_naturaleza'
df_destinos.loc[85:99, 'tipo_destino'] = 'capitales_provincia'
df_destinos.loc[100:, 'tipo_destino'] = 'viaje_ceuta_melilla'

df_destinos = df_destinos[['id_destino', 'destino', 'tipo_destino']]
df_destinos.loc[101]

df_destinos

df_precios = pd.DataFrame({
    'id_precio': np.random.randint(1,100,16)
})
df_precios.index = range(1, len(df_precios) + 1)
df_precios['id_precio'] = df_precios.index


df_precios.loc[:4, 'tipo_destino'] = 'zona_costera'
df_precios.loc[5:8, 'tipo_destino'] = 'zona_baleares'
df_precios.loc[9:12, 'tipo_destino'] = 'zona_canarias'
df_precios.loc[13, 'tipo_destino'] = 'circuitos_culturales'
df_precios.loc[14, 'tipo_destino'] = 'turismo_naturaleza'
df_precios.loc[15, 'tipo_destino'] = 'capitales_provincia'
df_precios.loc[16, 'tipo_destino'] = 'viaje_ceuta_melilla'

duraciones = [7,9,7,9,7,9,7,9,7,9,7,9,5,4,3,4]
df_precios['duracion'] = duraciones
df_precios['transporte'] = 1

for i in range(1, min(13, len(df_precios)), 2):
    df_precios.loc[i:i+1, 'transporte'] = 1

for i in range(2, min(13, len(df_precios)), 4):
    df_precios.loc[i:i+1, 'transporte'] = 0

suplemento_hab_indv = [22,22,22,22,22,22,22,22,24,24,24,24,26,26,26,26]
df_precios['sup_hab_ind'] = suplemento_hab_indv

precios = [228.93, 253.65, 210.72, 290.07, 267.63, 253.77, 210.47, 331.49,
           355.30, 253.65, 210.39, 435.95, 293.16, 286.82, 124.68, 286.82]

df_precios['precio'] = precios

df_precios

df_viajes = pd.DataFrame({
    'id_viaje': np.random.randint(1,5,5000)
})
df_viajes.index = range(1, len(df_viajes) + 1)
df_viajes['id_viaje'] = df_viajes.index

df_viajes['destino'] = None
for i in df_viajes.index:
    df_viajes['destino'][i] = random.choice(destinos)


mapeo_ids = df_destinos.set_index('destino')['id_destino']
df_viajes['id_destino'] = df_viajes['destino'].map(mapeo_ids)

mapeo_tipo = df_destinos.set_index('destino')['tipo_destino']
df_viajes['tipo_destino'] = df_viajes['destino'].map(mapeo_tipo)

df_viajes['id_precio'] = 1
for i in df_viajes.index:
    if df_viajes['tipo_destino'][i] == 'turismo_naturaleza':
        df_viajes['id_precio'][i] = 14
    elif df_viajes['tipo_destino'][i] == 'circuitos_culturales':
        df_viajes['id_precio'][i] = 13
    elif df_viajes['tipo_destino'][i] == 'capitales_provincia':
        df_viajes['id_precio'][i] = 15
    elif df_viajes['tipo_destino'][i] == 'viaje_ceuta_melilla':
        df_viajes['id_precio'][i] = 16
    elif df_viajes['tipo_destino'][i] == 'zona_canarias':
        df_viajes['id_precio'][i] = np.random.choice([9,10,11,12])
    elif df_viajes['tipo_destino'][i] == 'zona_baleares':
        df_viajes['id_precio'][i] = np.random.choice([5,6,7,8])
    elif df_viajes['tipo_destino'][i] == 'zona_costera':
        df_viajes['id_precio'][i] = np.random.choice([1,2,3,4])

df_viajes = df_viajes[['id_viaje', 'id_destino', 'id_precio']]

df_viajes

df_destinos.to_csv('destinos.csv')

df_precios.to_csv('precios.csv')

df_viajes.to_csv('viajes.csv')

