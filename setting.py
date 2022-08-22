from lib2to3.pygram import python_grammar
import pygame

# 스크린 사이즈 설정
screen_width = 800
screen_height = 600
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
    eyes[idx] = pygame.transform.scale(eyes[idx],(800,600))

eyeBall = pygame.image.load("img/eyeBall.png")
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