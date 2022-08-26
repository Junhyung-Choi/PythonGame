import pygame
from setting import *

class Button:
    def __init__(self, x1, y1, size):
        self.x_pos = x1
        self.y_pos = y1
        self.width = size[0]
        self.height = size[1]
        self.is_clicked = False

    def click(self):
        print('클릭됨')

    def click_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if self.x_pos <= event.pos[0] <= self.x_pos + self.width and self.y_pos <= event.pos[1] <= self.y_pos + self.height:
                self.click()

    def show(self):
        pygame.draw.rect(screen, (0, 0, 0), [self.x_pos, self.y_pos, self.width, self.height])

class PauseButton(Button):
    def show(self):
        screen.blit(img_pause, (self.x_pos, self.y_pos))

    def click(self):
        self.is_clicked = not(self.is_clicked)
        print('일시정지')

class SpeechBubbleButton(Button):
    def __init__(self, x1, y1, size, text='테스트'):
        super().__init__(x1, y1, size)
        self.text = text

    def show(self):
        screen.blit(img_speech_bubble, (self.x_pos, self.y_pos))
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x_pos + 17, self.y_pos + (SPEECH_BUBBLE_H / 2) - FONT_SIZE))

    def click(self):
        print(self.text + ' 클릭됨')
        self.is_clicked = not(self.is_clicked)
        
class TimeCheckButton(Button):
    def show(self):
        if(self.is_clicked):
            screen.blit(img_meeting_watch_clock,(WATCH_CLOCK_X,WATCH_CLOCK_Y))
            img_meeting_time_check.set_alpha(100)
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
            img_meeting_time_check.set_alpha(256)
        else:
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))

    def click(self):
        self.is_clicked = not(self.is_clicked)

class ProposeButton(Button):
    def show(self):
        screen.blit(img_meeting_propose, (self.x_pos, self.y_pos))
    
    def click(self):
        print('호감을 나타냅니다.')