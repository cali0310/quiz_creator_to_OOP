import os
import json
from colorama import Fore, Style

class QuizDataManager:
    def __init__(self, file_name="quiz_questions.txt"):
        self.file_name = file_name

    def load_questions(self):
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return []
        except Exception as error:
            print(Fore.RED + f"Error loading quiz questions: {error}" + Style.RESET_ALL)
            return []

    def save_questions(self, questions_list):
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(questions_list, file, indent=4)
            return True
        except Exception as error:
            print(Fore.RED + f"Error saving quiz questions: {error}" + Style.RESET_ALL)
            return False

    def reset_questions(self):
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4)
            print(Fore.GREEN + "\n✅ Questions have been reset!" + Style.RESET_ALL)
            return True
        except Exception as error:
            print(Fore.RED + f"Error resetting questions: {error}" + Style.RESET_ALL)
            return False
