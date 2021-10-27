import piezas
import tablero, pygame

pantalla = pygame.display.set_mode((700, 600))
pantalla.fill((0, 0, 0))
# Definición del color de casillas

azul = (0, 0, 255)
verde=(0,255,0)
rojo=(255,0,0)
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

peonBlanco1 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["a",2], ["a", 2])
peonBlanco2 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["b", 2], ["b", 2])
peonBlanco3 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["c", 2], ["c", 2])
peonBlanco4 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["d", 2], ["d", 2])
peonBlanco5 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["e", 2], ["e", 2])
peonBlanco6 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["f", 2], ["f", 2])
peonBlanco7 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["g", 2], ["g", 2])
peonBlanco8 = tablero.piezaObjeto("Blanco", "Peon", peonBlanco, ["h", 2], ["h", 2])
torreBlanca1 = tablero.piezaObjeto("Blanco", "Torre", torreBlanca, ["a", 1], ["a", 1])
torreBlanca2 = tablero.piezaObjeto("Blanco", "Torre", torreBlanca, ["h", 1], ["h", 1])
caballoBlanco1 = tablero.piezaObjeto("Blanco", "Caballo", caballoBlanco, ["b", 1], ["b", 1])
caballoBlanco2 = tablero.piezaObjeto("Blanco", "Caballo", caballoBlanco, ["g", 1], ["g", 1])
alfilBlanco1 = tablero.piezaObjeto("Blanco", "Alfil", alfilBlanco, ["c", 1], ["c", 1])
alfilBlanco2 = tablero.piezaObjeto("Blanco", "Alfil", alfilBlanco, ["f", 1], ["f", 1])
reynaBlanca1 = tablero.piezaObjeto("Blanco", "Reyna", reynaBlanca, ["d", 1], ["d", 1])
reyBlanco1 = tablero.piezaObjeto("Blanco", "Rey", reyBlanco, ["e", 1], ["e", 1])

peonNegro1 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["a", 7], ["a", 7])
peonNegro2 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["b", 7], ["b",7])
peonNegro3 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["c",7], ["c",7])
peonNegro4 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["d", 7], ["d", 7])
peonNegro5 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["e", 7], ["e", 7])
peonNegro6 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["f", 7], ["f",7])
peonNegro7 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["g", 7], ["g", 7])
peonNegro8 = tablero.piezaObjeto("Negro", "Peon", peonNegro, ["h", 7], ["h", 7])
torreNegra1 = tablero.piezaObjeto("Negro", "Torre", torreNegra, ["a", 8], ["a",8])
torreNegra2 = tablero.piezaObjeto("Negro", "Torre", torreNegra, ["h", 8], ["h", 8])
caballoNegro1 = tablero.piezaObjeto("Negro", "Caballo", caballoNegro, ["b", 8], ["b", 8])
caballoNegro2 = tablero.piezaObjeto("Negro", "Caballo", caballoNegro, ["g", 8], ["g", 8])
alfilNegro1 = tablero.piezaObjeto("Negro", "Alfil", alfilNegro, ["c", 8], ["c", 8])
alfilNegro2 = tablero.piezaObjeto("Negro", "Alfil", alfilNegro, ["f", 8], ["f", 8])
reynaNegra1 = tablero.piezaObjeto("Negro", "Reyna", reynaNegra, ["d", 8], ["d",8])
reyNegro1 = tablero.piezaObjeto("Negro", "Rey", reyNegro, ["e", 8], ["e", 8])

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

def imprime():
    tablero.imprimeTablero(negro, blanco)
    peonNegro1.mostrarPieza()
    peonNegro2.mostrarPieza()
    peonNegro3.mostrarPieza()
    peonNegro4.mostrarPieza()
    peonNegro5.mostrarPieza()
    peonNegro6.mostrarPieza()
    peonNegro7.mostrarPieza()
    peonNegro8.mostrarPieza()
    torreNegra1.mostrarPieza()
    torreNegra2.mostrarPieza()
    caballoNegro1.mostrarPieza()
    caballoNegro2.mostrarPieza()
    alfilNegro1.mostrarPieza()
    alfilNegro2.mostrarPieza()
    reynaNegra1.mostrarPieza()
    reyNegro1.mostrarPieza()

    peonBlanco1.mostrarPieza()
    peonBlanco2.mostrarPieza()
    peonBlanco3.mostrarPieza()
    peonBlanco4.mostrarPieza()
    peonBlanco5.mostrarPieza()
    peonBlanco6.mostrarPieza()
    peonBlanco7.mostrarPieza()
    peonBlanco8.mostrarPieza()
    torreBlanca1.mostrarPieza()
    torreBlanca2.mostrarPieza()
    caballoBlanco1.mostrarPieza()
    caballoBlanco2.mostrarPieza()
    alfilBlanco1.mostrarPieza()
    alfilBlanco2.mostrarPieza()
    reynaBlanca1.mostrarPieza()
    reyBlanco1.mostrarPieza()

def main():

    #Creación de 32 objetos que correspponden a las 32 piezas de ajedrez
    #imprime()
    #print("MENÜ")
    #print("1. Presiona la tecla i para imprimir el tablero.")
    #print("2. Presione la tecla l para poner las piezas en su posición original.")
    #print("5. Presione la tecla c para cerrar la ventana del juego.")


    #Actividad 13. Mostrar la pieza de ajedrez reyna
    #torreNegra1.mostrarPieza()
    #print(torreNegra1.posicionInicial[0],torreNegra1.posicionInicial[1])

    # Actualizando posiciones de la reyna negra
    #reynaNegra1.moverPieza("d",4)
    #print(reynaNegra1.posicionActual)

    #12 Dibuja los 32 objetos en pantalla

    #reynaNegra1.mostrarPieza()
    # Botón Inicio
    print("MENÜ")
    print("Presiona el botón I para mostrar los botones de Inicio: ")
    print("     1- Cuadro verde para iniciar partida.")
    print("     2- Cuadro azul para reiniciar partida")
    print("     3- Cuadro rojo para salir del programa.\n")
    print("Presiona el botón O para mostrar las teclas de Configuración: ")
    print("     1- Presiona tecla 1  para color del tablero rojo y blanco")
    print("     2- Presiona tecla 1  para color del tablero verde y blanco")
    print("     3- Presiona tecla 1  para color del tablero gris y blanco \n")
    print("Presiona el botón P para mostrar la ayuda: ")
    print("     1- Créditos")



    fuente = pygame.font.Font(None, 17)
    iP = fuente.render("Iniciar Partida", 0, (0, 0, 0))
    rP = fuente.render("Reiniciar Partida", 0, (0, 0, 0))
    salir = fuente.render("Salir", 0, (0, 0, 0))
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
                if mousex > 6 and mousex < 100 and mousey >30 and mousey < 90:
                    pantalla.fill((47, 79, 79))
                    marron = (100, 10, 10)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(marron, blanco)
                    tablero.limpiaTablero()
                elif mousex > 10 and mousex < 90 and mousey >120 and mousey < 180:
                    pantalla.fill((47, 79, 79))
                    marron = (100, 10, 10)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(marron, blanco)
                    tablero.limpiaTablero()
                elif mousex > 30 and mousex < 90 and mousey >209 and mousey < 270:
                    running = False
                elif mousex > 100 and mousex < 160 and mousey >120 and mousey < 180:
                    pantalla.fill((47, 79, 79))
                    marron = (100, 10, 10)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(marron, blanco)
                    tablero.limpiaTablero()


            if event.type == pygame.KEYDOWN:
                #La ventana no se cierra con break, se debe cambiar a false la variable running para salir del bucle "While"
                if event.key == pygame.K_c:
                    running = False
                #Con el botón esc se regresa a las posiciones originales
                if event.key == pygame.K_l:
                    tablero.imprimeTablero()
                    tablero.limpiaTablero()

                # Con el botón i es inicio
                if event.key == pygame.K_i:
                    # Botón Inicio
                    cadena="AA"
                    pygame.draw.rect(pantalla, verde, pygame.Rect(5, 30, 90, 60))
                    pantalla.blit(iP,(10,50))
                    # Botón Configuración
                    pygame.draw.rect(pantalla, azul, pygame.Rect(5, 120, 90, 60))
                    pantalla.blit(rP, (10, 145))
                    # Botón Salir
                    pygame.draw.rect(pantalla, rojo, pygame.Rect(5, 210, 60, 60))
                    pantalla.blit(salir, (10, 235))

                #Con el boton o imprime pieza
                if event.key == pygame.K_o:
                    print("ssasa")
                    #piezas.muevePieza(diccionario)
                    peonBlanco1.posicionActual[1]=3
                    piezas.muevePieza(diccionario)
                    imprime()


                if event.key == pygame.K_1:
                    pantalla.fill((47, 79, 79))
                    negro = (100, 10, 10)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(negro, blanco)
                    imprime()
                if event.key == pygame.K_2:
                    pantalla.fill((47, 79, 79))
                    negro = (100, 100, 0)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(negro, blanco)
                    imprime()
                if event.key == pygame.K_3:
                    pantalla.fill((47, 79, 79))
                    negro = (100, 100, 100)
                    blanco = (255, 255, 255)
                    tablero.imprimeTablero(negro, blanco)
                    imprime()
                if event.key == pygame.K_p:
                    print("AYUDA")
        imprime()
        pygame.display.update()


main()