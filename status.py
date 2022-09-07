import random
import json

class GameStatus:
    def __init__(self, scene_name):
        self.scene_name = scene_name
        self.mode = 1
        self.left_time = 1
        self.current_questions = []
        self.current_question = []
        self.__root_question_chapter1__ = self.__make_questions__(1)
        self.__root_question_chapter2__ = self.__make_questions__(2)
    
    def __make_questions__(self, index):
        with open('./data.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        root_question = Question("root")
        if(index == 1):
            for first in json_data["혹시 취미가"]:
                for fq in first.keys():
                    first_question = Question(fq)
                    for second_dict in first.values():
                        for key,val in second_dict:
                            second_question = Question(key)
                            first_question.child_questions.append(second_question)
                            print(sq)
                    root_question.child_questions.append(first_question)
        elif(index == 2):
            pass
            
    
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
    def __init__(self, sentence):
        self.point = 0
        self.sentence = sentence
        self.index = 0
        self.child_questions = []


if __name__ == "__main__":
    gs = GameStatus("meeting")

