import customtkinter as ctk
from choice_frame import ChoiceFrame
from data.sqlite import SQLHandler

# setup frame: left side for comboboxes with exercises and sets selectors, right for muscles frames
class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="yellow")
        self.grid_columnconfigure((0,1,2), weight=1)

        self.sql_handler = SQLHandler()
        self.muscle_multiplier = {}
        self.sets = None
        self.muscles = self.sql_handler.read_all_muscles()
        self.total_sets_list = []
    
    def btn_callback(self):
        for k, v in self.muscle_multiplier.items():
            for i in range(len(self.muscles)):
                if self.muscles[i] == k:
                    label = self.total_sets_list[i]
                    print(label)
                    amount = float(label.cget('text'))
                    print(amount)
                    amount += v
                    print(amount)
                    self.total_sets_list[i].configure(text=amount)
        self.muscle_multiplier = {}

    def create_widgets(self, parent):
    
        for i in range(len(self.muscles)):
            muscle = ctk.CTkLabel(master=self, text_color="red")
            muscle.grid(column=1, row=i, sticky="news")
            muscle.configure(text=self.muscles[i])
            sets = ctk.CTkLabel(master=self, text_color="red")
            sets.grid(column=2, row=i, sticky="news")
            sets.configure(text="0")
            self.total_sets_list.append(sets)

        programming_side = ChoiceFrame(self)
        programming_side.grid(column=0)
        programming_side.create_widgets(self)


        btn = ctk.CTkButton(self, text="Count sets", command=self.btn_callback)
        btn.grid(column=0)
        