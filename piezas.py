import pygame

pantalla = pygame.display.set_mode((700, 600))
peonBlanco1 = pygame.image.load("piezas/WhitePawn.png")


def imprimePieza(diccionario):
    # Imprimir piezas
    pantalla.blit(peonBlanco1, (105, 335))

def muevePieza():
    if x1 == x2 and x2 == 'a' or x2 == 'b' or x2 == 'c' or x2 == 'd' or x2 == 'e' or x2 == 'f' or x2 == 'g' or x2 == 'h' and y1 <= 9:
        print("Mueve peon")
        # Actualizando la posición del peón
        diccionario[peonBlanco1][1] = diccionario[peonBlanco1][1] + 1
    else:
        print("Movimiento no válido")
