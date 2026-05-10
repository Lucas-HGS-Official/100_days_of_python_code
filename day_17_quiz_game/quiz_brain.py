class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.user_score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num].text
        self.question_num += 1
        user_answer = input(
            f"Q.{self.question_num} {current_question} (True/False): "
        ).lower()
        return user_answer

    def check_answer(self, user_answer):
        current_answer = self.question_list[self.question_num - 1].answer
        if user_answer == current_answer.lower():
            self.user_score += 1
            print("You are correct!!")
            print(f"your current score is: {self.user_score}/{self.question_num}")
        else:
            print("You are wrong!!")
            print(f"The correct answer was: {current_answer}")
            print(f"your current score is: {self.user_score}/{self.question_num}")
        print("")
