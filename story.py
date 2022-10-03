import pygame
import setting
import time
import animation
import sound

global story_animation, story_sounds

def process_event(event):
    global story_sounds
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == setting.LEFT:
        if setting.SKIP_X <= event.pos[0] <= setting.SKIP_X + setting.SKIP_W and setting.SKIP_Y <= event.pos[1] <= setting.SKIP_Y + setting.SKIP_H:
            print("스킵합니다.\n\n")
            setting.skip = True
        elif setting.ALL_SKIP_X <= event.pos[0] <= setting.ALL_SKIP_X + setting.SKIP_W and setting.ALL_SKIP_Y <= event.pos[1] <= setting.ALL_SKIP_Y + setting.SKIP_H:
            print("모두 스킵합니다.\n\n")
            story_sounds.now_sound.stop()
            setting.stage = 2

def init_ani():
    global story_animation
    story_animation = animation.Animation("img/story/meeting_", setting.STORY_NUMBERS)
    story_animation.update()

def render():
    global story_animation, story_sounds
    if setting.first:
        setting.first = False
        setting.start_t = time.time()
        init_ani()
        story_sounds = sound.SceneSound("sound/story/", 5)
        story_sounds.play()

    
    currnet_t = time.time()
    
    if setting.start_t + setting.scene_t <= currnet_t or setting.skip:
        setting.start_t = time.time()
        setting.skip = False
        story_animation.update()
        if setting.story_scene_number != 0:
            story_sounds.update()
            story_sounds.play()
        setting.story_scene_number += 1

    if setting.story_scene_number >= setting.STORY_NUMBERS:
        setting.screen.blit(story_animation.now_img, (0,0))
        setting.stage = 2
        return 0

    setting.screen.blit(story_animation.now_img, (0, 0))
    setting.screen.blit(setting.skip_img, (setting.SKIP_X, setting.SKIP_Y))
    setting.screen.blit(setting.skip_img, (setting.ALL_SKIP_X, setting.ALL_SKIP_Y))