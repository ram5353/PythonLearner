from data import question_data
from question_model import Question
import quiz_brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

question = quiz_brain.QuizBrain(question_bank)
while question.still_has_questions():
    question.next_question()

print("you have completed the quiz")
print(f"Your final score is {question.score}/{len(question_bank)}")




