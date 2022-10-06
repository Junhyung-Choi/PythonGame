import pygame
import setting
from animation import *
from script import *
from sound import *

global story_animation, story_sounds

def process_event(event):
    global story_sounds
    if event.type == pygame.QUIT:
        setting.running = False
            
    # 마우스 버튼이 스킵 버튼을 눌렸을 때
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == setting.LEFT:
        if setting.NEXT_SCENE_X <= event.pos[0] <= setting.NEXT_SCENE_X + setting.NEXT_SCENE_W and setting.NEXT_SCENE_Y <= event.pos[1] <= setting.NEXT_SCENE_Y + setting.NEXT_SCENE_H and story_animation.index < story_animation.frame_num - 1:
            forward()
            print("다음씬을 재생합니다.")
        elif setting.BACKWARD_SCENE_X <= event.pos[0] <= setting.BACKWARD_SCENE_X + setting.BACKWARD_SCENE_W and setting.BACKWARD_SCENE_Y <= event.pos[1] <= setting.BACKWARD_SCENE_Y + setting.BACKWARD_SCENE_H and 0 < story_animation.index <= story_animation.frame_num - 1 and not setting.tutorial:
            backward()
            print("이전씬을 재생합니다.")
        elif setting.GO_TUTORIAL_X <= event.pos[0] <= setting.GO_TUTORIAL_X + setting.GO_TUTORIAL_W  and setting.GO_TUTORIAL_Y <= event.pos[1] <= setting.GO_TUTORIAL_Y + setting.GO_TUTORIAL_H and story_animation.index == story_animation.frame_num - 1 and not setting.tutorial:
            setting.tutorial = True
            forward(True)
            print("튜토리얼로 이동합니다.")
        elif setting.NEXT_STAGE_X <= event.pos[0] <= setting.NEXT_STAGE_X + setting.NEXT_STAGE_W  and setting.NEXT_STAGE_Y <= event.pos[1] <= setting.NEXT_STAGE_Y + setting.NEXT_STAGE_H and story_animation.index == story_animation.frame_num:
            setting.stage = 2
            print("다음 스테이지로 이동합니다.")

def init_ani():
    global story_animation
    story_animation = StoryAnimation("img/story/meeting_", setting.STORY_NUMBERS)
    setting.alpha = 250

def init_sound():
    global story_sounds
    story_sounds = SceneSounds("sound/story/", 5)
    story_sounds.play()

def init_script():
    global story_script, tutorial_skip_script
    story_script = Script("Go Tutorial")
    tutorial_skip_script = Script("Play Now")
    tutorial_skip_script.color = [250, 250, 250]

def forward(tutorial = False):
    story_animation.update(tutorial)
    if story_animation.index == story_animation.frame_num:
        story_sounds.stop()
    elif story_animation.index >= 2 and not tutorial:
        story_sounds.update(True)
        story_sounds.play()

def backward():
    story_animation.backward()
    if story_animation.index >= 1:
        story_sounds.backward(True)
        story_sounds.play()

def render():
    
    if setting.first:
        # Story init 하는 부분입니다.
        setting.first = False
        init_ani()
        init_sound()
        init_script()

    # Fade in Fade out을 진행하는 부분입니다.
    if 0 <= story_animation.index < story_animation.frame_num - 1 and setting.alpha > 0:
        setting.alpha -= 2

        if story_script.color[0] > 0:
            for i in range(3):
                story_script.color[i] -= 2

    elif story_animation.index == story_animation.frame_num - 1 and setting.alpha < 250 and setting.tutorial == True:
        setting.alpha += 2

        for i in range(3):
                story_script.color[i] += 2
        if setting.alpha == 250:
            setting.tutorial = False
            forward(False)
    elif story_animation.index == story_animation.frame_num:
        setting.alpha -= 2
    setting.back_img.set_alpha(setting.alpha)

    # 스토리 이미지를 보여줍니다.
    setting.screen.blit(story_animation.now_img, (0, 0))
    setting.screen.blit(setting.back_img, (0, 0))

    # 화살표 이미지를 상황에 따라 보여줍니다.
    if story_animation.index > 0 and story_animation.index != story_animation.frame_num:
        setting.screen.blit(setting.backward_scene_img, (setting.BACKWARD_SCENE_X, setting.BACKWARD_SCENE_Y))
    if story_animation.index < story_animation.frame_num - 1:
        setting.screen.blit(setting.next_scene_img, (setting.NEXT_SCENE_X, setting.NEXT_SCENE_Y))
    if story_animation.index == story_animation.frame_num - 1:
        setting.screen.blit(setting.go_tutorial_img, (setting.GO_TUTORIAL_X, setting.GO_TUTORIAL_Y))
        story_script.show_all_script(setting.GO_TUTORIAL_X + 10, setting.GO_TUTORIAL_Y + 15)
    if story_animation.index == story_animation.frame_num:
        setting.screen.blit(setting.next_stage_img, (setting.NEXT_STAGE_X, setting.NEXT_STAGE_Y))
        tutorial_skip_script.show_all_script(setting.NEXT_STAGE_X + 10, setting.NEXT_STAGE_Y + 15)
        if 0 <= tutorial_skip_script.timer % 10 <= 4:
            tutorial_skip_script.color = [0, 0, 0]
        else:
            tutorial_skip_script.color = [250, 250, 250]
        tutorial_skip_script.timer += 1