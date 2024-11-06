import customtkinter as ctk

class ProgrammingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        # self.grid(row=0, column=0, sticky="ewns")

    def create_widgets(self, parent):
        # create the grid
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)

        # create widgets 
        # for 1 training day per week
        advice_d1 = ctk.CTkLabel(self, text="Pick max 7 exercises from dropdown menu below. Number of exercises is not random. You can pick less - and adjust later - but more wont give you better gains. One thing for sure: you will spent more than two hours in the gym meanwhile much of your sets will be counterproductive.", fg_color="black", text_color="white", font=("Helvatica", 18))

        d1_lbl = ctk.CTkLabel(self, text="Day 1",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 27))
           
        exercise_1 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        sets_1 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])

        d2_lbl = ctk.CTkLabel(self, text="Day 2")
        d3_lbl = ctk.CTkLabel(self, text="Day 3")
        d4_lbl = ctk.CTkLabel(self, text="Day 4")
        d5_lbl = ctk.CTkLabel(self, text="Day 5")
        d6_lbl = ctk.CTkLabel(self, text="Day 6")
        d7_lbl = ctk.CTkLabel(self, text="Day 7")

        # place widgets
        # for 1 day
        advice_d1.grid(row=0, column=0, columnspan=2)
        d1_lbl.grid(row=1, column=0, columnspan=2)
        exercise_1.grid(row=2, column=0)
        sets_1.grid(row=2, column=1)