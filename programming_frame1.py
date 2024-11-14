import customtkinter as ctk

class ProgrammingFrame1(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")

    # create widgets
    def create_widgets(self, parent):
        day_frame = ctk.CTkFrame(self, fg_color="yellow")
        day_frame.pack(expand=True, fill="both")
        label_frame = ctk.CTkFrame(day_frame, fg_color="pink")
        label_frame.pack(expand=True, fill="x")
        d1_lbl = ctk.CTkLabel(master=label_frame, text="Day 1",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 27))
        etq_frame = ctk.CTkFrame(day_frame, fg_color="red")
        etq_frame.pack(expand=True, fill="x")
        ex_lbl = ctk.CTkLabel(master=etq_frame, text="Exercise",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        st_lbl = ctk.CTkLabel(master=etq_frame, text="Sets",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))

        
        choice_frame_ex = ctk.CTkFrame(day_frame)
        choice_frame_ex.pack(side="left", fill="both")
        choice_frame_set = ctk.CTkFrame(day_frame)
        choice_frame_set.pack(side="left", fill="both")
        exercises = []
        sets = []
        for i in range(2):
            exercise = ctk.CTkComboBox(master=choice_frame_ex, values=["press", "2", "3", "4", "5", "6"])
            set = ctk.CTkComboBox(master=choice_frame_set, values=["1", "2", "3", "4", "5"])
            exercises.append(exercise)
            sets.append(set)

        # place widgets
        d1_lbl.pack()

        ex_lbl.pack(side="left", expand=True, fill="both")
        for i in range(len(exercises)):
            exercises[i].pack()
        
        st_lbl.pack(side="left", expand=True, fill="both")
        for i in range(len(exercises)):
            sets[i].pack()
       

class ProgrammingFrame2(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")

    # create widgets 
    def create_widgets(self, parent):
        d1_lbl = ctk.CTkLabel(self, text="Day 1",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 27))
        d2_lbl = ctk.CTkLabel(self, text="Day 2",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 27))
        ex_lbl = ctk.CTkLabel(self, text="Exercise",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        st_lbl = ctk.CTkLabel(self, text="Sets",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        ex2_lbl = ctk.CTkLabel(self, text="Exercise",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        st2_lbl = ctk.CTkLabel(self, text="Sets",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
           
        exercise_1 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_2 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_3 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_4 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_5 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_6 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise_7 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        sets_1 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_2 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_3 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_4 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_5 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_6 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets_7 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        exercise2_1 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_2 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_3 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_4 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_5 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_6 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        exercise2_7 = ctk.CTkComboBox(self, values=["press", "2", "3", "4", "5", "6" , "7"])
        sets2_1 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_2 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_3 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_4 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_5 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_6 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        sets2_7 = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5"])
        
        # place widgets
        advice_d1.grid(row=0, column=0, columnspan=4, sticky="wens")
        d1_lbl.grid(row=1, column=0, columnspan=2, sticky="n")
        d2_lbl.grid(row=1, column=2, columnspan=2)
        ex_lbl.grid(row=2, column=0)
        exercise_1.grid(row=3, column=0)
        exercise_2.grid(row=4, column=0)
        exercise_3.grid(row=5, column=0)
        exercise_4.grid(row=6, column=0)
        exercise_5.grid(row=7, column=0)
        exercise_6.grid(row=8, column=0)
        exercise_7.grid(row=9, column=0)
        ex2_lbl.grid(row=2, column=2)
        exercise2_1.grid(row=3, column=2)
        exercise2_2.grid(row=4, column=2)
        exercise2_3.grid(row=5, column=2)
        exercise2_4.grid(row=6, column=2)
        exercise2_5.grid(row=7, column=2)
        exercise2_6.grid(row=8, column=2)
        exercise2_7.grid(row=9, column=2)
        st_lbl.grid(row=2, column=1)
        sets_1.grid(row=3, column=1)
        sets_2.grid(row=4, column=1)
        sets_3.grid(row=5, column=1)
        sets_4.grid(row=6, column=1)
        sets_5.grid(row=7, column=1)
        sets_6.grid(row=8, column=1)
        sets_7.grid(row=9, column=1)
        st2_lbl.grid(row=2, column=3)
        sets2_1.grid(row=3, column=3)
        sets2_2.grid(row=4, column=3)
        sets2_3.grid(row=5, column=3)
        sets2_4.grid(row=6, column=3)
        sets2_5.grid(row=7, column=3)
        sets2_6.grid(row=8, column=3)
        sets2_7.grid(row=9, column=3)