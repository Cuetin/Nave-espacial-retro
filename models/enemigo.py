import pygame
from pygame.locals import *
import os
from random import randint
from .proyectil import Proyectil
from constantes import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distancia, imagen1, imagen2):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_enemigo1 = pygame.image.load(imagen1)
        self.imagen_enemigo2 = pygame.image.load(imagen2)
        self.lista_imagenes = [self.imagen_enemigo1, self.imagen_enemigo2]
        self.pos_imagen = 0
        self.imagen_enemigo = self.lista_imagenes[self.pos_imagen]
        self.rect = self.imagen_enemigo.get_rect()
        self.velocidad = 20
        self.lista_disparos = []
        self.rect.top = posy
        self.rect.left = posx
        self.tiempo_cambio = 1
        self.probabilidad_disparo = 1
        self.derecha = True
        self.contador = 0
        self.max_descenso = self.rect.top+40
        self.limite_derecha = posx + distancia
        self.limite_izquierda = posx - distancia
        self.conquista = False
    
    def render(self, superficie):
        self.imagen_enemigo = self.lista_imagenes[self.pos_imagen]
        superficie.blit(self.imagen_enemigo, self.rect)

    def comportamiento(self, tiempo):
        if self.conquista == False:
            self.__movimientos()
            self.__atacar()
            if self.tiempo_cambio == tiempo:
                self.pos_imagen += 1
                self.tiempo_cambio += 1

                if self.pos_imagen > len(self.lista_imagenes)-1:
                    self.pos_imagen = 0

    def __atacar(self):
        if(randint(0, 100) < self.probabilidad_disparo):
            self.__disparar()

    def __disparar(self):
        x, y = self.rect.center
        mi_proyectil = Proyectil(x, y, RUTA2, False)
        self.lista_disparos.append(mi_proyectil)

    def __movimientos(self):
        if self.contador < 3:
            self.__movimientoLateral()
        else:
            self.__descenso()

    def __descenso(self):
        if self.max_descenso == self.rect.top:
            self.contador = 0
            self.max_descenso = self.rect.top + 40
        else:
            self.rect.top += 1

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left += self.velocidad
            if self.rect.left > self.limite_derecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left -= self.velocidad
            if self.rect.left < self.limite_izquierda:
                self.derecha = True

