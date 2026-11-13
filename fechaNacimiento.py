import sys

print('Programa que devuelve tu fecha de nacimiento en formato de dd/mm/aa\n')
while True:
    try:
        año = int(input('Introduce un año: '))
        if 1900 <= año <= 2026: break
    except ValueError as error:
        print(error, 'Introduce un numero entero que este dentro del rango [1900 a 2026].', file=sys.stderr)
        
if año % 400 == 0:
    esBisiesto = True 
else:
    esBisiesto = False
    
while True:
    try:
        mes = int(input('Introduce un mes: '))
        if 1 <= mes <= 12: break
    except ValueError as error:
        print(error, 'Introduce un numero entero que este dentro del rango [1 a 12].', file=sys.stderr)

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        numDia = 31
    case 4 | 5 | 9 | 6 | 11:
        numDia = 30
    case 2:
        if esBisiesto == False: numDia = 28
        else: numDia = 29
    case _:
        print('Introduce un mes válido.')

while True:
    try:
        dia = int(input('Introduce un dia: '))
        if 1 <= dia <= numDia:
            break
    except ValueError as error:
        print(error, f'Introduce un numero entero que este dentro del rango [1 a {numDia}].', file=sys.stderr)
        

print(f'{dia:02d}/{mes:02d}/{año % 100:02d}')

# principales caracteristicas de la programacion orientada a objetos
# abstraccion
# encapsulamiento
# ocultacion
# polimorfismo
# herencia
