import random

class GameStatus:
    def __init__(self, scene_name):
        self.scene_name = scene_name
        self.mode = 1
        self.left_time = 1
        self.current_questions = []
        self.current_question = []
        self.__root_question__ = []
        self.point = 0
        self.questions = self.__make_questions__()
    
    def __make_questions__(self):
        questions = []
        
        ## 질문 리스트 추가하는 과정
        for _ in range(10):
            questions.append(Question("New Question_" + str(_)))

        return questions
    
    def etc_button_clicked(self, button_type):
        if(button_type == "pause"):
            pass
        elif (button_type == "time"):
            pass
        elif (button_type == "goback"):
            pass
    
    def speech_button_clicked(self, index):
        if(index == 1):
            pass
        elif (index == 2):
            pass
        elif (index == 3):
            pass
        elif (index == 4):
            pass

class Question:
    def __init__(self):
        self.point = 0
        self.sentence = "Question Sentence"
        self.index = 0
        self.child_questions = []


if __name__ == "__main__":
    print("status.py called")