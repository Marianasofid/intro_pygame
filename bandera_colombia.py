# Importamos la libreria pygame
import pygame

# inicializamos los modulos de pygame
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("bandera_colombia")

# establecemos las dimensiones de laa ventana
ventana = pygame.display.set_mode((400,400))

# definimos un color
amarillo = (255, 255, 0)

# crea una superficie
amarillo_superficie = pygame.Surface((400,200))

# rellenamos la superficie
amarillo_superficie.fill(amarillo)

# inserto o muevo la superficie en la ventana
ventana.blit(amarillo_superficie, (0,0))




# definimos un color
azul = (0, 0, 255)

# crea una superficie
azul_superficie = pygame.Surface((400,100))

# rellenamos la superficie
azul_superficie.fill(azul)


# inserto o muevo la superficie en la ventana
ventana.blit(azul_superficie, (0,200))



# definamos un clor
rojo = (255, 0, 0)

# crea una superficie 
rojo_superficie = pygame.Surface((400,100))

# rellenamos la superficie
rojo_superficie.fill(rojo)

# inserto o muevo la superficie en la ventana
ventana.blit(rojo_superficie, (0,300))

# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event =pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame,quit()

