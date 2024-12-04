import customtkinter as ctk

class SubBtn(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__()
        self.frame = parent
        self.btn = ctk.CTkButton(self.frame, text="Submit", command=submit)
        self.btn.grid(row=3, column=0, columnspan=2, sticky="n")

        def submit():
            for i in range(len(parent.combo_exercise_list)):
                for j in range(len(parent.combo_exercise_list[i])):
                    parent.combo_exercise_list[i][j] 
