import pygame
from sys import exit

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
CELESTE = (0, 255, 255)
VIOLETA = (255, 0, 255)
MARRON = (124, 60, 0)
AMARILLO = (255, 255, 0)
CREMA = (255, 210, 190)

RESOLUCION = (1250, 900)
screen = pygame.display.set_mode(RESOLUCION)
TITULO_JUEGO = "Cubitos"

pygame.init()


class Juego:
    pass

    def __init__(
                 self, color_fondo,
                 pantalla,
                 cord_x_jugador_1=1000,
                 cord_y_jugador_1=450,
                 cord_x_jugador_2=200,
                 cord_y_jugador_2=450,
                 cord_x_pelota=625,
                 cord_y_pelota=450,
                 velocidad_x_jugador_1=0,
                 velocidad_y_jugador_1=0,
                 velocidad_x_jugador_2=0,
                 velocidad_y_jugador_2=0,
                 direccion_pelota_tecla_presionada_1="nada",
                 ):

        self.pantalla = pantalla
        self.color_fondo = color_fondo
        self.cord_x_jugador_1 = cord_x_jugador_1
        self.cord_y_jugador_1 = cord_y_jugador_1
        self.velocidad_x_jugador_1 = velocidad_x_jugador_1
        self.velocidad_y_jugador_1 = velocidad_y_jugador_1
        self.cord_x_jugador_2 = cord_x_jugador_2
        self.cord_y_jugador_2 = cord_y_jugador_2
        self.velocidad_x_jugador_2 = velocidad_x_jugador_2
        self.velocidad_y_jugador_2 = velocidad_y_jugador_2
        self.cord_x_pelota = cord_x_pelota
        self.cord_y_pelota = cord_y_pelota
        self.direccion_pelota_tecla_presionada_1 = direccion_pelota_tecla_presionada_1

    def __set__(self):
        pygame.display.set_caption(TITULO_JUEGO)

    def hacer_pantalla_juego(self):
        while True:
            self.pantalla.fill(self.color_fondo)
            cubito_1 = pygame.draw.rect(self.pantalla, ROJO, (self.cord_x_jugador_1, self.cord_y_jugador_1, 50, 50))
            cubito_2 = pygame.draw.rect(self.pantalla, CELESTE, (self.cord_x_jugador_2, self.cord_y_jugador_2, 50, 50))
            pelota = pygame.draw.circle(self.pantalla, MARRON, (self.cord_x_pelota, self.cord_y_pelota), 15)

            if pelota.colliderect(cubito_1) or pelota.colliderect(cubito_2):
                if self.direccion_pelota_tecla_presionada_1 == "arriba":
                    self.cord_x_pelota += 0
                    self.cord_y_pelota += -1
                elif self.direccion_pelota_tecla_presionada_1 == "abajo":
                    self.cord_x_pelota += 0
                    self.cord_y_pelota += 1
                elif self.direccion_pelota_tecla_presionada_1 == "derecha":
                    self.cord_x_pelota += 1
                    self.cord_y_pelota += 0
                elif self.direccion_pelota_tecla_presionada_1 == "izquierda":
                    self.cord_x_pelota += -1
                    self.cord_y_pelota += 0
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    exit("SALIO")

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.velocidad_y_jugador_1 = -1
                        self.direccion_pelota_tecla_presionada_1 = "arriba"
                    elif evento.key == pygame.K_DOWN:
                        self.velocidad_y_jugador_1 = 1
                        self.direccion_pelota_tecla_presionada_1 = "abajo"
                    elif evento.key == pygame.K_RIGHT:
                        self.velocidad_x_jugador_1 = 1
                        self.direccion_pelota_tecla_presionada_1 = "derecha"
                    elif evento.key == pygame.K_LEFT:
                        self.velocidad_x_jugador_1 = -1
                        self.direccion_pelota_tecla_presionada_1 = "izquierda"
                    if evento.key == pygame.K_w:
                        self.velocidad_y_jugador_2 = -1
                        self.direccion_pelota_tecla_presionada_1 = "arriba"
                    elif evento.key == pygame.K_s:
                        self.velocidad_y_jugador_2 = 1
                        self.direccion_pelota_tecla_presionada_1 = "abajo"
                    elif evento.key == pygame.K_d:
                        self.velocidad_x_jugador_2 = 1
                        self.direccion_pelota_tecla_presionada_1 = "derecha"
                    elif evento.key == pygame.K_a:
                        self.velocidad_x_jugador_2 = -1
                        self.direccion_pelota_tecla_presionada_1 = "izquierda"

                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_UP:
                        self.velocidad_y_jugador_1 = 0
                    elif evento.key == pygame.K_DOWN:
                        self.velocidad_y_jugador_1 = 0
                    elif evento.key == pygame.K_RIGHT:
                        self.velocidad_x_jugador_1 = 0
                    elif evento.key == pygame.K_LEFT:
                        self.velocidad_x_jugador_1 = 0
                    if evento.key == pygame.K_w:
                        self.velocidad_y_jugador_2 = 0
                    elif evento.key == pygame.K_s:
                        self.velocidad_y_jugador_2 = 0
                    elif evento.key == pygame.K_d:
                        self.velocidad_x_jugador_2 = 0
                    elif evento.key == pygame.K_a:
                        self.velocidad_x_jugador_2 = 0

            self.cord_x_jugador_1 += self.velocidad_x_jugador_1
            self.cord_y_jugador_1 += self.velocidad_y_jugador_1
            self.cord_x_jugador_2 += self.velocidad_x_jugador_2
            self.cord_y_jugador_2 += self.velocidad_y_jugador_2
            pygame.display.flip()


jugadores = Juego(CREMA, screen)
jugadores.__set__(), jugadores.hacer_pantalla_juego()
pygame.quit()