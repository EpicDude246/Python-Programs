
import pygame, sys
pygame.init()
HEIGHT = 600
WIDTH = 600

screensize = (HEIGHT, WIDTH)

surface = pygame.display.set_mode(screensize)

pygame.draw.rect(surface, (0, 0, 255), (1,1,100,50))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()