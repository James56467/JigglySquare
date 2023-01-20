import math
import pygame
import BouncyCube

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Bouncy Cube")

bouncy = BouncyCube.BouncyCube(100.0, 100.0, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bouncy.wPress = True
            if event.key == pygame.K_a:
                bouncy.aPress = True
            if event.key == pygame.K_s:
                bouncy.sPress = True
            if event.key == pygame.K_d:
                bouncy.dPress = True
            if event.key == pygame.K_q:
                bouncy.qPress = True
            if event.key == pygame.K_e:
                bouncy.ePress = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                bouncy.wPress = False
            if event.key == pygame.K_a:
                bouncy.aPress = False
            if event.key == pygame.K_s:
                bouncy.sPress = False
            if event.key == pygame.K_d:
                bouncy.dPress = False
            if event.key == pygame.K_q:
                bouncy.qPress = False
            if event.key == pygame.K_e:
                bouncy.ePress = False
    screen.fill((10, 200, 160))
    bouncy.update(screen)
    pygame.display.update()
    

pygame.quit()
