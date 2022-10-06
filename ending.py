import pygame
import setting
import animation
import time
import sound
import button
import scene
import prototype

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
        self.prototype = prototype.Prototype()
        
    def load_file(self, kind):
        self.scene.add_scene("img/ending/Ending_" + kind + "_", 4 if kind == "good" else (3 if kind == "normal" else 2))
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
            
            self.scene.imgs[self.scene.index - 1].set_alpha(self.alpha)
            
            setting.screen.blit(self.back_img, (0, 0))
            setting.screen.blit(self.scene.imgs[self.scene.index - 1], (0, 0))

            if self.alpha < -50:
                self.prototype.render()
                if self.sound.sounds[self.sound.index] == None:
                    self.sound.sounds[self.sound.index - 1].stop()
                else:
                    self.sound.sounds[self.sound.index].stop()

                if kind == "normal":
                    self.normal_sound.stop()
        
        else:
            if self.fadeIn < 250 and self.scene.index == 3:
                self.scene.imgs[self.scene.index].set_alpha(self.fadeIn)
                setting.screen.blit(self.back_img, (0, 0))
                self.fadeIn += 3
            elif self.scene.index > 3:
                self.fadeIn = 250

            setting.screen.blit(self.scene.imgs[self.scene.index], (0, 0))

        if kind == "normal" and self.scene.index == 3:
            self.normal_sound.play()
        elif kind == "normal" and self.scene.index == 2:
            self.normal_sound.stop()
            
        self.sound.play()
        
        self.next_btn.show()
        if not self.alpha < -50:
            self.prev_btn.show()

