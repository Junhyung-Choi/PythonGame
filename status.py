import json
from random import randint

MODE_CHOICE = 0
MODE_CHECK = 1

class GameStatus:
    def __init__(self, scene_name, button1, button2, button3, button4):
        self.score = 0
        self.scene_name = scene_name
        self.mode = MODE_CHOICE
        self.left_time = 1
        self.__root_question_chapter1__ = self.__make_questions__(1)
        self.__root_question_chapter2__ = self.__make_questions__(2)
        self.current_question : Question = self.__root_question_chapter1__
        self.current_questions = self.current_question.child_questions
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.button4 = button4
        self.button1.text = self.current_questions[0].sentence
        self.button2.text = self.current_questions[1].sentence
        self.button3.text = self.current_questions[2].sentence
        self.button4.text = self.current_questions[3].sentence
    
    def __str__(self):
        return (self.scene_name + "'s Game Status Instance")

    def __make_questions__(self, index):
        with open('./data.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        root_question = Question("root",0,0)
        if(index == 1):
            fcnt = 0
            for first in json_data["혹시 취미가"]:
                for fk,fv in first.items():
                    print("First Question Making: " + fk + " && index : " + str(fcnt))
                    first_question = Question(fk,randint(-3,3),fcnt)
                    fcnt += 1

                    scnt = 0
                    for second in fv:
                        for sk,sv in second.items():
                            second_question = Question(sk,randint(-3,3),scnt)
                            scnt += 1

                            tcnt = 0
                            for third in sv:
                                third_question = Question(third,randint(-3,3),tcnt)
                                tcnt += 1

                                second_question.child_questions.append(third_question)
                            first_question.child_questions.append(second_question)
                    root_question.child_questions.append(first_question)
        elif(index == 2):
            pass
        return root_question
            
    
    def etc_button_clicked(self, button_type):
        if(button_type == "pause"):
            pass
        elif (button_type == "time"):
            pass
        elif (button_type == "goback"):
            pass
    
    # 각 버튼마다 동작을 다르게 해줘야함 (1,2,3,4)
    # 각 상황마다 동작을 다르게 해줘야함 (MODE_CHOICE, MODE_CHECK)
    def speech_button_clicked(self, index: int):
        sen = ""

        if(self.mode == MODE_CHECK):
            sen += "MODE_CHECK"
        else:
            sen += "MODE_CHOICE"
        
        print("Clicked: " + sen +  " / Q: " + self.current_question.sentence)
        # MODE_CHOICE : 4개중에 선택하는 단계
        if self.mode == MODE_CHOICE:
            self.current_question = self.current_questions[index]
            # 자식 질문이 있을때
            self.mode = MODE_CHECK
            
            # 현재 질문분야를 갱신하고, 텍스트 또한 갱신
            self.button1.text = "짧게 던지기"
            self.button2.text = "깊게 들어가기"
            self.button3.text = "다른 질문 고르기"
            self.button4.text = ""

        # MODE_CHECK : 3개(자신, 자식, 형재자매) 중에 선택하는 단계
        elif self.mode == MODE_CHECK:

            # 현재 질문 포인트에 대한 동작 애니메이션 재생시키기 
            if(index == 0):
                print("Play Current Animation: " + self.current_question.sentence)
                print("Score : " + str(self.current_question.point))
                print("Index: " + str(self.current_question.idx))
                # play_current_animation()
                pass
            elif (index == 1):
                if not (self.current_question.child_questions):
                    print("끝남")
                    return
               
                self.mode = MODE_CHOICE
                
                # 현재 질문을 확정하고, 그에 대한 포인틀르 얻고, 이에 대한 자식 질문들을 갱신함
                self.score += self.current_question.point
            
                self.current_questions = self.current_question.child_questions
                # 현재 질문에 대한 반응을 get 하고 그 다음 질문들을 만들어야 하므로 button들을 갱신
                self.button1.text = self.current_questions[0].sentence
                self.button2.text = self.current_questions[1].sentence
                self.button3.text = self.current_questions[2].sentence
                self.button4.text = self.current_questions[3].sentence

                pass

            # 현재 질문을 취소하고, 본인 부모로 올라가 다시 고르는것
            elif (index == 2):
                self.mode = MODE_CHOICE
                # 모드가 이미 바뀌었으므로 아무것도 하지 않아도 사용 가능함
                self.button1.text = self.current_questions[0].sentence
                self.button2.text = self.current_questions[1].sentence
                self.button3.text = self.current_questions[2].sentence
                self.button4.text = self.current_questions[3].sentence
                pass
            elif (index == 3):
                pass
        print("Current Score : " + str(self.score))
        print("--------\n\n")

class Question:
    def __init__(self, sentence, point, idx):
        self.point = point
        self.sentence = sentence
        self.idx = idx
        self.child_questions = []
    
    def __str__(self):
        return self.sentence


if __name__ == "__main__":
    # gs = GameStatus("meeting")
    # print(gs)
    # print(gs.__root_question_chapter1__.sentence)
    # for q in gs.__root_question_chapter1__.child_questions:
    #     print(q)
    #     print("child---------------")
    #     for i in q.child_questions:
    #         print(i)
    pass

