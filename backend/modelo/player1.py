import pygame
from backend.modelo.player import *
import random

class Player1(Player):

    # construtor
    def __init__(self, x, y, nome, nome_imagem):
        super().__init__(x, y, nome, nome_imagem)
        self.estrategia = 1
        self.vel = 1
 
    # verificação de teclas
    def check_keys(self):
        max = 1870

        #Jogador manual
        if self.estrategia == 1:
            # captura alguma eventual tecla que foi pressionada
            pk = pygame.key.get_pressed()
            # alguma tecla especial foi pressionada?
            if pk[pygame.K_a]:
                self.rect.x -= 2
            if pk[pygame.K_d]:
                self.rect.x += 2
        #Maluco
        elif self.estrategia == 2:
            self.rect.x += random.randint(-20,20)
        #De uma ponta à outra
        elif self.estrategia == 3:
            if self.rect.x <= 0:
                self.vel = self.vel*-1
                self.rect.x = 1
            if self.rect.x >= max:
                self.vel = self.vel*-1
                self.rect.x = max-1
            self.rect.x += self.vel