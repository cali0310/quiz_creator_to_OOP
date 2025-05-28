import tkinter as tk

class QuizWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("General Knowledge Quiz")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.bg_color = "#F5ECD5"
        self.master.configure(bg=self.bg_color)
        self.frame = tk.Frame(master, bg=self.bg_color)
        self.frame.pack(fill="both", expand=True)

    def pack_widgets(self, widgets):
        for widget in widgets:
            widget.pack(pady=5)