import pygame, os, random
from backend.config.config import *
from backend.modelo.Jogador import *
from backend.modelo.Delay import *
from backend.modelo.Shoot import *
from backend.modelo.CollisionObject import *

# obter caminho de execução deste programa
caminho = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):

    # construtor
    def __init__(self, x, y, playerID):
        super().__init__()
        self.playerDB = db.session.query(Jogador).filter_by(id = playerID).first()
        self.color = self.playerDB.color #Player's color and HUD color
        self.image = pygame.image.load("imagem\\nave" + self.color + ".png") #Load the spaceship sprite with the chosen color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pontos = 0 #User points based on kills. The quantity depends on the DB estrategy points
        self.lifes = self.playerDB.lifes
        self.estrategia = self.playerDB.estrategia # Default user manual mode
        self.vel = 1 #Default velocity
        self.platform_shoot = pygame.sprite.Group()  #Set of shots created
        self.remove_shoot = [] #List to remove collided shoots
        self.delay1 = Delay()
        self.delay2 = Delay()

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
            if self.pontos == 0:
                self.rect.x += 1 * self.vel

        #Teleporter
        elif self.estrategia == 5:
            if self.delay2.delay(200):
                self.rect.x = random.randint(0 , 1870)

        #Tick shooter
        elif self.estrategia == 6:
            if self.rect.x <= 0:
                self.vel = self.vel*-1
                self.rect.x = 1
            if self.rect.x >= max:
                self.vel = self.vel*-1
                self.rect.x = max-1
            self.rect.x += pygame.time.get_ticks()//100 * self.vel

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
    
    def isDead(self):
        if self.lifes <= 0:
            self.kill()

            #Sound effects
            explosion_sound = pygame.mixer.Sound("sounds/soundEffects/Explosion_00.mp3")
            pygame.mixer.Sound.play(explosion_sound)
            explosion_sound.set_volume(0.5)

    #Sistema de tiro
    def shoot(self):
        #Not shoot while dead
        if self.isDead():
            pass
        else:
            if self.delay1.delay(500): #Delay shots
                self.platform_shoot.add(Shoot(self.rect.x + 16 - 5, self.rect.y, 5, 20))

                #Sound Effects:
                shoot_sound = pygame.mixer.Sound("sounds/soundEffects/Shoot_01.mp3")
                pygame.mixer.Sound.play(shoot_sound)
                shoot_sound.set_volume(0.2)


    def collisionShots(self, obstacles_group):
        #Check to see if shoots colided with obstacles
        if CollisionObject().destroyBothObj(self.platform_shoot, obstacles_group):
            self.pontos += self.playerDB.shotPoints #Adds points
            
 
    def collisionObstacles(self, player, obstacles_group):
        #If player colided with any obstacle, then delete obstacle and subtract player's life by one
        if CollisionObject().destroy2Obj(player, obstacles_group):
            self.lifes -= 1

            #Sound Effects:
            crash_sound = pygame.mixer.Sound("sounds/soundEffects/Hit_02.mp3")
            pygame.mixer.Sound.play(crash_sound)