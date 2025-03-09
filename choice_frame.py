import customtkinter as ctk
from data.sqlite import SQLHandler
from CTkMessagebox import CTkMessagebox

class ToplevelWindowAddExercise(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.sql_handler = SQLHandler()
        self.muscle_list = self.sql_handler.read_all_muscles()

        self.label = ctk.CTkLabel(self, text='Name your new exercise')
        self.label.pack(padx=20, pady=20)
        self.entry = ctk.CTkEntry(self, placeholder_text='Exercise name')
        self.entry.pack(padx=20, pady=20)

        self.label_musc = ctk.CTkLabel(self, text='What muscle ')
        self.label_musc.pack(padx=20, pady=20)
        self.musc = ctk.CTkComboBox(self, values=self.muscle_list)
        self.musc.pack(padx=20, pady=20)


class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.configure(fg_color='transparent')

        self.toplevel_window_add_exercise = None

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
            if self.toplevel_window_add_exercise is None or not self.toplevel_window_add_exercise.winfo_exists():
                # create window if its None or destroyed
                self.toplevel_window = ToplevelWindowAddExercise(self)
            else:
                self.toplevel_window_add_exercise.focus()
            # dialog_name = ctk.CTkInputDialog(text='Create a name of your exercise. It should not start with digit, space or non-letter sign', title='Name your exercise')
            # name = dialog_name.get_input()
            # dialog_musc = ctk.CTkInputDialog(text=f'What muscle are you going to train with {name}. If more that one, add another exercise with the same name but different muscle and weight', title='Muscles trained')
            # muscle = dialog_musc.get_input()
            # dialog_weight = ctk.CTkInputDialog(text=f'Set weight of {name}. Choose number from 0 (indicate that this exercise has almost no impact for given muscle group) to 1 (indicate that chosen muscle is main mover during that exercise). If more that one, add another exercise with the same name but different muscle and weight', title='Muscle trained')
            # weight = int(dialog_weight.get_input())
            # if self.sql_handler.check_if_exists(muscle, name) == []:
            #     try:
            #         self.sql_handler.new_exercise(muscle, name, weight)
            #         ex_added = self.sql_handler.check_add_correctly(muscle, name, weight)
            #         print(type(ex_added))
            #         print(ex_added)
            #         if (muscle, name, weight) in ex_added:
            #             CTkMessagebox(title='Great!',
            #                         message='Your exercise was successfully added.',
            #                         icon='check',
            #                         option_1='Thanks')
            #     except:
            #         CTkMessagebox(title='Ups...',
            #                     message='Something went wrong.',
            #                     icon='cancel')
            # else:
            #     CTkMessagebox(title='Exercise status',
            #                   message='It seems your exercise is already on the list.',
            #                   icon='warning')

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