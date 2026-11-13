import math

# Programa para calcular area de distintas figuras.
print('''Elige una opción:
0) Salir del programa
1) Calcular el área de un tríangulo
2) Calcular  el área de un circulo
3) Calcilar el área de un rectangulo''')

opUsuario = int(input('Elección: '))
while not 0 <= opUsuario < 3:
    opUsuario = int(input('Elección: '))
    
match opUsuario:
    case 0:
        print('Adios :b')
    case 1:
        base = float(input('Introduce la base de tu triangulo: '))
        altura = float(input('Introduce la altura de tu tiangulo: '))
        print(f'El área de tu triangulo es: (base * altura) / 2 = {base * altura / 2:.2f}')
    case 2:
        radio = float(input('Introduce el radio de tu circulo: '))
        print(f'El área de tu circulo es: PI * radio^2 = {math.pi * (radio)**2:.2f}')
    case 3:
        base = float(input('Introduce la base de tu rectangulo: '))
        altura = float(input('Introduce la altura de tu rectangulo: '))
        print(f'El área de tu rectangulo es: (base * altura) = {base * altura:.2f}')