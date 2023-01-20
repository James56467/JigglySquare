import math
import pygame

class World:
    def __init__(self, groundLevel):
        self.groundLevel = groundLevel
    
    def paint(self,screen):
        pygame.draw.rect(screen,(0,0,0),(0,self.groundLevel,800,600-self.groundLevel))
