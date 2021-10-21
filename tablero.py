import pygame

# Inicializando pygame
pygame.init()

# Se crea la ventana
pantalla = pygame.display.set_mode((700, 600))

# Se añade el encabezado
pygame.display.set_caption("Mi ajedrez en Python")

# Definición del color de casillas
negro = (0, 0, 0)
blanco = (255, 255, 255)


def dibujaTablero(pantalla):
    pantalla.fill((47, 79, 79))
    # Fila 1
    pygame.draw.rect(pantalla, negro, pygame.Rect(100, 30, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(160, 30, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(220, 30, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(280, 30, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(340, 30, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(400, 30, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(460, 30, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(520, 30, 60, 60))
    # Fila 2
    pygame.draw.rect(pantalla, blanco, pygame.Rect(100, 90, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(160, 90, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(220, 90, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(280, 90, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(340, 90, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(400, 90, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(460, 90, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(520, 90, 60, 60))
    # Fila 3
    pygame.draw.rect(pantalla, negro, pygame.Rect(100, 150, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(160, 150, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(220, 150, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(280, 150, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(340, 150, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(400, 150, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(460, 150, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(520, 150, 60, 60))
    # Fila 4
    pygame.draw.rect(pantalla, blanco, pygame.Rect(100, 210, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(160, 210, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(220, 210, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(280, 210, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(340, 210, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(400, 210, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(460, 210, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(520, 210, 60, 60))
    # Fila 5
    pygame.draw.rect(pantalla, negro, pygame.Rect(100, 270, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(160, 270, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(220, 270, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(280, 270, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(340, 270, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(400, 270, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(460, 270, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(520, 270, 60, 60))
    # Fila 6
    pygame.draw.rect(pantalla, blanco, pygame.Rect(100, 330, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(160, 330, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(220, 330, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(280, 330, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(340, 330, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(400, 330, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(460, 330, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(520, 330, 60, 60))
    # Fila 7
    pygame.draw.rect(pantalla, negro, pygame.Rect(100, 390, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(160, 390, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(220, 390, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(280, 390, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(340, 390, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(400, 390, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(460, 390, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(520, 390, 60, 60))
    # Fila 8
    pygame.draw.rect(pantalla, blanco, pygame.Rect(100, 450, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(160, 450, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(220, 450, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(280, 450, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(340, 450, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(400, 450, 60, 60))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(460, 450, 60, 60))
    pygame.draw.rect(pantalla, negro, pygame.Rect(520, 450, 60, 60))


def llenaTablero(pantalla):
    playerImg = pygame.image.load("caballo.jpg")
    pantalla.blit(playerImg, (465, 455))


# Se ejecuta la ventana hasta que se decida cerrar
def main():
    # Invoca a dibuja tablero

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        dibujaTablero(pantalla)
        llenaTablero(pantalla)


main()
