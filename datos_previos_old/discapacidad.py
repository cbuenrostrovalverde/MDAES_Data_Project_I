
'''
Situación de discapacidad
Si la persona solicitante tiene un grado de discapacidad ≥33% se valorará con 10 puntos
'''

def discapacidad (tipo):
    score = 10
    if tipo == 0:
     score = 0
    else:
     score = 10
     

    return score


conclusion = (discapacidad(0))
print(conclusion)


