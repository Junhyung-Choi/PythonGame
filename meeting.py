import pygame
import setting
from button import *
from animation import *
from status import *

buttons = []
animations = []
global current_ani, gamestatus, isEventAvailable
gamestatus = None
isEventAvailable = False

def process_event(event):
    if(isEventAvailable):
        process_event_btn(event)

def render():
    global current_ani, isEventAvailable
    if (setting.is_init_interface and not isEventAvailable):
        isEventAvailable = True
    if not(setting.is_init_interface):
        isEventAvailable = False
        init_ani()
        init_btn()
        init_status()
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
    show_btn()

    if not(setting.is_init_interface):
        setting.is_init_interface = True

def process_event_btn(event):
    for i in buttons:
        i.click_event(event,gamestatus)

def init_ani():
    girl_watchphone = Animation("img/meeting/Girl_WatchPhone/girl_watchPhone_",60)
    girl_smile = Animation("img/meeting/Girl_Smile/girl_smile_", 31)
    girl_eyebrowup = Animation("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_", 20)
    girl_armup = Animation("img/meeting/Girl_ArmUp/girl_armUp_", 60)
    girl_armdown = Animation("img/meeting/Girl_ArmDown/girl_armDown_", 60)

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
