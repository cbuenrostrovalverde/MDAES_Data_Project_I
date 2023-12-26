
'''
La valoración de esta variable se realizará de la siguiente forma: 
a los menores de 60 años, 1 punto; con 60 años 2 puntos, y un punto más por cada año cumplido hasta alcanzar los 20 puntos con 78 años cumplidos. 
A las personas que superen los 78 años se les asignará igualmente el máximo de 20 puntos.
'''



def puntosEdad(edad):
    score = 0
    if edad < 60 :
     score = 1
    elif edad == 60 :
     score = 2
    elif 61 < edad < 78:
       score = 2
       for i in range (edad-61):
          score += 1
    else:
      score = 20  
        
    return score

print(puntosEdad(73))
