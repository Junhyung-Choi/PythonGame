import button
import status
import pygame
import setting
import time
import animation
import meeting

class MiddleScene():
    def __init__(self, sound):
        self.imgs = None
        self.start_t = time.time()
        self.current_scene_number = 0
        self.is_running = False
        self.isStarted = False
        self.is_load_imgs = False
        self.sound = sound
        self.is_played_gulp = False
    def start(self):
        if not self.isStarted:
            self.isStarted = True
            self.is_running = True
            self.start_t = time.time()
    
    def load_imgs(self, score):
        if (score - 15 < -3):
            self.imgs = animation.Animation("img/meeting/middle/midChap_Bad_", 3)
            print('==========BAD==========')
        elif (-3 <= score - 15 <= 3):
            self.imgs = animation.Animation("img/meeting/middle/midChap_Normal_", 3)
            print('==========NORMAL==========')
        elif (3 < score - 15):
            self.imgs = animation.Animation("img/meeting/middle/midChap_Good_", 3)
            print('==========GOOD==========')

    def render(self, kind):
        if not self.is_load_imgs:
            self.load_imgs(kind)
            self.is_load_imgs = True
            self.sound.play()

        
        setting.screen.blit(self.imgs.now_img, (0, 0))
        
        if self.is_running:
            currnet_t = time.time()
            if self.current_scene_number > 4:
                if self.start_t + 2 <= currnet_t:
                    self.is_running = False
                    meeting.isEventAvailable = True
                    gs : status.GameStatus = meeting.gamestatus
                    gs.set_Second_Phase()

            elif self.start_t + 2 <= currnet_t:
                self.start_t = time.time()
                self.imgs.update()
                self.sound.update()
                self.current_scene_number += 1

            elif self.start_t + 1 <= currnet_t and self.current_scene_number == 1 and not self.is_played_gulp:
                self.sound.play()
                self.is_played_gulp = True