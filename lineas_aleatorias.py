import pygame 
import sys 
import random

negro = (0, 0, 0)
rosita = (249, 127, 242)
blanco = (255,255,255)
cian = (0,255,255)
pygame.init()


ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Lineas aleatorias")

clock = pygame.time.Clock()

XX = 300


# Cuadrado1
while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    pygame.draw.rect(ventana, rosita , (50, 50, 400, 400))

    fuente_arial = pygame.font.SysFont("Arial", 23, 1, 1)
    texto = fuente_arial.render("Colegio San José de Guanenta", 1, blanco)
    ventana.blit(texto,(80,8))

    fuente_arial = pygame.font.SysFont("Arial", 18, 1, 1)
    texto = fuente_arial.render("Especialidad Sistemas", 1, blanco)
    ventana.blit(texto,(150,29))

    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Mariana Delgado", 1, blanco)
    ventana.blit(texto,(155,455))


    # líneas random
    for i in range(100):
        coordenadax1 = random.randint(45, 435)
        coordenaday1 = random.randint(45, 435)
        coordenadax2 = random.randint(45, 435)
        coordenaday2 = random.randint(45, 435)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.line(ventana, color, (coordenadax1, coordenaday1), (coordenadax2, coordenaday2), 2)


    pygame.display.flip()


