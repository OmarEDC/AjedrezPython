import pygame
from pygame.locals import *

# Inicializando pygame
pygame.init()

# Se crea la ventana
pantalla = pygame.display.set_mode((700, 600))

# Se añade el encabezado
pygame.display.set_caption("Mi ajedrez en Python")

# Definición del color de casillas
negro = (100, 10, 10)
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
    # Piezas blancas
    # Posición
    x = 105
    y = 335
    peonBlanco1 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (x, y))
    peonBlanco2 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (165, 395))
    peonBlanco3 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (225, 395))
    peonBlanco4 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (285, 395))
    peonBlanco5 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (345, 395))
    peonBlanco6 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (405, 395))
    peonBlanco7 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (465, 395))
    peonBlanco8 = pygame.image.load("piezas/WhitePawn.png")
    pantalla.blit(peonBlanco1, (525, 395))
    torreBlanca1 = pygame.image.load("piezas/WhiteRook.png")
    torreBlanca1 = pygame.transform.scale(torreBlanca1, (55, 55))
    pantalla.blit(torreBlanca1, (105, 455))
    torreBlanca2 = pygame.transform.scale(torreBlanca1, (55, 55))
    pantalla.blit(torreBlanca1, (525, 455))
    caballoBlanco1 = pygame.image.load("piezas/WhiteKnight.png")
    caballoBlanco1 = pygame.transform.scale(caballoBlanco1, (55, 55))
    pantalla.blit(caballoBlanco1, (165, 455))
    caballoBlanco2 = pygame.transform.scale(caballoBlanco1, (55, 55))
    pantalla.blit(caballoBlanco1, (465, 455))
    alfilBlanco1 = pygame.image.load("piezas/WhiteBishop.png")
    alfilBlanco1 = pygame.transform.scale(alfilBlanco1, (55, 55))
    pantalla.blit(alfilBlanco1, (225, 455))
    alfilBlanco2 = pygame.transform.scale(alfilBlanco1, (55, 55))
    pantalla.blit(alfilBlanco2, (405, 455))
    reynaBlanca = pygame.image.load("piezas/WhiteQueen.png")
    reynaBlanca = pygame.transform.scale(reynaBlanca, (55, 55))
    pantalla.blit(reynaBlanca, (285, 455))
    reyBlanco = pygame.image.load("piezas/WhiteKing.png")
    reyBlanco = pygame.transform.scale(reyBlanco, (55, 55))
    pantalla.blit(reyBlanco, (345, 455))

    # Piezas negras
    peonNegro1 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro1, (105, 95))
    peonNegro2 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro2, (165, 95))
    peonNegro3 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro3, (225, 95))
    peonNegro4 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro4, (285, 95))
    peonNegro5 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro5, (345, 95))
    peonNegro6 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro6, (405, 95))
    peonNegro7 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro7, (465, 95))
    peonNegro8 = pygame.image.load("piezas/BlackPawn.png")
    pantalla.blit(peonNegro8, (525, 95))

    torreNegra1 = pygame.image.load("piezas/BlackRook.png")
    torreNegra1 = pygame.transform.scale(torreNegra1, (55, 55))
    pantalla.blit(torreNegra1, (105, 35))
    torreNegra2 = pygame.transform.scale(torreNegra1, (55, 55))
    pantalla.blit(torreNegra2, (525, 35))
    caballoNegro1 = pygame.image.load("piezas/BlackKnight.png")
    caballoNegro1 = pygame.transform.scale(caballoNegro1, (55, 55))
    pantalla.blit(caballoNegro1, (165, 35))
    caballoNegro2 = pygame.transform.scale(caballoNegro1, (55, 55))
    pantalla.blit(caballoNegro2, (465, 35))
    alfilNegro1 = pygame.image.load("piezas/BlackBishop.png")
    alfilNegro1 = pygame.transform.scale(alfilNegro1, (55, 55))
    pantalla.blit(alfilNegro1, (225, 35))
    alfilNegro2 = pygame.transform.scale(alfilNegro1, (55, 55))
    pantalla.blit(alfilNegro2, (405, 35))
    reynaNegra = pygame.image.load("piezas/BlackQueen.png")
    reynaNegra = pygame.transform.scale(reynaNegra, (55, 55))
    pantalla.blit(reynaNegra, (285, 35))
    reyNegro = pygame.image.load("piezas/BlackKing.png")
    reyNegro = pygame.transform.scale(reyNegro, (55, 55))
    pantalla.blit(reyNegro, (345, 35))


    # Tuplas piezas blancas
#    peonBlanco1 = ('a', 2)
#    peonBlanco2 = ('b', 2)
#    peonBlanco3 = ('c', 2)
#    peonBlanco4 = ('d', 2)
#    peonBlanco5 = ('e', 2)
#    peonBlanco6 = ('f', 2)
#    peonBlanco7 = ('g', 2)
#    peonBlanco8 = ('h', 2)
#    torreBlanca1 = ('a', 1)
#    torreBlanca2 = ('h', 1)
#    caballoBlanco1 = ('b', 1)
#    caballoBlanco2 = ('g', 1)
#    alfilBlanco1 = ('c', 1)
#    alfilBlanco2 = ('f', 1)
#    reynaBlanca = ('d', 1)
#    reyBlanco = ('e', 1)

    # Tuplas piezas negras
#    peonNegro1 = ("a7", "Peón", "Negro")
#    peonNegro2 = ('b', 7)
#    peonNegro3 = ('c', 7)
#    peonNegro4 = ('d', 7)
#    peonNegro5 = ('e', 7)
#    peonNegro6 = ('f', 7)
#    peonNegro7 = ('g', 7)
#    peonNegro8 = ('h', 7)
#    torreNegra1 = ('a', 8)
#    torreNegra2 = ('h', 8)
#    caballoNegro1 = ('b', 8)
#    caballoNegro2 = ('g', 8)
#    alfilNegro1 = ('c', 8)
#    alfilNegro2 = ('f', 8)
#    reynaNegra = ('d', 8)
#    reyNegro = ('e', 8)


    # Crear lista que almacene todas las tuplas
    piezas = [peonBlanco1, peonBlanco2, peonBlanco3, peonBlanco4, peonBlanco5, peonBlanco6, peonBlanco7, peonBlanco8,
                  torreBlanca1, torreBlanca2, caballoBlanco1, caballoBlanco2, alfilBlanco1, alfilBlanco2, reynaBlanca,
                  reyBlanco, peonNegro1, peonNegro2, peonNegro3, peonNegro4, peonNegro5, peonNegro6, peonNegro7, peonNegro8,
                  torreNegra1, torreNegra2, caballoNegro1, caballoNegro2, alfilNegro1, alfilNegro2, reynaNegra, reyNegro]
    print(piezas[0])

    diccionario = { peonBlanco1:["a", 2,"Peon","Blanco"], peonBlanco2:["b", 2,"Peon","Blanco"], peonBlanco3:["c", 2, "Peon", "Blanco"],
                    peonBlanco4:["d", 2, "Peon", "Blanco"], peonBlanco5:["e", 2, "Peon", "Blanco"], peonBlanco6:["f", 2, "Peon", "Blanco"],
                    peonBlanco7:["g", 2, "Peon", "Blanco"], peonBlanco8:["h", 2, "Peon", "Blanco"], torreBlanca1:["a", 1, "Torre", "Blanco"],
                    torreBlanca2:["h", 1, "Torre", "Blanco"], caballoBlanco1:["b", 1, "Caballo", "Blanco"], caballoBlanco2:["g", 1, "Caballo", "Blanco"],
                    alfilBlanco1:["c", 1, "Alfil", "Blanco"], alfilBlanco2:["f", 1, "Alfil", "Blanco"], reynaBlanca:["d", 1, "Reyna", "Blanco"],
                    peonNegro1:["a", 7, "Peon", "Negro"], peonNegro2:["b", 7, "Peon", "Negro"], peonNegro3:["c", 7, "Peon", "Negro"],
                    peonNegro4:["d", 7, "Peon", "Negro"], peonNegro5:["e", 7, "Peon", "Negro"], peonNegro6:["f", 7, "Peon", "Negro"],
                    peonNegro7:["g", 7, "Peon", "Negro"], peonNegro7:["h", 7, "Peon", "Negro"], torreNegra1:["a", 7,"Torre", "Negro"],
                    torreNegra2:["h", 8, "Torre", "Negro"], caballoNegro1:["b", 8, "Caballo", "Negro"], caballoNegro2:["g", 8, "Caballo", "Negro"],
                    alfilNegro1:["c", 8, "Alfil", "Negro"], alfilNegro2:["f", 8, "Alfil", "Negro"], reynaNegra:["d", 8, "Reyna", "Negro"],
                    reyNegro:["e", 8, "Rey", "Negro"]}

    # 4. Cambia el valor de la variable de posición de una pieza
    # diccionario[peonBlanco7][0] = "g3"
    # print(diccionario[peonBlanco1])

    # 5. Cambia la variable de nombre de una pieza. La imagen del peonBlanco7 por el de la reynaBlanca
    # diccionario[peonBlanco7][1] = reynaBlanca
    # print(diccionario[peonBlanco7])
    # Poner las coordenadas correctas del peonBlanco7
    # x, y = 465, 395
    # Visualizar en el tablero
    # pantalla.blit(diccionario[peonBlanco7][1], (x, y))
    # pantalla.blit(peonBlanco, (x, y))

    # 6. Cambia la variable bando de una pieza. La imagen del reyNegro
    # diccionario[reyNegro][2] = reyBlanco
    # print(diccionario[reyNegro])

    # Coordenadas del reyNegro
    # x, y = 345, 35
    # pantalla.blit(diccionario[reyNegro][2], (x, y))

    # Obteniendo casilla actual del peón, en este caso peonBlanco1
    x1 = diccionario[peonBlanco1][0]  # columna 'a'
    y1 = diccionario[peonBlanco1][1]  # fila 2

    # Suponiendo que el peón se quiere mover a la casilla a3, entonces:
    x2 = 'e'
    y2 = 10

    # Movimiento de los peones
    if x1 == x2 and x2=='a' or x2=='b' or x2=='c' or x2=='d' or x=='e' or x=='f' or x=='g' or x=='h' and y1 <=9:
        print("Mueve peon")
        # Actualizando la posición del peón
        diccionario[peonBlanco1][1] = diccionario[peonBlanco1][1] + 1
    else:
        print("Movimiento no válido")

    print(diccionario[peonBlanco1])



# Se ejecuta la ventana hasta que se decida cerrar
def main():
    # Invoca a dibuja tablero
    dibujaTablero(pantalla)
    llenaTablero(pantalla)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Usando el evento para reconocer click izq del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Se presionó el botón izquierdo del mouse")
                mousex, mousey = pygame.mouse.get_pos()
                print(mousex, mousey)
        pygame.display.update()


main()
