import pygame
from backend.modelo.player import *

class Player2(Player):

    # construtor
    def __init__(self, x, y, nome, nome_imagem):
        super().__init__(x, y, nome, nome_imagem)
 
    # verificação de teclas
    def check_keys(self):
        # captura alguma eventual tecla que foi pressionada
        pk = pygame.key.get_pressed()
        # alguma tecla especial foi pressionada?
        if pk[pygame.K_LEFT]:
            self.rect.x -= 2
        if pk[pygame.K_RIGHT]:
            self.rect.x += 2