import pygame, os
from backend.config.config import *
from backend.modelo.shoot import *
import random
from backend.modelo.delay import *
from backend.modelo.collisionObject import *

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
        self.lifes = 3
        self.estrategia = 1 # Default user manual mode
        self.vel = 1 #Default velocity
        self.platform_shoot = pygame.sprite.Group()  #Set of shots created
        self.remove_shoot = [] #List to remove collided shoots
        self.delay1 = Delay()
    
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

        #Sharp shooter
        elif self.estrategia == 4:
            if self.rect.x <= 0:
                self.vel = self.vel*-1
                self.rect.x = 1
            if self.rect.x >= max:
                self.vel = self.vel*-1
                self.rect.x = max-1
            self.rect.x += self.pontos * self.vel

        #Teleporter
        elif self.estrategia == 5:
            self.rect.x = random.randint(0 , 1870)

    #Sistema de colisao:
    def salvar_xy(self):
        self.antes_x = self.rect.x
        self.antes_y = self.rect.y

    def restaurar_xy(self):    
        self.rect.x = self.antes_x
        self.rect.y = self.antes_y
    
    # verificar se houve alguma atualização
    # na situação do jogador
    def update(self):
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
    
    def isDead(self, player, player_group):
        if self.lifes <= 0:
            player_group.remove(player)

    #Sistema de tiro
    def shoot(self):
        #Not shoot while dead
        if self.lifes <= 0:
            pass
        else:
            if self.delay1.delay(500): #Delay shots
                self.platform_shoot.add(Shoot(self.rect.x + 16 - 5, self.rect.y, 5, 20)) # create bullet and add to the group
                shoot_sound = pygame.mixer.Sound("sounds/soundEffects/Shoot_01.mp3")
                pygame.mixer.Sound.play(shoot_sound)
                shoot_sound.set_volume(0.2)


    def collisionShots(self, obstacles_group):
        #Check to see if shoots colided with obstacles
        if CollisionObject().destroyBothObj(self.platform_shoot, obstacles_group):
            self.pontos += 1 #Adds one point and remove obstacle
 
    def collisionObstacles(self, player, obstacles_group):
        #If player colided with any obstacle, then delete obstacle and subtract player's life by one
        if CollisionObject().destroy2Obj(player, obstacles_group):
            self.lifes -= 1
            crash_sound = pygame.mixer.Sound("sounds/soundEffects/Hit_02.mp3")
            pygame.mixer.Sound.play(crash_sound)