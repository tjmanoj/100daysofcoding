class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_no = self.question_number
        choice = input(f"Q.{q_no + 1}:{self.question_list[q_no].text} (True/False)?:")
        self.check_answer(choice, self.question_list[q_no].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You're correct")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Correct answer is: {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number + 1}")
