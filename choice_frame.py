import customtkinter as ctk
from data.sqlite import SQLHandler

class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.configure(fg_color='transparent')


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

        combo_ex = ctk.CTkComboBox(master=self,
                                    values=self.exercises_list,  
                                    command=ex_callback,  
                                    font=('', 18), 
                                    dropdown_font=('', 18),
                                    width=230)
        combo_ex.grid(column=1, row=0, padx=15, pady=10, sticky='W')
        combo_ex_lbl = ctk.CTkLabel(self, 
                                    text='Pick exercise:',
                                    font=('', 18, 'bold'))
        combo_ex_lbl.grid(column=0, row=0, padx=15, sticky='E')
        combo_set = ctk.CTkComboBox(master=self,
                                    values=['1', '2', '3', '4', '5'], 
                                    command=set_callback, 
                                    font=('', 18), 
                                    dropdown_font=('', 18),
                                    width=70)
        combo_set.grid(column=1, row=1, padx=15, pady=10, sticky='W')
        combo_set_lbl = ctk.CTkLabel(self, 
                                    text='Woking sets:',
                                    font=('', 18, 'bold'))
        combo_set_lbl.grid(column=0, row=1, padx=15, sticky='E')