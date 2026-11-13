import sys
sys.path.append('../funcionCalcularAreaTriangulo')

from calcularAreaTriangulo import CalcularAreaTriangulo as cat

try:
    print(cat(25, 65))
    
except Exception as error:
    print(f'Error: {error} ...')