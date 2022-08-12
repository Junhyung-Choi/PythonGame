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

# 파이게임 
pygame.init()

# 게임 전체 루프
while setting.running:
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


        ####################################################

        # 스테이지별 이벤트
        if setting.stage == 0: # 시작 화면일때
            menu.process_event(event=event)

        elif setting.stage == 1: # 첫 번째 stage 이벤트
            story.process_event(event=event)

        elif setting.stage == 2: # 두 번째 stage 이벤트
            meeting.process_event(event=event)

        ####################################################

    # 각 스테이지별 따로 설졍해줘야 하는 요소들
    if setting.stage == 0:
        menu.render()
    elif setting.stage == 1:
        story.render()
    elif setting.stage == 2:
        meeting.render()

    if setting.stage != 0:
        setting.screen.blit(setting.background, (0, 0))
        setting.screen.blit(setting.character, (setting.character_x_pos, setting.character_y_pos)) #배경에 캐릭터 그려주기

    pygame.display.update()

pygame.quit()