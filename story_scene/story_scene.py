import pygame
import time


def scene():
    LEFT = 1
    RIGHT = 3
    # 아직 씬이 나오지 않았으므로, 임시 씬 이미지
    story_img = pygame.image.load("img/background.png")
    skip_img = pygame.image.load("img/skip.png")

    story_img_x_pos = 0
    story_img_y_pos = 0
    skip_x_pos_start = 0
    skip_y_pos_start = 0
    skip_x_pos_end = 0
    skip_y_pos_end = 0

    running = True
    while running:

        # 스킵 버튼의 위치
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            screen.blit(story_img, (story_img_x_pos, story_img_y_pos))
            screen.blit(skip_img, (skip_x_pos_start, skip_y_pos_start))
            
            # 마우스 버튼이 스킵 버튼을 눌렸을 때
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if(skip_x_pos_start, skip_y_pos_start) <= (event.pos[0], event.pos[1]) <= (skip_x_pos_end, skip_y_pos_end):
                    print("스킵합니다.")

        pygame.display.update()
    return