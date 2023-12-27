CREATE TABLE IF NOT EXISTS precios (
    id_precio SERIAL PRIMARY KEY,
    tipo_destino VARCHAR(25),
    duracion INT,
    transporte BOOLEAN,
    sup_hab_ind INT,
    precio INT
);

CREATE TABLE IF NOT EXISTS destinos (
    id_destino SERIAL PRIMARY KEY,
    destino VARCHAR(20),
    tipo_destino VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS viajes (
    id_viaje SERIAL PRIMARY KEY,
    id_destino INT,
    id_precio INT,
    FOREIGN KEY (id_destino) REFERENCES destinos (id_destino),
    FOREIGN KEY (id_precio) REFERENCES precios (id_precio)
);

CREATE TABLE IF NOT EXISTS datos (
    id_solicitante SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS años_ant (
    id_solicitante SERIAL PRIMARY KEY,
    lista_espera VARCHAR(10),
    años_ant_viajado INT,
    num_max_viaje_por_temp INT,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS caract (
    id_caract SERIAL PRIMARY KEY,
    id_solicitante INT,
    sexo VARCHAR(10),
    edad INT,
    trabajo VARCHAR(20),
    años_trabajados INT,
    movilidad VARCHAR(10),
    discapacidad BOOLEAN,
    enfermedad BOOLEAN,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS fam_num (
    id_fam_num SERIAL PRIMARY KEY,
    id_solicitante INT,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    familia_numerosa BOOLEAN,
    edad_hijo INT,
    trabaja_hijo BOOLEAN,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS habitacion (
    id_habitacion SERIAL PRIMARY KEY,
    id_solicitante INT,
    hab_ind BOOLEAN,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS pensiones (
    id_pensiones SERIAL PRIMARY KEY,
    id_solicitante INT,
    renta INT,
    pension INT,
    tipo_pension VARCHAR(10),
    estado_civil VARCHAR(10),
    pension_conyuge INT,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS viajero (
    id_viajero SERIAL PRIMARY KEY,
    id_solicitante INT,
    domicilio VARCHAR(30),
    vehiculo BOOLEAN,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante)
);

CREATE TABLE IF NOT EXISTS solicitudes (
    id_solicitud SERIAL PRIMARY KEY,
    id_solicitante INT,
    id_viaje INT,
    FOREIGN KEY (id_solicitante) REFERENCES datos (id_solicitante),
    FOREIGN KEY (id_viaje) REFERENCES viajes (id_viaje)
);
