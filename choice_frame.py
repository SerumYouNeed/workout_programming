import customtkinter as ctk
from data.sqlite import SQLHandler

class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1,2,3), weight=1)

        self.sql_handler = SQLHandler()
        self.exercises_list = self.sql_handler.read_all_exercises()

    def create_widgets(self, parent):
        def ex_callback(ex):
            lst = self.sql_handler.read_multiplier_muscle(ex)
            # loop sets muscle_multiplier dict 
            for i in range(len(lst)):
                parent.muscle_multiplier[lst[i][1]] = lst[i][0]
            print(parent.muscle_multiplier)

        def set_callback(set):
            parent.sets = int(set)

        def both_callback(sets):
            set_callback(sets)
            if parent.sets != None:
                for key, value in parent.muscle_multiplier.items():
                    parent.muscle_multiplier[key] = value * parent.sets
            print(parent.muscle_multiplier)

        combo_ex = ctk.CTkComboBox(master=self, values=self.exercises_list, command=ex_callback)
        combo_ex.grid(column=1, row=0)
        combo_set = ctk.CTkComboBox(master=self, values=["1", "2", "3", "4", "5"], command=both_callback)
        combo_set.grid(column=2, row=0)