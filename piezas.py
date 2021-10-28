import pygame, tablero

pantalla = pygame.display.set_mode((700, 600))
peonBlanco1 = pygame.image.load("piezas/WhitePawn.png")

x1=0
x2=0
y1=0
y2=0
xf=0
yf=0


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

def conversion (x1):
    print("aaaaaaa")
    if x1>100 and x1<160:
        xf = 'a'
    elif x1>160 and x1<220:
        xf = 'b'
    elif x1>220 and x1<280:
        xf = 'c'
    elif x1>280 and x1<340:
        xf = 'd'
    elif x1>340 and x1<400:
        xf = 'e'
    elif x1>400 and x1<460:
        xf = 'f'
    elif x1>460 and x1<520:
        xf = 'g'
    elif x1>520 and x1<580:
        xf = 'h'
    else:
        xf=0
    #print(xf)
    return xf

def conversion1(y):
    print("ddddd")
    if y>30 and y<90:
        yf = 8
    elif y>90 and y<150:
        yf = 7
    elif y>150 and y<210:
        yf = 6
    elif y>210 and y<270:
        yf = 5
    elif y>270 and y<330:
        yf = 4
    elif y>330 and y<390:
        yf = 3
    elif y>390 and y<450:
        yf = 2
    elif y>450 and y<510:
        yf = 1
    else:
        yf=0
    #print(yf)
    return yf

def muevePieza(diccionario, x1, y1):
    print("Peon bbbbbbb")
    i=0
    while i != 32:
        print("WHILE")
        print(x1, y1)
        i+=1
        print(diccionario[i][0])
        print(diccionario[i][1])
        if diccionario[i][0] == x1 and diccionario[i][1]== y1:
            #print(diccionario["PeonBlanco111111111"])
            estado= True
            break
        else:
            estado =False
    return estado

        #if(diccionario["PeonBlanco1"][2] =="PeonBlanco1"):
            #print("Peon balnco 1")
            #x1=diccionario
            #if x1 == x2 and x2 == 'a' or x2 == 'b' or x2 == 'c' or x2 == 'd' or x2 == 'e' or x2 == 'f' or x2 == 'g' or x2 == 'h' and y1 <= 9:
            #    print("Mueve peon")
                # Actualizando la posición del peón
           #     diccionario[peonBlanco1][1] = diccionario[peonBlanco1][1] + 1
          #  else:
         #       print("Movimiento no válido")

