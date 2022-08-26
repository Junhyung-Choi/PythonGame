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