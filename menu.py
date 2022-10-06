import pygame
import setting

global is_inited, bgm
is_inited = False

def init():
    global is_inited, bgm
    is_inited = True
    bgm = pygame.mixer.Sound("./sound/menu_bgm.mp3")
    bgm.play(-1)

def remap(old_val, old_min, old_max, new_min, new_max):
    return (new_max - new_min)*(old_val - old_min) / (old_max - old_min) + new_min

def process_event(event):
    if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
        # 아래는 예시입니다.
        if event.key == pygame.K_1:
            stage = 1
            print("게임시작")
        if event.key == pygame.K_2:
            print("패치노트")
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX, mouseY = pygame.mouse.get_pos()
        if(180 < mouseX < 260 and 480 < mouseY < 540):
            print("Next Scene")
            pygame.mixer.Sound("./sound/btn_click.wav").play()
            setting.stage += 1
            bgm.stop()
        if(540 < mouseX < 620 and 480 < mouseY < 540):
            pygame.mixer.Sound("./sound/btn_click.wav").play()
            print("GAME OVER")

def render():
    global is_inited
    if not is_inited:
        init()
    setting.screen.blit(setting.main_background, (0, 0))
    
    frame_number = 36
    maxHeight = setting.screen.get_height()
    maxWidth = setting.screen.get_width()
    
    mouseX, mouseY = pygame.mouse.get_pos()
    # print(mouseY)
    eyeX = int(remap(mouseX,0,maxWidth,230,350))
    eyeY = int(remap(mouseY,0,maxHeight,280,320))
    setting.screen.blit(setting.eyeBall,(eyeX,eyeY))
    setting.screen.blit(setting.eyeBall,(eyeX+200,eyeY))
    
    # if(mouseY < maxHeight / 2):
    #     setting.screen.blit(setting.eyes[17],(0,0))
    # else:
    xfidx = 0
    yfidx = 0
    if mouseX < 170:
        xfidx = 0
    if mouseX > 630:
        xfidx = 35
    if mouseY > 540:
        yfidx = 35
    xfidx = int(remap(mouseX,170,630,0,frame_number-1))
    if(xfidx < 0):
        xfidx = -xfidx
    yfidx = int(remap(mouseY,0,540,0,frame_number-1))
    fidx = min(xfidx, yfidx)
    if(fidx > 35):
        fidx = 35
    # fidx = int(remap(mouseX,170,630,0,frame_number-1))
    setting.screen.blit(setting.eyes[fidx],(0,0))
    
    setting.screen.blit(setting.main_title, (176/2,54/2))
    setting.screen.blit(setting.main_table, (-40/2,899/2))

    if(180 < mouseX < 260 and 480 < mouseY < 540):
        if not setting.is_run_left_sound:
            pygame.mixer.Sound("./sound/btn_hover.wav").play()
            setting.is_run_left_sound = True
        setting.screen.blit(setting.menu_button_click,(377/2,974/2))
    else:
        setting.screen.blit(setting.menu_button,(377/2,974/2))
        setting.is_run_left_sound = False

    if(540 < mouseX < 620 and 480 < mouseY < 540):
        if not setting.is_run_right_sound:
            pygame.mixer.Sound("./sound/btn_hover.wav").play()
            setting.is_run_right_sound = True
        setting.screen.blit(setting.menu_button_click,(1087/2,974/2))
    else:
        setting.screen.blit(setting.menu_button,(1087/2,974/2))
        setting.is_run_right_sound = False
        