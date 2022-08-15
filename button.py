import pygame
from setting import *

class Button:
    def __init__(self, x1, y1, size, btn_type):
        self.x_pos = x1
        self.y_pos = y1
        self.size = size
        self.btn_type = btn_type

    def click(self):
        if (self.btn_type == 'skip'):
            print('스킵합니다.')
        elif (self.btn_type == 'heart'):
            print('호감을 표시합니다.')

    def click_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if self.x_pos <= event.pos[0] <= self.x_pos + self.size and self.y_pos <= event.pos[1] <= self.y_pos + self.size:
                self.click()

    def show(self):
        pygame.draw.rect(screen, (255, 255, 255), [self.x_pos, self.y_pos, self.size, self.size])