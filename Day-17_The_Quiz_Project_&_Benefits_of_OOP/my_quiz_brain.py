"""This Quiz Brain was written by me (mostly). Check quiz_brain.py for Angela's code"""


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.current_question = ""
        self.current_answer = ""

    def choose_questions(self, que_no):
        self.current_question = self.questions_list[que_no].text
        self.question_number += 1
        return self.current_question

    def check_answer(self, que_no, user_choice):
        self.current_answer = self.questions_list[que_no].answer
        if user_choice == self.current_answer:
            return 1
        else:
            return 0

# TODO 1: asking the questions
# TODO 2: checking if the answer is correct
# TODO 3: checking if we are at the end of quiz
