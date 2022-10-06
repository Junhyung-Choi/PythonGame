import time
import setting

class Script():
    """
    자막과 관련한 것을 다루는 객체
    """
    
    def __init__(self, text):
        self.is_first_script = True
        self.is_finished = False
        self.start_time = 0
        self.current_time = 0
        self.delay = 0.1
        self.text_index = 0
        self.text = text
        self.render_text = ""
        self.color = [0, 0, 0]
        self.timer = 0

    def show_all_script(self, x, y):
        myText = setting.myFont.render(self.text, True, self.color)
        setting.screen.blit(myText, (x, y))

    def show_script(self, x, y):
        myText = setting.myFont.render(self.render_text, True, self.color)
        if self.is_first_script:
            self.is_first_script = False
            self.start_time = time.time()

        self.current_time = time.time()
        if len(self.text) + 20 < self.text_index:
            self.is_finished = True
            return

        elif self.current_time >= self.start_time + self.delay:
            self.start_time = self.current_time
            # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
            
            setting.screen.blit(myText, (x, y)) #(글자변수, 위치)
            
            if self.text_index < len(self.text):
                self.render_text += self.text[self.text_index]
            self.text_index += 1
        else:
            setting.screen.blit(myText, (x, y))