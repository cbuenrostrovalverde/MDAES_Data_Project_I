def puntosMovilidad(movilidad):
    score = 0
    limitada = 'limitada'
    media = 'media'
    perfecta = 'perfecta'
    if movilidad == limitada:
        score+=5
    elif movilidad == media:
        score+=3
    elif movilidad == perfecta:
        score +=2
    return score
    
print(puntosMovilidad('limitada'))
print(puntosMovilidad('media'))
print(puntosMovilidad('perfecta'))

def puntosEnfermedad(enfermedad):
    score = 0
    terminal = "terminal"
    normal = "normal"
    if enfermedad == terminal:
        score +=8
    elif enfermedad == normal:
        score +=2
    return score
    
print(puntosEnfermedad("terminal"))
print(puntosEnfermedad("normal"))

