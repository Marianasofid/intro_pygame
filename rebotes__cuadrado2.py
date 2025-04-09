import pygame 
import sys

rojo = (255,0,0)

import random 
def color_aleatorio():
    r = random.randint(0,255)
    return (r)

rojo = (255,0,0)
rojo = (255,0,0)
rojo = (255,0,0)
azul = (0,0,255)

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Los cuadrados que rebota,")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO

    if XX >= 320:
        XX = 320
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3
    

    pygame.draw.rect(ventana, rojo, (XX, 0, 50, 50))
    pygame.draw.rect(ventana, color_aleatorio, (205, 205, 100, 100))
    pygame.draw.rect(ventana, rojo, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, rojo, (450, XX, 50, 50))
    pygame.draw.rect(ventana, rojo, (0, XX, 50, 50))



    pygame.display.flip()
