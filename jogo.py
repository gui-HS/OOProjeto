import pygame, math
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *
from backend.running.instanciaTiro import tiros
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
    
# DEFINING MAIN VARIABLES IN SCROLLING
scroll = 0
    
# CHANGE THE BELOW 1 TO UPPER NUMBER IF
# YOU GET BUFFERING OF THE IMAGE
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
tiles = math.ceil(FrameWidth / bg.get_width()) + 4

#Frame para cadência de tiros:
previous_time = pygame.time.get_ticks()

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
y = 620

# carrega jogador do banco de dados
jogador = db.session.query(Jogador).first()
jogador2 = db.session.query(Jogador).filter_by(nome = "Fernando").first()

# cria o jogador em modelo de classe do jogo (usando os jogadores carregados anteriormente)
player = Player1(x, y, jogador.nome, jogador.nome_imagem)
player2 = Player1(x, y, jogador2.nome, jogador2.nome_imagem)

player.estrategia = 2
player2.estrategia = 3

# cria grupo de jogadores
player_group = pygame.sprite.Group()
# adiciona jogador no grupo :-)
player_group.add(player)
player_group.add(player2)

# cria grupo de tiros
platform_shot = pygame.sprite.Group()
platform_shot2 = pygame.sprite.Group()

# Main game loop
running = True
grupo1 = True

# Configuração tiros
largura_tiro = 10
altura_tiro = 20

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
            #grupo1 = False
    
    #Limitar o FPS do jogo:
    current_time = time.time()
    dt = current_time - prev_time

    sleep_time = 1./FPS - dt
    if sleep_time > 0:
        time.sleep(sleep_time)
    screen.blit(bg, (0,0))

    #tiros(player, player2, largura_tiro, altura_tiro, platform_shot, platform_shot, previous_time)


    if player.estrategia == 1:
    #Tiro simultâneo dois player
        if pk[pygame.K_p] and pk[pygame.K_SPACE]: 
            if pk[pygame.K_SPACE]: 
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > 500:
                    previous_time = current_time
                    novo_tiro = Shot(player.rect.x + 16 - (largura_tiro/2), player.rect.y, largura_tiro, altura_tiro) # cria um tiro
                    platform_shot.add(novo_tiro)
                    novo_tiro = Shot(player2.rect.x + 16 - (largura_tiro/2), player2.rect.y, largura_tiro, altura_tiro) # cria um tiro
                    platform_shot2.add(novo_tiro)

        #Tiro player 1
        if pk[pygame.K_SPACE]: 
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > 500:
                previous_time = current_time
                novo_tiro = Shot(player.rect.x + 16 - (largura_tiro/2), player.rect.y, largura_tiro, altura_tiro) # cria um tiro
                platform_shot.add(novo_tiro)

        #Tiro player 2
        if pk[pygame.K_p]: 
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > 500:
                previous_time = current_time
                novo_tiro = Shot(player2.rect.x + 16 - (largura_tiro/2), player2.rect.y, largura_tiro, altura_tiro) # cria um tiro
                platform_shot2.add(novo_tiro)

    elif player.estrategia == 2 or player2.estrategia == 3:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            novo_tiro = Shot(player.rect.x + 16 - (largura_tiro/2), player.rect.y, largura_tiro, altura_tiro) # cria um tiro
            novo_tiro2 = Shot(player2.rect.x + 16 - (largura_tiro/2), player2.rect.y, largura_tiro, altura_tiro) # cria um tiro
            platform_shot.add(novo_tiro)
            platform_shot2.add(novo_tiro2)



    # lista de tiros de colidiram e serão removidos:
    remover_tiros = []

    # percorrer cada tiro
    for tiro in platform_shot:

        quem_colidiu_com_tiro = pygame.sprite.spritecollide(tiro, platform_group, False)

        # se colidiu...
        if quem_colidiu_com_tiro:
            # contabiliza pontos para o jogador :-) depende de quantos coletou
            player.pontos += len(quem_colidiu_com_tiro)
            # remove o obstáculo do grupo
            platform_group.remove(quem_colidiu_com_tiro)
            # mostra quantos objetos foram atingidos
            print("Player 1: objetos coletados:", player.pontos)
            # marca o tiro para ser removido
            # por que eu não removo esse tiro imediatamente?
            # não é boa prática tirar tábuas da ponte enquanto estou andando sobre a ponte
            remover_tiros.append(tiro)

    for tiro in platform_shot2:
        quem_colidiu_com_tiro = pygame.sprite.spritecollide(tiro, platform_group, False)
        if quem_colidiu_com_tiro:
            player2.pontos += len(quem_colidiu_com_tiro)
            platform_group.remove(quem_colidiu_com_tiro)
            print("Player 2: objetos coletados:", player2.pontos)
            remover_tiros.append(tiro)

    print(player2.rect.x)
    # remove os tiros que devem ser removidos
    for t in remover_tiros:
        platform_shot.remove(t)

    for t in remover_tiros:
        platform_shot2.remove(t)

    #Exibir pontos na tela
    escrever_texto(screen, 10, 10, f"P1 pontos: {player.pontos}", blue)
    escrever_texto(screen, 630, 10, f"p2 pontos: {player2.pontos}", blue)

    player_group.draw(screen) # desenhar jogadores
    platform_group.draw(screen) # desenhar obstaculos
    platform_group.draw(screen) # mostra os obstáculos
    platform_shot.draw(screen) # desenhar os tiros
    platform_shot2.draw(screen) # desenhar os tiros
    platform_group.update() # movimenta todos os obstáculos
    platform_shot.update() # movimenta os tiros
    platform_shot2.update() # movimenta os tiros
    player_group.update(platform_group)
    pygame.display.flip() # atualiza a tela
    
    # atualizar a tela
    # https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
    pygame.display.update()   

    clock.tick(1000)
pygame.quit()