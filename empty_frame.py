import customtkinter as ctk
from choice_frame import ChoiceFrame
from data.sqlite import SQLHandler

# setup frame: left side for comboboxes with exercises and sets selectors, right for muscles frames
class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="yellow")
        self.grid_columnconfigure((0,1,2), weight=1)

        self.sql_handler = SQLHandler()
        self.muscle_multiplier = {}
        self.sets = None

    def create_widgets(self, parent):
        muscles = self.sql_handler.read_all_muscles()

        for i in range(len(muscles)):
            muscle = ctk.CTkLabel(master=self, text_color="red")
            muscle.grid(column=1, row=i, sticky="news")
            muscle.configure(text=muscles[i])
            sets = ctk.CTkLabel(master=self, text_color="red")
            sets.grid(column=2, row=i, sticky="news")
            sets.configure(text="0")

        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0, row=0)
        programming_side.create_widgets(self)
        