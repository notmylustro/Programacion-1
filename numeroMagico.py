import random
import sys

try:
    num = int(input('Introduce un numero entre 1 al 100: '))
except ValueError as error:
    print('Error:', error, file=sys.stderr)
numMagico = random.randint(1, 100)

extremoMayor = 100
extremoMenor = 0

while num != numMagico:
    num = int(input('Introduce un numero entre 1 al 100: '))
    while not extremoMenor < num < extremoMayor:
        if num < numMagico:
            extremoMayor = num - 1
            print(f'Tu numero es menor a el número magico, se encuentra entre {extremoMenor} y {extremoMayor}')
        elif num > numMagico:
            extremoMenor = num + 1
            print(f'Tu numero es menor a el número magico, se encuentra entre {extremoMenor} y {extremoMayor}')
        else:
            print('Q vrg hiciste')
print(f'Lo lograste el numero magico es {numMagico}')



    
    