class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, question_no, question_list) -> None:
        self.question_no = 0
        self.question_list = question_list

    def next_question(self):
        text = self.question_list[self.question_no]
        input(f"Q.{self.question_no}: {text.text}. True or False? ")