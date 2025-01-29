import customtkinter as ctk
from data.sqlite import SQLHandler

class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)

        self.sql_handler = SQLHandler()
        self.exercises_list = self.sql_handler.read_all_exercises()

    def create_widgets(self, parent):
        def ex_callback(ex):
            parent.exercise = ex
            lst = self.sql_handler.read_multiplier_muscle(ex)
            # loop sets muscle_multiplier dict 
            for i in range(len(lst)):
                parent.muscle_multiplier[lst[i][1]] = lst[i][0]

        def set_callback(set):
            parent.sets = int(set)

        combo_ex = ctk.CTkComboBox(master=self, values=self.exercises_list, state="readonly", command=ex_callback, width=200, height=20, font=('Helvatica', 20))
        combo_ex.grid(column=0, row=0, padx=5)
        combo_set = ctk.CTkComboBox(master=self, values=["1", "2", "3", "4", "5"], state="readonly", command=set_callback)
        combo_set.grid(column=1, row=0, padx=5)