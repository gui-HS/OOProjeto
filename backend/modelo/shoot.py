from backend.config.config import *

caminho = os.path.dirname(os.path.abspath(__file__))

class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        arquivo_imagem = os.path.join(caminho, "../../imagem/shrok.png")
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = -4 # o tiro está subindo, velocidade y negativa
        
    def update(self):
        if (self.rect.y > 0): # se NÃO chegou no topo da tela
            self.rect.y = self.rect.y + self.velocity_y # move o tiro para cima
        else: # senão
            self.kill() # remove o tiro, porque ele chegou no topo da tela