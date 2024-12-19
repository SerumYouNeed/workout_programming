import customtkinter as ctk
from choice_frame import ChoiceFrame
from data.sqlite import SQLHandler

class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="yellow")
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

    # def btn_delete_sets_callback(self):
    #     for k, v in self.muscle_multiplier.items():
    #         for i in range(len(self.muscles)):
    #             if self.muscles[i] == k:
    #                 label = self.total_sets_list[i]
    #                 amount = float(label.cget('text'))
    #                 amount -= v
    #                 self.total_sets_list[i].configure(text=amount)
    #     self.muscle_multiplier = {}

    # def btn_callback(self):
    #     for k, v in self.muscle_multiplier.items():
    #         for i in range(len(self.muscles)):
    #             if self.muscles[i] == k:
    #                 label = self.total_sets_list[i]
    #                 print(label)
    #                 amount = float(label.cget('text'))
    #                 amount += v
    #                 print(amount)
    #                 print(amount)
    #                 self.total_sets_list[i].configure(text=amount)
    #     self.muscle_multiplier = {}

    def create_widgets(self, parent):
    
        # for i in range(len(self.muscles)):
        #     muscle = ctk.CTkLabel(master=self, text_color="red")
        #     muscle.grid(column=1, row=i, sticky="news")
        #     muscle.configure(text=self.muscles[i])
        #     sets = ctk.CTkLabel(master=self, text_color="red")
        #     sets.grid(column=2, row=i, sticky="news")
        #     sets.configure(text="0")
        #     self.total_sets_list.append(sets)

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
            day_lbl.grid(column=i*2, row=0, columnspan=2)
            MyBtn(trainig_program_frame, i*2)        

class MyBtn(ctk.CTkButton):
    def __init__(self, master, column):
        super().__init__(master)
        self.row = 2

        def btn_add_ex_callback():
            # self: button, master: training_program_frame, master.master: empty_frame
            sets = "sets"
            if master.master.sets == 1:
                sets = "set"
            lbl_txt = f"{master.master.exercise} - {master.master.sets} {sets}"
            ex_label = ctk.CTkLabel(master=master, text=lbl_txt, font=("Helvatica", 18))
            delete_btn = ctk.CTkButton(master=master, text="X", width=15, height=15, text_color="black", fg_color="tomato", hover_color="red")
            # add exercise: sets to master.master.daily_routines dict
            dict_key = f"Day {int(column/2 + 1)}"
            master.master.daily_routines[dict_key].append({master.master.exercise:master.master.sets})
            ex_label.grid(column=column+1, row=self.row) 
            delete_btn.grid(column=column, row=self.row, padx=5, pady=3)
            self.row += 1
            print(master.master.daily_routines)

        btn = ctk.CTkButton(master=master, text="Add exercise", width=100, height=22, fg_color="PaleGreen3", hover_color="green3", text_color="black",command=btn_add_ex_callback)
        btn.grid(row=1, column=column, columnspan=2, ipadx=10, ipady=3)
        

