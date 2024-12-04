import customtkinter as ctk

# right side of setup
class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="red")
        self.grid_columnconfigure((0), weight=2)
        self.grid_columnconfigure((1), weight=1)
        self.sql_handler = parent.sql_handler

    def create_widgets(self):
        muscles = self.sql_handler.read_all_muscles()
        for i in range(len(muscles)):
            muscle = ctk.CTkLabel(master=self, text_color="white")
            muscle.grid(column=0, row=i, sticky="news")
            muscle.configure(text=muscles[i])
            sets = ctk.CTkLabel(master=self, text_color="white")
            sets.grid(column=1, row=i, sticky="news")
            sets.configure(text="0")

