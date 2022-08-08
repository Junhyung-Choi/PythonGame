import pygame
from setting import *

def process_event(event):
    if event.type == pygame.QUIT:
        running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        if(skip_x_pos_start, skip_y_pos_start) <= (event.pos[0], event.pos[1]) <= (skip_x_pos_end, skip_y_pos_end):
            print("스킵합니다.")

def render():
    screen.blit(story_img, (story_img_x_pos, story_img_y_pos))
    screen.blit(skip_img, (skip_x_pos_start, skip_y_pos_start))