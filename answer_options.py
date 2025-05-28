import tkinter as tk

class AnswerOptions(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F5ECD5")
        self.selected_option = tk.StringVar()
        self.option_buttons = {}

        for option_letter in ['a', 'b', 'c', 'd']:
            radio_button = tk.Radiobutton(
                self,
                text="",
                variable=self.selected_option,
                value=option_letter,
                font=("Helvetica", 12),
                bg="#F5ECD5",
                anchor="w",
                justify="left",
                wraplength=450
            )
            radio_button.pack(anchor="w", pady=2)
            self.option_buttons[option_letter] = radio_button

    def update_choices(self, choices):
        for opt in ['a', 'b', 'c', 'd']:
            self.option_buttons[opt].config(text=f"{opt.upper()}. {choices[opt]}")

    def get_selected(self):
        return self.selected_option.get()

    def clear_selection(self):
        self.selected_option.set("")