from backend.modelo.player import Player
from backend.modelo.jogador import Jogador
import pygame
from backend.config.config import *
from backend.objetos.obstaculo import *
import time
from backend.modelo.resultadoDaPartida import *
from backend.modelo.delay import *

class Partida:
    def __init__(self):
        x = 290 #Player initial position X
        y = 850 #Player inicial position Y

        # carrega jogador do banco de dados
        pBlue = db.session.query(Jogador).first()
        pGreen = db.session.query(Jogador).filter_by(id = 2).first()
        pRed = db.session.query(Jogador).filter_by(id = 3).first()
        pPink = db.session.query(Jogador).filter_by(id = 4).first()
        pYellow = db.session.query(Jogador).filter_by(id = 5).first()

        # cria o jogador em modelo de classe do jogo (usando os jogadores carregados anteriormente)
        self.player1 = Player(x, y, pBlue.nome, pBlue.nome_imagem)
        self.player2 = Player(x, y, pGreen.nome, pGreen.nome_imagem)
        self.player3 = Player(x, y, pRed.nome, pRed.nome_imagem)
        self.player4 = Player(x, y, pPink.nome, pPink.nome_imagem)
        self.player5 = Player(x, y, pYellow.nome, pYellow.nome_imagem)

        #Set player estrategy
        self.player1.estrategia = 2
        self.player2.estrategia = 3
        self.player3.estrategia = 4
        self.player4.estrategia = 5
        self.player5.estrategia = 6
    
    def partida(self, player_group):
        pygame.init()
        #----------------------------- Variables -----------------------------# 
        caminho = os.path.dirname(os.path.abspath(__file__))
        font = pygame.font.SysFont(None, 25) #Letter font

        def escrever_texto( janela, x, y, msg, color ):
            text = font.render( msg, True, color)
            janela.blit(text, ( x, y ) )

        backgroundMusic = pygame.mixer.Sound("sounds/music/WAV/Venus.wav")

        #Play background music
        pygame.mixer.music.load("sounds/music/WAV/Venus.wav")
        pygame.mixer.music.play(-1)


        clock = pygame.time.Clock()
        FPS = 900 #Set default FPS (not working as expected)
        prev_time = time.time() #Get current time in seconds
        pygame.display.set_caption("Jogo de navizinha") #Game name
        screen = pygame.display.set_mode((FrameWidth,FrameHeight)) #Set width and height of screen
        bg = pygame.image.load("imagem\space4.jpg").convert() #Background Image
        blue = (255,255,255) #Hud color
        #----------------------------- Main Game Loop -----------------------------#
        running = True
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((FrameWidth,FrameHeight)) #Set width and height of screen

        #instanciate obstacles
        obsctacleInstance()

        while running:
            pk = pygame.key.get_pressed()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            
            if (pk[pygame.K_ESCAPE]):
                running = False
            
            for player in player_group:
                    if (player.pontos >= 2000000):
                        print(f"O P1 Conseguiu:{player}")
                        running = False
            

            if len(player_group.sprites()) == 0 or len(platform_group.sprites()) ==0:
                running = False

            #Limitar o FPS do jogo:
            current_time = time.time()
            dt = current_time - prev_time

            sleep_time = 1./FPS - dt
            if sleep_time > 0:
                time.sleep(sleep_time)
            screen.blit(bg, (0,0))

            for player in player_group:
                player.shoot() #Shoot
                player.collisionShots(platform_group) #Remove shots who colided with obstacles
                player.collisionObstacles(player, platform_group) #Check if player colided with objects
                player.isDead() #Delete player if dead
            
            i = 10
            for player in player_group:
                escrever_texto(screen, i, 10, f"{player.nome} pontos: {player.pontos}", pygame.Color('blue'))
                i += 250

            for player in player_group:
                player.platform_shoot.draw(screen) # desenhar os tiros
                player.platform_shoot.update() # movimenta os tiros

            player_group.draw(screen) # desenhar jogadores
            platform_group.draw(screen) # mostra os obstáculos
            platform_group.update() # movimenta todos os obstáculos
            player_group.update()
            pygame.display.flip() # atualiza a tela
            
            pygame.display.update()

            clock.tick(1000)

        player_group.empty()
        platform_group.empty()
        pygame.quit()

    def onePlayer(self):
        player_group = pygame.sprite.Group()
        player_group.add(self.player2)
        self.partida(player_group)
        p1 = ResultadoDaPartida(lifes=self.player2.lifes, strategy=self.player2.estrategia, points=self.player2.pontos, type=1)
        db.session.add(p1)
        db.session.commit()
        self.resetPlayers()
        return

    def twoPlayers(self):
        player_group = pygame.sprite.Group()
        player_group.add(self.player1)
        player_group.add(self.player2)
        self.partida(player_group)
        print("2 Player Simulation finished")
        self.resetPlayers()
        return
    

    '''
    players.txt
    número, vidas, estrategia, pontos por tiro
    1, 10, 1, 20
    2, 15, 2, 15
    3, 5, 1, 30
    
    
    batalhas.txt
    1,2
    1,3
    1,2,3
    

    joga sozinho até haver jogadoes com vida
    quando morrerm os bichso, aparem d novo
    '''

    def threePlayers(self):
        player_group = pygame.sprite.Group()
        player_group.add(self.player1)
        player_group.add(self.player2)
        player_group.add(self.player3)
        self.partida(player_group)
        print("3 Player Simulation finished")
        self.resetPlayers()
        return

    def allPlayers(self):
        player_group = pygame.sprite.Group()
        player_group.add(self.player1)
        player_group.add(self.player2)
        player_group.add(self.player3)
        player_group.add(self.player4)
        player_group.add(self.player5)
        self.partida(player_group)
        playerList = [self.player1, self.player2, self.player3, self.player4, self.player5]
        for i in playerList:
            p1 = ResultadoDaPartida(lifes=i.lifes, strategy=i.estrategia, points=i.pontos, type=5)
            db.session.add(p1)
            db.session.commit()
        self.resetPlayers()
        return

    def resetPlayers(self):
        playerList = [self.player1, self.player2, self.player3, self.player4, self.player5]
        for i in playerList:
            i.lifes = 3
            i.pontos = 0
            i.platform_shoot = pygame.sprite.Group()
            i.remove_shoot = []
            i.delay1 = Delay()
            i.delay2 = Delay()
