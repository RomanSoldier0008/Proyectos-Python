import pygame

pygame.init()

# COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VIOLETA = (100, 0, 100)
CREMA = (250, 160, 160)

# PANTALLA
RESOLUCION = (1250, 800)
pantalla = pygame.display.set_mode(RESOLUCION)
reloj = pygame.time.Clock()

# NOMBRE Y COLOR DE FONDO
pygame.display.set_caption("PONG")

# ANCHO Y ALTO DE LAS PALETAS
PLAYER_ANCHO = 20
PLAYER_ALTO = 400

# COORDENADAS Y VELOCIDAD DEL JUGADOR 1
coordenada_x_player_1 = 20
coordenada_y_player_1 = 200
velocidad_en_y_jugador_1 = 0

# COORDENADAS Y VELOCIDAD DEL JUGADOR 2
coordenada_x_player_2 = 1210
coordenada_y_player_2 = 200
velocidad_en_y_jugador_2 = 0

# COORDENADAS DE LA PELOTA
coordenada_x_pelota = 625
coordenada_y_pelota = 400
velocidad_pelota_x = 3
velocidad_pelota_y = 3
contador = 2
numero_de_colisiones = 0
contador_2 = 0

seguir_jugando = True
while seguir_jugando:
    if coordenada_y_pelota >= 800 or coordenada_y_pelota <= 0:
        velocidad_pelota_y *= -1
    if coordenada_x_pelota >= 1250 or coordenada_x_pelota <= 0:
        coordenada_x_pelota = 625
        coordenada_y_pelota = 400
        velocidad_pelota_x *= -1
        velocidad_pelota_y *= -1
        if velocidad_pelota_x > 0:
            velocidad_pelota_x = 3
        elif velocidad_pelota_x < 0:
            velocidad_pelota_x = -3

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seguir_jugando = False
        if evento.type == pygame.KEYDOWN:
            # JUGADOR 1
            if evento.key == pygame.K_w:
                velocidad_en_y_jugador_1 = -4
            if evento.key == pygame.K_s:
                velocidad_en_y_jugador_1 = 4
            # JUGADOR 2
            if evento.key == pygame.K_UP:
                velocidad_en_y_jugador_2 = -4
            if evento.key == pygame.K_DOWN:
                velocidad_en_y_jugador_2 = 4
        if evento.type == pygame.KEYUP:
            # JUGADOR 1
            if evento.key == pygame.K_w:
                velocidad_en_y_jugador_1 = 0
            if evento.key == pygame.K_s:
                velocidad_en_y_jugador_1 = 0
            # JUGADOR 2
            if evento.key == pygame.K_UP:
                velocidad_en_y_jugador_2 = 0
            if evento.key == pygame.K_DOWN:
                velocidad_en_y_jugador_2 = 0

    # MODIFICA LAS COORDENADAS PARA DAR MOVIMIENTO A LOS JUGADORES Y LA PELOTA
    coordenada_y_player_1 += velocidad_en_y_jugador_1
    coordenada_y_player_2 += velocidad_en_y_jugador_2
    coordenada_x_pelota += velocidad_pelota_x
    coordenada_y_pelota += velocidad_pelota_y

    pantalla.fill(CREMA)
    jugador_1 = pygame.draw.rect(pantalla, AMARILLO, (coordenada_x_player_1, coordenada_y_player_1,
                                                      PLAYER_ANCHO, PLAYER_ALTO))
    jugador_2 = pygame.draw.rect(pantalla, AMARILLO, (coordenada_x_player_2, coordenada_y_player_2,
                                                      PLAYER_ANCHO, PLAYER_ALTO))
    pelota = pygame.draw.circle(pantalla, BLANCO, (coordenada_x_pelota, coordenada_y_pelota), 20)
    if pelota.colliderect(jugador_1) or pelota.colliderect(jugador_2):
        velocidad_pelota_x *= -1
        numero_de_colisiones += 1
        if numero_de_colisiones == contador:
            velocidad_pelota_x += 2
            numero_de_colisiones = 0
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()