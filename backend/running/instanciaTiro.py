import pygame
from backend.modelo.armas import Shot

def tiros(player, player2, largura_tiro, altura_tiro, platform_shot, platform_shot2, previous_time):
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

    #Tiro player 2
    if pk[pygame.K_p]: 
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 3500:
            previous_time = current_time
            novo_tiro = Shot(player2.rect.x + 16 - (largura_tiro/2), player2.rect.y, largura_tiro, altura_tiro) # cria um tiro
            platform_shot2.add(novo_tiro)

    