from doctest import script_from_examples
import time
from turtle import delay
import setting

class Script():
    is_first_script = True
    start_time = 0
    current_time = 0
    delay = 0.1
    text_index = 0
    render_text = ""

    @staticmethod
    def init():
        Script.is_first_script = True
        Script.start_time = 0
        Script.current_time = 0
        Script.delay = 0.1
        Script.text_index = 0
        Script.render_text = ""

    @staticmethod
    def show_script(text):
        myText = setting.myFont.render(Script.render_text, True, (0, 0, 0))
        if Script.is_first_script:
            Script.is_first_script = False
            Script.start_time = time.time()

        Script.current_time = time.time()
        if len(text) + 20 < Script.text_index:
            return

        elif Script.current_time >= Script.start_time + Script.delay:
            Script.start_time = Script.current_time
            # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
            
            setting.screen.blit(myText, (30,30)) #(글자변수, 위치)
            # print("작동중")
            
            if Script.text_index < len(text):
                Script.render_text += text[Script.text_index]
            Script.text_index += 1
        else:
            setting.screen.blit(myText, (30,30))