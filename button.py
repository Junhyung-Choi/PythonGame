import pygame
from setting import *

class Button:
    def __init__(self, x1, y1, size, btn_type, run='none'):
        self.x_pos = x1
        self.y_pos = y1
        self.width = size[0]
        self.height = size[1]
        self.btn_type = btn_type
        self.run = run

    def click(self):
        if self.run != 'none':
            self.run()
        elif self.btn_type == 'pause':
            print('일시정지')

    def click_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if self.x_pos <= event.pos[0] <= self.x_pos + self.width and self.y_pos <= event.pos[1] <= self.y_pos + self.height:
                self.click()
                return self.btn_type

    def show(self):
        if self.btn_type == 'pause':
            screen.blit(img_pause, (self.x_pos, self.y_pos))
        elif self.btn_type == 'speech_bubble':
            screen.blit(img_speech_bubble, (self.x_pos, self.y_pos))
        elif self.btn_type == 'propose':
            screen.blit(img_meeting_propose, (self.x_pos, self.y_pos))
        elif self.btn_type == 'time_check':
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
        else:
            pygame.draw.rect(screen, (0, 0, 0), [self.x_pos, self.y_pos, self.width, self.height])