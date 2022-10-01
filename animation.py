from enum import Enum
import pygame
import setting

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
        self.isPlayed = False
        self.isArmOnTable = True
    
    def init(self):
        self.now_img = self.imgs[0]
        self.index = 0
        self.isPlayed = False

    def update(self):
        if(not self.isPlayed):
            self.now_img = self.imgs[self.index]
            self.index += 1
            if self.index >= len(self.imgs):
                self.isPlayed = True

class Animator():
    def __init__(self):
        self.current_animation : Animation = None
        self.animations = {}
        self.state = AnimatorState.STOP
        self.next_animation : Animation = None
        self.isMiddleSceneAnimationStarted = False
        self.middleSceneStartFunction = None

    def init(self):
        self.current_animation = self.animations["armdown"]
        self.current_animation.now_img = self.current_animation.imgs[59]
        self.current_animation.isPlayed = True
    
    def bindMiddleSceneStartFunction(self, func):
        self.middleSceneStartFunction = func
    
    def update(self):
        """
        # 애니메이션 전환 함수
        
        update 함수가 호출될때마다 자동 호출.
        """
        if(self.state == AnimatorState.TRANS):
            # 실제로 다음 애니메이션을 갱신해야 하는 경우
            if(self.current_animation.isPlayed):
                # 다음 애니메이션이랑 지금 애니메이션이랑 팔 위치가 다르다면
                if self.current_animation.isArmOnTable != self.next_animation.isArmOnTable:
                    # 팔 올린거에서 내려야 하는 상황일때
                    if self.current_animation.isArmOnTable == True:
                        self.current_animation = self.animations["armdown"]
                        self.current_animation.init()
                    # 팔 내린거에서 올려야 하는 상황일때
                    else:
                        self.current_animation = self.animations["armup"]
                        self.current_animation.init()
                # 팔을 교체하지 않아도 됨.
                else: 
                    self.current_animation = self.next_animation
                    self.current_animation.init()
                    self.state = AnimatorState.PLAY
                    self.next_animation = None
            # 기존 애니메이션이 아직 끝나지 않은 경우
            else:
                pass
            self.current_animation.update()

        elif(self.state == AnimatorState.PLAY):
            if(self.current_animation.isPlayed == True):
                self.state == AnimatorState.STOP
            else:
                self.current_animation.update()
        
        elif(self.state == AnimatorState.STOP):
            print("STOP")
            if(self.isMiddleSceneAnimationStarted):
                print("What")
                self.middleSceneStartFunction()
            pass
    
    def render(self):
        """
        Return:
            현재 Animator가 출력해야 하는 이미지를 리턴함
        """
        self.update()
        return self.current_animation.now_img

    def translate(self, key):
        """
        ### 애니메이션을 전환하는 함수\n
        한번 애니메이션이 전환 중이라면 다음 전환은 입력받지 않음. (디버그 라인 출력)\n
        다음 애니메이션에 `key`로 입력받은 애니메이션을 등록해둔 후 state를 변경\n
        current_animation이 계속해서 재생되지 않도록 loop 또한 변경함
        """
        # 만일 전환중인 상황이라면
        if(self.state == AnimatorState.TRANS):
            print("You cannot translate animation now.")
            print("This animator is currently tranlsating animation")
        # 만일 전환중인 상황이 아니라면 전환
        else:
            self.next_animation = self.animations[key]
            self.state = AnimatorState.TRANS
            # self.current_animation.loop = False // loop 하는 애니매이션 존재 X
    
    def add_animation(self, key, ani):
        self.animations[key] = ani

    def translate_nextphase(self):
        """
        ### 중간 점검 이미지가 나오기 전 폰이 울리는 애니메이션으로 전환하기 위한 함수
        """

        # 현재 손이 위로 올라와있는지 아닌지
        isArmOnTable = self.current_animation.isArmOnTable
        if(isArmOnTable):
            self.translate("ringpositive")
        else:
            self.translate("ringnegative")
        self.isMiddleSceneAnimationStarted = True

class AnimatorState(Enum):
    PLAY = 1
    TRANS = 2
    STOP = 3

