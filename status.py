import random
import json

class GameStatus:
    def __init__(self, scene_name):
        self.scene_name = scene_name
        self.mode = 1
        self.left_time = 1
        self.current_questions = []
        self.current_question = []
        self.__root_question__ = self.__make_questions__()
        self.point = 0
    
    def __make_questions__(self):
        with open('./data.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
    
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