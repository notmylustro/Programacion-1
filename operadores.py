# nombre = "Jose"
# edad = 21
# peso = 1/3
# #3print("Introduzca un número entero: ", end='>')
# #var = int(input("Introduzca un número entero: "))
# 
# #print(var+1)
# 
# #var = float(input("Introduzca un número real: "))
# 
# #print(var+1)
# 
# print("{:30.10s}, tienes {:^5} años y pesos {:10.3f} kg.".format(nombre, edad, peso))
# 
# print("%s, tienes %d años y pesas %e kg." % (nombre, edad, peso))
# #            ^Maximo de caracteres                ^ Numero de digitos en expansion decimal
# #print("|{:<40g}".format(edad))
# print(f"{nombre:>30.10}, tienes {edad:^5} años y pesas {peso:<5.20e} kg.")
# 
# print("%30.10s, tienes %s años y pesas %-15.2e kg." % (nombre, str(edad).center(5), peso))
# a, b = 10, 3
# 
# #print(a=b)
# print(a+b)
# print(a//b)
# print(b:=a)

x, y = 5, 3
print(f"x = {x}\ny = {y}\n")

x, y = y, x
print(f"x = {x}\ny = {y}")
