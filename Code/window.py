import pygame


# crée la fenêtre
pygame.init()
# nom de la fenêtre
pygame.display.set_caption('Pavage')

# taille de la fenêtre
screen: pygame.surface.Surface = pygame.display.set_mode((800,800))
# remplie la fenêtre en gris
screen.fill("white")

