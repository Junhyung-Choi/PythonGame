import pygame
# 초기 변수 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Python Game")

start_background = pygame.image.load("img/start.png")
background = pygame.image.load("img/background.png")