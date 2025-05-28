import os
from colorama import Fore, Style

class Screen:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_header():
        Screen.clear()
        print(Fore.CYAN + Style.BRIGHT + "\n" + "\U0001F3AF  QUIZ CREATOR 🎯" + Style.RESET_ALL)