import pygame
import setting
import animation
import time

class Ending():
    def __init__(self):
        self.alpha = 900
        self.common_imgs = animation.Animation("img/ending/Ending_begin_", 2)
        self.separate_img = None
        self.separate_back_img = None
        self.is_loaded_common_img = False
        self.is_common_imgs_running = True
        self.current_scene_number = 0
        self.start_t = time.time()

    def load_separate_img(self, kind):
        self.separate_img = pygame.image.load("img/ending/" + kind + ".png")
        self.separate_img = pygame.transform.scale(self.separate_img, (800, 600))
        self.separate_back_img = pygame.image.load("img/ending/back.png")
        self.separate_back_img = pygame.transform.scale(self.separate_back_img, (800, 600))

    def render(self, kind):
        if not self.is_loaded_common_img:
            self.load_separate_img(kind)
            self.is_loaded_common_img = True

        setting.screen.blit(self.common_imgs.now_img, (0, 0))

        if self.is_common_imgs_running:
            currnet_t = time.time()
            if self.current_scene_number > 2:
                if self.start_t + 2 <= currnet_t:
                    self.is_common_imgs_running = False

            elif self.start_t + 2 <= currnet_t:
                self.start_t = time.time()
                self.common_imgs.update()
                self.current_scene_number += 1

        else:
            self.alpha -= 3
            
            if self.alpha < -50:
                setting.stage = 0

            self.separate_img.set_alpha(self.alpha)
            
            setting.screen.blit(self.separate_back_img, (0, 0))
            setting.screen.blit(self.separate_img, (0, 0))