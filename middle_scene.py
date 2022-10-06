import button
import status
import pygame
import setting
import time
import animation
import meeting
import sound
import scene

class MiddleScene():
    def __init__(self):
        self.scene = None
        self.is_started = False
        self.is_running = False
        self.is_loaded = False
        self.sound = sound.SceneSounds("sound/meeting/middle/", 2)
        self.next_btn = button.NextButton(self)
        self.prev_btn = button.PrevButton(self)

    def start(self):
        if not self.is_started:
            self.is_started = True
            self.is_running = True
    
    def load_file(self, score):
        if (score - 15 < -3):
            self.scene = scene.Scene("img/meeting/middle/midChap_Bad_", 3)
            self.sound.add_sound("sound/meeting/middle/bad/", 1)
            print('==========BAD==========')
        elif (-3 <= score - 15 <= 3):
            self.scene = scene.Scene("img/meeting/middle/midChap_Normal_", 3)
            self.sound.add_sound("sound/meeting/middle/normal/", 1)
            print('==========NORMAL==========')
        elif (3 < score - 15):
            self.scene = scene.Scene("img/meeting/middle/midChap_Good_", 3)
            self.sound.add_sound("sound/meeting/middle/good/", 1)
            print('==========GOOD==========')
        
        self.scene.add_None()

    def render(self, kind):
        if not self.is_loaded:
            self.load_file(kind)
            self.is_loaded = True

        if self.scene.imgs[self.scene.index] == None:
            self.is_running = False
            gs : status.GameStatus = meeting.gamestatus
            gs.set_Second_Phase()
            meeting.bgm.set_volume(1.0)
            return

        setting.screen.blit(self.scene.imgs[self.scene.index], (0, 0))
        self.sound.play()

        self.next_btn.show()
        self.prev_btn.show()