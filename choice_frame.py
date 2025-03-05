import customtkinter as ctk
from data.sqlite import SQLHandler
from CTkMessagebox import CTkMessagebox

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

        def new_exercise():
            dialog_name = ctk.CTkInputDialog(text='Create a name of your exercise. It should not start with digit, space or non-letter sign', title='Name your exercise')
            name = dialog_name.get_input()
            dialog_musc = ctk.CTkInputDialog(text=f'What muscle are you going to train with {name}. If more that one, add another exercise with the same name but different muscle and weight', title='Muscles trained')
            muscle = dialog_musc.get_input()
            dialog_weight = ctk.CTkInputDialog(text=f'Set weight of {name}. Choose number from 0 (indicate that this exercise has almost no impact for given muscle group) to 1 (indicate that chosen muscle is main mover during that exercise). If more that one, add another exercise with the same name but different muscle and weight', title='Muscle trained')
            weight = int(dialog_weight.get_input())
            try:
                self.sql_handler.new_exercise(muscle, name, weight)
                ex_list = self.sql_handler.read_all_exercises()
                if name in ex_list:
                    CTkMessagebox(title='Great!',
                                  message='Your exercise was successfully added.',
                                  icon='check',
                                  option_1='Thanks')
            except:
                CTkMessagebox(title='Ups...',
                              message='Something went wrong.',
                              icon='cancel')

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

        add_exercise_lbl = ctk.CTkLabel(self,
                                        text='Add new exercise to the list:',
                                        font=('', 18, 'bold'))
        add_exercise_lbl.grid(column=0, row=2, padx=15, sticky='E')
        add_exercise_btn = ctk.CTkButton(self,
                                         text='New exercise',
                                         font=('', 15),
                                         command=new_exercise)
        add_exercise_btn.grid(column=1, row=2, padx=15, pady=10, sticky='W')