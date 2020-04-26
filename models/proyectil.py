import pygame
from pygame.locals import *
import os

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_proyectil = pygame.image.load(ruta)
        self.rect = self.imagen_proyectil.get_rect()
        self.velocidad = 20
        self.rect.top = posy
        self.rect.left = posx
        self.disparo_personaje = personaje

    def trayectoria(self):
        if self.disparo_personaje == True:
            self.rect.top -= self.velocidad
        else:
            self.rect.top += self.velocidad

    def render(self, superficie):
        superficie.blit(self.imagen_proyectil, self.rect)
