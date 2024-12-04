import customtkinter as ctk
from programming_frame import ProgrammingFrames
from muscle_frame import MuscleFrame

# setup frame: left side for comboboxes with exercises and sets selectors, right for muscles frames
class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="yellow")
        self.grid_columnconfigure((0), weight=2)
        self.grid_columnconfigure((1), weight=1)
        root = self.winfo_toplevel()
        print(type(root))

        self.sql_handler = parent.sql_handler

    def create_widgets(self, parent):
        programming_side = ProgrammingFrames(self)
        programming_side.grid(column=0, row=0)
        programming_side.create_widgets(self)
        muscle_side = MuscleFrame(self)
        muscle_side.grid(column=1, row=0)
        muscle_side.create_widgets()
        