class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_no = 0
        self.question_list = question_list

    def still_has_question(self):
        return len(self.question_list) > self.question_no

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.question} (True/False):: ")
        self.check_answer(user_answer, current_question.answer, self.question_no)

    def check_answer(self, user_answer, correct_answer, question_no):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{question_no}.")
        print()
