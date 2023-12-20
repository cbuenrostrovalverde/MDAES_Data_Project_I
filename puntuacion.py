from creacióndelosValoresRandomDeLasVariables import df 

def puntosEdad(edad):
    return

def puntosDiscapacidad(discapacidad):
    return

def puntosIrpf(irpf):
    return

def puntosPension(pension):
    return

def puntosFamiliaNumerosa(familiaNumerosa):
    return

def puntosListaEspera(listaEspera):
    return

def puntosrepeticionDestinos(repeticionDestinos):
    return

def puntosEstadoCivil(estadoCivil):
    return

def puntosPContributiva(pensionContributiva):
    return

def puntosparticipacionanyosanteriores(participacion):
    return

def puntosVehiculo(Vehiculo):
    return

def puntosCosteViaje(coste):
    return

def puntosHuellaCarbono(huella):
    return

def puntosHabitacionIndividual(habitacionIndividual):
    return

def puntosMobilidad(mobilidad):

    
    return

def puntosestadoSaludud(estado):
    
    
    return

for indice, fila in df.iterrows():
    df.at[indice, 'Score'] = puntosEdad(fila['Edad']) + puntosDiscapacidad(fila['Discapacidad']) +\
          puntosIrpf(fila['IRPF'])+ puntosPension(fila['Familia_numerosa'])+ puntosListaEspera(fila['Lista espera'])\
            +puntosrepeticionDestinos(fila['Repeticion destinos']) + puntosEstadoCivil(fila['Estado civil'])+\
            puntosPContributiva(fila['P.Contributiva'])+puntosparticipacionanyosanteriores(fila['Participación últimos dos años'])+\
            puntosVehiculo(fila['Vehiculo (S/N)']) + puntosHabitacionIndividual(fila['Habitacion Individual'])+\
            puntosMobilidad(fila['Mobilidad'])+puntosestadoSaludud(fila['Estado de Salud'])
    