import customtkinter as ctk
from combobox import ComboBoxExercise, ComboBoxSet
from submit import SubBtn

class ProgrammingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,3,4), weight=1)
        self.grid_rowconfigure(2, weight=3)
        root = self.winfo_toplevel()
        # list of muscles load per frame
        self.muscles_load = []
        # self.muscle_multiplier = {}

        self.sql_handler = parent.sql_handler

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
        btn = SubBtn(self)
        
        # frame with choices
        choice_frame_ex = ctk.CTkFrame(self, fg_color="black")
        choice_frame_ex.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        choice_frame_set = ctk.CTkFrame(self, fg_color="black")
        choice_frame_set.grid_rowconfigure((0,1,2,3,4,5), weight=1)

        # place widgets
        day_lbl.grid(column=0, row=0, columnspan=2, sticky="news")
        ex_lbl.grid(column=0, row=1, sticky="news") 
        st_lbl.grid(column=1, row=1, sticky="news")
        choice_frame_ex.grid(column=0, row=2, sticky="news")
        choice_frame_set.grid(column=1, row=2, sticky="news")
        btn.grid(row=3, column=0, columnspan=2, sticky="n")

        exercises_list = self.sql_handler.read_all_exercises()
        self.combo_exercise_list = []
        self.combo_set_list = []
        for i in range(3):    
            exercise = ComboBoxExercise(choice_frame_ex, exercises_list, 0, i)
            exercise.set("--exercise--")
            set = ComboBoxSet(choice_frame_set, ["1", "2", "3", "4", "5"], 1, i)
            set.set("--sets--")
            set.bind("<<ComboboxSelected>>", setting_muscles_load(set.sets, exercise))


# left side of setup
class ProgrammingFrames(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.sql_handler = parent.sql_handler


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