'''
Existen dos categorías de familia numerosa: Familia Numerosa General: 
familias de hasta 4 hijos (*) Familia Numerosa de Categoría Especial: familias con 5 o más hijos.
'''
import df from base_datos_nueva.ipynb

# tipo 0 familia no numerosa 0putnos
# tipo 1 familia numerosa normal 5 putnos
# tipo 2 familia numerosa especial 10 putnos

def familia_numerosa(familia_numerosa):
    score = 0
    edad_hijo=df['edad_hijo']
    if familia_numerosa == 0:
        score = 0
    elif familia_numerosa == 1 :
        if edad_hijo != None and edad_hijo < 26:
            if trabaja_hijo = None and trabaja_hijo == 0 
        score = 5
    else:
        score = 10

    return score


conclusion = familia_numerosa(1)
print(conclusion)    



