from question_model import Question
from data import question_data
from my_quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    new_question = Question(item['text'], item['answer'])
    question_bank.append(new_question)

# print(question_bank[11].text)

score = 0
question_index = 0
new_que = QuizBrain(question_bank)
quiz_on = True
while quiz_on:
    print(f"\nQuestion {question_index + 1}/12")
    print(new_que.choose_questions(question_index))
    user_ans = input("Enter True or False: ")
    if new_que.check_answer(question_index, user_ans) == 1:
        score += 1
        print(f"Score: {score}")
    else:
        print(f"Wrong answer!\nScore: {score}")
    question_index += 1
    if question_index == 12:
        print(f"\nQuiz Complete! Final Score: {score}")
        quiz_on = False
