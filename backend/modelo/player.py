import pygame, os
from backend.config.config import *
from backend.modelo.shoot import *
import random

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
        self.nome = nome #User's name can be found on database
        self.pontos = 0 #User points based on kills
        self.estrategia = 1 # Default user manual mode
        self.vel = 1 #Default velocity
        self.previous_time = pygame.time.get_ticks() #Variable to delay shoots
        self.platform_shoot = pygame.sprite.Group()  #Set of shoots created
        self.remove_shoot = [] #List to remove collided shoots
 
    # Tipo de jogadores:
    def check_keys(self):
        max = 1870 #MaxWidth - spriteWidth

        #Jogador manual
        if self.estrategia == 1:
            pk = pygame.key.get_pressed()
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
    
    #Sistema de tiro
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.previous_time > 500: #Create a delay of 500ms
            self.previous_time = pygame.time.get_ticks() #Reset time
            self.platform_shoot.add(Shoot(self.rect.x + 16 - 5, self.rect.y, 5, 20)) # create bullet and add to the group

    #Check Bullet collisions
    def collisionShoots(self, obstacles_group):
        #Adds collided shoots to the list and count player's points
        for tiro in self.platform_shoot:
            quem_colidiu_com_tiro = pygame.sprite.spritecollide(tiro, obstacles_group, False)
            if quem_colidiu_com_tiro:
                self.pontos += len(quem_colidiu_com_tiro)
                obstacles_group.remove(quem_colidiu_com_tiro)
                print("Player 2: objetos coletados:", self.pontos)
                self.remove_shoot.append(tiro)
        
        #Remove shoots
        for t in self.remove_shoot:
            self.platform_shoot.remove(t)
