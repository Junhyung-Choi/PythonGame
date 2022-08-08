import pygame
from setting import *

def remap(old_val, old_min, old_max, new_min, new_max):
    return (new_max - new_min)*(old_val - old_min) / (old_max - old_min) + new_min

def process_event(event):
    if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
        # 아래는 예시입니다.
        if event.key == pygame.K_1:
            stage = 1
            print("게임시작")
        if event.key == pygame.K_2:
            print("패치노트")
    if event.type == pygame.MOUSEMOTION:
        print(pygame.mouse.get_pos())

def render():
    screen.blit(start_background, (0, 0))
    frame_number = 24
    maxHeight = screen.get_height()
    maxWidth = screen.get_width()
    
    mouseX, mouseY = pygame.mouse.get_pos()
    if(mouseY < maxHeight / 2):
        print("Normal Image")
        print(mouseX,mouseY)
    else:
        print("Frame : " + str(remap(mouseX,0,maxHeight,0,frame_number)))
        print(mouseX,mouseY)