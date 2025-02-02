import customtkinter as ctk
from data.sqlite import SQLHandler

# List of muscles should be trained. Once added to the right muscle should disapeare.
class MuscleLeftFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1,2), weight=1)

        self.sql_handler = SQLHandler()
        self.muscles = self.sql_handler.read_all_muscles()

    def create_widgets(self):
        for i in self.muscles:
            muscle = ctk.CTkLabel(master=self, text_color="yellow", font=("Helvatica", 18), text=i)
            muscle.grid(column=1, sticky="NSEW")