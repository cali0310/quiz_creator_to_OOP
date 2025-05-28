import time
from colorama import Fore

class Animator:
    @staticmethod
    def loading_animation(message, duration=1.5):
        animation_chars = "|/-\\"
        total_steps = int(duration * 10)
        for step_index in range(total_steps):
            current_char = animation_chars[step_index % len(animation_chars)]
            print(f"\r{Fore.YELLOW}{message} {current_char}", end="", flush=True)
            time.sleep(0.05)
        print()