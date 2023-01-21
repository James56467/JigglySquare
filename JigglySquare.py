import pygame
import World
import Point

class JigglySquare:
    def __init__(self, xPos, yPos, halfDiagonal):
        self.points = [Point.Point(xPos, yPos - halfDiagonal),
                       Point.Point(xPos + halfDiagonal, yPos),
                       Point.Point(xPos, yPos + halfDiagonal),
                       Point.Point(xPos - halfDiagonal, yPos)]
        self.halfDiagonal = halfDiagonal

        self.wPress = False
        self.sPress = False
        
        self.aPress = False
        self.dPress = False
        
        self.world = World.World(500)
    
    def distance(self, firstID, secondID):
        return (((abs(self.points[firstID].xPos - self.points[secondID].xPos)**2)+(abs(self.points[firstID].yPos - self.points[secondID].yPos)**2))**0.5)
    
    def restForce(self, pointID, oppositeID):
        for i in range(4):
            if(i != pointID and self.distance(pointID,i) != 0):
                if(i == oppositeID):
                    self.points[pointID].xVel -= ((self.points[pointID].xPos - self.points[i].xPos)/self.distance(pointID,i)) * (self.distance(pointID,i) - (200)) / 1000
                    self.points[pointID].yVel -= ((self.points[pointID].yPos - self.points[i].yPos)/self.distance(pointID,i)) * (self.distance(pointID,i) - (200)) / 1000
                else:
                    self.points[pointID].xVel -= ((self.points[pointID].xPos - self.points[i].xPos)/self.distance(pointID,i)) * (self.distance(pointID,i) - (141.42136)) / 1000
                    self.points[pointID].yVel -= ((self.points[pointID].yPos - self.points[i].yPos)/self.distance(pointID,i)) * (self.distance(pointID,i) - (141.42136)) / 1000
    
    def changeVel(self, xVel, yVel):
        for i in self.points:
            i.xVel += xVel
            i.yVel += yVel
        
    def update(self, screen):
        for i in self.points:
            i.update()
        
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
