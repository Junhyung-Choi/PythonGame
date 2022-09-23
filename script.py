import time
import pygame
 
pygame.init()
 
screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("text")
 
# 글자체(text font) 지정하기
text_size = 50
font_name = None
myFont = pygame.font.SysFont(font_name, text_size) #(글자체, 글자크기) None=기본글자체

text = "Hello World"
render_text = ""
index = 0

first = True
delay = 1

# 변수
x_pos = 0
y_pos = 0
 
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    screen.fill((255,255,0)) # 배경 노란색

    if first:
        first = False
        start_t = time.time()
    
    currnet_t = time.time()
    if len(text) <= index:
        play = False
    elif currnet_t >= start_t + delay:
        # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
        myText = myFont.render(render_text, True, (0,0,255)) #(Text,anti-alias, color)
        screen.blit(myText, (100,100)) #(글자변수, 위치)
        render_text += text[index]
        start_t = currnet_t
        index += 1
        pygame.display.update()
 
 
pygame.quit()