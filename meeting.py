import pygame
from setting import *
from button import *
from interface import *

def time_check(run=True):
    if run:
        screen.blit(img_meeting_watch_clock, (WATCH_CLOCK_X, WATCH_CLOCK_Y))
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

def process_event(event):
    interface(event, time_check, propose, button_1, button_2, button_3, button_4)

def render():
    pass

