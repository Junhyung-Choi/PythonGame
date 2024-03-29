import pygame
import setting
import time
from button import *
from animation import *
from status import *
from script import *
import sound
import middle_scene

buttons = []
animations = []

global gamestatus, isEventAvailable, middle_scene_obj, bgm, girlAnimator
girlAnimator = Animator()

gamestatus : GameStatus = None
isEventAvailable = False

def process_event(event):
    """
    Meeting Scene의 이벤트를 관리하는 함수
    """
    if(isEventAvailable):
        process_event_btn(event)
    
    elif setting.is_init_interface:
        if middle_scene_obj.is_running:
            if middle_scene_obj.is_running:
                middle_scene_obj.next_btn.click_event(event=event, gs=None, b=True)
                middle_scene_obj.prev_btn.click_event(event=event, gs=None, b=True)

def render(pause_obj):
    """
    Meeting Scene의 렌더링을 관리하는 함수
    """
    
    global isEventAvailable, middle_scene_obj, girlAnimator

    # 인터페이스가 준비 완료되었고, 이벤트가 사용 불가능한 상황이라면
    # 이벤트를 활성화한다.
    if (setting.is_init_interface and not isEventAvailable and not middle_scene_obj.is_running):
        isEventAvailable = True

    # 씬 시작이 준비되지 않은 상황이라면, 이를 초기화를 통해 활성화한다.
    if not(setting.is_init_interface):
        init()
    
    # 배경 렌더링
    screen.blit(setting.img_meeting_roombackground,(0,0))
    # 미팅 씬 창문 렌더링
    screen.blit(setting.img_meeting_window, (WINDOW_X, WINDOW_Y))
    # 샹들리에 렌더링
    screen.blit(setting.img_meeting_chandelier,(310,-30))

    # 플레이어 애니메이션 렌더
    screen.blit(girlAnimator.render(), (0, 0))

    # chapter 표시
    if isEventAvailable == True:
        if gamestatus.chapter == 1:
            chapter1_script.show_script(x = 30, y = 30)
        if gamestatus.chapter == 2 :
            chapter2_script.show_script(x = 30, y = 30)
    
    # 말풍선 렌더링
    if isEventAvailable == True:
        if gamestatus.chapter == 1:
            if not chapter1_girl_speech.is_finished == True:
                screen.blit(setting.img_meeting_script_box,(460, 180))
                chapter1_girl_speech.show_script(x = 515, y = 210)
        elif gamestatus.chapter == 2:
            if not chapter2_girl_speech.is_finished == True:
                screen.blit(setting.img_meeting_script_box,(460, 180))
                chapter2_girl_speech.show_script(x = 515, y = 210)
            

    # 버튼 렌더링
    show_btn()

    if middle_scene_obj.is_running:
        middle_scene_obj.render(gamestatus.score)
        isEventAvailable = False

    if not(setting.is_init_interface):
        setting.is_init_interface = True

    if pause_obj.is_pausing:
        isEventAvailable = False
    
    # 게임의 시간을 관리하기 위한 timer() loop에서 호출해준다.
    gamestatus.timer()

def init():
    """
    초기화 함수들을 관리하는 함수
    """
    global isEventAvailable, middle_scene_obj, bgm, girlAnimator
    isEventAvailable = False

    buttons.clear()
    animations.clear()
    girlAnimator = Animator()

    init_ani()
    init_btn()
    init_status()
    init_script()

    bgm = pygame.mixer.Sound("sound/meeting/meeting_bgm.mp3")
    bgm.play()

    middle_scene_obj = middle_scene.MiddleScene()
    girlAnimator.init()
    girlAnimator.bindMiddleSceneStartFunction(middle_scene_obj.start)
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
    global girlAnimator
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
    girl_eyebrowup = Animation("img/meeting/Girl_EyebrowUp/girl_eyebrowUp_", 36)
    
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
    btn_spch_bble_1 = SpeechBubbleButton(47, SPEECH_BUBBLE_Y, [SPEECH_BUBBLE_W, SPEECH_BUBBLE_H], 0, '해보세요.')
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
    # if gamestatus == None:
    #     gamestatus = GameStatus("meeting",buttons[0],buttons[1],buttons[2],buttons[3])
    gamestatus = GameStatus("meeting",buttons[0],buttons[1],buttons[2],buttons[3])

def init_script():
    """
    자막에 대한 객체를 생성해주는 함수
    """
    global chapter1_script, chapter2_script, chapter1_girl_speech, chapter2_girl_speech

    chapter1_script = Script("Chapter 1. 혹시 취미가?")
    chapter2_script = Script("Chapter 2. 평소에..?")
    chapter1_girl_speech = Script("혹시 취미가..?")
    chapter2_girl_speech = Script("평소에..?")


def show_btn():
    """
    버튼 렌더링 시 필요한 함수
    배경을 렌더링 하고, 각 버튼들에 맞는 show 함수를 호출
    """
    screen.blit(img_meeting_question_box, (Q_BOX_X, Q_BOX_Y))
    for i in buttons:
        i.show()
