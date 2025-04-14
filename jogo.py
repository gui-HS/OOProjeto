import pygame, math
from backend.config.config import *
from backend.modelo import *
from backend.objetos.obstaculo import *

pygame.init()
clock = pygame.time.Clock()
  
FrameHeight = 768
FrameWidth = 768


# PYGAME FRAME WINDOW
pygame.display.set_caption("Jogo de navizinha")
screen = pygame.display.set_mode((FrameWidth,FrameHeight))

# IMAGE
bg = pygame.image.load("imagem/espaco2.png").convert()
  
# DEFINING MAIN VARIABLES IN SCROLLING
scroll = 0
   
# CHANGE THE BELOW 1 TO UPPER NUMBER IF
# YOU GET BUFFERING OF THE IMAGE
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
tiles = math.ceil(FrameWidth / bg.get_width()) + 1

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
jogador2 = db.session.query(Jogador2).first()

# cria o jogador em modelo de classe do jogo
player = Player(x, y, jogador.nome, jogador.nome_imagem)
player2 = Player2(x, y, jogador2.nome, jogador2.nome_imagem)

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

# Configuração tiros
largura_tiro = 10
altura_tiro = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    if player.pontos == 20 or player2.pontos == 20:
            running = False
            print(f"O P1 Conseguiu:{player.pontos}, " +\
            f"O P2 Conseguiu:{player2.pontos}")
  
    # APPENDING THE IMAGE TO THE BACK
    # OF THE SAME IMAGE
    i = 0
    while(i < tiles):
        screen.blit(bg, (bg.get_width()*i
                         + scroll, 0))
        i += 1
    # FRAME FOR SCROLLING
    scroll -= 1
  
    # RESET THE SCROLL FRAME
    if abs(scroll) > bg.get_width():
        scroll = 0
    # CLOSINF THE FRAME OF SCROLLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pk = pygame.key.get_pressed()


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

    if pk[pygame.K_p]: 
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > 500:
                    previous_time = current_time
                    novo_tiro = Shot(player2.rect.x + 16 - (largura_tiro/2), player2.rect.y, largura_tiro, altura_tiro) # cria um tiro
                    platform_shot2.add(novo_tiro)

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


    # remove os tiros que devem ser removidos
    for t in remover_tiros:
        platform_shot.remove(t)

    for t in remover_tiros:
        platform_shot2.remove(t)

    #screen.fill("lightgray")  

    # pede para cada jogador se "atualizar"
    player_group.update(platform_group)

    escrever_texto(screen, 10, 10, f"P1 pontos: {player.pontos}", blue)
    escrever_texto(screen, 630, 10, f"p2 pontos: {player2.pontos}", blue)

    player_group.draw(screen)
    platform_group.draw(screen)
    platform_group.draw(screen) # mostra os obstáculos
    platform_shot.draw(screen) # desenhar os tiros
    platform_shot2.draw(screen) # desenhar os tiros
    platform_group.update() # movimenta todos os obstáculos
    platform_shot.update() # movimenta os tiros
    platform_shot2.update() # movimenta os tiros
    pygame.display.flip() # atualiza a tela
    
    # atualizar a tela
    # https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
    pygame.display.update()   

    clock.tick(200)
pygame.quit()