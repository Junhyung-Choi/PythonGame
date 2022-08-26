import pygame
import setting
from button import *

buttons = []

# 버튼 클릭 함수
def time_check(run=True):
    if run:
        print(buttons[0].is_clicked)
        buttons[5].is_clicked = True
    return 'time_check'


def propose(run=True):
    if run:
        print("호감")
    return 'propose'


def button_1():
    print("버튼1")


def button_2():
    print("버튼2")


def button_3():
    print("버튼3")


def button_4():
    print("버튼4")


def init_btn(left_button, right_button, button_1, button_2, button_3, button_4):
    # 버튼 객체 생성
    btn_pause = Button(PAUSE_BTN_X, PAUSE_BTN_Y, [PAUSE_BTN_SIZE, PAUSE_BTN_SIZE], 'pause')
    btn_timecheck = Button(LEFT_CIRCLE_BTN_X, LEFT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE], left_button(False), left_button)
    btn_propose = Button(RIGHT_CIRCLE_BTN_X, RIGHT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE], right_button(False), right_button)
    btn_spch_bble_1 = Button(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_1)
    btn_spch_bble_2 = Button(47 + SPEECH_BUBBLE_W + 25, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_2)
    btn_spch_bble_3 = Button(47 + SPEECH_BUBBLE_W * 2 + 50, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_3)
    btn_spch_bble_4 = Button(47 + SPEECH_BUBBLE_W * 3 + 75, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 'speech_bubble', button_4)
   
    buttons.extend((btn_spch_bble_1, btn_spch_bble_2, btn_spch_bble_3, btn_spch_bble_4))
    buttons.extend((btn_pause, btn_timecheck, btn_propose))

def process_event_btn(event):
    # 버튼 이벤트
    for i in buttons:
        i.click_event(event)

def show_btn():
    # 인터페이스 렌더링
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))

    for i in buttons:
        i.show()


def process_event(event):
    process_event_btn(event)

def render():
    if not(setting.is_init_interface):
        init_btn(time_check, propose, button_1, button_2, button_3, button_4)
        setting.is_init_interface = True

    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))
    show_btn()