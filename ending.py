import pygame
import setting
import animation
import time
import sound
import button
import scene

class Ending():
    def __init__(self):
        self.alpha = 500
        self.scene = scene.Scene("img/ending/Ending_begin_", 2)
        self.back_img = pygame.image.load("img/ending/back.png")
        self.sound = sound.SceneSounds("sound/ending/", 1)
        self.next_btn = button.NextButton(setting.SKIP_X, setting.SKIP_Y, [setting.SKIP_W, setting.SKIP_H], self)
        self.prev_btn = button.PrevButton(setting.BACKWARD_X, setting.BACKWARD_Y, [setting.SKIP_W, setting.SKIP_H], self)
        self.is_loaded = False
        
    def load_file(self, kind):
        self.scene.add_scene("img/ending/Ending_" + kind + "_", 4 if kind == "good" else 3)
        self.back_img = pygame.transform.scale(self.back_img, (800, 600))
        self.sound.add_sound("sound/ending/" + kind + "/", (3 if kind == "normal" else 2))

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

        setting.screen.blit(self.scene.imgs[self.scene.index], (0, 0))

        if self.scene.index == 1:
            self.sound.index = 0
        elif self.scene.index == 4:
            self.sound.index = 2
        self.sound.play()
            

        print(self.sound.index)
        self.next_btn.show()
        self.prev_btn.show()

        # if self.current_scene_number > (7 if kind == "good" else 6):
        #     self.alpha -= 3
            
        #     if self.alpha < -50:
        #         setting.stage = 0

        #     self.separate_imgs.now_img.set_alpha(self.alpha)
            
        #     setting.screen.blit(self.back_img, (0, 0))
        #     setting.screen.blit(self.separate_imgs.now_img, (0, 0))