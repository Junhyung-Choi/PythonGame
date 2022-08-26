import pygame
from setting import *
from button import *

buttons = []

def init_interface(left_button, right_button, button_1, button_2, button_3, button_4):
    # 버튼 객체 생성
    button_pause = Button(PAUSE_BTN_X, PAUSE_BTN_Y, [PAUSE_BTN_SIZE, PAUSE_BTN_SIZE], 'pause')
    button_time_check = Button(LEFT_CIRCLE_BTN_X, LEFT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE], left_button(False), left_button)
    button_propose = Button(RIGHT_CIRCLE_BTN_X, RIGHT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE], right_button(False), right_button)
    button_speech_bubble_1 = Button(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_1)
    button_speech_bubble_2 = Button(47 + SPEECH_BUBBLE_W + 25, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_2)
    button_speech_bubble_3 = Button(47 + SPEECH_BUBBLE_W * 2 + 50, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_3)
    button_speech_bubble_4 = Button(47 + SPEECH_BUBBLE_W * 3 + 75, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_4)

    buttons.extend((button_pause, button_time_check, button_propose, button_speech_bubble_1, button_speech_bubble_2, button_speech_bubble_3, button_speech_bubble_4))

def event_interface(event):
    # 버튼 이벤트
    for i in buttons:
        i.click_event(event)

def show_interface():
    # 인터페이스 렌더링
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))

    for i in buttons:
        i.show()