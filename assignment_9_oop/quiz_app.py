import time
from colorama import Fore, Style
import emoji
from screen import Screen
from input_handler import InputHandler
from quiz_creator import QuizCreator
from quiz_data_manager import QuizDataManager

class QuizApp:
    def __init__(self):
        self.data_manager = QuizDataManager()
        self.creator = QuizCreator(self.data_manager)

    def run(self):
        while True:
            Screen.display_header()
            print(f"\n{Fore.CYAN}" + emoji.emojize(":bar_chart:") + f" Current question count: {Fore.WHITE}{len(self.creator.questions)}")
            print(Fore.YELLOW + "═" * 50 + Style.RESET_ALL)

            print(f"\n{Fore.GREEN}1.{Style.RESET_ALL} Add a new question")
            print(f"{Fore.RED}2.{Style.RESET_ALL} Reset questions")
            print(f"{Fore.RED}3.{Style.RESET_ALL} Exit")

            choice = InputHandler.get_input("\n" + emoji.emojize(":backhand_index_pointing_right: Choose an option (1-3): "))

            if choice == '1':
                self.creator.add_question()
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

            elif choice == '2':
                self.creator.reset_questions()
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

            elif choice == '3':
                Screen.display_header()
                print(Fore.CYAN + "\nThank you for using the Quiz Creator!")
                print(f"Your questions are saved in {self.data_manager.file_name}")
                print(Fore.YELLOW + "\n" + emoji.emojize("Exiting program... :right_arrow:") + Style.RESET_ALL)
                time.sleep(1.5)
                break

            else:
                print(Fore.RED + "\nInvalid choice! Please select 1, 2, or 3." + Style.RESET_ALL)
                time.sleep(1.5)
