import customtkinter as ctk
from data.sqlite import SQLHandler

class ComboBoxExercise(ctk.CTkComboBox):
    def __init__(self, parent, val, col, row):
        super().__init__(parent)
        self.muscle_multiplier = {}
        
        self.sql_handler = SQLHandler()

        # set muscle: multiplier dict taking an exercise from combo
        def combo_callbacks(input):
            exercise = ex_callback(input)
            for i in range(len(exercise)):
                self.muscle_multiplier[exercise[i][1]] = exercise[i][0]
            parent.combo_exercise_list.append(self.muscle_multiplier)
        
        # return list of tuples (multiplier, muscle)
        def ex_callback(exercise):
            return self.sql_handler.read_multiplier_muscle(exercise)
            
        self.combo = ctk.CTkComboBox(master=parent, values=val, command=combo_callbacks)
        self.combo.grid(column=col, row=row, sticky="news")

class ComboBoxSet(ctk.CTkComboBox):
    def __init__(self, parent, val, col, row):
        super().__init__(parent)
        self.sets = None

        self.sql_handler = SQLHandler()

        def set_callback(set):
            self.sets = set
            
        self.combo = ctk.CTkComboBox(master=parent, values=val, command=set_callback)
        self.combo.grid(column=col, row=row, sticky="news")


