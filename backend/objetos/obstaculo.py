import pygame
from backend.modelo.obstaculo import *

# cria grupo de obstáculos
platform_group = pygame.sprite.Group()


#criar uma linha de obstaculos
for j in range(0,5):
    for i in range(0,38): # criar 20 objetos
        mx = i*50
        my = j*50
        platform_group.add(Obstacle(mx, my, "../../inimigo/tohou.png"))

#criar uma coluna de obstaculos
for j in range(0,5):
    #criar uma linha de obstaculos
    for i in range(0,19): # criar 20 objetos
        mx = i*100
        my = j*50
        platform_group.add(Obstacle(mx, my, "../../inimigo/tohou2.png"))