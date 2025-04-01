import pygame, random, sys
pygame.init()


WNDW_HEIGHT = 800
WNDW_WIDTH = 600
screen = pygame.display.set_mode((WNDW_HEIGHT, WNDW_WIDTH))


title = pygame.display.set_caption("Dangle Guy")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)



nooseImg = pygame.image.load("Noose.png")
NooseX = 400
NooseY = 300
