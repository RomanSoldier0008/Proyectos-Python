import pygame
from sys import exit

# COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

TAMANO = (800, 800)
VENTANA = pygame.display.set_mode(TAMANO)

# BUCLE INFINITO
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit("SALISTE")

    # COLOR DE FONDO
    VENTANA.fill(BLANCO)

    # DIBUJOS
    for i in range(200, 401, 200):
        pygame.draw.rect(VENTANA, VERDE, (i, 100, 100, 100))
        pygame.draw.rect(VENTANA, VERDE, (i, 300, 100, 100))
    pygame.draw.rect(VENTANA, NEGRO, (300, 0, 100, 100))
    pygame.draw.rect(VENTANA, VERDE, (300, 200, 100, 100))

    # ACTUALIZAR PANTALLA
    pygame.display.flip()