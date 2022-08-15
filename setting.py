from lib2to3.pygram import python_grammar
import pygame

# 스크린 사이즈 설정
screen_width = 1600
screen_height = 1200
screen = pygame.display.set_mode((screen_width, screen_height))

# 현재 씬 
running = True
stage = 0

# 윈도우 설정
pygame.display.set_caption("Python Game")

# 이미지 에셋 업로드
start_background = pygame.image.load("img/start.png")
background = pygame.image.load("img/background.png")

eyes = []
for idx in range(36):
    eyes.append(pygame.image.load("img/eye_" + str(idx) + ".png"))
eyeBall = pygame.image.load("img/eyeBall.png")

main_table = pygame.image.load("img/Main_Table.png")
main_table = pygame.transform.scale(main_table,(1681,312))

main_title = pygame.image.load("img/Main_Title.png")
main_title = pygame.transform.scale(main_title,(1249,404))


main_background = pygame.image.load("img/MainBG.png")


menu_button_click = pygame.image.load("img/Button_click.png")
menu_button_click = pygame.transform.scale(menu_button_click,(136,118))


menu_button = pygame.image.load("img/Button_normal.png")
menu_button = pygame.transform.scale(menu_button,(136,118))