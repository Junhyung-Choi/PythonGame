import pygame
from setting import *
from button import *

buttons = []
# 현재
# Menu에서 버튼에 들어갈 함수를 만들고
# 그걸 인터페이스로 넘겨서 인터페이스에서 버튼 클래스를 가지고
# 새로운 버튼 인스턴스를 만들어서 다시 미팅스 .py 에서 인터페이스를 렌더링 하는 구조

# 문제점
# 다른 씬에서 버튼을 쓰고 싶은데, 이 interfae.py 는 미팅 씬, 혹은 프로파일링 씬에만 종속되어있는 구조임

# 해결법 1. 
# 이걸 명확히 하기 위해, 각 버튼의 책임소재 및 렌더링은 버튼을 사용하는 씬별로 할당

# 해결법 2.
# 인터페이스를 하나의 클래스화 시켜서, 버튼 매개변수들을 *args 이걸로 받아서
# 인터페이스 내에 초기화 해야 하는 애들을 받아서 각 씬마다 인터페이스를 하나씩 생성해서
# 지금 있는 구조를 그대로 재사용 하게 하는거


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