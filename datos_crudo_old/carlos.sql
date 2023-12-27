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