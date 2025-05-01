import pygame, os
from backend.config.config import *

# obter caminho de execução deste programa
caminho = os.path.dirname(os.path.abspath(__file__))

# classe obstáculo
class Obstacle(pygame.sprite.Sprite):
    #Classe Construtor
    def __init__(self, x, y, arquivo_imagem):
        super().__init__()
        arquivo_imagem = os.path.join(caminho, arquivo_imagem)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 1

    #atualizar a movimentação pelo ticketrate
    def update(self):
        if (self.rect.y >= FrameHeight):
            self.rect.y = 1
        self.rect.y = self.rect.y + self.velocity_y