import sys
while True:
    try:
        num = int(input('Introduce un número entero, para convertirlo en asteriscos: '))
        if num < 3:
            print('Porfavor introduce un número entero mayor a 0.', file=sys.stderr)
        else:
            break 
    except ValueError as error:
        print(error, 'Porfavor introduce un número entero.', file=sys.stderr)

asteriscos = num*"*"

while True:
    try:
        num2 = int(input('¡Cuántas veces quieres repetir esa cadena? '))
        if num2 < 3:
            print('Porfavor introduce un número entero mayor a 0.', file=sys.stderr)
        else:
            break 
    except ValueError as error:
        print(error, 'Porfavor introduce un número entero.', file=sys.stderr)
print(num2*(f'{asteriscos}\n'))

print(asteriscos)
for i in range(num2):
    print("*", num*" " ,"*")
print(asteriscos)