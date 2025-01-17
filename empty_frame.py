import customtkinter as ctk
from choice_frame import ChoiceFrame
from data.sqlite import SQLHandler

class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1,2), weight=1)

        self.sql_handler = SQLHandler()
        self.muscle_multiplier = {}
        self.sets = None
        self.muscles = self.sql_handler.read_all_muscles()
        self.total_sets_list = []
        self.day = "1"
        self.exercise = None
        self.exercises_list = self.sql_handler.read_all_exercises()
        # daily_routines: {Day i: [{exercise : sets}, ...]}
        self.daily_routines = dict()
        # list o frames with del_btn/ex/set
        self.frames_to_delete = dict()

    def create_widgets(self, parent):

        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0)
        programming_side.create_widgets(self)

        trainig_program_frame = ctk.CTkFrame(self)
        trainig_program_frame.configure(fg_color="pink")
        trainig_program_frame["columns"] = list(range(0, parent.number_of_training_days * 2))
        trainig_program_frame.grid()
        for i in range(parent.number_of_training_days):
            day_name = f"Day {i+1}"
            self.daily_routines[day_name] = list()
            day_lbl = ctk.CTkLabel(master=trainig_program_frame, text="Day " + str(i + 1), font=("Helvatica", 22))
            # set label and button on every other column
            day_lbl.grid(column=i, row=0)
            MyBtn(trainig_program_frame, i)  

class DelExSetFrame(ctk.CTkFrame):
    def __init__(self, parent, column):
        super().__init__(parent)  
        self.configure(fg_color="white")
        self.grid_columnconfigure(2)    

class MyBtn(ctk.CTkButton):
    def __init__(self, master, column):
        super().__init__(master)
        self.row = 2


        def btn_add_ex_callback():
            frame = DelExSetFrame(master, column)
            # self: button, master: training_program_frame, master.master: empty_frame
            sets = "sets"
            if master.master.sets == 1:
                sets = "set"
            lbl_txt = f"{master.master.exercise} - {master.master.sets} {sets}"

            # add exercise: sets to master.master.daily_routines dict
            dict_key = f"Day {int(column + 1)}"
            master.master.daily_routines[dict_key].append({master.master.exercise:master.master.sets})

            ex_label = ctk.CTkLabel(master=frame, text=lbl_txt, font=("Helvatica", 18))

            def btn_del_ex_callback():
                ex_label.destroy()
                delete_btn.destroy()
                frame.destroy()

            delete_btn = ctk.CTkButton(master=frame, text="X", width=15, height=15, text_color="black", fg_color="tomato", hover_color="red", command=btn_del_ex_callback)
            ex_label.grid(column=1, row=0, padx=5, pady=3) 
            delete_btn.grid(column=0, row=0, padx=5, pady=3)
            frame.grid(column=column, row=self.row)

            self.row += 1
            print(master.master.daily_routines)


        btn = ctk.CTkButton(master=master, text="Add exercise", width=100, height=22, fg_color="PaleGreen3", hover_color="green3", text_color="black",command=btn_add_ex_callback)
        btn.grid(row=1, column=column, ipadx=10, ipady=3)
        

