from locale import currency
from this import d
import pygame
import setting
import button
import time

class Pause():
    def __init__(self):
        self.pause_time = None
        self.img = pygame.image.load("img/pause.png")
        self.img = pygame.transform.scale(self.img, (400, 250))
        self.is_pausing = False
        self.btn_start = button.Button(380, 300, [40, 20])

    def pause(self, current_time):
        print('일시정지')
        self.is_pausing = True
        self.pause_time = current_time

    def show(self):
        setting.screen.blit(self.img, (200, 100))
        self.btn_start.show()

    def event(self, event):
        self.btn_start.click_event(event, None)

        if self.is_pausing and self.btn_start.is_clicked:
            self.start()

    def start(self):
        print('실행')
        self.is_pausing = False
        self.btn_start.is_clicked = False
        setting.game_status = 'playing'

        return (time.time() - self.pause_time)
        # 이 값을 GameStatus의 남은 시간에 더하면 됨.