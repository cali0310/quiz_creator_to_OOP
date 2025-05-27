import tkinter as tk
from question_loader import QuestionLoader
from quiz_interface import QuizInterface
from tkinter import messagebox

def main():
    root = tk.Tk()
    question_loader = QuestionLoader("quiz_questions.json")
    questions = question_loader.load()

    if not questions:
        messagebox.showerror("No Questions Found", "No questions available in 'quiz_questions.json'")
        root.destroy()
        return

    app = QuizInterface(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()