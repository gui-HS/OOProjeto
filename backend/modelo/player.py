import pygame, os
from backend.config.config import *

# obter caminho de execução deste programa
caminho = os.path.dirname(os.path.abspath(__file__))

#Classe generica para jogador sem controles
class Player(pygame.sprite.Sprite):

    # construtor
    def __init__(self, x, y, nome, nome_imagem):
        super().__init__()
        arquivo_imagem = os.path.join(caminho, nome_imagem)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.nome = nome
        self.pontos = 0
 
    # verificação de teclas
    def check_keys(self):
        pass

    #Sistema de colisao:
    def salvar_xy(self):
        self.antes_x = self.rect.x
        self.antes_y = self.rect.y

    def restaurar_xy(self):    
        self.rect.x = self.antes_x
        self.rect.y = self.antes_y
    
    # verificar se houve alguma atualização
    # na situação do jogador
    def update(self, pg):
        self.salvar_xy()
        #self.rect.y += self.y_velocity        
        self.check_keys()
        # colidiu retorna o grupo de sprites que colidiu :-)
    # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > FrameWidth:
            self.rect.right = FrameWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= FrameHeight:
            self.rect.bottom = FrameHeight