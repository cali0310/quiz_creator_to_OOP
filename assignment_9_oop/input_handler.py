from colorama import Fore, Style

class InputHandler:
    @staticmethod
    def get_input(prompt, color=Fore.GREEN):
        return input(f"{color}{prompt}{Style.RESET_ALL}")