import pygame, random
from backend.modelo.obstaculo import *
from backend.objetos.perguntas import *

# cria grupo de obstáculos
platform_group = pygame.sprite.Group()


#criar mais um monte de obstáculos :-p
for i in range(0,25): # criar 20 objetos
    mx = random.randint(1, FrameWidth-100)
    my = 10 + random.randint(1, FrameHeight/10)
    platform_group.add(Obstacle(mx, my, "../../inimigo/tohou.png"))

for i in range(0,25): # criar 20 objetos
    mx = random.randint(1, FrameWidth-100)
    my = 10 + random.randint(1, FrameHeight/10)
    platform_group.add(Obstacle(mx, my, "../../inimigo/tohou2.png"))