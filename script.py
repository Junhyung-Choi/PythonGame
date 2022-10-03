import time
import setting

def show_script(text):
    myText = setting.myFont.render(setting.render_text, True, (0, 0, 0))
    if setting.first_script:
        setting.first_script = False
        # print("처음 작동중")
        setting.script_start_t = time.time()

    setting.script_currnet_t = time.time()
    if len(text) + 20 < setting.text_index:
        # setting.screen.blit(myText, (100,100))
        # print("출력 종료")
        return

    elif setting.script_currnet_t >= setting.script_start_t + setting.delay:
        setting.script_start_t = setting.script_currnet_t
        # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
        
        setting.screen.blit(myText, (30,30)) #(글자변수, 위치)
        # print("작동중")
        
        if setting.text_index < len(text):
            setting.render_text += text[setting.text_index]
        setting.text_index += 1
    else:
        setting.screen.blit(myText, (30,30))

