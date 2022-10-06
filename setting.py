import pygame

pygame.font.init()

is_init = False

LEFT = 1
RIGHT = 3

# 프레임
FPS = 60

# 스크린 사이즈 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# 현재 씬 
running = True
stage = -1

# 점수 저장소
score = 0

# 게임 상태 (진행중, 일시정지, 게임오버)
# 'playing', 'pause', 'gameover'
game_status = 'playing'

# 남은 시간
left_time_min = 0
left_time_second = 0

# 게임 오버 모달 창 띄워졌는지 여부
is_init_gameover = False

# 메뉴씬 소리 재생중인지 여부
is_run_left_sound = False
is_run_right_sound = False

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

FONT_SIZE = 12
# 미팅 이미지 파일
img_speech_bubble = pygame.image.load("img/meeting/Meeting_QuestionBox.png")
img_speech_bubble = pygame.transform.scale(img_speech_bubble, (SPEECH_BUBBLE_W, SPEECH_BUBBLE_H))
img_meeting_script_box = pygame.image.load("img/meeting/Meeting_SpeechBubble.png")
img_meeting_script_box = pygame.transform.scale(img_meeting_script_box, (300, 100))
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
img_meeting_chandelier = pygame.image.load("img/meeting/Meeting_Chandelier.png")
img_meeting_roombackground = pygame.image.load("img/meeting/Meeting_RoomBackground.png")
img_meeting_roombackground = pygame.transform.scale(img_meeting_roombackground, (800,600))

font = pygame.font.Font("font/DungGeunMo.ttf", FONT_SIZE)

is_init_interface = False
is_meet_next = False

# 텍스트

# 글자체(text font) 지정하기
text_size = 50
font_name = "font/DungGeunMo.ttf"
myFont = pygame.font.Font("font/DungGeunMo.ttf", 25)

text = "Hello World"
render_text = ""
text_index = 0

script_start_t = 0
script_currnet_t = 0
running_script = True
first_script = True
delay = 0.1

# 변수
x_pos = 0
y_pos = 0

play = True

is_script_activate = True
script_running_t = len(text) * delay + 0.5
script_t = 0

# 스토리 씬
first = True

STORY_NUMBERS = 6

LEFT = 1
RIGHT = 3

STORY_W = 300
STORY_H = 400

NEXT_SCENE_X = screen_width - 55
NEXT_SCENE_Y = screen_height / 2
NEXT_SCENE_W = 35
NEXT_SCENE_H = 26

BACKWARD_SCENE_X = 35
BACKWARD_SCENE_Y = screen_height / 2
BACKWARD_SCENE_W = 35
BACKWARD_SCENE_H = 26

GO_TUTORIAL_X = 600
GO_TUTORIAL_Y = 500
GO_TUTORIAL_W = 200
GO_TUTORIAL_H = 57

NEXT_STAGE_X = 550
NEXT_STAGE_Y = 120
NEXT_STAGE_W = 160
NEXT_STAGE_H = 57



next_scene_img = pygame.image.load("img/story/Next_Scene.png")
next_scene_img = pygame.transform.scale(next_scene_img, (NEXT_SCENE_W, NEXT_SCENE_H))
backward_scene_img = pygame.image.load("img/story/Before_Scene.png")
backward_scene_img = pygame.transform.scale(backward_scene_img, (BACKWARD_SCENE_W, BACKWARD_SCENE_H))
go_tutorial_img = pygame.image.load("img/story/SkipToPlay.png")
go_tutorial_img = pygame.transform.scale(go_tutorial_img, (GO_TUTORIAL_W, GO_TUTORIAL_H))
next_stage_img = pygame.image.load("img/story/SkipToPlay.png")
next_stage_img = pygame.transform.scale(go_tutorial_img, (NEXT_STAGE_W, NEXT_STAGE_H))
back_img = pygame.image.load("img/ending/back.png")
back_img = pygame.transform.scale(back_img, (800, 600))

alpha = 250
tutorial = False


# 메뉴 씬
eyes = []
for idx in range(36):
    eyes.append(pygame.image.load("img/eye/eye_" + str(idx) + ".png"))
    eyes[idx] = pygame.transform.scale(eyes[idx],(800,600))

eyeBall = pygame.image.load("img/eye/eyeBall.png")
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


img_gameover = pygame.image.load("img/gameover.png")
img_gameover = pygame.transform.scale(img_gameover, (400, 300))
