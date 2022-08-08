import pygame
import menu
from setting import *
pygame.init()

def stage1_rendering():
    print("최초 1회만 렌더링 되는 요소들")


# 이벤트 루프 변수
running = True
stage = 0
is_rendered = False

# 게임 전체 루프
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        # 모든 스테이지에서 공통적으로 사용되는 이벤트
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
            # 개발자 테스트용 스테이지 이동 키
            if event.key == pygame.K_MINUS: 
                stage -= 1
                print("현재 스테이지 : " + str(stage))
                is_rendered = False
            if event.key == pygame.K_EQUALS:
                stage += 1
                print("현재 스테이지 : " + str(stage))
                is_rendered = False

        ####################################################


        # 스테이지별 이벤트
        if stage == 0: # 시작 화면일때
            menu.event_process(event= event)

        elif stage == 1: # 첫 번째 stage 이벤트
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("stage1 에서 1번키 눌림")
                if event.key == pygame.K_2:
                    print("stage1 에서 2번키 눌림")

        elif stage == 2: # 두 번째 stage 이벤트
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("stage2 에서 1번키 눌림")
                if event.key == pygame.K_2:
                    print("stage2 에서 2번키 눌림")

        ####################################################

    # 각 스테이지별 따로 설졍해줘야 하는 요소들
    if stage == 0:
        #screen.blit(start_background, (0, 0))
        menu.render()
    elif stage == 1:
        if not(is_rendered):
            stage1_rendering()
            is_rendered = True
        pass
        # if 스테이지 클리어 조건 == True:
        #   stage = 2
        #   is_rendered = False
    elif stage == 2:
        pass

    if stage != 0:
        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos)) #배경에 캐릭터 그려주기


    pygame.display.update()

pygame.quit()