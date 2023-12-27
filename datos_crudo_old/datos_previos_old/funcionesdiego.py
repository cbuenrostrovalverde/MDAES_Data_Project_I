
# for indice, fila in df.iterrows():



        import pandas as pd

for indice, fila in df.iterrows():
 def total_puntos():
    score_total = 0

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
    def discapacidad (tipo):
       score = 10
       if df['Discapacidad'] == 0:
        score = 0
       else: 
        score = 10
        
        return score


  


  ###hay que cambiar para que la base de datos ponga 0 si no es familia numero y si es familia numerosa 1, familia numerosa especial 2     
#def familia_numerosa():
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

### VER SI DAMOS SCORE Y CUANTO Y REVISAR PORQUE NO SABEMOS COMO ENFOCARLA

  
        

    

def funcionVehiculoPropio(vehiculo):
    score=0
    if df['Vehiculo']==0:
        score+=20
    return score

#def funcionHabitacionIndividual(habitacion):
    score=0
    if df['Hab_ind']==0:
        score=5
    return score

### en la tabla años_ant_viajando creo que deberíamos cambiar a True o False y 
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
