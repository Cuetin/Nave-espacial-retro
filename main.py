import pygame, sys
from pygame.locals import *
from random import randint
from constantes import *
from models.nave import NaveEspacial
from models.proyectil import Proyectil
from models.enemigo import Enemigo
from models.nivel import Nivel
import os

def detenerTodo():
    for enemigo in LISTA_ENEMIGOS:
        for disparo in enemigo.lista_disparos:
            enemigo.lista_disparos.remove(disparo)
    
    
    LISTA_ENEMIGOS.clear()


def Aliens(lvl):
    #Iniciamos el modulo pygame para trabajar con el
    pygame.init()
    #Creamos la ventana del juego
    ventana = pygame.display.set_mode((ANCHO_V, ALTO_V))
    #Le ponemos titulo a la ventana
    pygame.display.set_caption("Aliens")

    #Cargamos la imagen de fondo
    imagen_fondo = pygame.image.load(os.path.join('Imagenes', 'Fondo.jpg'))
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_V, ALTO_V))
    #Cargamos la cancion de fondo
    pygame.mixer.music.load(os.path.join('Musica', 'Intro.mp3'))
    pygame.mixer.music.play(3)

    fuente = pygame.font.SysFont("Arial", 100)
    fuente2 = pygame.font.SysFont("Arial", 30)
    texto_derrota = fuente.render("GAME OVER",  0, (255, 0, 0))
    texto_return_d = fuente2.render("PRESIONA ENTER PARA VOLVER A EMPEZAR",  0, (255, 0, 0))
    texto_victoria = fuente.render("HAS GANADO!!",  0, (255, 0, 0))
    texto_return_v = fuente2.render("PRESIONA ENTER PARA CONTINUAR",  0, (255, 0, 0))

        
    for enemigo in LISTA_ENEMIGOS:
        print(enemigo.velocidad)

    nivel = Nivel(lvl)
    jugador = NaveEspacial()
    nivel.cargarEnemigos()
    en_juego = True
    derrota = False
    victoria = False
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
                    derrota = True
                    enemigo.conquista = True
                    detenerTodo()
                
                if len(enemigo.lista_disparos) > 0:
                    for x in enemigo.lista_disparos:
                        x.render(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            derrota = True
                            enemigo.conquista = True
                            detenerTodo()
                    

                        if x.rect.top > ANCHO_V+100:
                            enemigo.lista_disparos.remove(x)
                        else:
                            for disparo in jugador.lista_disparos:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.lista_disparos.remove(disparo)
                                    enemigo.lista_disparos.remove(x)

        else:
             victoria = True

        if victoria == True and enemigo.conquista == False:
            if lvl > 10:
                 pygame.mixer.music.fadeout(3000)
                 ventana.blit(texto_victoria, (250, 200))
            else:
                ventana.blit(texto_victoria, (250, 200))
                ventana.blit(texto_return_v, (250, 400))
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        lvl += 1
                        Aliens(lvl)

        if derrota == True:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(texto_derrota, (250, 200))
            ventana.blit(texto_return_d, (250, 400))
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    lvl = 1
                    Aliens(lvl)

        #Actualizamos el estado de la pantalla
        pygame.display.update()

if __name__ == '__main__':
    lvl = 1
    Aliens(lvl)