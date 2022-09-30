import time
import setting

def show_script():
    myText = setting.myFont.render(setting.render_text, True, (0,0,255)) #(Text,anti-alias, color)
    if setting.first_script:
        setting.first_script = False
        print("처음 작동중")
        setting.script_start_t = time.time()

    setting.script_currnet_t = time.time()
    if len(setting.text) - 1 < setting.text_index:
        print("출력 종료")
        return

    elif setting.script_currnet_t >= setting.script_start_t + setting.delay:
        setting.script_start_t = setting.script_currnet_t
        # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
        
        setting.screen.blit(myText, (100,100)) #(글자변수, 위치)
        print("작동중")
        if setting.text_index == len(setting.text) - 1:
            setting.text_index += 1
        else:
            setting.render_text += setting.text[setting.text_index]
            setting.text_index += 1
    else:
        setting.screen.blit(myText, (100,100))
