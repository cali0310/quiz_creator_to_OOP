import tkinter as tk

class QuestionDisplay(tk.Label):
    def __init__(self, master):
        super().__init__(
            master,
            text="",
            font=("Helvetica", 14),
            bg="#F5ECD5",
            wraplength=450
        )

    def update_text(self, text):
        self.config(text=text)