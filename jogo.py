import pygame
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *
from backend.modelo.partida import *

pygame.init()

partida1 = Partida()

partida1.allPlayers()
partida1.onePlayer()
partida1.threePlayers()

pygame.quit()