import math
import pygame
import World
import Point

class BouncyCube:
    def __init__(self, xPos, yPos, halfDiagonal):
        N = Point.Point(xPos, yPos - halfDiagonal)
        E = Point.Point(xPos + halfDiagonal, yPos)
        S = Point.Point(xPos, yPos + halfDiagonal)
        W = Point.Point(xPos - halfDiagonal, yPos)
        self.points = [N,E,S,W]
        self.rotPos = 0
        self.rotVel = 0
        self.halfDiagonal = halfDiagonal

        self.wPress = False
        self.sPress = False
        
        self.aPress = False
        self.dPress = False

        self.qPress = False
        self.ePress = False
        
        self.world = World.World(500)
    
    def distance(self, pointOne, pointTwo):
        return (((abs(pointOne.xPos - pointTwo.xPos)**2)+(abs(pointOne.yPos - pointTwo.yPos)**2))**0.5)
    
    def restForce(self, pointID, oppositeID):
        jumpForce = 0
        for i in range(4):
            if(i != pointID and self.distance(self.points[pointID],self.points[i]) != 0):
                if(i == oppositeID):
                    self.points[pointID].xVel -= ((self.points[pointID].xPos - self.points[i].xPos)/self.distance(self.points[pointID],self.points[i])) * (self.distance(self.points[pointID],self.points[i]) - (200)) / 1000
                    self.points[pointID].yVel -= ((self.points[pointID].yPos - self.points[i].yPos)/self.distance(self.points[pointID],self.points[i])) * (self.distance(self.points[pointID],self.points[i]) - (200)) / 1000
                else:
                    self.points[pointID].xVel -= ((self.points[pointID].xPos - self.points[i].xPos)/self.distance(self.points[pointID],self.points[i])) * (self.distance(self.points[pointID],self.points[i]) - (141.42136)) / 1000
                    self.points[pointID].yVel -= ((self.points[pointID].yPos - self.points[i].yPos)/self.distance(self.points[pointID],self.points[i])) * (self.distance(self.points[pointID],self.points[i]) - (141.42136)) / 1000
    
    def changeVel(self, xVel, yVel):
        for i in self.points:
            i.xVel += xVel
            i.yVel += yVel
        
    def update(self, screen):
        for i in self.points:
            i.update()
        self.rotPos += self.rotVel
        
        #gravity
        
        self.changeVel(0, 0.01)
        
        #maintaining distance of points
        
        self.restForce(0,2)
        self.restForce(1,3)
        self.restForce(2,0)
        self.restForce(3,1)
        
        #controls and friction
        
        if(self.wPress):
            jump = True
            for i in self.points:
                if(i.yPos == self.world.groundLevel and jump):
                    self.changeVel(0,-3)
                    jump = False
                
        elif(self.sPress):
            self.changeVel(0,0.01)
        else:
            pass
        
        if(self.aPress):
            avgXVel = 0
            for i in self.points:
                avgXVel += i.xVel
            avgXVel = avgXVel / 4
            if(avgXVel > -0.3):
                self.changeVel(-0.01,0)
        elif(self.dPress):
            avgXVel = 0
            for i in self.points:
                avgXVel += i.xVel
            avgXVel = avgXVel / 4
            if(avgXVel < 0.3):
                self.changeVel(0.01,0)
        else:
            pass
        
        if(self.qPress):
            self.rotVel = -0.2
        elif(self.ePress):
            self.rotVel = 0.2
        
        #collision
        
        for i in self.points:
            if(i.yPos + i.yVel > self.world.groundLevel):
                i.yPos = self.world.groundLevel
                i.yVel = 0
                i.xVel = i.xVel/1.2
        
        #paint
        
        self.paint(screen)

    def paint(self,screen):
        
        self.world.paint(screen)
        
        coords = []
        
        for i in self.points:
            coords = coords + [(i.xPos, i.yPos)]
        
        pygame.draw.lines(screen,(0,0,255),True,coords)
