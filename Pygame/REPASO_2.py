import pygame
from sys import exit
pygame.init()
y = 100
NEGRO = (0, 0, 0)
CREMA = (100, 100, 100)
AMARILLO = (100, 100, 0)
RESOLUCION = (800, 800)
PANTALLA = pygame.display.set_mode(RESOLUCION)
PANTALLA.fill(NEGRO)
pygame.display.set_caption("SANDIA")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit("Adiós")

    for x in range(100, 701, 50):
        pygame.draw.circle(PANTALLA, AMARILLO, (x, y), 20)
        if x == 700:
            if y < 700:
                y += 100
            elif y >= 700:
                y -= 100
            else:
                break
        else:
            continue
    pygame.display.flip()