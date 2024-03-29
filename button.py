from setting import *
import setting
from status import GameStatus
import meeting

class Button:
    def __init__(self, x1, y1, size):
        self.x_pos = x1
        self.y_pos = y1
        self.width = size[0]
        self.height = size[1]
        self.is_clicked = False

    def click(self, gs, b):
        print('클릭됨')
        self.is_clicked = True

    def click_event(self, event, gs : GameStatus, b=None):
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if self.x_pos <= event.pos[0] <= self.x_pos + self.width and self.y_pos <= event.pos[1] <= self.y_pos + self.height:
                if b != None:
                    self.click(gs, b)
                else:
                    self.click(gs)

    def show(self):
        pygame.draw.rect(screen, (100, 100, 100), [self.x_pos, self.y_pos, self.width, self.height])


class PauseButton(Button):
    def show(self):
        screen.blit(img_pause, (self.x_pos, self.y_pos))

    def click(self, gs: GameStatus):
        self.is_clicked = not self.is_clicked
        setting.game_status = 'pause'


class SpeechBubbleButton(Button):
    def __init__(self, x1, y1, size, index, text='테스트'):
        super().__init__(x1, y1, size)
        self.index = index
        self.text = text

    def show(self):
        screen.blit(img_speech_bubble, (self.x_pos, self.y_pos))
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x_pos + 17, self.y_pos + (SPEECH_BUBBLE_H / 2) - FONT_SIZE))

    def click(self, gs: GameStatus):
        print(self.text + ' 클릭됨')
        gs.speech_button_clicked(self.index)
        self.is_clicked = not self.is_clicked


class TimeCheckButton(Button):
    def __init__(self, x1, y1, size):
        super().__init__(x1, y1, size)
        self.y_now = 600
        self.gs = None
        self.time_font = pygame.font.Font("font/DungGeunMo.ttf", 32)

    def show(self):
        if self.is_clicked:
            if self.y_now - 60 > WATCH_CLOCK_Y:
                self.y_now -= 60
            else:
                self.y_now -= self.y_now - WATCH_CLOCK_Y
            screen.blit(img_meeting_watch_clock, (WATCH_CLOCK_X, self.y_now))
            if self.y_now == WATCH_CLOCK_Y:
                if not setting.game_status == 'pause':
                    minute, second = self.gs.get_left_min_sec()
                else:
                    minute, second = setting.left_time_min, setting.left_time_second
                if minute != 0:
                    time_text = str(minute) + ':' + str(second).zfill(2)
                else:
                    time_text = '0:' + str(second).zfill(2)
                text = self.time_font.render(time_text, True, (0, 0, 0))
                screen.blit(text, (230, self.y_now + 90))
            img_meeting_time_check.set_alpha(100)
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
            img_meeting_time_check.set_alpha(256)
        else:
            screen.blit(img_meeting_watch_clock, (WATCH_CLOCK_X, self.y_now))
            screen.blit(img_meeting_time_check, (self.x_pos, self.y_pos))
            if self.y_now + 60 < 600:
                self.y_now += 60
            elif self.y_now < 600:
                self.y_now += 600 - self.y_now

    def click(self, gs: GameStatus):
        if self.gs is None:
            self.gs = gs
        self.is_clicked = not self.is_clicked


class ProposeButton(Button):
    def show(self):
        screen.blit(img_meeting_propose, (self.x_pos, self.y_pos))

    def click(self, gs: GameStatus):
        if not self.is_clicked:
            if (meeting.gamestatus.score - 15 < -3):
                meeting.gamestatus.score -= 3
                meeting.gamestatus.girlAnimator.translate("neckmassage")
                print('==========BAD==========')
            elif (-3 <= meeting.gamestatus.score - 15 <= 3):
                meeting.gamestatus.score += 3
                meeting.gamestatus.girlAnimator.translate("smile")
                print('==========NORMAL==========')
            elif (3 < meeting.gamestatus.score - 15):
                meeting.gamestatus.score += 5
                meeting.gamestatus.girlAnimator.translate("biglaugh")
                print('==========GOOD==========')
            
            print("CURRENT SCORE: ", meeting.gamestatus.score)
            print('호감을 나타냅니다.')
        else:
            print("CURRENT SCORE: ", meeting.gamestatus.score)
            print("호감 표시는 1회만 가능합니다.")
        self.is_clicked = True
    
class NextButton(Button):
    def __init__(self, obj):
        super().__init__(setting.NEXT_SCENE_X, setting.NEXT_SCENE_Y, [setting.NEXT_SCENE_W, setting.NEXT_SCENE_H])
        self.obj = obj

    def show(self):
        if self.obj.scene.index < len(self.obj.scene.imgs) - 1:
            setting.screen.blit(setting.next_scene_img, (self.x_pos, self.y_pos))

    def click(self, gs : GameStatus, b):
        if self.obj.scene.index < len(self.obj.scene.imgs) - 1:
            self.obj.scene.update()
            self.obj.sound.update(b)

class PrevButton(Button):
    def __init__(self, obj):
        super().__init__(setting.BACKWARD_SCENE_X, setting.BACKWARD_SCENE_Y, [setting.BACKWARD_SCENE_W, setting.BACKWARD_SCENE_H])
        self.obj = obj

    def show(self):
        if self.obj.scene.index > 0:
            setting.screen.blit(setting.backward_scene_img, (self.x_pos, self.y_pos))

    def click(self, gs : GameStatus, b):
        if self.obj.scene.index > 0:
            self.obj.scene.backward()
            self.obj.sound.backward(b)

class RestartButton(Button):
    def __init__(self):
        super().__init__(319, 392, [161, 46])
        self.btn_img = pygame.image.load("img/ending/prototype/ReplayGame_normal.png")
        self.btn_img = pygame.transform.scale(self.btn_img, (self.width, self.height))
        self.btn_hover_img = pygame.image.load("img/ending/prototype/ReplayGame_Pressed.png")
        self.btn_hover_img = pygame.transform.scale(self.btn_hover_img, (self.width, self.height))

    def show(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        if self.x_pos <= mouseX <= self.x_pos + self.width and self.y_pos <= mouseY <= self.y_pos + self.height:
            setting.screen.blit(self.btn_hover_img, (self.x_pos, self.y_pos))
        else:
            setting.screen.blit(self.btn_img, (self.x_pos, self.y_pos))

    def click(self, gs: GameStatus):
        setting.stage = 0
        print('asdf')