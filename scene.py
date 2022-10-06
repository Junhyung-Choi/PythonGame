import pygame
import setting

class Scene():
    def __init__(self, path, img_num):
        self.imgs = []
        self.path = path
        self.img_num = img_num
        self.index = 0
        for i in range(self.img_num):
            img = pygame.image.load(self.path + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
    
    def update(self):
        if self.index < self.img_num:
            self.index += 1
            
    def backward(self):
        if self.index > 0:
            self.index -= 1

    def add_scene(self, path, img_num):
        self.img_num += img_num
        for i in range(img_num):
            img = pygame.image.load(path + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)

    def add_None(self):
        self.img_num += 1
        self.imgs.append(None)

    def render(self):
        setting.screen.blit(self.imgs[self.index], (0, 0))