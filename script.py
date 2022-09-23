import pygame
import setting
import time

def draw_script():
    text_color = (255, 255, 255)

    font = pygame.font.SysFont("font/DungGeunMo.ttf", 30, True, True)

    text = font.render("Hello world", True, text_color)

    setting.screen.blit(text, (100, 500))

    print("텍스트 출력 중")

    time.sleep(3)

    return 0

