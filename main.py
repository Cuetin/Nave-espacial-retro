import pygame, sys
from pygame.locals import *
from random import randint
from constantes import *
from models.nave import NaveEspacial
from models.proyectil import Proyectil
from models.enemigo import Enemigo
import os

def detenerTodo():
    for enemigo in LISTA_ENEMIGOS:
        for disparo in enemigo.lista_disparos:
            enemigo.lista_disparos.remove(disparo)

        enemigo.conquista = True

def cargarEnemigos(): 
    posx = 100
    for x in range(1, 5):
        enemigo = Enemigo(posx, 200, 100, MARCIANO1A, MARCIANO1B)
        LISTA_ENEMIGOS.append(enemigo)
        posx += 200
    posx = 100
    for x in range(1, 5):
        enemigo = Enemigo(posx, 100, 100, MARCIANO2A, MARCIANO2B)
        LISTA_ENEMIGOS.append(enemigo)
        posx += 200
    posx = 100
    for x in range(1, 5):
        enemigo = Enemigo(posx, 0, 100, MARCIANO3A, MARCIANO3B)
        LISTA_ENEMIGOS.append(enemigo)
        posx += 200

def Aliens():
    #Iniciamos el modulo pygame para trabajar con el
    pygame.init()
    #Creamos la ventana del juego
    ventana = pygame.display.set_mode((ANCHO_V, ALTO_V))
    #Le ponemos titulo a la ventana
    pygame.display.set_caption("Aliens")

    #Cargamos la imagen de fondo
    imagen_fondo = pygame.image.load(os.path.join('Imagenes', 'Fondo.jpg'))
    #Cargamos la cancion de fondo
    pygame.mixer.music.load(os.path.join('Musica', 'Intro.mp3'))
    pygame.mixer.music.play(3)

    fuente = pygame.font.SysFont("Arial", 100)
    texto = fuente.render("GAME OVER",  0, (255, 0, 0))

    jugador = NaveEspacial()
    cargarEnemigos()
    en_juego = True
    reloj = pygame.time.Clock()

    #Bucle infinito para que este abierto
    while True:
        #Ponemos 60 FPS
        reloj.tick(60)
        tiempo = int(pygame.time.get_ticks()/1000)
        #Comprobamos los eventos
        for event in pygame.event.get():
            #Se comprueba si se quiere salir
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if en_juego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        #Pintamos el fondo
        ventana.blit(imagen_fondo, (0, 0))
        #Pintamos la nave
        jugador.render(ventana)

        if len(jugador.lista_disparos) > 0:
            for x in jugador.lista_disparos:
                x.render(ventana)
                x.trayectoria()
                if x.rect.top < -10:
                    jugador.lista_disparos.remove(x)
                else:
                    for enemigo in LISTA_ENEMIGOS:
                        if x.rect.colliderect(enemigo.rect):
                            LISTA_ENEMIGOS.remove(enemigo)
                            jugador.lista_disparos.remove(x)

        if len(LISTA_ENEMIGOS) > 0:
            for enemigo in LISTA_ENEMIGOS:
                enemigo.comportamiento(tiempo)
                enemigo.render(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    en_juego = False
                    detenerTodo()
                
                if len(enemigo.lista_disparos) > 0:
                    for x in enemigo.lista_disparos:
                        x.render(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            en_juego = False
                            detenerTodo()

                        if x.rect.top > 900:
                            enemigo.lista_disparos.remove(x)
                        else:
                            for disparo in jugador.lista_disparos:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.lista_disparos.remove(disparo)
                                    enemigo.lista_disparos.remove(x)

        if en_juego == False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(texto, (250, 200))

        #Actualizamos el estado de la pantalla
        pygame.display.update()

if __name__ == '__main__':
    Aliens()