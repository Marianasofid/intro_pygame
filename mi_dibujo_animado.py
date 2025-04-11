import pygame
import sys
import random

blanco = (255,255,255)
grisito = (197,196,197)
gris = (150,146,150)
negro = (0, 0, 0)
grii = (189,185,189)
grisote = (100,97,100)
rosita = (249, 127, 242)
azulo = (14,20,108)
azul = (93,102,247)
azulito = (83,89,185)
oscuro = (10,15,92)
amarillo = (255, 214, 30)
rojo = (227,76,32)
Naranja = (255,120,0)
rojo = (255,0,0)

pygame.init()


ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Mi dibujo")

clock = pygame.time.Clock()

XX = 300


while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

    pygame.draw.rect(ventana, negro, ((50,50), (400,400)), 1)

    # Tren
    pygame.draw.rect(ventana, azulito, (200,300, 230,110))

    pygame.draw.circle(ventana, gris, (233,410), 35, )
    pygame.draw.circle(ventana, gris, (317,410), 35, )
    pygame.draw.circle(ventana, gris, (400,410), 35, )

    pygame.draw.rect(ventana, negro, (248,402, 55,25))
    pygame.draw.rect(ventana, negro, (335,402, 55,25))

    pygame.draw.rect(ventana, azul, (278,200, 135,100))

    pygame.draw.rect(ventana, azulo, (278,195, 135,35))
    pygame.draw.rect(ventana, azulo, (298,175, 100,28))
    pygame.draw.rect(ventana, grisito, (300,239, 92,50))

    # Chimenea
    pygame.draw.rect(ventana, azul, (215,260, 35,40))
    pygame.draw.rect(ventana, azulo, (204,250, 59,28))


    # Parte delantera
    pygame.draw.rect(ventana, azulo, (165,320, 35,65))
    pygame.draw.rect(ventana, oscuro, (160,300, 30,100))
    pygame.draw.circle(ventana, oscuro, (165,350), 25, )


    # Carita
    pygame.draw.circle(ventana, amarillo, (345,260), 35, )
    pygame.draw.circle(ventana, blanco, (330,255), 10, )
    pygame.draw.circle(ventana, blanco, (360,255), 10, )

    # Pupilas
    pygame.draw.circle(ventana, negro, (330,255), 5, )
    pygame.draw.circle(ventana, negro, (360,255), 5, )

    # Boca
    pygame.draw.circle(ventana, rojo, (345,275), 7, )


    # nombre
    fuente_arial = pygame.font.SysFont("Arial", 15, 350, 350)
    texto = fuente_arial.render("Mariana Delgado", 1, negro)
    ventana.blit(texto,(250,345))

  

    












    pygame.display.flip()

