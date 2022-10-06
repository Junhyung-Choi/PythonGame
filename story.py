import pygame
import setting
from animation import *
import sound
from script import *

global story_animation, story_sounds

def process_event(event):
    global story_sounds
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == setting.LEFT:
        if setting.NEXT_SCENE_X <= event.pos[0] <= setting.NEXT_SCENE_X + setting.NEXT_SCENE_W and setting.NEXT_SCENE_Y <= event.pos[1] <= setting.NEXT_SCENE_Y + setting.NEXT_SCENE_H and story_animation.index < story_animation.frame_num:
            skip()
            print("스킵합니다.\n\n")
        elif setting.NEXT_STAGE_X <= event.pos[0] <= setting.NEXT_STAGE_X + setting.NEXT_STAGE_W  and setting.NEXT_STAGE_Y <= event.pos[1] <= setting.NEXT_STAGE_Y + setting.NEXT_STAGE_H:
            print("다음 스테이지로 넘어갑니다.\n\n")
            story_sounds.now_sound.stop()
            setting.stage = 2
        elif setting.BACKWARD_SCENE_X <= event.pos[0] <= setting.BACKWARD_SCENE_X + setting.BACKWARD_SCENE_W and setting.BACKWARD_SCENE_Y <= event.pos[1] <= setting.BACKWARD_SCENE_Y + setting.BACKWARD_SCENE_H and story_animation.index > 0:
            backward()
            print("뒤로 이동합니다.\n\n")

def init_ani():
    global story_animation
    story_animation = StoryAnimation("img/story/meeting_", setting.STORY_NUMBERS)

def init_sound():
    global story_sounds
    story_sounds = sound.SceneSound("sound/story/", 5)
    story_sounds.play()

def init_script():
    global story_script
    story_script = Script("Play now")

def skip():
    story_animation.update()
    if story_animation.index >= 2:
        story_sounds.update()
        story_sounds.play()

def backward():
    story_animation.backward()
    if story_animation.index >= 1:
        story_sounds.backward()
        story_sounds.play()

def render():
    
    if setting.first:
        # Story init 하는 부분입니다.
        setting.first = False
        init_ani()
        init_sound()
        init_script()

    # 스토리 이미지를 보여줍니다.
    setting.screen.blit(story_animation.now_img, (0, 0))

    # 화살표 이미지를 상황에 따라 보여줍니다.
    if story_animation.index > 0:
        setting.screen.blit(setting.backward_scene_img, (setting.BACKWARD_SCENE_X, setting.BACKWARD_SCENE_Y))
    if story_animation.index < story_animation.frame_num:
        setting.screen.blit(setting.next_scene_img, (setting.NEXT_SCENE_X, setting.NEXT_SCENE_Y))
    if story_animation.index == story_animation.frame_num:
        setting.screen.blit(setting.next_stage_img, (setting.NEXT_STAGE_X, setting.NEXT_STAGE_Y))
        story_script.show_all_script(setting.NEXT_STAGE_X + 10, setting.NEXT_STAGE_Y + 15)