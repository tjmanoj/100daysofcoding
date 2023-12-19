from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

ques = QuizBrain(question_bank)

while ques.still_has_questions():
    ques.next_question()

print("You've completed the quizz!!")
print(f"Your final score is: {ques.score}/{len(question_bank)}")
