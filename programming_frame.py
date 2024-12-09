import customtkinter as ctk
from choice_frame_ex import ChoiceFrame

class ProgrammingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        # root = self.winfo_toplevel()

    # create widgets
    def create_widgets(self):
        day_lbl = ctk.CTkLabel(master=self,
                              fg_color="black",
                              text_color="white")
        ex_lbl = ctk.CTkLabel(master=self, text="Exercise",
                              fg_color="black",
                              text_color="white")
        st_lbl = ctk.CTkLabel(master=self, text="Sets",
                              fg_color="black",
                              text_color="white")
        
        # frame with choices
        choice_frame = ChoiceFrame(self)
        choice_frame.create_widgets()

        # place widgets
        day_lbl.grid(column=0, row=0, columnspan=2, sticky="news")
        ex_lbl.grid(column=0, row=1, sticky="news") 
        st_lbl.grid(column=1, row=1, sticky="news")
        choice_frame.grid(column=0, row=2, columnspan=2, sticky="news")

# left side of setup
class ProgrammingFrames(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

    def create_widgets(self, parent):
        day_frame1 = ProgrammingFrame(self)
        # day_frame2 = ProgrammingFrame(self)
        # day_frame3 = ProgrammingFrame(self)
        # day_frame4 = ProgrammingFrame(self)
        # day_frame5 = ProgrammingFrame(self)
        # day_frame6 = ProgrammingFrame(self)
        day_frame1.grid(row=0, column=0, sticky="news")
        # day_frame2.grid(row=0, column=1, sticky="news")
        # day_frame3.grid(row=1, column=0, sticky="news")
        # day_frame4.grid(row=1, column=1, sticky="news")
        # day_frame5.grid(row=2, column=0, sticky="news")
        # day_frame6.grid(row=2, column=1, sticky="news")
        day_frame1.create_widgets()
        # day_frame2.create_widgets()
        # day_frame3.create_widgets()
        # day_frame4.create_widgets()
        # day_frame5.create_widgets()
        # day_frame6.create_widgets()