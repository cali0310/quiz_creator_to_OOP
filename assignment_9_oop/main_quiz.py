from colorama import init
from quiz_app import QuizApp

init(autoreset=True)

if __name__ == "__main__":
    try:
        app = QuizApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
