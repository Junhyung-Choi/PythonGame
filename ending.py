import pygame
import setting
import animation
import time
import sound
import button
import scene

class Ending():
    def __init__(self):
        self.alpha = 250
        self.fadeIn = 0
        self.scene = scene.Scene("img/ending/Ending_begin_", 2)
        self.back_img = pygame.image.load("img/ending/back.png")
        self.sound = sound.SceneSounds("sound/ending/", 1)
        self.normal_sound = sound.Sound("sound/ending/normal/back.mp3")
        self.next_btn = button.NextButton(self)
        self.prev_btn = button.PrevButton(self)
        self.is_loaded = False

    def load_file(self, kind):
        self.scene.add_scene("img/ending/Ending_" + kind + "_", 4 if kind == "good" else 3)
        self.scene.add_None()
        self.back_img = pygame.transform.scale(self.back_img, (800, 600))
        self.sound.add_sound("sound/ending/" + kind + "/", 2)
        if kind == "good":
            self.sound.add_None()

    def render(self, score):
        if 0 <= score < 8:
            kind = "hell"
        elif 8 <= score < 15:
            kind = "bad"
        elif 15 <= score < 22:
            kind = "normal"
        elif 22 <= score:
            kind = "good"

        if not self.is_loaded:
            self.load_file(kind)
            self.is_loaded = True

        if self.scene.imgs[self.scene.index] == None:
            self.alpha -= 2
            
            if self.alpha < -50:
                setting.stage = 0
            
            self.scene.imgs[self.scene.index - 1].set_alpha(self.alpha)
            
            setting.screen.blit(self.back_img, (0, 0))
            setting.screen.blit(self.scene.imgs[self.scene.index - 1], (0, 0))
        
        else:
            if self.fadeIn < 250 and self.scene.index == 0:
                self.fadeIn += 3
                self.scene.imgs[self.scene.index].set_alpha(self.fadeIn)
                setting.screen.blit(self.back_img, (0, 0))
            else:
                self.fadeIn = 250

            setting.screen.blit(self.scene.imgs[self.scene.index], (0, 0))


        if kind == "normal" and self.scene.index == 3:
            self.normal_sound.play()
        self.sound.play()
        

        print(self.sound.index)
        self.next_btn.show()
        self.prev_btn.show()

