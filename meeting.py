import pygame
import setting
from button import *
from interface import *


def time_check(run=True):
    if run:
        screen.blit(setting.img_meeting_watch_clock, (WATCH_CLOCK_X, WATCH_CLOCK_Y))
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

def render_window():
    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))

def process_event(event):
    event_interface(event)

def render():
    if not(setting.is_init_interface):
        init_interface(time_check, propose, button_1, button_2, button_3, button_4)
        is_init_interface = True

    render_window()
    show_interface()