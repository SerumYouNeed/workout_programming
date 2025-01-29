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
        self.grid_columnconfigure((0,1,2), weight=1)

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
        # first row
        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0, row=0, pady=20)
        programming_side.create_widgets(self)

        muscle_lbl = ctk.CTkLabel(master=self, text_color="yellow", font=("Helvatica", 18), text="List of muscle to load:")
        muscle_lbl.grid(column=1, row=0, pady=20)
        muscle_lbl = ctk.CTkLabel(master=self, text_color="yellow", font=("Helvatica", 18), text="List of loaded muscles:")
        muscle_lbl.grid(column=2, row=0, pady=20)

        trainig_program_frame = ctk.CTkFrame(self)
        trainig_program_frame.configure(fg_color="black")
        trainig_program_frame["columns"] = list(range(0, parent.number_of_training_days * 2))
        trainig_program_frame.grid()
        for i in range(parent.number_of_training_days):
            day_name = f"Day {i+1}"
            self.daily_routines[day_name] = list()
            day_lbl = ctk.CTkLabel(master=trainig_program_frame, 
                                   text="Day " + str(i + 1), 
                                   font=("Helvatica", 22),
                                   text_color="white")
            # set label and button on every other column
            day_lbl.grid(column=i, row=0)
            MyBtn(trainig_program_frame, i)  

        muscle_left_frame = MuscleLeftFrame(self)
        muscle_left_frame.grid(column=1, row=1)
        muscle_left_frame.create_widgets()
        self.new_muscle_frame = MuscleFrame(self)
        self.new_muscle_frame.grid(column=2, row=1, sticky='NSEW')
        legend_frame = LegendFrame(self)
        legend_frame.grid(sticky="S", columnspan=3)

class DelExSetFrame(ctk.CTkFrame):
    def __init__(self, parent, column):
        super().__init__(parent)  
        self.configure(fg_color="black")
        self.grid_columnconfigure(2)    

class MyBtn(ctk.CTkButton):
    def __init__(self, master, column):
        super().__init__(master)
        self.row = 2
        self.sql_handler = SQLHandler()

        def btn_add_ex_callback():
            multiplier_muscle_list =  self.sql_handler.read_multiplier_muscle(master.master.exercise)
            frame = DelExSetFrame(master, column)
            # self: button, master: training_program_frame, master.master: empty_frame
            sets = "sets"
            if master.master.sets == 1:
                sets = "set"
            lbl_txt = f"{master.master.exercise} - {master.master.sets} {sets}"
            
            # add exercise: sets to master.master.daily_routines dict
            dict_key = f"Day {int(column + 1)}"
            master.master.daily_routines[dict_key].append({master.master.exercise:master.master.sets})
            
            ex_label = ctk.CTkLabel(master=frame, 
                                    text=lbl_txt, 
                                    font=("Helvatica", 18),
                                    text_color="white", )

            def btn_del_ex_callback():
                # delete load from total load dict from empty_frame
                for i in multiplier_muscle_list:
                    multiplier, muscle = i
                    total_load = master.master.sets * multiplier
                    master.master.total_load_per_muscle[muscle] -= total_load
                    if master.master.total_load_per_muscle[muscle] == 0:
                        del master.master.total_load_per_muscle[muscle]

                ex_label.destroy()
                delete_btn.destroy()
                frame.destroy()
                print(master.master.total_load_per_muscle)

            delete_btn = ctk.CTkButton(master=frame, text="X", width=15, height=15, text_color="black", fg_color="tomato", hover_color="red", command=btn_del_ex_callback)
            ex_label.grid(column=1, row=0, padx=5, pady=3) 
            delete_btn.grid(column=0, row=0, padx=5, pady=3)
            frame.grid(column=column, row=self.row)

            self.row += 1
            print(master.master.daily_routines)

            # calculate load for total dict in empty_frame
            for i in multiplier_muscle_list:
                multiplier, muscle = i                
                total_load = master.master.sets * multiplier
                if muscle in master.master.total_load_per_muscle.keys():
                    master.master.total_load_per_muscle[muscle] += total_load
                else:
                    master.master.total_load_per_muscle[muscle] = total_load
            print(master.master.total_load_per_muscle)
            
            # update right side with total load
            master.master.new_muscle_frame.update_table_total_load(master.master)

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
        

