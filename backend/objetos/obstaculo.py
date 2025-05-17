import pygame
from backend.modelo.obstaculo import *

# cria grupo de obstáculos
platform_group = pygame.sprite.Group()


#criar uma coluna de obstaculos
for j in range(0,2):
    #Criar uma linha de obstaculos
    for i in range(0,38):
        mx = i*50
        my = j*50
        if (i%2)==0:
            platform_group.add(Obstacle(mx, my, "../../inimigo/tohou.png"))
        else:
            platform_group.add(Obstacle(mx, my, "../../inimigo/tohou2.png"))