import pygame, time
from backend.modelo import *
from backend.config.config import *
from backend.objetos.obstaculo import *
from sqlalchemy import desc
from datetime import datetime

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
        obsctacleInstance(1)

        #instantiate match
        player_list = self.batalha()

        bla = 0
        player_group = player_list[0]

        #times
        begin = pygame.time.get_ticks()
        matchTime = pygame.time.get_ticks() - begin
        
        while running:
            
            matchTime = (pygame.time.get_ticks() - begin)//1000
            print(matchTime//1000)
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
                    #self.batalhaDB(player_group, matchTime)
                    player_group = player_list[bla]
                    platform_group.empty()
                    obsctacleInstance(1)
                    begin = pygame.time.get_ticks()

            if len(player_group.sprites()) == 0 or len(platform_group.sprites()) ==0:
                if  bla >= len(player_list)-1:
                    running = False
                    self.batalhaDB(player_group, matchTime)
                else:
                    bla += 1
                    self.batalhaDB(player_group, matchTime)
                    player_group = player_list[bla]
                    obsctacleInstance(1)
                    begin = pygame.time.get_ticks()

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

            #Write time
            escrever_texto(screen, 1820, 10, f"Time: {matchTime}", (255, 255, 255))

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

            pygame.draw.rect(bg, (0, 0, 0), pygame.Rect(0, 0, FrameWidth, FrameHeight))

            #Most points Column
            self.top10Column(bg,"points",50,150)

            #Most lifes Column
            self.top10Column(bg,"lifes",700,150)

            #Most time Column 
            self.top10Column(bg,"time",1350,150)

            screen.blit(bg, (0,0))

            pygame.display.flip() # atualiza a tela
            pygame.display.update()

        pygame.quit()

    def top10Column(self, screen, columnName, x, y):
        font = pygame.font.SysFont(None, 35) #Letter font
        def escrever_texto( janela, x, y, msg, color ):
            text = font.render( msg, True, color)
            janela.blit(text, ( x, y ) )

        #Most column name Column 
        escrever_texto(screen, x, 120, f"Most {columnName}", (255,255,255)) #Get in decrescent order
        bla = db.session.query(ResultadoDaPartida.ResultadoDaPartida).order_by(desc(getattr(ResultadoDaPartida.ResultadoDaPartida, columnName))).limit(15).all()

        if columnName == "time": #GET IN CRESCENT ORDER
            bla = db.session.query(ResultadoDaPartida.ResultadoDaPartida).order_by(getattr(ResultadoDaPartida.ResultadoDaPartida, columnName)).limit(15).all()
        
        for resultado in bla:
            mostrar = str(resultado).split()
            
            
            dict = {"id":0, "lifes":1, "strategy":2, "shotPoints":3, "points":4, "time":5}
            mostrar2 = dict[columnName]

            for i in mostrar[mostrar2]:
                print(i)
                if ord(i) == 44: #Remove , at the end
                    mostrar[mostrar2] = mostrar[mostrar2][:-1]

            text = " player" + str(mostrar[0][:-1]) + ": " + str(mostrar[mostrar2]) + ", str: " + str(mostrar[2][:-1])
            escrever_texto(screen, x, y, text, (255,255,255))
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

    def batalhaDB(self, player_group, time):
        for player2 in player_group:
            p1  = ResultadoDaPartida.ResultadoDaPartida(lifes = player2.lifes, strategy = player2.estrategia, shotPoints = player2.playerDB.shotPoints, points = player2.pontos, time = time)
            db.session.add(p1)
            db.session.commit()

if __name__ == "__main__":
    Partida().addPlayers() #Add players to database
    Partida().partida() #Iniciate match based on the configuration file batalhas.txt