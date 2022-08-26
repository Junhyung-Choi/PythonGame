import pygame

class Animation():
    def __init__(self):
        self.index = 0
        self.now_img = ''
        self.imgs = []

    def update(self):
        self.index += 1
        if self.index >= len(self.imgs):
            self.index = 0
        self.now_img = self.imgs[self.index]

class GirlWatchPhone(Animation):
    def call_imgs(self):
        for i in range(60):
            img = pygame.image.load("img/meeting/Girl_WatchPhone/girl_watchPhone__" + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]

class GirlSmile(Animation):
    def call_imgs(self):
        for i in range(39):
            img = pygame.image.load("img/meeting/Girl_Smile/girl_smile_" + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]
    
class GirlEyebrowUp(Animation):
    def call_imgs(self):
        for i in range(20):
            img = pygame.image.load("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_" + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]

class GirlArmUp(Animation):
    def call_imgs(self):
        for i in range(60):
            img = pygame.image.load("img/meeting/Girl_armUp/girl_armUp_" + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]

class GirlArmDown(Animation):
    def call_imgs(self):
        for i in range(60):
            img = pygame.image.load("img/meeting/Girl_armDown/girl_armDown_" + str(i) + ".png")
            img = pygame.transform.scale(img, (800, 600))
            self.imgs.append(img)
        self.now_img = self.imgs[0]