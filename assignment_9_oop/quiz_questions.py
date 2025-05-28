class QuizQuestion:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer.lower()

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "correct_answer": self.correct_answer
        }
