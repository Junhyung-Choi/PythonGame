from turtle import Screen
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

def render():
    setting.screen.blit(setting.main_background, (0, 0))
    frame_number = 36
    maxHeight = setting.screen.get_height()
    maxWidth = setting.screen.get_width()
    
    mouseX, mouseY = pygame.mouse.get_pos()
    setting.screen.blit(setting.eyeBall,(mouseX,mouseY))
    
    if(mouseY < maxHeight / 2):
        setting.screen.blit(setting.eyes[17],(0,0))
    else:
        fidx = int(remap(mouseX,0,maxWidth,0,frame_number))
        setting.screen.blit(setting.eyes[fidx],(0,0))
    
    setting.screen.blit(setting.main_title, (0,0))
    setting.screen.blit(setting.main_table, (0,0))
    setting.screen.blit(setting.menu_button,(0,0))
    setting.screen.blit(setting.menu_button,(100,0))