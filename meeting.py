import pygame
from setting import *
from button import *

def interface(event):
    button_heart = Button(10, 10, 50, 'heart')
    button_skip = Button(70, 10, 50, 'skip')

    button_heart.click_event(event)
    button_skip.click_event(event)

    button_heart.show()
    button_skip.show()

    pygame.display.update()

def process_event(event):
    if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
        # 아래는 예시입니다.
        if event.key == pygame.K_1:
            print("1번키 눌림")
        if event.key == pygame.K_2:
            print("2번키 눌림")

    interface(event)

def render():
    pass