import pygame
import setting
import animation
import time

class Ending():
    def __init__(self):
        self.alpha = 500
        self.common_imgs = animation.Animation("img/ending/Ending_begin_", 2)
        self.separate_imgs = None
        self.separate_back_img = pygame.image.load("img/ending/back.png")
        self.is_loaded_separate_img = False
        self.is_common_imgs_running = True
        self.current_scene_number = 0
        self.start_t = None

    def load_separate_img(self, kind):
        self.separate_imgs = animation.Animation("img/ending/Ending_" + kind + "_", 4 if kind == "good" else 3)
        self.separate_back_img = pygame.transform.scale(self.separate_back_img, (800, 600))

    def render(self, score):
        if 0 <= score < 8:
            kind = "hell"
        elif 8 <= score < 15:
            kind = "bad"
        elif 15 <= score < 22:
            kind = "normal"
        elif 22 <= score:
            kind = "good"

        if not self.is_loaded_separate_img:
            self.load_separate_img(kind)
            self.is_loaded_separate_img = True
            self.start_t = time.time()



        if self.is_common_imgs_running:
            setting.screen.blit(self.common_imgs.now_img, (0, 0))
        else:
            setting.screen.blit(self.separate_back_img, (0, 0))
            setting.screen.blit(self.separate_imgs.now_img, (0, 0))

        # print("CURRENT SCENE NUMBER : ", self.current_scene_number)
        # print("START TIME : ", self.start_t)
        current_t = time.time()
        # print("CURRENT TIME : ", current_t)
        if self.current_scene_number > 1 and self.is_common_imgs_running:
            if self.start_t + 2 <= current_t:
                self.is_common_imgs_running = False
        
        elif self.start_t + 2 <= current_t:
            self.start_t = time.time()
            self.current_scene_number += 1
            
            if self.is_common_imgs_running:
                self.common_imgs.update()
                print('update', self.current_scene_number)
            else:
                self.separate_imgs.update()
                print('update', self.current_scene_number)
            
        if self.current_scene_number > (7 if kind == "good" else 6):
            self.alpha -= 3
            
            if self.alpha < -50:
                setting.stage = 0

            self.separate_imgs.now_img.set_alpha(self.alpha)
            
            setting.screen.blit(self.separate_back_img, (0, 0))
            setting.screen.blit(self.separate_imgs.now_img, (0, 0))