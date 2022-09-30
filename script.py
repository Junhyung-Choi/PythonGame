
import time
import pygame
import setting

def show_script():
    while setting.play:
        if setting.first_script:
            setting.first_script = False
            print("처음 작동중")
            start_t = time.time()
        
        currnet_t = time.time()
        if len(setting.text) - 1 < setting.text_index:
            setting.play = False
            print("마지막 작동 중")
        elif currnet_t >= start_t + setting.delay:
            # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
            myText = setting.myFont.render(setting.render_text, True, (0,0,255)) #(Text,anti-alias, color)
            setting.screen.blit(myText, (100,100)) #(글자변수, 위치)
            print("작동중")
            if setting.text_index == len(setting.text) - 1:
                setting.text_index += 1
                pass
            else:
                setting.render_text += setting.text[setting.text_index]
                start_t = currnet_t
                setting.text_index += 1
    return
