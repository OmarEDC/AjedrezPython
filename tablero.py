import pygame

# Inicializando pygame
pygame.init()

# Se crea la ventana
pantalla = pygame.display.set_mode((700, 600))

# Se añade el encabezado
pygame.display.set_caption("Mi ajedrez en Python")

# Definición del color de casillas
negro = (100, 10, 10)
blanco = (255, 255, 255)

peonBlanco = pygame.image.load("piezas/WhitePawn.png")
torreBlanca = pygame.image.load("piezas/WhiteRook.png")
torreBlanca = pygame.transform.scale(torreBlanca, (55, 55))
caballoBlanco = pygame.image.load("piezas/WhiteKnight.png")
caballoBlanco = pygame.transform.scale(caballoBlanco, (55, 55))
alfilBlanco = pygame.image.load("piezas/WhiteBishop.png")
alfilBlanco = pygame.transform.scale(alfilBlanco, (55, 55))
reynaBlanca = pygame.image.load("piezas/WhiteQueen.png")
reynaBlanca = pygame.transform.scale(reynaBlanca, (55, 55))
reyBlanco = pygame.image.load("piezas/WhiteKing.png")
reyBlanco = pygame.transform.scale(reyBlanco, (55, 55))
peonNegro = pygame.image.load("piezas/BlackPawn.png")
torreNegra = pygame.image.load("piezas/BlackRook.png")
torreNegra = pygame.transform.scale(torreNegra, (55, 55))
caballoNegro = pygame.image.load("piezas/BlackKnight.png")
caballoNegro = pygame.transform.scale(caballoNegro, (55, 55))
alfilNegro = pygame.image.load("piezas/BlackBishop.png")
alfilNegro = pygame.transform.scale(alfilNegro, (55, 55))
reynaNegra = pygame.image.load("piezas/BlackQueen.png")
reynaNegra = pygame.transform.scale(reynaNegra, (55, 55))
reyNegro = pygame.image.load("piezas/BlackKing.png")
reyNegro = pygame.transform.scale(reyNegro, (55, 55))
peonNegro1=peonNegro
peonNegro2=peonNegro
peonNegro3=peonNegro
peonNegro4=peonNegro
peonNegro5=peonNegro
peonNegro6=peonNegro
peonNegro7=peonNegro
peonNegro8=peonNegro
torreNegra1=torreNegra
torreNegra2=torreNegra
caballoNegro1=caballoNegro
caballoNegro2=caballoNegro
alfilNegro1=alfilNegro
alfilNegro2=alfilNegro
peonBlanco1=peonBlanco
peonBlanco2=peonBlanco
peonBlanco3=peonBlanco
peonBlanco4=peonBlanco
peonBlanco5=peonBlanco
peonBlanco6=peonBlanco
peonBlanco7=peonBlanco
peonBlanco8=peonBlanco
torreBlanca1=torreBlanca
torreBlanca2=torreBlanca
caballoBlanco1=caballoBlanco
caballoBlanco2=caballoBlanco
alfilBlanco1=alfilBlanco
alfilBlanco2=alfilBlanco\

playerx = 255
playery=255
playerchange = 0


def dibujaTablero(pantalla):
    pantalla.fill((47, 79, 79))
    """
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

    #Pintar tablero de 8*8 con while
    i=0
    x=100
    y=30
    bandera=0
    j=0
    while j!=8:
        while i!=8:
            if bandera == 0:
                i+=1
                pygame.draw.rect(pantalla, blanco, pygame.Rect(x, y, 60, 60))
                x=x+60
                bandera=1
            else:
                i+=1
                pygame.draw.rect(pantalla, negro, pygame.Rect(x, y, 60, 60))
                x = x + 60
                bandera = 0
        if i==8 and bandera == 1:
            bandera = 0
        else:
            bandera = 1
        j += 1
        i = 0
        y += 60
        x = 100
"""
    bandera=0
    x = 100
    y = 30
    for i in range(64):
        if bandera == 0:
            i += 1
            pygame.draw.rect(pantalla, blanco, pygame.Rect(x, y, 60, 60))
            x = x + 60
            bandera = 1
        else:
            i += 1
            pygame.draw.rect(pantalla, negro, pygame.Rect(x, y, 60, 60))
            x = x + 60
            bandera = 0
        if i==8 or i==16 or i==24 or i==32 or i==40 or i==48 or i==56:
            y=y+60
            x=100
            if bandera==0:
                bandera=1
            else:
                bandera=0



def llenaTablero(pantalla):

    # Tuplas piezas blancas
    peonBlanco1 = ('a', 2)
    peonBlanco2 = ('b', 2)
    peonBlanco3 = ('c', 2)
    peonBlanco4 = ('d', 2)
    peonBlanco5 = ('e', 2)
    peonBlanco6 = ('f', 2)
    peonBlanco7 = ('g', 2)
    peonBlanco8 = ('h', 2)
    torreBlanca1 = ('a', 1)
    torreBlanca2 = ('h', 1)
    caballoBlanco1 = ('b', 1)
    caballoBlanco2 = ('g', 1)
    alfilBlanco1 = ('c', 1)
    alfilBlanco2 = ('f', 1)
    reynaBlanca = ('d', 1)
    reyBlanco = ('e', 1)

    # Tuplas piezas negras
    peonNegro1 = ("a7", "Peón", "Negro")
    peonNegro2 = ('b', 7)
    peonNegro3 = ('c', 7)
    peonNegro4 = ('d', 7)
    peonNegro5 = ('e', 7)
    peonNegro6 = ('f', 7)
    peonNegro7 = ('g', 7)
    peonNegro8 = ('h', 7)
    torreNegra1 = ('a', 8)
    torreNegra2 = ('h', 8)
    caballoNegro1 = ('b', 8)
    caballoNegro2 = ('g', 8)
    alfilNegro1 = ('c', 8)
    alfilNegro2 = ('f', 8)
    reynaNegra = ('d', 8)
    reyNegro = ('e', 8)


    # Crear lista que almacene todas las tuplas
    piezas = [peonBlanco1, peonBlanco2, peonBlanco3, peonBlanco4, peonBlanco5, peonBlanco6, peonBlanco7, peonBlanco8,
                  torreBlanca1, torreBlanca2, caballoBlanco1, caballoBlanco2, alfilBlanco1, alfilBlanco2, reynaBlanca,
                  reyBlanco, peonNegro1, peonNegro2, peonNegro3, peonNegro4, peonNegro5, peonNegro6, peonNegro7, peonNegro8,
                  torreNegra1, torreNegra2, caballoNegro1, caballoNegro2, alfilNegro1, alfilNegro2, reynaNegra, reyNegro]
    print(piezas[0])



    diccionario = { 1:["a", 2,"Peon","Blanco"], 2:["b", 2,"Peon","Blanco"], 3:["c", 2, "Peon", "Blanco"],
                    4:["d", 2, "Peon", "Blanco"], 5:["e", 2, "Peon", "Blanco"], 6:["f", 2, "Peon", "Blanco"],
                    7:["g", 2, "Peon", "Blanco"], 8:["h", 2, "Peon", "Blanco"], 9:["a", 1, "Torre", "Blanco"],
                    10:["h", 1, "Torre", "Blanco"], 11:["b", 1, "Caballo", "Blanco"], 12:["g", 1, "Caballo", "Blanco"],
                    13:["c", 1, "Alfil", "Blanco"], 14:["f", 1, "Alfil", "Blanco"], 15:["d", 1, "Reyna", "Blanco"],
                    16:["e", 1, "Rey", "Blanco"], 17:["a", 7, "Peon", "Negro"], 18:["b", 7, "Peon", "Negro"],
                    19:["c", 7, "Peon", "Negro"], 20:["d", 7, "Peon", "Negro"], 21:["e", 7, "Peon", "Negro"],
                    22:["f", 7, "Peon", "Negro"], 23:["g", 7, "Peon", "Negro"], 24:["h", 7, "Peon", "Negro"],
                    25:["a", 7,"Torre", "Negro"], 26:["h", 8, "Torre", "Negro"], 27:["b", 8, "Caballo", "Negro"],
                    28:["g", 8, "Caballo", "Negro"], 29:["c", 8, "Alfil", "Negro"], 30:["f", 8, "Alfil", "Negro"],
                    31:["d", 8, "Reyna", "Negro"], 32:["e", 8, "Rey", "Negro"]}


    #5. Cambiar todas las piezas de ajedrez al bando blanco

    #i=0
    #while i!=32:
    #    i+=1
    #    diccionario[i][3]="Blanco"
    #    print(diccionario[i])

    #Cambia de bando sólo al equipo blanco al negro
    #i=0
    #while i!=32:
    #    i+=1
    #    if diccionario[i][3]=="Blanco":
    #        diccionario[i][3] = "Negro"
    #        print(diccionario[i])

    #Contar cada pieza de ajedrez
    piezasTotales=0
    for pieza in piezas:
        piezasTotales+=1
    print("la cantidad de piezas son: ",piezasTotales)

    #Contar total de piezas por bando
    iB=0
    iW=0
    n=0
    for pieza in piezas:
        n+=1
        if diccionario[n][3]=="Blanco":
            iW+=1
        else:
            iB+=1
    print("Piezas blancas totales: ", iW)
    print("Piezas negras totales: ", iB)


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
"""
    # Obteniendo casilla actual del peón, en este caso peonBlanco1
    x1 = diccionario[peonBlanco1][0]  # columna 'a'
    y1 = diccionario[peonBlanco1][1]  # fila 2

    # Suponiendo que el peón se quiere mover a la casilla a3, entonces:
    x2 = 'e'
    y2 = 10

    # Movimiento de los peones
    if x1 == x2 and x2=='a' or x2=='b' or x2=='c' or x2=='d' or x2=='e' or x2=='f' or x2=='g' or x2=='h' and y1 <=9:
        print("Mueve peon")
        # Actualizando la posición del peón
        diccionario[peonBlanco1][1] = diccionario[peonBlanco1][1] + 1
    else:
        print("Movimiento no válido")

    print(diccionario[peonBlanco1])
"""

def imprimeTablero():
    bandera=0
    x = 100
    y = 30
    for i in range(64):
        if bandera == 0:
            i += 1
            pygame.draw.rect(pantalla, blanco, pygame.Rect(x, y, 60, 60))
            x = x + 60
            bandera = 1
        else:
            i += 1
            pygame.draw.rect(pantalla, negro, pygame.Rect(x, y, 60, 60))
            x = x + 60
            bandera = 0
        if i==8 or i==16 or i==24 or i==32 or i==40 or i==48 or i==56:
            y=y+60
            x=100
            if bandera==0:
                bandera=1
            else:
                bandera=0




def limpiaTablero():
    pantalla.blit(peonNegro1, (105, 95))
    pantalla.blit(peonNegro2, (165, 95))
    pantalla.blit(peonNegro3, (225, 95))
    pantalla.blit(peonNegro4, (285, 95))
    pantalla.blit(peonNegro5, (345, 95))
    pantalla.blit(peonNegro6, (405, 95))
    pantalla.blit(peonNegro7, (465, 95))
    pantalla.blit(peonNegro8, (525, 95))
    pantalla.blit(torreNegra1, (105, 35))
    pantalla.blit(torreNegra2, (525, 35))
    pantalla.blit(caballoNegro1, (165, 35))
    pantalla.blit(caballoNegro2, (465, 35))
    pantalla.blit(alfilNegro1, (225, 35))
    pantalla.blit(alfilNegro2, (405, 35))
    pantalla.blit(reynaNegra, (285, 35))
    pantalla.blit(reyNegro, (345, 35))
    pantalla.blit(peonBlanco1, (105, 395))
    pantalla.blit(peonBlanco1, (165, 395))
    pantalla.blit(peonBlanco1, (225, 395))
    pantalla.blit(peonBlanco1, (285, 395))
    pantalla.blit(peonBlanco1, (345, 395))
    pantalla.blit(peonBlanco1, (405, 395))
    pantalla.blit(peonBlanco1, (465, 395))
    pantalla.blit(peonBlanco1, (525, 395))
    pantalla.blit(torreBlanca1, (105, 455))
    pantalla.blit(torreBlanca1, (525, 455))
    pantalla.blit(caballoBlanco1, (165, 455))
    pantalla.blit(caballoBlanco1, (465, 455))
    pantalla.blit(alfilBlanco1, (225, 455))
    pantalla.blit(alfilBlanco2, (405, 455))
    pantalla.blit(reynaBlanca, (285, 455))
    pantalla.blit(reyBlanco, (345, 455))




def limpiaTablero1():
    pantalla.blit(peonNegro1, (105, 135))
    pantalla.blit(peonNegro2, (165, 95))
    pantalla.blit(peonNegro3, (225, 95))
    pantalla.blit(peonNegro4, (285, 95))
    pantalla.blit(peonNegro5, (345, 95))
    pantalla.blit(peonNegro6, (405, 95))
    pantalla.blit(peonNegro7, (465, 95))
    pantalla.blit(peonNegro8, (525, 95))
    pantalla.blit(torreNegra1, (105, 35))
    pantalla.blit(torreNegra2, (525, 35))
    pantalla.blit(caballoNegro1, (165, 35))
    pantalla.blit(caballoNegro2, (465, 35))
    pantalla.blit(alfilNegro1, (225, 35))
    pantalla.blit(alfilNegro2, (405, 35))
    pantalla.blit(reynaNegra, (285, 35))
    pantalla.blit(reyNegro, (345, 35))
    pantalla.blit(peonBlanco1, (105, 395))
    pantalla.blit(peonBlanco1, (165, 395))
    pantalla.blit(peonBlanco1, (225, 395))
    pantalla.blit(peonBlanco1, (285, 395))
    pantalla.blit(peonBlanco1, (345, 395))
    pantalla.blit(peonBlanco1, (405, 395))
    pantalla.blit(peonBlanco1, (465, 395))
    pantalla.blit(peonBlanco1, (525, 395))
    pantalla.blit(torreBlanca1, (105, 455))
    pantalla.blit(torreBlanca1, (525, 455))
    pantalla.blit(caballoBlanco1, (165, 455))
    pantalla.blit(caballoBlanco1, (465, 455))
    pantalla.blit(alfilBlanco1, (225, 455))
    pantalla.blit(alfilBlanco2, (405, 455))
    pantalla.blit(reynaBlanca, (285, 315))
    pantalla.blit(reyBlanco, (345, 455))

"""
# Se ejecuta la ventana hasta que se decida cerrar
def main():

    diccionario = {"peonBlanco1": ["a", 2, "Peon", "Blanco"], 2: ["b", 2, "Peon", "Blanco"], 3: ["c", 2, "Peon", "Blanco"],
                   4: ["d", 2, "Peon", "Blanco"], 5: ["e", 2, "Peon", "Blanco"], 6: ["f", 2, "Peon", "Blanco"],
                   7: ["g", 2, "Peon", "Blanco"], 8: ["h", 2, "Peon", "Blanco"], 9: ["a", 1, "Torre", "Blanco"],
                   10: ["h", 1, "Torre", "Blanco"], 11: ["b", 1, "Caballo", "Blanco"],
                   12: ["g", 1, "Caballo", "Blanco"],
                   13: ["c", 1, "Alfil", "Blanco"], 14: ["f", 1, "Alfil", "Blanco"], 15: ["d", 1, "Reyna", "Blanco"],
                   16: ["e", 1, "Rey", "Blanco"], 17: ["a", 7, "Peon", "Negro"], 18: ["b", 7, "Peon", "Negro"],
                   19: ["c", 7, "Peon", "Negro"], 20: ["d", 7, "Peon", "Negro"], 21: ["e", 7, "Peon", "Negro"],
                   22: ["f", 7, "Peon", "Negro"], 23: ["g", 7, "Peon", "Negro"], 24: ["h", 7, "Peon", "Negro"],
                   25: ["a", 7, "Torre", "Negro"], 26: ["h", 8, "Torre", "Negro"], 27: ["b", 8, "Caballo", "Negro"],
                   28: ["g", 8, "Caballo", "Negro"], 29: ["c", 8, "Alfil", "Negro"], 30: ["f", 8, "Alfil", "Negro"],
                   31: ["d", 8, "Reyna", "Negro"], 32: ["e", 8, "Rey", "Negro"], 33: ["e", 8, "Rey", "Negro"]}

 #   imprimeTablero()
#    imprimePieza(diccionario)
    # Invoca a dibuja tablero
    #dibujaTablero(pantalla)
    #llenaTablero(pantalla)
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

            if event.type == pygame.KEYDOWN:
                #La ventana no se cierra con break, se debe cambiar a false la variable running para salir del bucle "While"
                if event.key == pygame.K_c:
                    running = False
                #Con el botón esc se regresa a las posiciones originales
                if event.key == pygame.K_ESCAPE:
                    limpiaTablero()
                    break

        pygame.display.update()

main()
"""

class piezaObjeto:
    def __init__(self, bando, tipoDePieza, imagen, posicionInicial, posicionActual):
        self.bando=bando
        self.tipoDePieza=tipoDePieza
        self.imagen=imagen
        self.posicionInicial=posicionInicial
        self.posicionActual=posicionActual


