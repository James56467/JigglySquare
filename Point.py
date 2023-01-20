import math
import pygame

class Point:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = 0
        self.yVel = 0
    
    def update(self):
        self.xPos += self.xVel
        self.yPos += self.yVel
        self.xVel = self.xVel * 0.995
        self.yVel = self.yVel * 0.995
