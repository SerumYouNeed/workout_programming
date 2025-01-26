import customtkinter as ctk

class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.configure(fg_color="white")

    def create_widgets(self):
        self.entry = ctk.CTkLabel(master=self, text="")
        self.entry.grid()

    def update_table_total_load(self, parent):
        entry_label_full = ""
        for k, v in parent.total_load_per_muscle.items():
            if v > 1:
                text = f'{k}: {v}sets\n'
            else: 
                text = f'{k}: {v}set\n'
            entry_label_full += text
        self.entry.configure(text= entry_label_full)    