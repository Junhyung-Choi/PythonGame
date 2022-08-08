import pygame
# 초기 변수 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Python Game")

start_background = pygame.image.load("img/start.png")
background = pygame.image.load("img/background.png")

#캐릭터 불러오기
character = pygame.image.load("img/dot.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
#캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이는 변수
character_y_pos = screen_height - character_height #이미지가 화면 세로의 가장 아래 위치

# 이벤트 루프 변수
running = True
stage = 0
is_rendered = False