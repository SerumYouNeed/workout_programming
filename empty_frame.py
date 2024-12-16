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
        self.muscles = self.sql_handler.read_all_muscles()
        self.total_sets_list = []
        self.day = "1"
        self.exercise = None
        self.exercises_list = self.sql_handler.read_all_exercises()

    def btn_delete_sets_callback(self):
        for k, v in self.muscle_multiplier.items():
            for i in range(len(self.muscles)):
                if self.muscles[i] == k:
                    label = self.total_sets_list[i]
                    amount = float(label.cget('text'))
                    amount -= v
                    self.total_sets_list[i].configure(text=amount)
        self.muscle_multiplier = {}

    def btn_callback(self):
        for k, v in self.muscle_multiplier.items():
            for i in range(len(self.muscles)):
                if self.muscles[i] == k:
                    label = self.total_sets_list[i]
                    print(label)
                    amount = float(label.cget('text'))
                    amount += v
                    print(amount)
                    print(amount)
                    self.total_sets_list[i].configure(text=amount)
        self.muscle_multiplier = {}

    def create_widgets(self, parent):

        def ex_callback(ex):
            self.exercise = ex
            print(self.exercise)
        combo_ex = ctk.CTkComboBox(master=self, values=self.exercises_list, command=ex_callback)
        combo_ex.grid()
    
        for i in range(len(self.muscles)):
            muscle = ctk.CTkLabel(master=self, text_color="red")
            muscle.grid(column=1, row=i, sticky="news")
            muscle.configure(text=self.muscles[i])
            sets = ctk.CTkLabel(master=self, text_color="red")
            sets.grid(column=2, row=i, sticky="news")
            sets.configure(text="0")
            self.total_sets_list.append(sets)

        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0)
        programming_side.create_widgets(self)

        btn = ctk.CTkButton(self, text="Count sets", command=self.btn_callback)
        btn.grid(column=0)

        btn_delete_sets = ctk.CTkButton(self, text="Delete sets", command=self.btn_delete_sets_callback)
        btn_delete_sets.grid(column=0)

        trainig_program_frame = ctk.CTkFrame(self)
        trainig_program_frame.configure(fg_color="pink")
        trainig_program_frame["columns"] = list(range(0, parent.number_of_training_days))
        trainig_program_frame.grid()
        for i in range(parent.number_of_training_days):
            day_lbl = ctk.CTkLabel(master=trainig_program_frame, text="Day " + str(i + 1), anchor="s")
            day_lbl.grid(column=i, row=0)
            MyBtn(trainig_program_frame, i)        

class MyBtn(ctk.CTkButton):
    def __init__(self, master, column):
        super().__init__(master)
        self.row = 2

        def btn_add_ex_callback():
            # self: button, master: training_program_frame, master.master: empty_frame
            ex_label = ctk.CTkLabel(master=master, text=master.master.exercise)
            ex_label.grid(column=column, row=self.row)
            self.row += 1

        btn = ctk.CTkButton(master=master, command=btn_add_ex_callback)
        btn.grid(row=1, column=column)
        

