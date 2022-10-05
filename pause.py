import pygame
import setting
import time
import meeting

class Pause():
    def __init__(self):
        self.pause_time = None

        self.background = pygame.image.load("img/PauseUI/PauseBox.png")
        self.background = pygame.transform.scale(self.background, (650,170))
        self.backgroundPosition = (175//2,461//2)
        
        # 0: Normal / 1: Pressed
        self.yesButtons = []
        # 0: Normal
        tmp = pygame.image.load("img/PauseUI/Pause_Yes_Normal.png")
        tmp = pygame.transform.scale(tmp, (160, 50))
        self.yesButtons.append(tmp)
        # 1: Pressed
        tmp = pygame.image.load("img/PauseUI/Pause_Yes_Pressed.png")
        tmp = pygame.transform.scale(tmp, (160, 50))
        self.yesButtons.append(tmp)
        self.yesPosition = (314//2,658//2)
        self.yesIndex = 0

        # 0: Normal / 1: Pressed
        self.noButtons = []
        # 0: Normal
        tmp = pygame.image.load("img/PauseUI/Pause_No_Normal.png")
        tmp = pygame.transform.scale(tmp, (160, 50))
        self.noButtons.append(tmp)
        # 1: Pressed
        tmp = pygame.image.load("img/PauseUI/Pause_No_Pressed.png")
        tmp = pygame.transform.scale(tmp, (160, 50))
        self.noButtons.append(tmp)
        self.noPosition = (996//2,665//2)
        self.noIndex = 0

        self.is_pausing = False

    def pause(self, current_time):
        print('일시정지')
        self.is_pausing = True
        self.pause_time = current_time
        setting.left_time_min, setting.left_time_second = meeting.gamestatus.get_left_min_sec()

    def show(self):
        screen = setting.screen
        
        # 배경 렌더링
        screen.blit(self.background,self.backgroundPosition)

        # 버튼 렌더링
        screen.blit(self.yesButtons[self.yesIndex],self.yesPosition)
        screen.blit(self.noButtons[self.noIndex],self.noPosition)

        # setting.screen.blit(self.img, (200, 100))
        # self.btn_start.show()

    def event(self, event:pygame.event.Event):
        mouseX, mouseY = pygame.mouse.get_pos()
        
        # 게임 종료 버튼
        if(self.yesPosition[0] <= mouseX <= self.yesPosition[0] + 160 and self.yesPosition[1] <= mouseY <= self.yesPosition[1] + 50):
            self.yesIndex = 1
            # 클릭시 
            if event.type == pygame.MOUSEBUTTONUP and event.button == setting.LEFT:
                self.is_pausing = False
                setting.game_status = 'playing'
                setting.stage = 0
        else:
            self.yesIndex = 0
        
        # 일시정지 해제 버튼
        if(self.noPosition[0] <= mouseX <= self.noPosition[0] + 160 and self.noPosition[1] <= mouseY <= self.noPosition[1] + 50):
            self.noIndex = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == setting.LEFT:
                self.is_pausing = False
                self.start()
        else:
            self.noIndex = 0


    def start(self):
        print('실행')
        self.is_pausing = False
        setting.game_status = 'playing'
        
        if meeting.gamestatus.scene_name == 'meeting':
            ctime = self.pause_time
            ntime = time.time()
            use_time = ntime - ctime
            use_time = int(use_time)
            meeting.gamestatus.game_sec += use_time