import pygame
import random
import math


def deg_to_rad(angle: float) -> float:
    """transmorme les degrés en radian"""
    return angle*math.pi/180


# crée la fenêtre
pygame.init()
# nom de la fenêtre
pygame.display.set_caption('Pavage')
# taille de la fenêtre
screen: pygame.surface.Surface = pygame.display.set_mode((500,500))
# remplie la fenêtre en gris
screen.fill("gray")
"""
angle120: float = deg_to_rad(120)
size: float = 100

# crée les point
point1: list[float] = (250, 150)
point2: list[float] = (point1[0] + size*math.sin(angle120), point1[1] - size*math.cos(angle120))
point3: list[float] = (point2[0] + size*math.cos(angle120), point2[1] + size*math.sin(angle120))
point5: list[float] = (point1[0] - size*math.sin(angle120), point1[1] - size*math.cos(angle120))
point4: list[float] = (point5[0] - size*math.cos(angle120), point5[1] + size*math.sin(angle120))

poly_point: list[list] = (point1, point2, point3, point4, point5)
# crée le polygone
poly: pygame.rect.Rect = pygame.draw.polygon(screen,"red",poly_point)
# crée la bordure du polygone 
pygame.draw.polygon(screen,"black",poly_point,3)"""

running: bool = True
while running:

    # permet de fermer la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # si la touche entrer en presser
    """keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
    
    if keys[pygame.K_KP_ENTER]:
        
        # change la couleur du polygone (atention au épiletique)
        poly = pygame.draw.polygon(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),poly_point)
        pygame.draw.polygon(screen,"black",poly_point,3)"""
    
    # rafréchi la fenêtre
    pygame.display.flip()