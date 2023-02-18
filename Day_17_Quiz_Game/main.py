from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
quiz = QuizBrain(question_bank)

for x in range(0, len(question_data)):
    quiz.next_question()
    if quiz.still_nas_questions():
        print("\n")
    else:
        print("\n")
        print("You've completed the quiz.")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")
