def puntosEdad():
    score_total = 0
    score = 0
    if df['Edad'] < 60 :
        score = 1
    elif df['Edad'] == 60 :
        score = 2
    elif 61 < df['Edad'] < 78:
        score = 2
    for i in range (df['Edad']-61):
        score += 1
    else:
        score = 20  
    return score

# Falta trabajo (Pero no vemos que sea importante)


## la columna de la tabla se llama mobilidad, hay que cambiar y poner el nombre bien
def puntosMovilidad(movilidad):
    score = 0
    limitada = 'limitada'
    media = 'media'
    perfecta = 'perfecta'
    if df['Movilidad'] == limitada:
        score+=5
    elif df['Movilidad'] == media:
        score+=3
    elif df['Movilidad'] == perfecta:
        score +=2
    return score

# Discapacidad

def discapacidad (tipo):
    score = 10
    if df['Discapacidad'] == 0:
        score = 0
    else: 
        score = 10
    
    return score

## con eso otorgar puntuacion HAY QUE ESTABLECER CUANTOS PUNTOS DAMOS 


def puntosEnfermedad(enfermedad):
    score = 0
    terminal = "terminal"
    normal = "normal"
    if df['Enfermedad'] == terminal:
        score +=8
    elif df['Enfermedad'] == normal:
        score +=2
    return score

### VER SI DAMOS SCORE Y CUANTO Y REVISAR PORQUE NO SABEMOS COMO ENFOCARLA

def funcionVehiculoPropio(vehiculo):
    score=0
    if df['Vehiculo']==0:
        score+=20
    return score


# Domicilio hay algo que podamos evaluar???


  ###hay que cambiar para que la base de datos ponga 0 si no es familia numero y si es familia numerosa 1, familia numerosa especial 2     
def familia_numerosa():
    score = 0
    edad_hijo = df['edad_hijo']
    trabaja_hijo = df['trabaja_hijo']

    if familia_numerosa == 0:
        score = 0
    elif familia_numerosa == 1:
        if edad_hijo is not None and edad_hijo < 26:
            if trabaja_hijo is None or trabaja_hijo == 0:
                score = 5
    else:
        score = 10

    return score

# Habitación Individual:

def funcionHabitacionIndividual(habitacion):
    score=0
    if df['Hab_ind']==0:
        score=5
    return score


# Renta
df=0

a=1050*14
b=1200*14
c=1350*14
d=1500*14
e=1650*14
f=1800*14
g=1950*14
h=2100*14

def puntosEdad(edad):
    score=0
    if a<df['edad']<=b:
        score=35
    elif b<df['edad']<=c:
        score=30
    elif c<df['edad']<=d:
        score=25
    elif d<df['edad']<=e:
        score=20
    elif e<df['edad']<=f:
        score=15
    elif f<df['edad']<=g:
        score=10
    elif g<df['edad']<=h:
        score=5
    else:
        score=0
    return score

# lista Espera

def funcionListaEspera(listaEspera):
    score=0
    if df[listaEspera]== 1:
        score+=50
    return score

#Lista Espera:

def funcionListaEspera(listaEspera):
    score=0
    if df['Años Anteriores']== 1:
        score+=50
    return score

# Numero Max viajes

def maxViajes():
    score=0
    if df['Numero Maximo Viajes']==3:
        score+=20
    elif df['Numero Maximo Viajes']==2:
        score+=30
    elif df['Numero Maximo Viajes']==1:
        score+=30
    else:
        score=0