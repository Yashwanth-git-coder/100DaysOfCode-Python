from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_questions = Questions(question_text, question_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)

while quiz.is_still_as_question():
    quiz.next_question()

print("You are completed the Quiz ! Thank You")
print(f"Your final Score is : {quiz.score}/{quiz.question_number }")