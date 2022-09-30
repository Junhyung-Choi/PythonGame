import pygame
import setting
import time
from button import *
from animation import *
from status import *
from script import *

buttons = []
animations = []
girlAnimator = Animator()
global current_ani, gamestatus, isEventAvailable
gamestatus = None
isEventAvailable = False


def process_event(event):
    """
    Meeting Scene의 이벤트를 관리하는 함수
    """
    if(isEventAvailable):
        process_event_btn(event)

def render():
    """
    Meeting Scene의 렌더링을 관리하는 함수
    """
    global current_ani, isEventAvailable

    # 인터페이스가 준비 완료되었고, 이벤트가 사용 불가능한 상황이라면
    # 이벤트를 활성화한다.
    if (setting.is_init_interface and not isEventAvailable):
        isEventAvailable = True

    # 씬 시작이 준비되지 않은 상황이라면, 이를 초기화를 통해 활성화한다.
    if not(setting.is_init_interface):
        init()

    # 클릭 이벤트에 따른 애니메이션 제어 (변경 필요)
    index = 0
    while(index < 5):
        if buttons[index].is_clicked == True:
            if index != current_ani:
                if current_ani != -1:
                    buttons[current_ani].is_clicked = False
                current_ani = index
            screen.blit(animations[index].now_img, (0, 0))
            animations[index].update()
        index += 1

    # 미팅 씬 배경화면 렌더링
    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))

    """ script_now_t = time.time()
    if setting.is_script_activate:
        setting.is_script_activate = False
        setting.script_t = time.time()
    if setting.script_t + setting.script_running_t >= script_now_t:
        pass
    else:
        show_btn()
    if setting.running_script:
        setting.running_script = False
        show_script() """
    
    show_script()
    # 버튼 렌더링
    show_btn()

    
    if not(setting.is_init_interface):
        setting.is_init_interface = True

def init():
    """
    초기화 함수들을 관리하는 함수
    """
    global isEventAvailable, current_ani
    isEventAvailable = False
    init_ani()
    init_btn()
    init_status()
    current_ani = -1

def process_event_btn(event):
    """
    이벤트 호출 값을 버튼에게 넘겨주기 위한 함수
    """
    for i in buttons:
        i.click_event(event,gamestatus)

def init_ani():
    """
    애니메이션 이미지 호출 및 애니메이션 관리 객체에 등록
    """
    girl_watchphone = Animation("img/meeting/Girl_WatchPhone/girl_watchPhone_",60)
    girl_smile = Animation("img/meeting/Girl_Smile/girl_smile_", 31)
    girl_eyebrowup = Animation("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_", 20)
    girl_armup = Animation("img/meeting/Girl_ArmUp/girl_armUp_", 60)
    girl_armdown = Animation("img/meeting/Girl_ArmDown/girl_armDown_", 60)

    girlAnimator.add_animation("watchPhone",girl_watchphone)
    girlAnimator.add_animation("smile",girl_smile)
    girlAnimator.add_animation("eyebrowup",girl_eyebrowup)
    girlAnimator.add_animation("armup",girl_armup)
    girlAnimator.add_animation("armdown",girl_armdown)

    animations.extend((girl_watchphone, girl_smile, girl_eyebrowup, girl_armup, girl_armdown))

def init_btn():
    """
    버튼 이미지 로드 및 버튼 관리 객체에 등록하는 함수
    """

    # 기타 버튼들
    btn_pause = PauseButton(PAUSE_BTN_X, PAUSE_BTN_Y, [PAUSE_BTN_SIZE, PAUSE_BTN_SIZE])
    btn_timecheck = TimeCheckButton(LEFT_CIRCLE_BTN_X, LEFT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
    btn_propose = ProposeButton(RIGHT_CIRCLE_BTN_X, RIGHT_CIRCLE_BTN_Y, [CIRCLE_BTN_SIZE, CIRCLE_BTN_SIZE])
    # 대화 버튼들
    btn_spch_bble_1 = SpeechBubbleButton(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 0, '폰 확인해보세요.')
    btn_spch_bble_2 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W + 25, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 1, '웃어보세요.')
    btn_spch_bble_3 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 2 + 50, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 2, '눈썹을 위로 올려보세요.')
    btn_spch_bble_4 = SpeechBubbleButton(47 + SPEECH_BUBBLE_W * 3 + 75, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 3,'탁자에 팔꿈치를 올려보세요.')
    # 버튼 관리 객체에 등록
    buttons.extend((btn_spch_bble_1, btn_spch_bble_2, btn_spch_bble_3, btn_spch_bble_4))
    buttons.extend((btn_pause, btn_timecheck, btn_propose))


def init_status():
    """
    GameStatus 객체를 생성하고, 버튼들을 등록하는 함수
    """
    global gamestatus
    if gamestatus == None:
        gamestatus = GameStatus("meeting",buttons[0],buttons[1],buttons[2],buttons[3])


def show_btn():
    """
    버튼 렌더링 시 필요한 함수
    배경을 렌더링 하고, 각 버튼들에 맞는 show 함수를 호출
    """
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))
    for i in buttons:
        i.show()

def show_script():
    while setting.play:
        if setting.first_script:
            setting.first_script = False
            print("처음 작동중")
            start_t = time.time()
        
        currnet_t = time.time()
        if len(setting.text) - 1 < setting.text_index:
            setting.play = False
            print("마지막 작동 중")
        elif currnet_t >= start_t + setting.delay:
            # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
            myText = setting.myFont.render(setting.render_text, True, (0,0,255)) #(Text,anti-alias, color)
            setting.screen.blit(myText, (100,100)) #(글자변수, 위치)
            print("작동중")
            if setting.text_index == len(setting.text) - 1:
                setting.text_index += 1
                pass
            else:
                setting.render_text += setting.text[setting.text_index]
                start_t = currnet_t
                setting.text_index += 1
    return