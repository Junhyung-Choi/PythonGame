import pygame

pygame.font.init()

LEFT = 1
RIGHT = 3

# 스크린 사이즈 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# 현재 씬 
running = True
stage = 0

# 윈도우 설정
pygame.display.set_caption("Python Game")

# 이미지 에셋 업로드
start_background = pygame.image.load("img/start.png")
background = pygame.image.load("img/background.png")

PAUSE_BTN_SIZE = 32
PAUSE_BTN_X = 730
PAUSE_BTN_Y = 16
img_pause = pygame.image.load("img/pause_normal.png")
img_pause = pygame.transform.scale(img_pause, (PAUSE_BTN_SIZE, PAUSE_BTN_SIZE))


# 미팅 이미지 파일 상수
CIRCLE_BTN_SIZE = 100
LEFT_CIRCLE_BTN_X = 13
LEFT_CIRCLE_BTN_Y = 375
RIGHT_CIRCLE_BTN_X = 687
RIGHT_CIRCLE_BTN_Y = 375

Q_BOX_X = 13 # 질문 박스
Q_BOX_Y = 495

SPEECH_BUBBLE_W = 158 # 말풍선
SPEECH_BUBBLE_H = 52
SPEECH_BUBBLE_Y = Q_BOX_Y + 26

WATCH_CLOCK_W = 491 # 시계 볼때 팔
WATCH_CLOCK_H = 261
WATCH_CLOCK_X = 0
WATCH_CLOCK_Y = 286

WINDOW_W = 196
WINDOW_H = 185
WINDOW_X = 28
WINDOW_Y = 169

# 미팅 이미지 파일
img_speech_bubble = pygame.image.load("img/meeting/Meeting_QuestionBox.png")
img_speech_bubble = pygame.transform.scale(img_speech_bubble, (SPEECH_BUBBLE_W, SPEECH_BUBBLE_H))
img_meeting_question_box = pygame.image.load("img/meeting/Meeting_QuestionBG.png")
img_meeting_question_box = pygame.transform.scale(img_meeting_question_box, (775, 105))
img_meeting_propose = pygame.image.load("img/meeting/Meeting_propose.png")
img_meeting_propose = pygame.transform.scale(img_meeting_propose, (CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE))
img_meeting_time_check = pygame.image.load("img/meeting/Meeting_Timecheck.png")
img_meeting_time_check = pygame.transform.scale(img_meeting_time_check, (CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE))
img_meeting_watch_clock = pygame.image.load("img/meeting/Meeting_checkTime.png")
img_meeting_watch_clock = pygame.transform.scale(img_meeting_watch_clock, (WATCH_CLOCK_W, WATCH_CLOCK_H))
img_meeting_window = pygame.image.load("img/meeting/Meeting_Window.png")
img_meeting_window = pygame.transform.scale(img_meeting_window, (WINDOW_W, WINDOW_H))

font = pygame.font.Font("font/DungGeunMo.ttf", 15)

is_init_interface = False

# 스토리 씬
t = 0
first = True


# 메뉴 씬
eyes = []
for idx in range(36):
    eyes.append(pygame.image.load("img/eye_" + str(idx) + ".png"))
    eyes[idx] = pygame.transform.scale(eyes[idx],(800,600))

eyeBall = pygame.image.load("img/eyeBall.png")
eyeBall = pygame.transform.scale(eyeBall,(eyeBall.get_width()/2,eyeBall.get_height()/2))

main_table = pygame.image.load("img/Main_Table.png")
main_table = pygame.transform.scale(main_table,(1681/2,312/2))

main_title = pygame.image.load("img/Main_Title.png")
main_title = pygame.transform.scale(main_title,(1249/2,404/2))

main_background = pygame.image.load("img/MainBG.png")
main_background = pygame.transform.scale(main_background,(main_background.get_width()/2,main_background.get_height()/2))

menu_button_click = pygame.image.load("img/Button_click.png")
menu_button_click = pygame.transform.scale(menu_button_click,(136/2,118/2))

menu_button = pygame.image.load("img/Button_normal.png")
menu_button = pygame.transform.scale(menu_button,(136/2,118/2))