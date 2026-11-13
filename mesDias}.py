print('Algoritmo que te indica el numero dias que tiene ese mes que introduzcas')

while True:
    año = int(input("Introduce un año: "))
    if 2026 >= año > 1582:
        if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
            esBisiesto = True
            break
while True:
    mes = int(input("Introduce un mes: "))
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                print('Tu mes tiene 31 dias')
        case 4 | 5 | 9 | 6 | 11:
                print('Tu mes tiene 30 dias')
        case 2:
            if esBisiesto == False:
                print('Tu mes tiene 28 dias')
            else:
                print('Tu mes tiene 29 dias')
        case _:
            print('Introduce un mes válido.')
            
                
#             
        
    
        
