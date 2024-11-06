import customtkinter as ctk

class ProgrammingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid(row=0, column=0, sticky="ewns")

    def create_widgets_d1(self):
        # create the grid
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)

        # create widgets

        d1_lbl = ctk.CTkLabel(self, text="Day 1")
        d2_lbl = ctk.CTkLabel(self, text="Day 2")
        d3_lbl = ctk.CTkLabel(self, text="Day 3")
        d4_lbl = ctk.CTkLabel(self, text="Day 4")
        d5_lbl = ctk.CTkLabel(self, text="Day 5")
        d6_lbl = ctk.CTkLabel(self, text="Day 6")
        d7_lbl = ctk.CTkLabel(self, text="Day 7")