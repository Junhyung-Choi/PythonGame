from curses import flash
import pygame
import setting
import time

LEFT = 1
RIGHT = 3
# 아직 씬이 나오지 않았으므로, 임시 씬 이미지
story_img = pygame.image.load("img/background.png")
skip_img = pygame.image.load("img/skip.png")

story_img_x_pos = setting.screen_width / 2
story_img_y_pos = setting.screen_height / 2
skip_x_pos_start = 400
skip_y_pos_start = 520
skip_x_pos_end = 460
skip_y_pos_end = 600
scene_t = 5


def process_event(event):
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        if skip_x_pos_start <= event.pos[0] <= skip_x_pos_end and skip_y_pos_start <= event.pos[1] <= skip_y_pos_end:
            print("스킵합니다.")
            setting.first = True
    

def render():
    if setting.first:
        setting.first = False
        setting.t = time.time()
    currnet_t = time.time()
    if setting.t + scene_t <= currnet_t:
        print("다음장면으로 넘어갑니다.")
        setting.first = True
    setting.screen.blit(story_img, (story_img_x_pos, story_img_y_pos))
    setting.screen.blit(skip_img, (skip_x_pos_start, skip_y_pos_start))