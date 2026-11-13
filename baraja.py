import random
import pygame

pygame.init()

def CrearBaraja():
    """Crea una baraja de 52 cartas estándar (4 palos y 13 denominaciones)."""
    PALOS = ('♥','♦','♣','♠')
    DENOMINACIONES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    
    # Combinamos cada palo con cada denominación usando un diccionario
    baraja = []
    for palo in PALOS:
        for valor in DENOMINACIONES:
            baraja.append({'Valor': valor, 'Palo': palo})
            
    return baraja

baraja = crear_baraja()

def Barajear(baraja):
    return random.shuffle(baraja)

def EvaluarPuntos(mano)

