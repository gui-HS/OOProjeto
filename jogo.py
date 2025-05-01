import pygame, math
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *
import time

pygame.init()
clock = pygame.time.Clock()

FPS = 600
prev_time = time.time()

# PYGAME FRAME WINDOW
pygame.display.set_caption("Jogo de navizinha")
screen = pygame.display.set_mode((FrameWidth,FrameHeight))

# IMAGE
bg = pygame.image.load("imagem\space4.jpg").convert()

#Cor do HUD de pontos
blue = (255,255,255)

# criação da fonte (apenas uma vez)
font = pygame.font.SysFont(None, 25)

# função para escrever texto na tela
def escrever_texto( janela, x, y, msg, color ):
    text = font.render( msg, True, color)
    janela.blit(text, ( x, y ) )

# obter caminho de execução deste programa
caminho = os.path.dirname(os.path.abspath(__file__))

# posições iniciais do player
x = 290
y = 850

# carrega jogador do banco de dados
jogador = db.session.query(Jogador).first()
jogador2 = db.session.query(Jogador).filter_by(nome = "Fernando").first()

# cria o jogador em modelo de classe do jogo (usando os jogadores carregados anteriormente)
player = Player(x, y, jogador.nome, jogador.nome_imagem)
player2 = Player(x, y, jogador2.nome, jogador2.nome_imagem)

player.estrategia = 2
player2.estrategia = 3

# cria grupo de jogadores
player_group = pygame.sprite.Group()
# adiciona jogador no grupo :-)
player_group.add(player)
player_group.add(player2)

# Main game loop
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