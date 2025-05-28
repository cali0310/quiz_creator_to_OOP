class QuizController:
    #Handles quiz flow, question tracking, and score
    def __init__(self, questions):#Initialize with list of questions
        self.questions = questions
        self.current_index = 0
        self.score = 0

    def get_current_question(self): #Return current question
        return self.questions[self.current_index]

    def get_correct_answer(self): #Return correct answer key (a/b/c/d)
        return self.questions[self.current_index]['correct_answer']

    def get_correct_answer_text(self): #Return text of correct answer
        correct_key = self.get_correct_answer()
        return self.questions[self.current_index]['choices'][correct_key]

    def increment_score(self):
        self.score += 1

    def next_question(self):
        self.current_index += 1

    def is_finished(self):
        return self.current_index >= len(self.questions)

