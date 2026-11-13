import random
import sys
import pygame

# Inicializar Pygame.
pygame.init()

# Dimensiones de la ventana y colores.
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Blackjack - 1 Jugador vs Banca (Pygame)")

VERDE_MESA = (30, 70, 32)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 204, 0)
ROJO = (220, 50, 50)
VERDE_BOTON = (46, 125, 50)
GRIS_BOTON = (180, 180, 180)

# Fuentes.
FUENTE_TITULO = pygame.font.SysFont("Rockwell", 28, bold=True)
FUENTE_TEXTO = pygame.font.SysFont("Arial", 18, bold=True)
FUENTE_CARTA = pygame.font.SysFont("Arial", 16)


def crear_baraja():
    palos = ('♥', '♦', '♣', '♠')
    denominaciones = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    )
    nueva_baraja = []
    for palo in palos:
        for valor in denominaciones:
            nueva_baraja.append({"valor": valor, "palo": palo})
    
    if not nueva_baraja:
        raise ValueError("Error crítico: La baraja no pudo ser creada.")
        
    random.shuffle(nueva_baraja)
    return nueva_baraja


def calcular_puntos(mano):
    # Validar que se introduzca una mano válida (tipo lista).
    if not isinstance(mano, list):
        raise TypeError(f"Se esperaba una lista para la mano, pero se recibió: {type(mano)}")
    
    if len(mano) == 0:
        raise ValueError("La mano está vacía, no se pueden calcular puntos.")

    puntos = 0
    ases = 0
    for carta in mano:
        if not isinstance(carta, dict) or "valor" not in carta:
            raise ValueError(f"Formato de carta inválido en la mano: {carta}")
            
        val = carta["valor"]
        if val in ("J", "Q", "K"):
            puntos += 10
        elif val == "A":
            puntos += 11
            ases += 1
        elif val.isdigit() or (val.startswith('-') and val[1:].isdigit()): # Soporte por si acaso
            puntos += int(val)
        else:
            raise ValueError(f"Valor de carta desconocido: '{val}'")

    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1

    return puntos


def es_blackjack_natural(mano):
    if not isinstance(mano, list):
        raise TypeError("La mano proporcionada debe ser una lista.")
        
    if len(mano) == 2:
        valores = [c["valor"] for c in mano]
        tiene_as = "A" in valores

        tiene_diez = False
        for v in valores:
            if v in ("10", "J", "Q", "K"):
                tiene_diez = True
                break

        return tiene_as and tiene_diez
    return False


def reiniciar_juego(juego):
    if not isinstance(juego, dict):
        raise TypeError("El objeto 'juego' debe ser un diccionario.")
        
    juego["baraja"] = crear_baraja()
    juego["mano_jugador"] = [juego["baraja"].pop(), juego["baraja"].pop()]
    juego["mano_dealer"] = [juego["baraja"].pop(), juego["baraja"].pop()]
    juego["mensaje"] = ""

    bj_jugador = es_blackjack_natural(juego["mano_jugador"])
    bj_dealer = es_blackjack_natural(juego["mano_dealer"])

    if bj_jugador or bj_dealer:
        juego["estado"] = "fin"
        if bj_jugador and bj_dealer:
            juego["mensaje"] = "¡Empate! Ambos tienen Blackjack natural."
        elif bj_jugador:
            juego["mensaje"] = "¡Blackjack natural! ¡Has ganado!"
        else:
            juego["mensaje"] = "La banca tiene Blackjack natural. Gana la banca."
    else:
        juego["estado"] = "jugando"


def pedir_carta(juego):
    if not isinstance(juego, dict) or "estado" not in juego or "baraja" not in juego:
        raise ValueError("El diccionario del juego está incompleto o es inválido.")
        
    if juego["estado"] != "jugando":
        return
        
    if len(juego["baraja"]) == 0:
        raise IndexError("No quedan más cartas en la baraja para repartir.")
    
    juego["mano_jugador"].append(juego["baraja"].pop())
    
    puntos = calcular_puntos(juego["mano_jugador"])
    
    if puntos > 21:
        juego["estado"] = "fin"
        juego["mensaje"] = "Te pasaste de 21. ¡Gana la banca!"
    else:
        # Calculamos los puntos sumando los ases estrictamente como 11 (sin reducción).
        puntos_brutos = 0
        ases_en_mano = 0
        for carta in juego["mano_jugador"]:
            val = carta["valor"]
            if val in ("J", "Q", "K"):
                puntos_brutos += 10
            elif val == "A":
                puntos_brutos += 11
                ases_en_mano += 1
            else:
                puntos_brutos += int(val)
        
        # Si la suma bruta superaba 21, pero el puntaje real es <= 21, el As nos salvó.
        if puntos_brutos > 21 and ases_en_mano > 0:
            juego["mensaje"] = "¡Salvado por el AS!"
        else:
            juego["mensaje"] = ""

def evaluar_ganador(juego):
    if not isinstance(juego, dict):
        raise TypeError("El objeto 'juego' debe ser un diccionario.")
        
    puntos_j = calcular_puntos(juego["mano_jugador"])
    puntos_d = calcular_puntos(juego["mano_dealer"])

    if puntos_d > 21:
        juego["mensaje"] = "La banca se pasó de 21. ¡Has ganado!"
    elif puntos_j > puntos_d:
        juego["mensaje"] = "¡Has ganado con más puntos!"
    elif puntos_j < puntos_d:
        juego["mensaje"] = "Gana la banca por mayor puntuación."
    else:
        juego["mensaje"] = "¡Empate!"


def plantarse(juego):
    if not isinstance(juego, dict):
        raise TypeError("El objeto 'juego' debe ser un diccionario.")
        
    if juego["estado"] != "jugando":
        return
    juego["estado"] = "dealer_turno"
    
    while calcular_puntos(juego["mano_dealer"]) < 17:
        if len(juego["baraja"]) == 0:
            raise IndexError("La baraja se quedó sin cartas durante el turno del dealer.")
        juego["mano_dealer"].append(juego["baraja"].pop())

    juego["estado"] = "fin"
    evaluar_ganador(juego)


# --- Interfaz Gráfica con Pygame ---
def dibujar_carta(superficie, x, y, carta, oculta=False):
    # Validación estricta de datos de entrada.
    if superficie is None:
        raise ValueError("La superficie de Pygame no puede ser None.")
    if not isinstance(carta, dict) or "valor" not in carta or "palo" not in carta:
        raise ValueError(f"Datos de carta inválidos para dibujar: {carta}")

    rect_carta = pygame.Rect(x, y, 70, 100)
    pygame.draw.rect(superficie, BLANCO, rect_carta, border_radius=5)
    pygame.draw.rect(superficie, NEGRO, rect_carta, 2, border_radius=5)

    if oculta:
        rect_dorso = pygame.Rect(x + 5, y + 5, 60, 90)
        pygame.draw.rect(superficie, (150, 0, 0), rect_dorso, border_radius=3)
    else:
        # Validación de color correcta usando tupla.
        if carta["palo"] in ('♥', '♦'):
            texto_val = FUENTE_CARTA.render(str(carta["valor"]), True, ROJO)
            texto_palo = FUENTE_CARTA.render(str(carta["palo"]), True, ROJO)
        elif carta["palo"] in ('♣', '♠'):
            texto_val = FUENTE_CARTA.render(str(carta["valor"]), True, NEGRO)
            texto_palo = FUENTE_CARTA.render(str(carta["palo"]), True, NEGRO)
        else:
            raise ValueError(f"Palo de carta desconocido: '{carta['palo']}'")
            
        superficie.blit(texto_val, (x + 8, y + 8))
        superficie.blit(texto_palo, (x + 8, y + 30))


def main():
    juego = {
        "baraja": [],
        "mano_jugador": [],
        "mano_dealer": [],
        "estado": "jugando",
        "mensaje": "",
    }

    reiniciar_juego(juego)
    reloj = pygame.time.Clock()

    btn_pedir_rect = pygame.Rect(220, 500, 110, 40)
    btn_plantar_rect = pygame.Rect(345, 500, 110, 40)
    btn_reiniciar_rect = pygame.Rect(470, 500, 110, 40)

    while True:
        VENTANA.fill(VERDE_MESA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn_pedir_rect.collidepoint(pos) and juego["estado"] == "jugando":
                    pedir_carta(juego)
                elif btn_plantar_rect.collidepoint(pos) and juego["estado"] == "jugando":
                    plantarse(juego)
                elif btn_reiniciar_rect.collidepoint(pos):
                    reiniciar_juego(juego)

        # Título.
        titulo = FUENTE_TITULO.render("BLACKJACK", True, BLANCO)
        VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))

        # --- Dealer ---
        lbl_dealer = FUENTE_TEXTO.render("Mano del Dealer:", True, BLANCO)
        VENTANA.blit(lbl_dealer, (50, 80))

        for i, carta in enumerate(juego["mano_dealer"]):
            oculta = (i == 1) and (juego["estado"] == "jugando")
            dibujar_carta(VENTANA, 50 + (i * 85), 110, carta, oculta)

        if juego["estado"] == "jugando":
            puntos_d_str = "Puntos: ?"
        else:
            puntos_d_str = f"Puntos: {calcular_puntos(juego['mano_dealer'])}"
        lbl_puntos_d = FUENTE_TEXTO.render(puntos_d_str, True, AMARILLO)
        VENTANA.blit(lbl_puntos_d, (50, 225))

        # --- Jugador ---
        lbl_jugador = FUENTE_TEXTO.render("Tu Mano:", True, BLANCO)
        VENTANA.blit(lbl_jugador, (50, 275))

        for i, carta in enumerate(juego["mano_jugador"]):
            dibujar_carta(VENTANA, 50 + (i * 85), 305, carta)

        puntos_j_str = f"Puntos: {calcular_puntos(juego['mano_jugador'])}"
        lbl_puntos_j = FUENTE_TEXTO.render(puntos_j_str, True, AMARILLO)
        VENTANA.blit(lbl_puntos_j, (50, 420))

        # --- Mensaje de Resultado ---
        if juego["mensaje"]:
            lbl_msj = FUENTE_TITULO.render(juego["mensaje"], True, (0, 255, 204))
            VENTANA.blit(lbl_msj, (ANCHO // 2 - lbl_msj.get_width() // 2, 455))

        # --- Dibujar Botones ---
        color_pedir = VERDE_BOTON if juego["estado"] == "jugando" else GRIS_BOTON
        pygame.draw.rect(VENTANA, color_pedir, btn_pedir_rect, border_radius=5)
        txt_pedir = FUENTE_TEXTO.render("Pedir", True, BLANCO)
        VENTANA.blit(txt_pedir, (btn_pedir_rect.centerx - txt_pedir.get_width() // 2, btn_pedir_rect.centery - txt_pedir.get_height() // 2))

        color_plantar = ROJO if juego["estado"] == "jugando" else GRIS_BOTON
        pygame.draw.rect(VENTANA, color_plantar, btn_plantar_rect, border_radius=5)
        txt_plantar = FUENTE_TEXTO.render("Plantarse", True, BLANCO)
        VENTANA.blit(txt_plantar, (btn_plantar_rect.centerx - txt_plantar.get_width() // 2, btn_plantar_rect.centery - txt_plantar.get_height() // 2))

        pygame.draw.rect(VENTANA, (40, 116, 166), btn_reiniciar_rect, border_radius=5)
        txt_reiniciar = FUENTE_TEXTO.render("Reiniciar", True, BLANCO)
        VENTANA.blit(txt_reiniciar, (btn_reiniciar_rect.centerx - txt_reiniciar.get_width() // 2, btn_reiniciar_rect.centery - txt_reiniciar.get_height() // 2))

        pygame.display.flip()
        reloj.tick(60)


if __name__ == "__main__":
    main()