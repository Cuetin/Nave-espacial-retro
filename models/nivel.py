from .enemigo import Enemigo
from constantes import *

class Nivel:
    def __init__(self, lvl):
        self.lvl = lvl

    def cargarEnemigos(self): 
        posx = ANCHO_V/2
        pari = 1
        for x in range(0, self.lvl):
            enemigo = Enemigo(posx, 200, 600-(self.lvl*100), MARCIANO1A, MARCIANO1B)
            LISTA_ENEMIGOS.append(enemigo)
            if pari % 2 == 0:
                posx += 200 * pari
                pari += 1
            else:
                posx -= 200 * pari
                pari += 1
        posx = ANCHO_V/2
        pari = 1
        for x in range(0, self.lvl):
            enemigo = Enemigo(posx, 100, 600-(self.lvl*100), MARCIANO2A, MARCIANO2B)
            LISTA_ENEMIGOS.append(enemigo)
            if pari % 2 == 0:
                posx += 200 * pari
                pari += 1
            else:
                posx -= 200 * pari
                pari += 1
        posx = ANCHO_V/2
        pari = 1
        for x in range(0, self.lvl):
            enemigo = Enemigo(posx, 0, 600-(self.lvl*100), MARCIANO3A, MARCIANO3B)
            LISTA_ENEMIGOS.append(enemigo)
            if pari % 2 == 0:
                posx += 200 * pari
                pari += 1
            else:
                posx -= 200 * pari
                pari += 1