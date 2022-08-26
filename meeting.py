import pygame
import setting
from button import *
from animation import *

buttons = []
animations = []

def process_event(event):
    process_event_btn(event)

def render():
    if not(setting.is_init_interface):
        init_btn()
        init_ani()
        setting.is_init_interface = True
    
    index = 0
    while(index < 5):
        if buttons[index].is_clicked == True:
            screen.blit(animations[index].now_img, (0, 0))
            animations[index].update()
        index += 1

    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))
    show_btn()

def process_event_btn(event):
    for i in buttons:
        i.click_event(event)

def init_ani():
    girl_watchphone = GirlWatchPhone()
    girl_smile = GirlSmile()
    girl_eyebrowup = GirlEyebrowUp()
    girl_armup = GirlArmUp()
    girl_armdown = GirlArmDown()

    animations.extend((girl_watchphone, girl_smile, girl_eyebrowup, girl_armup, girl_armdown))

    for i in animations:
        i.call_imgs()

def init_btn():
    btn_spch_bble_1 = SpeechBubbleButton(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], '폰 확인해보세요.')
    btn_spch_bble_2 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W + 25, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], '웃어보세요.')
    btn_spch_bble_3 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 2 + 50, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], '눈썹을 위로 올려보세요.')
    btn_spch_bble_4 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 3 + 75, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], '탁자에 팔꿈치를 올려보세요.')
    btn_pause = PauseButton(PAUSE_BTN_X, PAUSE_BTN_Y, [PAUSE_BTN_SIZE, PAUSE_BTN_SIZE])
    btn_timecheck = TimeCheckButton(LEFT_CIRCLE_BTN_X, LEFT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
    btn_propose = ProposeButton(RIGHT_CIRCLE_BTN_X, RIGHT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
   
    buttons.extend((btn_spch_bble_1, btn_spch_bble_2, btn_spch_bble_3, btn_spch_bble_4))
    buttons.extend((btn_pause, btn_timecheck, btn_propose))

def show_btn():
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))

    for i in buttons:
        i.show()
