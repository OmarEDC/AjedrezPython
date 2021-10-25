import tablero, piezas, pygame

pantalla = pygame.display.set_mode((700, 600))
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


diccionario = {    1: ["a", 2, "Peon", "Blanco"], 2: ["b", 2, "Peon", "Blanco"], 3: ["c", 2, "Peon", "Blanco"],
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

def main():

    #Creación de 32 objetos que correspponden a las 32 piezas de ajedrez
    peonBlanco1 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "a2", "a3")
    peonBlanco2 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "b2", "b2")
    peonBlanco3 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "c2", "c2")
    peonBlanco4 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "d2", "d2")
    peonBlanco5 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "e2", "e2")
    peonBlanco6 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "f2", "f2")
    peonBlanco7 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "g2", "g2")
    peonBlanco8 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, "h2", "h2")
    torreBlanca1 = tablero.piezaObjeto("Blanco", "Torre", torreBlanca, "a1", "a1")
    torreBlanca2 = tablero.piezaObjeto("Blanco", "Torre", torreBlanca, "h1", "h1")
    caballoBlanco1 = tablero.piezaObjeto("Blanco", "Caballo", caballoBlanco, "b1", "b1")
    caballoBlanco2 = tablero.piezaObjeto("Blanco", "Caballo", caballoBlanco, "g1", "g1")
    alfilBlanco1 = tablero.piezaObjeto("Blanco", "Alfil", alfilBlanco, "c1", "c1")
    alfilBlanco2 = tablero.piezaObjeto("Blanco", "Alfil", alfilBlanco, "f1", "f1")
    reynaBlanca1 = tablero.piezaObjeto("Blanco", "Reyna", reynaBlanca, "d1", "d1")
    reyBlanco1 = tablero.piezaObjeto("Blanco", "Rey", reyBlanco, "e1", "e1")

    peonNegro1 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "a7", "a7")
    peonNegro2 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "b7", "b7")
    peonNegro3 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "c7", "c7")
    peonNegro4 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "d7", "d7")
    peonNegro5 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "e7", "e7")
    peonNegro6 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "f7", "f7")
    peonNegro7 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "g7", "g7")
    peonNegro8 = tablero.piezaObjeto("Negro", "Peon", peonNegro, "h7", "h7")
    torreNegra1 = tablero.piezaObjeto("Negro", "Torre", torreNegra, "a8", "a1")
    torreNegra2 = tablero.piezaObjeto("Negro", "Torre", torreNegra, "h8", "h1")
    caballoNegro1 = tablero.piezaObjeto("Negro", "Caballo", caballoNegro, "b8", "b1")
    caballoNegro2 = tablero.piezaObjeto("Negro", "Caballo", caballoNegro, "g8", "g1")
    alfilNegro1 = tablero.piezaObjeto("Negro", "Alfil", alfilNegro, "c8", "c1")
    alfilNegro2 = tablero.piezaObjeto("Negro", "Alfil", alfilNegro, "f8", "f1")
    reynaNegra1 = tablero.piezaObjeto("Negro", "Reyna", reynaNegra, "d8", "d1")
    reyNegro1 = tablero.piezaObjeto("Negro", "Rey", reyNegro, "e8", "e8")



    print("MENÜ")
    print("1. Presiona la tecla i para imprimir el tablero.")
    print("2. Presione la tecla l para poner las piezas en su posición original.")
    print("5. Presione la tecla c para cerrar la ventana del juego.")


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
                if event.key == pygame.K_l:
                    tablero.imprimeTablero()
                    tablero.limpiaTablero()
                # Con el botón i se imprime el tablero
                if event.key == pygame.K_i:
                    tablero.imprimeTablero()

                #Con el boton o imprime pieza
                if event.key == pygame.K_o:
                    piezas.imprimePieza(diccionario)




        pygame.display.update()


main()