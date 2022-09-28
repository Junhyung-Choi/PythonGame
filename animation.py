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
        self.state = AnimatorState.PLAY
        self.nextanimation = None
    
    def update(self):
        # 트랜스 상태일때는 애니메이션이 끝났는지를 확인해야함
        # current_animation이 loop = True 라면 이걸 False로 변경 (이건 translate에서 변경해도 될듯)
        # current_animation의 now_img가 마지막 img일때 current_animation 등을 진행
        # 만일 current_animation의 상태가 팔이 전환되는 상황이 필요하다면 이를 전환 할 수 있어야 함
        if(self.state == AnimatorState.TRANS):
            self.current_animation.update()
        if(self.state == AnimatorState.PLAY):
            pass
        if(self.state == AnimatorState.STOP):
            pass
        pass
    
    def render(self):
        return self.current_animation.now_img

    
    def translate(self, key):
        self.state = AnimatorState.TRANS
        self.current_animation = self.animations[key]
    
    def add_animation(self, key, ani):
        self.animations[key] = ani
    

class AnimatorState(Enum):
    PLAY = 1
    TRANS = 2
    STOP = 3

