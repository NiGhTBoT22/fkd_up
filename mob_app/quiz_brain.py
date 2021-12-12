
class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        length = len(self.question_list)
        if length > self.question_number:
            return True
        else:
            return False
    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"q{self.question_number}:{item.question} ")
        self.check_answer(answer,item.answer)

    def check_answer(self,user_input,solution):
        if user_input.lower() == solution.lower():
            self.score += 1
            print("correct")
        else:
            print("wrong")

        print(f"your score is {self.score}/{self.question_number}")
        
    