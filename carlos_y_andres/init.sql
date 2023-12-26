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

CREATE TABLE IF NOT EXISTS pensiones (
    id_solicitante SERIAL PRIMARY KEY,
    renta int,
    pension int,
    tipo_pension VARCHAR (10),
    estado_civil VARCHAR (10),
    pension_conyuge int
);

CREATE TABLE IF NOT EXISTS precios (
    id_precio SERIAL PRIMARY KEY,
    tipo_destino VARCHAR (25),
    duracion int,
    transporte boolean,
    sup_hab_ind int,
    precio int
);

CREATE TABLE IF NOT EXISTS solicitudes (
    id_solicitante SERIAL PRIMARY KEY,
    id_viaje SERIAL
);

CREATE TABLE IF NOT EXISTS viajero (
    id_solicitante SERIAL PRIMARY KEY,
    domicilio VARCHAR (30),
    vehiculo boolean
);

CREATE TABLE IF NOT EXISTS viajes (
    id_viaje SERIAL,
    id_destino SERIAL PRIMARY KEY,
    id precio SERIAL
);