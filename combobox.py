import customtkinter as ctk
from data.sqlite import SQLHandler

class ComboBoxExercise(ctk.CTkComboBox):
    def __init__(self, parent, val, col, row):
        super().__init__(parent)
        # in what proportion what muscle are working during given exercise
        # self.muscle_multiplier = {}
        
        self.sql_handler = SQLHandler()

        # handler return list of tuples (multiplier, muscle)
        def ex_callback(exercise):
            lst = self.sql_handler.read_multiplier_muscle(exercise)
            # loop sets muscle_multiplier dict 
            for i in range(len(lst)):
                parent.muscle_multiplier[lst[i][1]] = lst[i][0]
            
        

class ComboBoxSet(ctk.CTkComboBox):
    def __init__(self, parent, val, col, row):
        super().__init__(parent)
        self.sets = None

        self.sql_handler = SQLHandler()

        def set_callback(set):
            self.sets = int(set)
            for k, v in parent.parent.muscle_multiplier:
                parent.parent.muscle_multiplier[k] = v * self.sets
            print(parent.parent.muscle_multiplier)
            
        self.combo = ctk.CTkComboBox(master=parent, values=val, command=set_callback)
        self.combo.grid(column=col, row=row, sticky="news")


