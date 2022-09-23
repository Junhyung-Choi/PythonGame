import pygame
import setting
import time
import animation

animations = []

LEFT = 1
RIGHT = 3


SKIP_X = 700
SKIP_Y = 520
STORY_X = 0
STORY_Y = 0
skip_x_pos_start = 400
skip_y_pos_start = 520
skip_x_pos_end = 460
skip_y_pos_end = 600
scene_t = 3



def process_event(event):
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        if SKIP_X <= event.pos[0] <= SKIP_X + setting.SKIP_W and SKIP_Y <= event.pos[1] <= SKIP_Y + setting.SKIP_H:
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
    setting.screen.blit(setting.skip_img, (SKIP_X, SKIP_Y))

    if setting.currnet_scene_number > setting.STORY_NUMBERS:
        setting.stage = 2
        return 0
    
    currnet_t = time.time()
    if setting.start_t + scene_t <= currnet_t or setting.skip:
        setting.start_t = time.time()
        setting.skip = False
        animations[0].update()
        setting.currnet_scene_number += 1
    
    


    

    

    
    

    """ setting.screen.blit(setting.story_imgs[setting.currnet_scene_number], (STORY_X, STORY_Y)) """
    
    """ setting.screen.blit(setting.skip_img, (SKIP_X, SKIP_Y)) """

    """ if setting.first:
        setting.first = False
        setting.screen.blit(setting.story_imgs[setting.currnet_scene_number], (STORY_X, STORY_Y))
        setting.start_t = time.time()

    currnet_t = time.time()
    if setting.start_t + scene_t <= currnet_t:
        setting.start_t = time.time()
        setting.currnet_scene_number += 1
        setting.screen.blit(setting.story_imgs[setting.currnet_scene_number], (STORY_X, STORY_Y))
        
        print("다음장면으로 넘어갑니다.") """
