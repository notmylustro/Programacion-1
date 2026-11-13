import sys

while True:
    try:
        j = int(input('Introduce n cantidad de elementos para determinar el máximo y mínimo: '))
        if j < 1:
            print('Introduce un numero mayor 0.')
        else:
            break 
    except ValueError as error:
        print(error, 'Porfavor introduce un numero entero.', file=sys.stderr)
        
while True:
    try:     
        for i in range(1,j):
            num = int(input(f'Introduce el #{i} numero: '))
            if num < 0 and i == j:
                
    except ValueError as error:
        print(error, 'Porfavor introduce un numero entero.', file=sys.stderr)

        
