import customtkinter as ctk
from choice_frame import ChoiceFrame
from data.sqlite import SQLHandler
from muscle_frame import MuscleFrame
from legend_frame import LegendFrame
from muscle_left_frame import MuscleLeftFrame

class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid_columnconfigure(0, weight=2)

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
        # list o frames with del_btn/ex/set
        self.frames_to_delete = dict()
        # calculated load: {muscle: load}
        self.total_load_per_muscle = dict()

    def create_widgets(self, parent):
        # zero row
        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0, row=0, pady=20)
        programming_side.create_widgets(self)

        muscle_lbl = ctk.CTkLabel(master=self, text_color="yellow", font=("Helvatica", 18), text="List of muscle to load:", bg_color="black")
        muscle_lbl.grid(column=1, row=0, pady=20, sticky="NSEW")
        muscle_lbl = ctk.CTkLabel(master=self, text_color="yellow", font=("Helvatica", 18), text="List of loaded muscles:", bg_color="black")
        muscle_lbl.grid(column=2, row=0, pady=20, sticky="NSEW")

        # first row
        trainig_program_frame = ctk.CTkFrame(self)
        trainig_program_frame.configure(fg_color="black")
        trainig_program_frame["columns"] = list(range(0, parent.number_of_training_days * 2))
        trainig_program_frame.grid(column=0, row=1, sticky="NSEW")
        for i in range(parent.number_of_training_days):
            day_name = f"Day {i+1}"
            self.daily_routines[day_name] = list()
            day_lbl = ctk.CTkLabel(master=trainig_program_frame, 
                                   text="Day " + str(i + 1), 
                                   font=("Helvatica", 22),
                                   text_color="white")
            # set label and button on every other column
            day_lbl.grid(column=i, row=0, pady=15)
            MyBtn(trainig_program_frame, i)  

        muscle_left_frame = MuscleLeftFrame(self)
        muscle_left_frame.grid(column=1, row=1, sticky="NSEW")
        muscle_left_frame.create_widgets()
        self.new_muscle_frame = MuscleFrame(self)
        self.new_muscle_frame.grid(column=2, row=1, sticky='NSEW')

        # second row
        legend_frame = LegendFrame(self)
        legend_frame.grid(column=1, row=2, columnspan=2, sticky="NSEW", pady=100)
        legend_frame.create_widgets()

        # third row
        def back():
            parent.switch_frame(parent._main_frame)

        back_btn = ctk.CTkButton(self, 
                                text="Back", 
                                width=100, 
                                height=22, 
                                font=("Helvatica", 15),
                                text_color="white",
                                fg_color="gray15",
                                corner_radius=8,
                                hover_color="gray18",
                                command=back)
        back_btn.grid(column=0, row=3)
        save_btn = ctk.CTkButton(self, 
                                width=100, 
                                height=22, 
                                font=("Helvatica", 15),
                                text_color="white",
                                fg_color="gray15",
                                corner_radius=8,
                                hover_color="gray18"
                                )
        save_btn.grid(column=1, row=3, columnspan=2)

# frame grouping delete button and exercise - sets label in one place. It remember exercise and sets on it.
class DelExSetFrame(ctk.CTkFrame):
    def __init__(self, master, column):
        super().__init__(master)  
        self.configure(fg_color="black")
        self.grid_columnconfigure(2)  
        self.ex_on_this_frame = master.master.exercise
        self.sets_on_this_frame = master.master.sets

class MyBtn(ctk.CTkButton):
    def __init__(self, master, column):
        super().__init__(master)
        self.row = 2
        self.sql_handler = SQLHandler()
        dict_key = f"Day {int(column + 1)}"
        self.entry_of_this_btn = dict()

        def btn_add_ex_callback():
            multiplier_muscle_list =  self.sql_handler.read_multiplier_muscle(master.master.exercise)
            frame = DelExSetFrame(master, column)
            frame.ex_on_this_frame = master.master.exercise
            frame.sets_on_this_frame = master.master.sets
            # self: button, master: training_program_frame, master.master: empty_frame
            sets = "sets"
            if master.master.sets == 1:
                sets = "set"
            lbl_txt = f"{master.master.exercise} - {master.master.sets} {sets}"
            
            # add exercise: sets to master.master.daily_routines dict
            master.master.daily_routines[dict_key].append({master.master.exercise:master.master.sets})
            
            self.entry_of_this_btn = {master.master.exercise:master.master.sets}

            ex_label = ctk.CTkLabel(master=frame, 
                                    text=lbl_txt, 
                                    font=("Helvatica", 18),
                                    text_color="white", )
            print(f'total load per muscle:{master.master.total_load_per_muscle}')

            def btn_del_ex_callback():
                # delete load from total load dict from empty_frame
                for i in multiplier_muscle_list:
                    multiplier, muscle = i
                    total_load = master.master.sets * multiplier
                    master.master.total_load_per_muscle[muscle] -= total_load
                    if master.master.total_load_per_muscle[muscle] == 0:
                        del master.master.total_load_per_muscle[muscle]

                master.master.daily_routines[dict_key].remove({frame.ex_on_this_frame:frame.sets_on_this_frame})

                ex_label.destroy()
                delete_btn.destroy()
                frame.destroy()
                print(master.master.total_load_per_muscle)
                print(master.master.daily_routines) 
                
                # update right side with total load
                master.master.new_muscle_frame.update_table_total_load(master.master)

            delete_btn = ctk.CTkButton(master=frame, text="X", width=15, height=15, text_color="black", fg_color="tomato", hover_color="red", command=btn_del_ex_callback)
            ex_label.grid(column=1, row=0, padx=5, pady=3) 
            delete_btn.grid(column=0, row=0, padx=5, pady=3)
            frame.grid(column=column, row=self.row)

            self.row += 1

            # calculate load for total dict in empty_frame
            for i in multiplier_muscle_list:
                multiplier, muscle = i                
                total_load = master.master.sets * multiplier
                if muscle in master.master.total_load_per_muscle.keys():
                    master.master.total_load_per_muscle[muscle] += total_load
                else:
                    master.master.total_load_per_muscle[muscle] = total_load
        
            # update right side with total load
            master.master.new_muscle_frame.update_table_total_load(master.master)
            print(master.master.total_load_per_muscle)
            print(master.master.daily_routines)

        btn = ctk.CTkButton(master=master, 
                            text="Add exercise", 
                            width=100, 
                            height=22, 
                            font=("Helvatica", 15),
                            text_color="white",
                            fg_color="gray15",
                            corner_radius=8,
                            hover_color="gray18",
                            command=btn_add_ex_callback)
        btn.grid(row=1, column=column, ipadx=10, ipady=3)
        

