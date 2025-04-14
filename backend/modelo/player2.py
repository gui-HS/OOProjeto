import pygame, os

FrameHeight = 768
FrameWidth = 768

# obter caminho de execução deste programa
caminho = os.path.dirname(os.path.abspath(__file__))


# classe JOGADOR!
class Player2(pygame.sprite.Sprite):

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
        # captura alguma eventual tecla que foi pressionada
        pk = pygame.key.get_pressed()
        # alguma tecla especial foi pressionada?
        if pk[pygame.K_LEFT]:
            self.rect.x -= 2
        if pk[pygame.K_RIGHT]:
            self.rect.x += 2 

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