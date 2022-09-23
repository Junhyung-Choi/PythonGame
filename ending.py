import pygame
import setting
from button import *
from animation import *
from status import *

global alpha 
alpha = 400

def render():
    global alpha
    alpha -= 3

    back = pygame.image.load("img/ending/back.png")
    back = pygame.transform.scale(back, (800, 600))
    end = pygame.image.load("img/ending/end.png")
    end = pygame.transform.scale(end, (800, 600))
    end.set_alpha(alpha)
    screen.blit(back, (0, 0))
    screen.blit(end, (0, 0))