import sys

def esParOImpar(int:num):
    if num % 2 == 0:
        EsPar = True
    else:
        EsPar = False
    return EsPar

while True:
    
    try:
        num = int(input('Introduce un numero para verificar si es par o impar: '))
        if num < 1:
            print('Introduce un numero mayor a 1.', file=sys.stderr)
        else:
            break
    except ValueError as error:
            print(error, 'Introduce un numero entero.', file=sys.stderr)


                  
par = esParOImpar(num)
print(par)