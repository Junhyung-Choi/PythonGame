import pygame
import setting
import time
import animation

animations = []

def process_event(event):
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == setting.LEFT:
        if setting.SKIP_X <= event.pos[0] <= setting.SKIP_X + setting.SKIP_W and setting.SKIP_Y <= event.pos[1] <= setting.SKIP_Y + setting.SKIP_H:
            print("스킵합니다.")
            setting.skip = True

def init_ani():
    story_img = animation.Animation("img/story/meeting_", setting.STORY_NUMBERS)
    animations.append(story_img)
    

def render():

    if setting.first:
        setting.first = False
        setting.start_t = time.time()
        init_ani()
        setting.currnet_scene_number += 1
        
    setting.screen.blit(animations[0].now_img, (0, 0))
    setting.screen.blit(setting.skip_img, (setting.SKIP_X, setting.SKIP_Y))

    if setting.currnet_scene_number >= setting.STORY_NUMBERS:
        setting.stage = 2
        return 0
    
    currnet_t = time.time()
    if setting.start_t + setting.scene_t <= currnet_t or setting.skip:
        setting.start_t = time.time()
        setting.skip = False
        animations[0].update()
        setting.currnet_scene_number += 1