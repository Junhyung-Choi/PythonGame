import pygame

# 스크린 사이즈 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 현재 씬 
running = True
stage = 0

# 윈도우 설정
pygame.display.set_caption("Python Game")

# 이미지 에셋 업로드
start_background = pygame.image.load("img/start.png")
background = pygame.image.load("img/background.png")

