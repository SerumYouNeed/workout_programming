import customtkinter as ctk
from data.sqlite import SQLHandler


# List of muscles should be trained. Once added to the right muscle should disapeare.
class MuscleLeftFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.configure(fg_color="transparent")

        self.sql_handler = SQLHandler()
        self.muscles = self.sql_handler.read_all_muscles()
        self.muscle_labels = []
        self.removed_muscle_after_update = []

    def create_widgets(self):
        for i in self.muscles:
            muscle = ctk.CTkLabel(master=self, font=("", 18), text=i)
            muscle.grid(column=1, sticky="NSEW")
            self.muscle_labels.append(muscle)

    def update_muscle_left_frame(self, muscle):
        for i in self.muscle_labels:
            if i.cget("text") == muscle:
                i.destroy()
            if i in self.muscles:
                self.removed_muscle_after_update.append(i)
                self.muscles.remove(muscle)

    def update_after_deletion(self):
        for lbl in self.muscle_labels:
            lbl.destroy()
        for i in self.removed_muscle_after_update:
            if i not in self.muscles:
                self.muscles.append(i)
        self.muscles.sort()
        self.create_widgets()
