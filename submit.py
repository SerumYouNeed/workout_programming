import customtkinter as ctk

class SubBtn(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__()
        self.frame = parent
        self.btn = ctk.CTkButton(self.frame, text="Submit", command=submit)
        # self.btn.grid(row=3, column=0, columnspan=2, sticky="n")

        def submit(set, exercise):
            if set != -1 and exercise != -1:
                for i in range(len(exercise.muscle_multiplier)):
                    self.muscles_load[exercise.muscle_multiplier[i][0]] = exercise.muscle_multiplier[i][1] * set
            print(self.muscles_load)

        #     for i in range(len(parent.combo_exercise_list)):
        #         for j in range(len(parent.combo_exercise_list[i])):
        #             parent.combo_exercise_list[i][j] 
