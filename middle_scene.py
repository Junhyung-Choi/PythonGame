import button
import status
import pygame
import setting
import time
import animation
import meeting

class MiddleScene():
    def __init__(self):
        self.imgs = animation.Animation("img/meeting/middle/", 5)
        self.start_t = time.time()
        self.current_scene_number = 0
        self.is_running = False

    def render(self):
        setting.screen.blit(self.imgs.now_img, (0, 0))

        if self.is_running:
            currnet_t = time.time()
            if self.current_scene_number > 4:
                if self.start_t + 2 <= currnet_t:
                    self.is_running = False
                    meeting.isEventAvailable = True

            elif self.start_t + 2 <= currnet_t:
                self.start_t = time.time()
                self.imgs.update()
                self.current_scene_number += 1