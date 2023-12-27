# minimo 565 euros mes 6784
print(6784.54/12)
# , maximo 
print(42830.29/12)

# Más 1.050 € hasta 1.200 €	35
# Más 1.200 € hasta 1.350 €	30
# Más 1.350 € hasta 1.500 €	25
# Más 1.500 € hasta 1.650 €	20
# Más 1.650 € hasta 1.800 €	15
# Más 1.800 € hasta 1.950 €	10
# Más 1.950 € hasta 2.100 €	5
# Más 2.100 €	0


# a= 1.050*12
# b=1.200*12
# c=1.350*12
# d=1.500*12
# e=1.650*12
# f=1.800*12
# g=1.950*12
# h=2.100*12
a= 13200
b=14400
c=16200
d=18000
e=19800
f=21600
g=23400
h=25200

def puntosEdad(edad):
    score=0
    if a<edad<=b:
        score=35
    elif b<edad<=c:
        score=30
    elif c<edad<=d:
        score=25
    elif d<edad<=e:
        score=20
    elif e<edad<=f:
        score=15
    elif f<edad<=g:
        score=10
    elif g<edad<=h:
        score=5
    else:
        score=0
    return score

print(puntosEdad(14000))
print(puntosEdad(15000))
print(puntosEdad(17000))
print(puntosEdad(19000))
print(puntosEdad(20000))
print(puntosEdad(22000))
print(puntosEdad(24000))
print(puntosEdad(26000))
