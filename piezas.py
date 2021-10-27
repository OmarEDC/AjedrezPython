import pygame, tablero

pantalla = pygame.display.set_mode((700, 600))
peonBlanco1 = pygame.image.load("piezas/WhitePawn.png")

x1=0
x2=0
y1=0
y2=0

def imprimePieza():
    tablero.imprimeTablero()
    jA.peonNegro1.mostrarPieza()
    jA.peonNegro2.mostrarPieza()
    jA.peonNegro3.mostrarPieza()
    jA.peonNegro4.mostrarPieza()
    jA.peonNegro5.mostrarPieza()
    jA.peonNegro6.mostrarPieza()
    jA.peonNegro7.mostrarPieza()
    jA.peonNegro8.mostrarPieza()
    jA.torreNegra1.mostrarPieza()
    jA.torreNegra2.mostrarPieza()
    jA.caballoNegro1.mostrarPieza()
    jA.caballoNegro2.mostrarPieza()
    jA.alfilNegro1.mostrarPieza()
    jA.alfilNegro2.mostrarPieza()
    jA.reynaNegra1.mostrarPieza()
    jA.reyNegro1.mostrarPieza()

    jA.peonBlanco1.mostrarPieza()
    jA.peonBlanco2.mostrarPieza()
    jA.peonBlanco3.mostrarPieza()
    jA.peonBlanco4.mostrarPieza()
    jA.peonBlanco5.mostrarPieza()
    jA.peonBlanco6.mostrarPieza()
    jA.peonBlanco7.mostrarPieza()
    jA.peonBlanco8.mostrarPieza()
    jA.torreBlanca1.mostrarPieza()
    jA.torreBlanca2.mostrarPieza()
    jA.caballoBlanco1.mostrarPieza()
    jA.caballoBlanco2.mostrarPieza()
    jA.alfilBlanco1.mostrarPieza()
    jA.alfilBlanco2.mostrarPieza()
    jA.reynaBlanca1.mostrarPieza()
    jA.reyBlanco1.mostrarPieza()


def muevePieza(diccionario):

    #Peon
    print(diccionario[1])
    if(diccionario[1]==1):
        print("Peon balnco 1")
        x1=diccionario
        if x1 == x2 and x2 == 'a' or x2 == 'b' or x2 == 'c' or x2 == 'd' or x2 == 'e' or x2 == 'f' or x2 == 'g' or x2 == 'h' and y1 <= 9:
            print("Mueve peon")
            # Actualizando la posición del peón
            diccionario[peonBlanco1][1] = diccionario[peonBlanco1][1] + 1
        else:
            print("Movimiento no válido")

