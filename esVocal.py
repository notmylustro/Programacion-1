# letras = {"a","e","i","o","u","á","é","í","ó","ú","ü"}
# while True:
#     respuesta = input("Introduce una letra para verificar si es vocal: ").lower()
#     if len(respuesta) == 1:
#         if respuesta in letras:
#                     print("Esa letra es una vocal.")
#         else:
#             print("Eso no e una vocal.")
#         #break 
#     elif (respuesta) == 0:
#         print("Porfavor introduce una .")
#     else:
#         print("Introduce un caracter por favor.")
#         
while True:
    respuesta = input("Introduce una letra para verificar si es vocal: ").lower()
    if len(respuesta) == 1:
        match respuesta:
            case "a" | "e" | "i" | "o" | "u" | "á" | "é" | "í" | "ó" | "ú" | "ü":
                print("Esa letra es una vocal.")
            case _:
                print("Eso no es una vocal.")
    else:
        print("Introduce un caracter por favor.")