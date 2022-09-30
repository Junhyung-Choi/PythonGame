import pygame
import setting
import time
from button import *
from animation import *
from status import *

buttons = []
animations = []
global current_ani, gamestatus
gamestatus = None

def process_event(event):
    process_event_btn(event)

def render():
    global current_ani
    if not(setting.is_init_interface):
        init_btn()
        init_ani()
        init_status()
        setting.is_init_interface = True
        current_ani = -1
    
    index = 0
    while(index < 5):
        if buttons[index].is_clicked == True:
            if index != current_ani:
                if current_ani != -1:
                    buttons[current_ani].is_clicked = False
                current_ani = index
            screen.blit(animations[index].now_img, (0, 0))
            animations[index].update()
        index += 1


    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))
    """ script_now_t = time.time()
    if setting.is_script_activate:
        setting.is_script_activate = False
        setting.script_t = time.time()
    if setting.script_t + setting.script_running_t >= script_now_t:
        pass
    else:
        show_btn()
    if setting.running_script:
        setting.running_script = False
        show_script() """
    
    show_script()
    show_btn()

def process_event_btn(event):
    for i in buttons:
        i.click_event(event,gamestatus)

def init_ani():
    girl_watchphone = Animation("img/meeting/Girl_WatchPhone/girl_watchPhone__",60)
    girl_smile = Animation("img/meeting/Girl_Smile/girl_smile_", 39)
    girl_eyebrowup = Animation("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_", 20)
    girl_armup = Animation("img/meeting/Girl_armUp/girl_armUp_", 60)
    girl_armdown = Animation("img/meeting/Girl_armDown/girl_armDown_", 60)

    animations.extend((girl_watchphone, girl_smile, girl_eyebrowup, girl_armup, girl_armdown))

def init_btn():
    btn_spch_bble_1 = SpeechBubbleButton(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 0, '폰 확인해보세요.')
    btn_spch_bble_2 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W + 25, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 1, '웃어보세요.')
    btn_spch_bble_3 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 2 + 50, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 2, '눈썹을 위로 올려보세요.')
    btn_spch_bble_4 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 3 + 75, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 3,'탁자에 팔꿈치를 올려보세요.')
    btn_pause = PauseButton(PAUSE_BTN_X, PAUSE_BTN_Y, [PAUSE_BTN_SIZE, PAUSE_BTN_SIZE])
    btn_timecheck = TimeCheckButton(LEFT_CIRCLE_BTN_X, LEFT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
    btn_propose = ProposeButton(RIGHT_CIRCLE_BTN_X, RIGHT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
   
    buttons.extend((btn_spch_bble_1, btn_spch_bble_2, btn_spch_bble_3, btn_spch_bble_4))
    buttons.extend((btn_pause, btn_timecheck, btn_propose))

def init_status():
    global gamestatus
    if gamestatus == None:
        gamestatus = GameStatus("meeting",buttons[0],buttons[1],buttons[2],buttons[3])

def show_btn():
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))

    for i in buttons:
        i.show()

def show_script():
    while setting.play:
        if setting.first_script:
            setting.first_script = False
            print("처음 작동중")
            start_t = time.time()
        
        currnet_t = time.time()
        if len(setting.text) - 1 < setting.text_index:
            setting.play = False
            print("마지막 작동 중")
        elif currnet_t >= start_t + setting.delay:
            # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
            myText = setting.myFont.render(setting.render_text, True, (0,0,255)) #(Text,anti-alias, color)
            setting.screen.blit(myText, (100,100)) #(글자변수, 위치)
            print("작동중")
            if setting.text_index == len(setting.text) - 1:
                setting.text_index += 1
                pass
            else:
                setting.render_text += setting.text[setting.text_index]
                start_t = currnet_t
                setting.text_index += 1
    return