import pygame

import setting
import menu
import story
import meeting
#############################################
#                                            
#    stage  0 : 메뉴 씬                      
#    stage  1 : 스토리 씬                    
#    stage  2 : 소개팅 씬                    
#    stage -1 : 오버레이 화면                
#                                            
#############################################

def loop():
    while setting.running:
        # 이벤트 처리
        event()
        # 각 스테이지 렌더링
        render()


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
            if event.key == pygame.K_EQUALS:
                setting.stage += 1
                print("현재 스테이지 : " + str(setting.stage))

        # 스테이지별 이벤트
        if setting.stage == 0: # 시작 화면일때
            menu.process_event(event=event)

        if setting.stage == 1: # 첫 번째 stage 이벤트
            story.process_event(event=event)

        if setting.stage == 2: # 두 번째 stage 이벤트
            meeting.process_event(event=event)

def render():
    if setting.stage != 0:
        setting.screen.blit(setting.background, (0, 0))

    if setting.stage == 0:
        menu.render()
        #pygame.display.update()
    elif setting.stage == 1:
        story.render()
        #pygame.display.update()
    elif setting.stage == 2:
        meeting.render()
    
    pygame.time.Clock().tick(setting.FPS)
    pygame.display.update()


# 파이게임 초기화
pygame.init()
# 게임 전체 루프
loop()
# 파이게임 종료
pygame.quit()