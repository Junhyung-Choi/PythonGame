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
    
    def init():
        print("initing")

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
        self.next_animation = None
    
    def update(self):
        """
        애니메이션의 다음

        if state == TRANS:
            if 애니메이션이 종료 됨:
                if 팔 교체해야함 :
                    팔 교체에 맞는 애니메이션으로 전환
                    다음 애니메이션 갱신하지 않음
                    여전히 trans 상태로 둠
                else (교체 안해도 됨):
                    다음 애니메이션 pop 후 현재 애니메이션으로 전환
                    state를 trans 에서 play로 전환
            else (종료되지 않음):
                current_animation의 update 함수 호출함.
        elif state == PLAY

            저쩌구
        elif state == STOP:
            그쩌구
        """
        if(self.state == AnimatorState.TRANS):
            if(self.current_animation.isPlayed):
                # if current_animation.isArmOnTable != self.next_animation.isArmOnTable: 관련 함수 작성
                # else:
                pass
            else:
                self.current_animation = self.next_animation
                self.current_animation.init()
                self.state = AnimatorState.PLAY
                self.next_animation = None
            self.current_animation.update()
        else:
            self.current_animation.update()
        if(self.state == AnimatorState.PLAY):
            pass
        if(self.state == AnimatorState.STOP):
            pass
        pass
    
    def render(self):
        """
        Return:
            현재 Animator가 출력해야 하는 이미지를 리턴함
        """
        return self.current_animation.now_img

    def translate(self, key):
        """
        ### 애니메이션을 전환하는 함수\n
        한번 애니메이션이 전환 중이라면 다음 전환은 입력받지 않음. (디버그 라인 출력)\n
        다음 애니메이션에 `key`로 입력받은 애니메이션을 등록해둔 후 state를 변경\n
        current_animation이 계속해서 재생되지 않도록 loop 또한 변경함
        """
        # 만일 전환중인 상황이라면
        if(self.state != AnimatorState.TRANS):
            print("You cannot translate animation now.")
            print("This animator is currently tranlsating animation")
        # 만일 전환중인 상황이 아니라면 전환
        else:
            self.next_animation = self.animations[key]
            self.state = AnimatorState.TRANS
            self.current_animation.loop = False
    
    def add_animation(self, key, ani):
        self.animations[key] = ani
    

class AnimatorState(Enum):
    PLAY = 1
    TRANS = 2
    STOP = 3

