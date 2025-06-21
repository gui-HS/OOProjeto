import pygame
from backend.modelo import *
from backend.config.config import *
from backend.objetos.obstaculo import *
from sqlalchemy import desc

class Partida:

    def __init__(self):
        self.match = 0

    def partida(self):
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
        pygame.display.set_caption("Jogo de navizinha") #Game name
        screen = pygame.display.set_mode((FrameWidth,FrameHeight)) #Set width and height of screen
        bg = pygame.image.load("imagem\space4.jpg").convert() #Background Image
        
        #----------------------------- Main Game Loop -----------------------------#
        clock = pygame.time.Clock()
        running = True

        screen = pygame.display.set_mode((FrameWidth,FrameHeight)) #Set width and height of screen

        #instanciate obstacles
        obsctacleInstance()

        #instantiate match
        player_list = self.batalha()

        bla = 0
        player_group = player_list[0]
        
        while running:
            pk = pygame.key.get_pressed()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.running = False
            
            if (pk[pygame.K_ESCAPE]):
                running = False

            if (pk[pygame.K_n]):
                if  bla >= len(player_list)-1:
                    running = False
                else:
                    bla += 1
                    self.batalhaDB(player_group)
                    player_group = player_list[bla]
                    platform_group.empty()
                    obsctacleInstance()

            if len(player_group.sprites()) == 0 or len(platform_group.sprites()) ==0:
                if  bla >= len(player_list)-1:
                    running = False
                else:
                    bla += 1
                    self.batalhaDB(player_group)
                    player_group = player_list[bla]
                    obsctacleInstance()

            screen.blit(bg, (0,0))
            for player in player_group:
                player.shoot() #Shoot
                player.collisionShots(platform_group) #Remove shots who colided with obstacles
                player.collisionObstacles(player, platform_group) #Check if player colided with objects
                player.isDead() #Delete player if dead
            
            i = 10
            for player in player_group:
                escrever_texto(screen, i, 10, f"{player.playerDB.nome} pontos: {player.pontos}", pygame.Color(player.color))
                i += 250

            for player in player_group:
                player.platform_shoot.draw(screen) # desenhar os tiros
                player.platform_shoot.update() # movimenta os tiros

            player_group.draw(screen) # desenhar jogadores
            platform_group.draw(screen) # mostra os obstáculos
            platform_group.update() # movimenta todos os obstáculos
            player_group.update() # movimenta os players
            pygame.display.flip() # atualiza a tela
            pygame.display.update()

            clock.tick(1000)

        scoreboard = True

        while scoreboard:
            pk = pygame.key.get_pressed()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.running = False
            
            if (pk[pygame.K_ESCAPE]):
                scoreboard = False

            pygame.draw.rect(bg, (255, 192, 203), pygame.Rect(210, 100, 1500, 900))


            #Most points Column
            self.top10Column(bg,"points",280,150)

            #Most lifes Column
            self.top10Column(bg,"lifes",820,150)

            screen.blit(bg, (0,0))

            pygame.display.flip() # atualiza a tela
            pygame.display.update()

        pygame.quit()

    def top10Column(self, screen, columnName, x, y):
        font = pygame.font.SysFont(None, 25) #Letter font
        def escrever_texto( janela, x, y, msg, color ):
            text = font.render( msg, True, color)
            janela.blit(text, ( x, y ) )

        #Most points Column 
        bla = db.session.query(ResultadoDaPartida.ResultadoDaPartida).order_by(desc(getattr(ResultadoDaPartida.ResultadoDaPartida, columnName))).limit(15).all()
        escrever_texto(screen, x, 120, f"Most {columnName}", (255,255,255))
        
        for resultado in bla:
            mostrar = str(resultado).split()
                
            texto = "ID: " + str(mostrar[0]) + " Lifes: " + str(mostrar[1]) + " Strategy: " + str(mostrar[2]) + \
                    " ShotPoints: " + str(mostrar[3]) + " Points: " + str(mostrar[4])
            escrever_texto(screen, x, y, texto, (255,255,255))
            y += 50
        
    def formatFile(self,file):
        file = open(file)
        file = file.readlines() #Create a list by every line of the file
        file = file[1:] #Cut the first comment
        g = [] #List to get the file without the \n at the end
        for i in file:
            i = i[:len(i)-1] #Cut the \n at the final
            g.append(i)
        return g
            
    def addPlayers(self):
        playerSet = self.formatFile("player.txt") #Player settings file

        for playerSettings in playerSet:
            settings = playerSettings.split(",")
            #Use the values os the settings list as the new player's attributes
            p1 = Jogador.Jogador(nome="player"+settings[0], pontos = 0, lifes = settings[1], shotPoints = settings[3], estrategia = settings[2], color = settings[4])
            db.session.add(p1)
            db.session.commit()

    def batalha(self):
        batalha = self.formatFile("batalhas.txt")
        player_group = pygame.sprite.Group()
        list_matches = []

        for battle in batalha:
            ids = battle.split(",")
            for playerID in ids:
                player = Player.Player(290, 850, playerID)
                player_group.add(player)
            list_matches.append(player_group)
            player_group = pygame.sprite.Group()
        return list_matches

    def batalhaDB(self, player_group):
        for player2 in player_group:
            p1  = ResultadoDaPartida.ResultadoDaPartida(lifes = player2.lifes, strategy = player2.estrategia, shotPoints = player2.playerDB.shotPoints, points = player2.pontos)
            db.session.add(p1)
            db.session.commit()

    '''
    joga sozinho até haver jogadoes com vida
    quando morrerm os bichos, aparem d novo
    '''
    
if __name__ == "__main__":
    Partida().addPlayers() #Add players to database
    Partida().partida() #Iniciate match based on the configuration file batalhas.txt