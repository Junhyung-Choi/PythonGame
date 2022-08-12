import pygame
import setting

def process_event(event):
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == setting.LEFT:
        if setting.skip_x_pos_start <= event.pos[0] <= setting.skip_x_pos_end and setting.skip_y_pos_start <= event.pos[1] <= setting.skip_y_pos_end:
            print("스킵합니다.")

def render():
    setting.screen.blit(setting.story_img, (setting.story_img_x_pos, setting.story_img_y_pos))
    setting.screen.blit(setting.skip_img, (setting.skip_x_pos_start, setting.skip_y_pos_start))