import customtkinter as ctk

class ProgrammingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.grid_rowconfigure(2, weight=3)

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
        choice_frame_ex = ctk.CTkFrame(self, fg_color="black")
        choice_frame_ex.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        choice_frame_set = ctk.CTkFrame(self, fg_color="black")
        choice_frame_set.grid_rowconfigure((0,1,2,3,4,5), weight=1)

        # frame with answears 
        # answear_frame = ctk.CTkFrame(day_frame, fg_color="black")
        # answear_frame.pack(expand=True, fill="both")
        # muscle_groups_frame = ctk.CTkFrame(answear_frame, fg_color="black")
        # muscle_groups_frame.pack(side="left", expand=True, fill="both")
        # sets_total_frame = ctk.CTkFrame(answear_frame, fg_color="black")
        # sets_total_frame.pack(side="right", expand=True, fill="both")

        # place widgets
        day_lbl.grid(column=0, row=0, columnspan=2, sticky="news")
        ex_lbl.grid(column=0, row=1, sticky="news") 
        st_lbl.grid(column=1, row=1, sticky="news")
        choice_frame_ex.grid(column=0, row=2, sticky="news")
        choice_frame_set.grid(column=1, row=2, sticky="news")
        
        for i in range(6):    
            exercise = ctk.CTkComboBox(master=choice_frame_ex, values=["press", "2", "3", "4", "5", "6"])
            set = ctk.CTkComboBox(master=choice_frame_set, values=["1", "2", "3", "4", "5"])
            exercise.grid(column=0, row=i, sticky="news")
            set.grid(column=1, row=i, sticky="news")

# setup frame: left side for programming, right for muscles frames
class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="yellow")
        self.grid_columnconfigure((0), weight=2)
        self.grid_columnconfigure((1), weight=1)

    def create_widgets(self, parent):
        programming_side = ProgrammingFrames(self)
        programming_side.grid(column=0, row=0)
        programming_side.create_widgets(self)
        muscle_side = MuscleFrame(self)
        muscle_side.grid(column=1, row=0)
        muscle_side.create_widgets(self)
        
# left side of setup
class ProgrammingFrames(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

    def create_widgets(self, parent):
        day_frame1 = ProgrammingFrame(self)
        day_frame2 = ProgrammingFrame(self)
        day_frame3 = ProgrammingFrame(self)
        day_frame4 = ProgrammingFrame(self)
        day_frame5 = ProgrammingFrame(self)
        day_frame6 = ProgrammingFrame(self)
        day_frame1.grid(row=0, column=0, sticky="news")
        day_frame2.grid(row=0, column=1, sticky="news")
        day_frame3.grid(row=1, column=0, sticky="news")
        day_frame4.grid(row=1, column=1, sticky="news")
        day_frame5.grid(row=2, column=0, sticky="news")
        day_frame6.grid(row=2, column=1, sticky="news")
        day_frame1.create_widgets()
        day_frame2.create_widgets()
        day_frame3.create_widgets()
        day_frame4.create_widgets()
        day_frame5.create_widgets()
        day_frame6.create_widgets()

# right side of setup
class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="red")
        self.grid_columnconfigure((0), weight=2)
        self.grid_columnconfigure((1), weight=1)

    def create_widgets(self, parent):
        muscles = ["Biceps", "Calves", "Chest", "Glutes", "Hamstrings", "Lats", "Lower back", "Upper back", "Quads", "Delts", "Traps", "Triceps"]

        for i in range(len(muscles)):
            muscle = ctk.CTkLabel(master=self, text_color="white")
            muscle.grid(column=0, row=i, sticky="news")
            muscle.configure(text=muscles[i])