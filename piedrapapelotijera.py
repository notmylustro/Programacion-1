import random 

opUsuario = int(input('Qué vas a jugar (1) piedra, (2) papel o (3) tijera: '))
opMaquina = random.randint(1,3)

if  opUsuario == opMaquina:
       print("Empataste")
elif opUsuario == 1 and opMaquina == 3 or opUsuario == 2 and opMaquina == 1 or opUsuario == 3 and opMaquina == 2:
            print('Ganaste!')
else:
            print('Perdiste')
       
