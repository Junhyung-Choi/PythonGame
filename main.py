import pygame

import setting
import menu
import story
import meeting
import ending
import pause
import time

#############################################
#                                            
#    stage  0 : 메뉴 씬                      
#    stage  1 : 스토리 씬                    
#    stage  2 : 소개팅 씬                    
#    stage -1 : 엔딩 씬                
#                                            
#############################################

global pause_obj, last_stage
last_stage = 0

def init():
    global pause_obj, ending_obj
    pause_obj = pause.Pause()
    ending_obj = ending.Ending()

    pygame.display.set_caption("DON'T ASK JUST SEE")
    
    setting.is_init = True

def reset():
    global pause_obj, ending_obj
    pause_obj = pause.Pause()
    ending_obj = ending.Ending()
    menu.init()

    setting.first = True
    setting.is_init_interface = False

def loop():
    while setting.running:
        # 각 스테이지 렌더링
        render()
        # 이벤트 처리
        event()


def event():
    # 이벤트 처리
    for event in pygame.event.get():
        # 모든 스테이지에서 공통적으로 사용되는 이벤트
        if event.type == pygame.QUIT:
            setting.running = False
        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
            # 개발자 테스트용 스테이지 이동 키
            if event.key == pygame.K_MINUS: 
                setting.stage -= 1
                print("현재 스테이지 : " + str(setting.stage))
            elif event.key == pygame.K_EQUALS:
                setting.stage += 1
                print("현재 스테이지 : " + str(setting.stage))

        if setting.game_status == 'pause':
            pause_obj.event(event)
            
        # 스테이지별 이벤트
        if setting.stage == 0: # 시작 화면일때
            menu.process_event(event=event)

        if setting.stage == 1: # 첫 번째 stage 이벤트
            story.process_event(event=event)

        if setting.stage == 2: # 두 번째 stage 이벤트
            meeting.process_event(event=event)

        if setting.stage == -1:
            if ending_obj.scene.index == 0 or ending_obj.scene.index == 3 or ending_obj.scene.index == 4:
                ending_obj.next_btn.click_event(event=event, gs=None, b=False)
            else:
                ending_obj.next_btn.click_event(event=event, gs=None, b=True)

            if ending_obj.scene.index == 1 or ending_obj.scene.index == 4 or ending_obj.scene.index == 5:
                ending_obj.prev_btn.click_event(event=event, gs=None, b=False)
            else:
                ending_obj.prev_btn.click_event(event=event, gs=None, b=True)
            if ending_obj.alpha < -50:
                ending_obj.prototype.restart.click_event(event=event, gs=None)


def render():
    global last_stage, pause_obj, ending_obj

    if(setting.stage == 0 and last_stage != setting.stage):
        reset()
    last_stage = setting.stage
    if not setting.is_init:
        init()


    if setting.stage != 0:
        setting.screen.blit(setting.background, (0, 0))

    if setting.stage == 0:
        menu.render()
        #pygame.display.update()
    elif setting.stage == 1:
        story.render()
        #pygame.display.update()
    elif setting.stage == 2:
        meeting.render(pause_obj)

    elif setting.stage == -1:        
        ending_obj.render(meeting.gamestatus.score)

    # 게임 상태 관리 (게임오버, 일시정지)
    if setting.game_status == 'pause':
        if not pause_obj.is_pausing:
            pause_obj.pause(time.time())
        pause_obj.show()

    pygame.time.Clock().tick(setting.FPS)
    pygame.display.update()


# 파이게임 초기화
pygame.init()
# 게임 전체 루프
loop()
# 파이게임 종료
pygame.quit()

