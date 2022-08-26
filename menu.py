from turtle import Screen
from wsgiref.util import setup_testing_defaults
import pygame
import setting

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
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX, mouseY = pygame.mouse.get_pos()
        if(180 < mouseX < 260 and 480 < mouseY < 540):
            print("Next Scene")
            setting.stage += 1
        if(540 < mouseX < 620 and 480 < mouseY < 540):
            print("GAME OVER")

def render():
    setting.screen.blit(setting.main_background, (0, 0))
    
    frame_number = 36
    maxHeight = setting.screen.get_height()
    maxWidth = setting.screen.get_width()
    
    mouseX, mouseY = pygame.mouse.get_pos()
    eyeX = int(remap(mouseX,0,maxWidth,230,350))
    eyeY = int(remap(mouseY,0,maxHeight,280,320))
    setting.screen.blit(setting.eyeBall,(eyeX,eyeY))
    setting.screen.blit(setting.eyeBall,(eyeX+200,eyeY))
    
    if(mouseY < maxHeight / 2):
        setting.screen.blit(setting.eyes[17],(0,0))
    else:
        if mouseX < 170:
            setting.screen.blit(setting.eyes[0],(0,0))
        elif mouseX > 630:
            setting.screen.blit(setting.eyes[35],(0,0))
        else:
            fidx = int(remap(mouseX,170,630,0,frame_number-1))
            setting.screen.blit(setting.eyes[fidx],(0,0))
    
    setting.screen.blit(setting.main_title, (176/2,54/2))
    setting.screen.blit(setting.main_table, (-40/2,899/2))

    if(180 < mouseX < 260 and 480 < mouseY < 540):
        setting.screen.blit(setting.menu_button_click,(377/2,974/2))
    else:
        setting.screen.blit(setting.menu_button,(377/2,974/2))

    if(540 < mouseX < 620 and 480 < mouseY < 540):
        setting.screen.blit(setting.menu_button_click,(1087/2,974/2))
    else:
        setting.screen.blit(setting.menu_button,(1087/2,974/2))
        