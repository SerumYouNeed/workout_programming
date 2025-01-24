import customtkinter as ctk

class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.configure(fg_color="white")
        self.muscles_dict = parent.total_load_per_muscle
        self.entry = ctk.CTkLabel(master=self)
        self.entry.grid()

    def create_widgets(self):
        print(self.muscles_dict)
        entry_label_full = ""
        for k, v in self.muscles_dict.items():
            if v > 1:
                text = f'{k}: {v}sets\n'
            else: 
                text = f'{k}: {v}set\n'
            entry_label_full += text
        self.entry.configure(text= entry_label_full)    