from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def func_main():
    if __name__ == "__main__":
        question_bank = []
        for question in question_data:
            question_bank.append(Question(question["text"], question["answer"]))

        quiz_brain = QuizBrain(question_bank)
        while quiz_brain.still_has_questions():
            quiz_brain.check_answer(quiz_brain.next_question())

        print("You've completed the quiz!!")
        print(f"Your final score was: {quiz_brain.user_score}/{len(question_bank)}")


func_main()
