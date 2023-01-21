import math
import pygame
import JigglySquare

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Jiggly Square")

jiggle = JigglySquare.JigglySquare(100.0, 100.0, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jiggle.wPress = True
            if event.key == pygame.K_a:
                jiggle.aPress = True
            if event.key == pygame.K_s:
                jiggle.sPress = True
            if event.key == pygame.K_d:
                jiggle.dPress = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                jiggle.wPress = False
            if event.key == pygame.K_a:
                jiggle.aPress = False
            if event.key == pygame.K_s:
                jiggle.sPress = False
            if event.key == pygame.K_d:
                jiggle.dPress = False
    screen.fill((10, 200, 160))
    jiggle.update(screen)
    pygame.display.update()
    

pygame.quit()
