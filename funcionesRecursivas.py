# Elabore una funcion recursiva que calcule el producto de dos números enteros
def multiplicar(int: a,b) -> int:
#     if not isinstance(a, int):
#         raise ValueError('Introduce un numero entero.')
#     if not isinstance(b, int):
#         raise ValueError('Introduce un numero entero.')
    
    if a or b == 0:
        return 0
    if b > 0:
        return multiplicar(a,b - 1) + a
    if b < 0:
        return - ProductoDeDosNumerosEnteros(a,-b)
 
a,b = int(input('Introduce dos numeros enteros: ')), int(input('Introduce dos numeros enteros: '))
ProductoDeDosNumerosEnteros(a,b)

#**************************************************************

#Elabore una funcion recursiva que calcule a ^ b donde a = R (Real) y b = Z (Entero)
def FuncionRec(x:float, y:int) -> float
    if y == 0:
        return 1
    return FuncionRec * (x ** y-1)

# a^-b = 1/a^b

#*********************************************************************

# Elabore una funcion recursiva que calcule C(n,r)
def FuncionRec2(n,r)
    if r or n and r == 0:
    
# C(n,r) = n!/r!(n-r)!
# 0 <= r <= n

#********************************************************************
# Tarea: Elabora una funcion que, dado un indice i, obtenga fi
# a) Iterativa
# b) Recursiva