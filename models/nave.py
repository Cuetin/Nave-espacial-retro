import pygame
from pygame.locals import *
import os
from constantes import *
from .proyectil import Proyectil

class NaveEspacial(pygame.sprite.Sprite):
    """Clase para las naves"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_nave = pygame.image.load(os.path.join('Imagenes', 'nave.jpg'))
        self.imagen_explosion = pygame.image.load(os.path.join('Imagenes', 'explosion.jpg'))
        self.rect = self.imagen_nave.get_rect()
        self.rect.centerx = ANCHO_V/2
        self.rect.centery = ALTO_V-30
        self.lista_disparos =[]
        self.vida = True
        self.velocidad = 25
        self.sonido_disparo = pygame.mixer.Sound(os.path.join('Musica', 'Laser-Shot-1.wav'))

    def movimientoDerecha(self):
        self.rect.left += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.right -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > ANCHO_V:
                self.rect.right = ANCHO_V-30

    def disparar(self, x, y):
        mi_proyectil = Proyectil(x, y, RUTA1, True)
        self.lista_disparos.append(mi_proyectil)
        self.sonido_disparo.play()

    def render(self, surface):
        surface.blit(self.imagen_nave, self.rect)

    def destruccion(self):
        self.vida = False
        self.velocidad = 0
        self.imagen_nave = self.imagen_explosion