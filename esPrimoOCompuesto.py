"""
Archivo: esPrimoOCompuesto.py
Descripción: Indentifica si el número introduncido es primo o compuesto.
Autor: JMLV
Fecha: 15/10/2026
"""
import math

num = int(input('Introduce un numero entero mayor a 1: '))

while True:
    num = int(input('Introduce un numero entero mayor a 1: '))
    if num >= 2:
       break
        
raiz = math.sqrt(num)
divisor = 2

while divisor <= raiz:
    if num % divisor == 0:
        break
    divisor += 1
    
if divisor == 0:
    print('Tu numero es primo.')
else:
    print('Tu numero es compuesto.')
    
# print('Es primo' if divisor > raiz else 'Es compuesto')