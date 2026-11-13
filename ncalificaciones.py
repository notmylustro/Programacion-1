import sys
print('== Programa que promedia n cantidad de calificiones ==')
cantExam = int(input("Introduce la cantidad de calificaciones a promediar: "))
while cantExam < 1:
    print('Introduce una cantidad mayor a 0', file=sys.stderr)
    cantExam = int(input("Introduce la cantidad de calificaciones a promediar: "))
i = 1
califs = 0
while i <= cantExam:
    calif = float(input(f'Introduce la calificacion de tu examen #{i}: '))
    if calif <= 0  or calif > 100:
        print('Introduce una cantidad mayor a 0 y no mayor a 100', file=sys.stderr)
    else:
        i += 1
        califs += calif
        
print('Tu promedio es de: ', califs / cantExam)