import tkinter as tk

class AnswerOptions(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F5ECD5")
        self.selected_option = tk.StringVar()
        self.option_buttons = {}

        for opt in ['a', 'b', 'c', 'd']:
            rb = tk.Radiobutton(
                self,
                text="",
                variable=self.selected_option,
                value=opt,
                font=("Helvetica", 12),
                bg="#F5ECD5",
                anchor="w",
                justify="left",
                wraplength=450
            )
            rb.pack(anchor="w", pady=2)
            self.option_buttons[opt] = rb

    def update_choices(self, choices):
        for opt in ['a', 'b', 'c', 'd']:
            self.option_buttons[opt].config(text=f"{opt.upper()}. {choices[opt]}")

    def get_selected(self):
        return self.selected_option.get()

    def clear_selection(self):
        self.selected_option.set("")