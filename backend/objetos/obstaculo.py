import pygame, random
from backend.modelo.obstaculo import *
from backend.objetos.perguntas import *

# cria grupo de obstáculos
platform_group = pygame.sprite.Group()

MAX_X = 800
MAX_Y = 600


#criar mais um monte de obstáculos :-p
for i in range(0,25): # criar 20 objetos
    mx = random.randint(1, MAX_X-100)
    my = 10 + random.randint(1, MAX_Y/10)
    platform_group.add(Obstacle(mx, my, "../../inimigo/"+inimigoImagem))

for i in range(0,25): # criar 20 objetos
    mx = random.randint(1, MAX_X-100)
    my = 10 + random.randint(1, MAX_Y/10)
    platform_group.add(Obstacle(mx, my, "../../inimigo/"+inimigoImagem2))