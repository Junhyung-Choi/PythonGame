import time
import pygame
from setting import *
import setting
from status import GameStatus

class Button:
    def __init__(self, x1, y1, size):
        self.x_pos = x1
        self.y_pos = y1
        self.width = size[0]
        self.height = size[1]
        self.is_clicked = False

    def click(self, gs):
        print('클릭됨')
        self.is_clicked = True

    def click_event(self, event, gs : GameStatus):
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if self.x_pos <= event.pos[0] <= self.x_pos + self.width and self.y_pos <= event.pos[1] <= self.y_pos + self.height:
                self.click(gs)

    def show(self):
        pygame.draw.rect(screen, (100, 100, 100), [self.x_pos, self.y_pos, self.width, self.height])

class PauseButton(Button):
    def show(self):
        screen.blit(img_pause, (self.x_pos, self.y_pos))

    def click(self, gs : GameStatus):
        self.is_clicked = not(self.is_clicked)
        setting.game_status = 'pause'

class SpeechBubbleButton(Button):
    def __init__(self, x1, y1, size,index, text='테스트'):
        super().__init__(x1, y1, size)
        self.index = index
        self.text = text

    def show(self):
        screen.blit(img_speech_bubble, (self.x_pos, self.y_pos))
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x_pos + 17, self.y_pos + (SPEECH_BUBBLE_H / 2) - FONT_SIZE))

    def click(self, gs : GameStatus):
        print(self.text + ' 클릭됨')
        gs.speech_button_clicked(self.index)
        self.is_clicked = not(self.is_clicked)
        
class TimeCheckButton(Button):
    def __init__(self, x1, y1, size):
        super().__init__(x1, y1, size)
        self.y_now = 600
        self.gs = None
        self.time_font = pygame.font.Font("font/DungGeunMo.ttf", 32)

    def show(self):
        if(self.is_clicked):
            if (self.y_now - 60 > WATCH_CLOCK_Y):
                self.y_now -= 60
            else:
                self.y_now -= self.y_now - WATCH_CLOCK_Y
            screen.blit(img_meeting_watch_clock,(WATCH_CLOCK_X, self.y_now))
            if(self.y_now == WATCH_CLOCK_Y):
                if not setting.game_status == 'pause':
                    minute,second = self.gs.get_left_min_sec()
                else:
                    minute, second = setting.left_time_min, setting.left_time_second
                time_text = ""
                if(minute != 0):
                    time_text = str(minute) + ':' + str(second).zfill(2)
                else:
                    time_text = '0:' + str(second).zfill(2)
                text = self.time_font.render(time_text, True, (0, 0, 0))
                screen.blit(text, (230,self.y_now + 90))
            img_meeting_time_check.set_alpha(100)
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
            img_meeting_time_check.set_alpha(256)
        else:
            screen.blit(img_meeting_watch_clock,(WATCH_CLOCK_X, self.y_now))
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
            if (self.y_now + 60 < 600):
                self.y_now += 60
            elif (self.y_now < 600):
                self.y_now += 600 - self.y_now

    def click(self, gs : GameStatus):
        if(self.gs == None):
            self.gs = gs
        self.is_clicked = not(self.is_clicked)

class ProposeButton(Button):
    def show(self):
        screen.blit(img_meeting_propose, (self.x_pos, self.y_pos))
    
    def click(self, gs : GameStatus):
        print('호감을 나타냅니다.')
        setting.stage = -1

class RestartButton(Button):
    def click(self, gs : GameStatus):
        print("Restart")
        setting.is_init_interface = False
        setting.stage = 0
        setting.game_status = 'playing'