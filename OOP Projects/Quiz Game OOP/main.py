from data import question_data
from quiz_brain import Question

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_q = Question(question_text,question_answer)
    question_bank.append(new_q)

print(question_bank[0].text)
print(question_bank[0].answer)