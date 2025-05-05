import pygame
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *
from backend.objetos.texto import *
import time

pygame.init()

#----------------------------- Variables -----------------------------#

caminho = os.path.dirname(os.path.abspath(__file__))
font = pygame.font.SysFont(None, 25) #Letter font
def escrever_texto( janela, x, y, msg, color ):
    text = font.render( msg, True, color)
    janela.blit(text, ( x, y ) )


clock = pygame.time.Clock()     
FPS = 600 #Set default FPS (not working as expected)
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
player = Player(x, y, jogador.nome, jogador.nome_imagem)
player2 = Player(x, y, jogador2.nome, jogador2.nome_imagem)

#Set player estrategy
player.estrategia = 2
player2.estrategia = 3

#Create and add players to the group
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(player2)

#----------------------------- Main Game Loop -----------------------------#
running = True

while running:
    pk = pygame.key.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    if pk[pygame.K_ESCAPE]:
        running = False
    
    if player.pontos == 20 or player2.pontos == 20:
            platform_group.empty()
            print(f"O P1 Conseguiu:{player.pontos}, " 
            f"O P2 Conseguiu:{player2.pontos}")
            platform_group.empty()
    
    #Limitar o FPS do jogo:
    current_time = time.time()
    dt = current_time - prev_time

    sleep_time = 1./FPS - dt
    if sleep_time > 0:
        time.sleep(sleep_time)
    screen.blit(bg, (0,0))

    player.shoot()
    player2.shoot()
    
    player.collisionShoots(platform_group)
    player2.collisionShoots(platform_group)

    #Exibir pontos na tela
    escrever_texto(screen, 10, 10, f"P1 pontos: {player.pontos}", blue)
    escrever_texto(screen, 630, 10, f"p2 pontos: {player2.pontos}", blue)

    player_group.draw(screen) # desenhar jogadores
    platform_group.draw(screen) # desenhar obstaculos
    platform_group.draw(screen) # mostra os obstáculos
    player.platform_shoot.draw(screen) # desenhar os tiros
    player2.platform_shoot.draw(screen) # desenhar os tiros
    platform_group.update() # movimenta todos os obstáculos
    player.platform_shoot.update() # movimenta os tiros
    player2.platform_shoot.update() # movimenta os tiros
    player_group.update(platform_group)
    pygame.display.flip() # atualiza a tela
    
    # atualizar a tela
    # https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
    pygame.display.update()   

    clock.tick(1000)
pygame.quit()