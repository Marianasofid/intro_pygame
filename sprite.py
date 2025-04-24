import pygame

# Inicializar Pygame
pygame.init()

# Establecer dimensiones de la pantalla
screen_ancho, screen_altura = 800, 600
screen = pygame.display.set_mode((screen_ancho, screen_altura))

# Definir los colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Crear una clase de sprite personalizada
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()  # Inicializar la clase base Sprite
        self.image = pygame.Surface((50, 50))  # Superficie del sprite
        self.image.fill(color)  # Rellenar el sprite con el color
        self.rect = self.image.get_rect()  # Obtener el rectángulo delimitador
        self.rect.x = x  # Posición en el eje X
        self.rect.y = y  # Posición en el eje Y

    def update(self):
        # Mover el sprite hacia la derecha
        self.rect.x += 5
        # Si el sprite sale de la pantalla, lo reincide en la parte izquierda
        if self.rect.x > screen_ancho:
            self.rect.x = -50  # Lo reincide fuera de la pantalla


# Crear el grupo de sprites
all_sprites = pygame.sprite.Group()

# Crear dos instancias de MySprite y agregarlas al grupo
sprite1 = MySprite(RED, 100, 100)
sprite2 = MySprite(GREEN, 200, 200)
all_sprites.add(sprite1, sprite2)

# Bucle principal del juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar todos los sprites en el grupo
    all_sprites.update()

    # Limpiar la pantalla (rellenar con el color negro)
    screen.fill(BLACK)

    # Dibujar todos los sprites en la pantalla
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los fotogramas por segundo
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()







## Clase sprite:
#Un Sprite es cualquier objeto del juego que puede ser representado en pantalla y que teien un comportamiento, ya sea moverse, sonar etc.

## Groups::
# Los grupos permiten manejar varios sprites a la vez: dibujarlos, actualizarlos o verificar colisiones entre ellos.