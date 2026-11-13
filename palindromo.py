import sys

while True: 
    try:
        cadena = str(input('Introduce una palabra o frase para determinar si es un palíndromo: '))
        if len(cadena) < 2:
            print('Introduce al menos 2 caracteres.', file=sys.stderrr)
        else:
            # "Limpiamos" el texto.
            cadena = cadena.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü", "u").replace(",", "")
            break
    except ValueError as error:
        print(error, 'Introduce por favor una palabra o frase, de al menos 2 caracteres.', file=sys.stderr)
        
# Aqui verificamos si la cadena es un palindromo, si dividiendolo en 2 da 0 si es par, de lo contrario tiene una letra central.
cadenaAlrevez = ""
for i in range(len(cadena),0,-1):
    cadenaAlrevez = cadenaAlrevez + cadena[i-1:i]
# print(cadena)
# print(cadenaAlrevez)
print('Es un palindromo' if cadena == cadenaAlrevez else 'No es palindromo')