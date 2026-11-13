try:
    print("Hola"[20])
except BaseException:
    print('Error general')
except IndexError:
    print('Errosito')