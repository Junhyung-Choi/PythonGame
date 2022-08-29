import pygame

class Animation():
    def __init__(self, path, frame_num):
        self.index = 0
        self.imgs = []
        self.path = path
        self.frame_num = frame_num
        for i in range(self.frame_num):
            img = pygame.image.load(self.path + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]

    def update(self):
        self.index += 1
        if self.index >= len(self.imgs):
            self.index = 0
        self.now_img = self.imgs[self.index]
