import pygame

#class to delay (To avoid more messy code) 

class Delay:
    def __init__(self):
        self.previous_time = pygame.time.get_ticks()

    def delay(self, time: int): #Delay in time ms
        current_time = pygame.time.get_ticks()
        if current_time - self.previous_time > time:
            self.previous_time = pygame.time.get_ticks()
            return True