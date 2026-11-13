import sys

while True:
    try:
        num = int(input('Introduce un numero mayor a uno para determinar si es primo o compuesto: '))
    except ValueError as error:
        print(error, 'Introduce un número entero porfavor.', file=sys.stderr)
        continue
    break
