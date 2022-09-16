import pygame
import setting
from button import *
from animation import *
from status import *

buttons = []

def active_gameover():
    setting.is_gameover = not setting.is_gameover

def show_box():
    if not setting.is_init_gameover:
        setting.is_init_gameover = True
        init_btn()

    setting.screen.blit(setting.img_gameover, (200, 100))
    buttons[0].show()

def init_btn():
    btn_restart = RestartButton(200, 100, [100, 100])
    buttons.append(btn_restart)

def process_event(event):
    for i in buttons:
        i.click_event(event, None)