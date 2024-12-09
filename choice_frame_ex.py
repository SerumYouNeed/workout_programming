import customtkinter as ctk
from data.sqlite import SQLHandler

class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure((0,1), weight=1)

        self.sql_handler = SQLHandler()
        self.muscle_multiplier = {}
        self.exercises_list = self.sql_handler.read_all_exercises()
        self.sets = None

    def create_widgets(self):
        def ex_callback(ex):
            lst = self.sql_handler.read_multiplier_muscle(ex)
            # loop sets muscle_multiplier dict 
            for i in range(len(lst)):
                self.muscle_multiplier[lst[i][1]] = lst[i][0]
            print(self.muscle_multiplier)

        def set_callback(set):
            self.sets = int(set)

        def both_callback(sets):
            set_callback(sets)
            if self.sets != None:
                for key, value in self.muscle_multiplier.items():
                    self.muscle_multiplier[key] = value * self.sets

        combo_ex = ctk.CTkComboBox(master=self, values=self.exercises_list, command=ex_callback)
        combo_ex.grid(column=0, row=0)
        combo_set = ctk.CTkComboBox(master=self, values=["1", "2", "3", "4", "5"], command=both_callback)
        combo_set.grid(column=1, row=0)