import random

class GameStatus:
    def __init__(self, scene_name):
        self.scene_name = scene_name
        self.point = 0
        self.questions = self.__make_questions__()
    
    def __make_questions__(self):
        questions = []
        
        ## 질문 리스트 추가하는 과정
        for _ in range(10):
            questions.append(Question("New Question_" + str(_)))

        return questions
    
class Question:
    def __init__(self, sentence):
        self.sentence = sentence
        self.answer = self.__make_random_answer__()
    
    def __make_random_answer__(self):
        answer_point_list = []
        for _ in range(4):
            answer_point_list.append(random.randint(-3,3))
        return answer_point_list


if __name__ == "__main__":
    q = Question("New Question")
    print(q.answer)
    print(q.sentence)

    gs = GameStatus("New Scene")
    print(gs.scene_name)
    print(gs.point)
    for q in gs.questions:
        print(q.answer)