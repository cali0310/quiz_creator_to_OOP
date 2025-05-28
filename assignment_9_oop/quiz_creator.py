import emoji
from colorama import Fore, Style
from screen import Screen
from animator import Animator
from input_handler import InputHandler
from quiz_question import QuizQuestion

class QuizCreator:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.questions = self.data_manager.load_questions()

    def create_question(self):
        Screen.display_header()
        print(Fore.GREEN + "\n" + emoji.emojize(":pencil:  CREATE NEW QUESTION") + Style.RESET_ALL)
        print(Fore.YELLOW + "═" * 50 + Style.RESET_ALL)

        question_text = InputHandler.get_input("\n" + emoji.emojize(":memo: Enter your question: "), Fore.CYAN)

        print(Fore.YELLOW + "\n--- Enter the four answer choices ---" + Style.RESET_ALL)
        choices = {}
        options = ['a', 'b', 'c', 'd']

        for opt in options:
            choices[opt] = InputHandler.get_input(f"Option {opt.upper()}: ")

        correct_answer = ''
        while True:
            correct_answer = InputHandler.get_input("\n" + "\u2705 Enter the correct answer (a/b/c/d): ", Fore.MAGENTA).lower()
            if correct_answer in options:
                break
            print(Fore.RED + "Invalid option! Please enter a, b, c, or d." + Style.RESET_ALL)

        return QuizQuestion(question_text, choices, correct_answer)

    def add_question(self):
        question = self.create_question()
        self.questions.append(question.to_dict())

        Animator.loading_animation("Saving question...")

        if self.data_manager.save_questions(self.questions):
            print(Fore.GREEN + "\n" + emoji.emojize(":check_mark_button: Question saved successfully!") + Style.RESET_ALL)
        else:
            print(Fore.RED + "\n" + emoji.emojize(":cross_mark: Failed to save question.") + Style.RESET_ALL)

    def reset_questions(self):
        if self.data_manager.reset_questions():
            self.questions.clear()
