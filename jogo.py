import pygame
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *
import time

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
FPS = 300 #Set default FPS (not working as expected)
prev_time = time.time() #Get current time in seconds
pygame.display.set_caption("Jogo de navizinha") #Game name
screen = pygame.display.set_mode((FrameWidth,FrameHeight)) #Set width and height of screen
bg = pygame.image.load("imagem\space4.jpg").convert() #Background Image
x = 290 #Player initial position X
y = 850 #Player inicial position Y
blue = (255,255,255) #Hud color

# carrega jogador do banco de dados
jogador = db.session.query(Jogador).first()
jogador2 = db.session.query(Jogador).filter_by(nome = "Fernando").first()

# cria o jogador em modelo de classe do jogo (usando os jogadores carregados anteriormente)
player1 = Player(x, y, jogador2.nome, jogador2.nome_imagem)
player2 = Player(x, y, jogador2.nome, jogador2.nome_imagem)
player3 = Player(x, y, jogador2.nome, jogador2.nome_imagem)

#Set player estrategy
player1.estrategia = 2
player2.estrategia = 3
player3.estrategia = 5

#Create and add players to the group
player_group = pygame.sprite.Group()
player_group.add(player1)
player_group.add(player2)
player_group.add(player3)

#----------------------------- Main Game Loop -----------------------------#
running = True

while running:
    pk = pygame.key.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    if pk[pygame.K_ESCAPE]:
        running = False
    
    if (player1.pontos >= 200 or player2.pontos >= 200 or player3.pontos >= 200):
            platform_group.empty()
            print(f"O P1 Conseguiu:{player1.pontos}, " 
            f"O P2 Conseguiu:{player2.pontos}")
            platform_group.empty()
    
    #Limitar o FPS do jogo:
    current_time = time.time()
    dt = current_time - prev_time

    sleep_time = 1./FPS - dt
    if sleep_time > 0:
        time.sleep(sleep_time)
    screen.blit(bg, (0,0))
    
    #Iterate through all players
    for player in player_group:
        if player.lifes > 0:
            player.shoot() #Shoot 
            player.collisionShots(platform_group) #Check if shots have colided
            player.collisionObstacles(player, platform_group) #Check if player colided with objects
        else:
            #If player lifes == 0, then remove from group
            player_group.remove(player)
            explosion_sound = pygame.mixer.Sound("sounds/soundEffects/Explosion_00.mp3")
            pygame.mixer.Sound.play(explosion_sound)
            explosion_sound.set_volume(0.5)

    escrever_texto(screen, 10, 10, f"player1 pontos: {player1.pontos}", blue)
    escrever_texto(screen, 210, 10, f"player2 pontos: {player2.pontos}", blue)
    escrever_texto(screen, 410, 10, f"player3 pontos: {player3.pontos}", blue)

    player_group.draw(screen) # desenhar jogadores
    platform_group.draw(screen) # mostra os obstáculos
    player1.platform_shoot.draw(screen) # desenhar os tiros
    player2.platform_shoot.draw(screen) # desenhar os tiros
    player3.platform_shoot.draw(screen) # desenhar os tiros
    platform_group.update() # movimenta todos os obstáculos
    player1.platform_shoot.update() # movimenta os tiros
    player2.platform_shoot.update() # movimenta os tiros
    player3.platform_shoot.update() # movimenta os tiros
    player_group.update()
    pygame.display.flip() # atualiza a tela
    
    # atualizar a tela
    # https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
    pygame.display.update()   

    clock.tick(1000)
pygame.quit()