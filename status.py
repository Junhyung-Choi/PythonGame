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

class QuestionBundle:
    def __init__(self, parent, child=None, questions):
        self.parent = parent
        self.child = child
        self.questions = questions

class Question:
    def __init__(self, sentence, child=None, bundle):
        self.sentence = sentence
        self.score = random.randint(-3, 3)
        self.child = child
        self.bundle = bundle

    def select(self):
        gs = self.child        


if __name__ == "__main__":
    q = Question("New Question")
    print(q.answer)
    print(q.sentence)

    gs = GameStatus("New Scene")
    print(gs.scene_name)
    print(gs.point)
    for q in gs.questions:
        print(q.answer)