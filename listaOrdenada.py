import random
import sys

while True:
    try:
        num = int(input('Introduce la cantidad de numeros a obtener: '))
        if num > 0:
            break
        else:
            print('Introduce un numero entero.', file=sys.stderr)
    except ValueError as error:
        print(f'Error: {error}. Introduce un numero entero', file=sys.stderr)

lista = [random.randint(1,9) for i in range(1,num+1)]

print(lista)
lista.sort()
print(lista)

listaOrdenada = []

# for i in range(0, len(lista)-1):
#     if lista[i] == lista[i+1]:
#         continue 
#     else:
#         listaOrdenada.append(lista[i])

for numero in lista:
    if not listaOrdenada or numero != listaOrdenada[-1]:
        listaOrdenada.append(numero)

print(listaOrdenada)

