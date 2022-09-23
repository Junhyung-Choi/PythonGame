from enum import Enum
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
        self.loop = True
        self.isPlayed = False
        self.isArmOnTable = True

    def update(self):
        # 루프를 돌아야 하거나, 한번 끝까지 재생되었거나
        if(self.loop or not self.isPlayed):
            self.index += 1
            if self.index >= len(self.imgs):
                self.isPlayed = True
                self.index = 0
            self.now_img = self.imgs[self.index]

class Animator():
    def __init__(self):
        self.current_animation = None
        self.animations = {}
        self.state = AnimatiorState.PLAY
    
    def update(self):
        pass
    
    def translate(self, key):
        self.state = AnimatiorState.TRANS
        self.current_animation = self.animations[key]
    
    def add_animation(self, key, ani):
        self.animations[key] = ani
    

class AnimatiorState(Enum):
    PLAY = 1
    TRANS = 2
    STOP = 3

