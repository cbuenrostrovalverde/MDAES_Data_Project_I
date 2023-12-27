CREATE TABLE IF NOT EXISTS años_ant (
    id_solicitante SERIAL PRIMARY KEY,
    lista_espera VARCHAR(10),
    años_ant_viajado int,
    num_max_viaje_por_temp int
);

CREATE TABLE IF NOT EXISTS caract (
    id_solicitante SERIAL PRIMARY KEY,
    sexo VARCHAR(10),
    edad int,
    trabajo VARCHAR (20),
    años_trabajados int,
    movilidad VARCHAR(10),
    discapacidad boolean,
    enfermedad boolean
);

CREATE TABLE IF NOT EXISTS datos (
    id_solicitante SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR (50)
);

CREATE TABLE IF NOT EXISTS destinos (
    id_destino SERIAL PRIMARY KEY,
    destino VARCHAR(20),
    tipo_destino VARCHAR (20)
);

CREATE TABLE IF NOT EXISTS fam_num (
    id_solicitante SERIAL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR (20),
    familia_numerosa boolean,
    edad_hijo int,
    trabaja_hijo boolean
);

CREATE TABLE IF NOT EXISTS habitacion (
    id_solicitante SERIAL PRIMARY KEY,
    hab_ind boolean
);
