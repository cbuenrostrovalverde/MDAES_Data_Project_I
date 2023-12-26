# Estado civil(no veo que sea una variable a evaluar, pero si opináis lo contrario decidimos)
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