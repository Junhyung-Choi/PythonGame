from tkinter.tix import Tree
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
gamestatus : GameStatus = None
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

    # 플레이어 애니메이션 렌더
    screen.blit(girlAnimator.render(), (0, 0))

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
    
    if (isEventAvailable):
        show_script("혹시 취미가?")
    # 버튼 렌더링
    show_btn()

    
    if not(setting.is_init_interface):
        setting.is_init_interface = True

def init():
    """
    초기화 함수들을 관리하는 함수
    """
    global isEventAvailable
    isEventAvailable = False
    init_ani()
    init_btn()
    init_status()

    girlAnimator.init()
    gamestatus.bindGirlAnimator(girlAnimator=girlAnimator)


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
    # 팔 올리기 : 부정 -> 긍정(팔 위에), 매칭 점수 없음
    girl_armup = Animation("img/meeting/Girl_ArmUp/girl_armUp_", 60)

    # 팔 내리기 : 긍정 -> 부정(팔 아래), 매칭 점수 없음
    girl_armdown = Animation("img/meeting/Girl_ArmDown/girl_armDown_", 60)
    girl_armdown.isArmOnTable = False
    
    # 크게 웃기 : 긍정(팔 위에), 매칭 점수 : 3점
    girl_biglaugh = Animation("img/meeting/Girl_BigLaugh/girl_biglaugh_", 60)

    # 웃기 : 긍정(팔 위에), 매칭 점수 : 2점
    girl_smile = Animation("img/meeting/Girl_Smile/girl_smile_", 78)

    # 눈썹 올리기 : 긍정(팔 위에), 매칭 점수 : 1점
    girl_eyebrowup = Animation("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_", 20)
    
    # 고개 끄덕이기 : 긍정(팔 위에), 매칭 점수 : 0점
    girl_shakehead = Animation("img/meeting/Girl_ShakeHead/girl_shakehead_", 13)
    
    # 목 만지기 : 부정(팔 아래에), 매칭 점수 : -1점
    girl_neckmassage = Animation("img/meeting/Girl_NeckMassage/girl_NeckMassage_", 60)
    girl_neckmassage.isArmOnTable = False
    
    # 바깥 쳐다보기 : 부정(팔 아래에), 매칭 점수 : -2점
    girl_watchoutside = Animation("img/meeting/Girl_WatchOutside/girl_watchoutside_", 31)
    girl_watchoutside.isArmOnTable = False

    # 핸드폰 보기 : 부정(팔 아래), 매칭 점수 : -3점
    girl_watchphone = Animation("img/meeting/Girl_WatchPhone/girl_watchPhone_",60)
    girl_watchphone.isArmOnTable = False

    # 중간 챕터 폰 올리기(부정) : 긍정(팔 위에)
    girl_chapter_change_phone_ring_positive = Animation("img/meeting/Girl_ChapterChangePhoneRing/Positive/girl_ChapChangePhoneRing_Positive_", 27)

    # 중간 챕터 폰 올리기(부정) : 부정(팔 아래에), 매칭 점수 : X점  
    girl_chapter_change_phone_ring_negative = Animation("img/meeting/Girl_ChapterChangePhoneRing/Negative/girl_ChapChangePhoneRing_Negative_", 27)
    girl_chapter_change_phone_ring_negative.isArmOnTable = False
    
    girlAnimator.add_animation("armup",girl_armup)
    girlAnimator.add_animation("armdown",girl_armdown)

    girlAnimator.add_animation("biglaugh", girl_biglaugh)
    girlAnimator.add_animation("smile", girl_smile)
    girlAnimator.add_animation("eyebrowup",girl_eyebrowup)
    girlAnimator.add_animation("shakehead",girl_shakehead)
    girlAnimator.add_animation("neckmassage",girl_neckmassage)
    girlAnimator.add_animation("watchoutside",girl_watchoutside)
    girlAnimator.add_animation("watchphone",girl_watchphone)

    girlAnimator.add_animation("ringpositive", girl_chapter_change_phone_ring_positive)
    girlAnimator.add_animation("ringnegative", girl_chapter_change_phone_ring_negative)

    girlAnimator.init()

    # animations.extend((girl_watchphone, girl_smile, girl_eyebrowup, girl_armup, girl_armdown))

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
