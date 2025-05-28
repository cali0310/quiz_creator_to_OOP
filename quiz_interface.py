from quiz_window import QuizWindow
from quiz_controller import QuizController
from quiz_display import QuestionDisplay
from answer_options import AnswerOptions
from feedback_display import FeedbackDisplay
from score_display import ScoreDisplay
from submit_button import SubmitButton
from exit_button import ExitButton

class QuizInterface:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.quiz_controller = QuizController(questions)

        self.quiz_window = QuizWindow(master)
        self.question_display = QuestionDisplay(self.quiz_window.frame)
        self.answer_options = AnswerOptions(self.quiz_window.frame)
        self.feedback_display = FeedbackDisplay(self.quiz_window.frame)
        self.score_display = ScoreDisplay(self.quiz_window.frame)
        self.submit_button = SubmitButton(self.quiz_window.frame, self._on_submit)
        self.exit_button = ExitButton(self.quiz_window.frame, self._on_exit)

        self._setup_layout()
        self._display_question()

    def _setup_layout(self):
        self.quiz_window.pack_widgets([
            self.question_display,
            self.answer_options,
            self.feedback_display,
            self.score_display,
            self.submit_button,
            self.exit_button
        ])

    def _display_question(self):
        if self.quiz_controller.is_finished():
            self._end_quiz()
            return
        question = self.quiz_controller.get_current_question()
        self.question_display.update_text(f"Q{self.quiz_controller.current_index + 1}: {question['question']}")
        self.answer_options.update_choices(question['choices'])
        self.answer_options.clear_selection()
        self.feedback_display.clear()
        self.submit_button.enable()
        self.score_display.update_score(self.quiz_controller.score)

    def _on_submit(self):
        selected = self.answer_options.get_selected()
        if not selected:
            from tkinter import messagebox
            messagebox.showwarning("No Selection", "Please choose an answer to proceed.")
            return

        correct_answer = self.quiz_controller.get_correct_answer()
        correct_answer_text = self.quiz_controller.get_correct_answer_text()

        if selected == correct_answer:
            self.quiz_controller.increment_score()
            self.feedback_display.show_feedback("Correct!", "green")
        else:
            self.feedback_display.show_feedback(
                f"The correct answer is: {correct_answer.upper()}. {correct_answer_text}", "red"
            )

        self.score_display.update_score(self.quiz_controller.score)
        self.submit_button.disable()
        self.master.after(1000, self._next_question)

    def _next_question(self):
        self.quiz_controller.next_question()
        self._display_question()

    def _end_quiz(self):
        from tkinter import messagebox
        total = len(self.questions)
        messagebox.showinfo("Quiz Completed", f"You scored {self.quiz_controller.score} out of {total}.")
        self.master.quit()

    def _on_exit(self):
        from tkinter import messagebox
        if messagebox.askyesno("Exit Quiz", "Are you sure you want to exit? Your progress will be lost."):
            self.master.quit()
