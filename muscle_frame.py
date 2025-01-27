import customtkinter as ctk

class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.configure(fg_color="black")
        self.entry = None

    def update_table_total_load(self, parent):
        if self.entry is not None:
            self.entry.destroy()
        self.entry = ctk.CTkLabel(master=self, text_color="white", font=("Helvatica", 18))
        self.entry.grid(column=1)
        entry_label_full = ""
        for k, v in parent.total_load_per_muscle.items():
            if v > 1:
                text = f'{k}: {v}sets\n'
            else: 
                text = f'{k}: {v}set\n'
            entry_label_full += text
        self.entry.configure(text= entry_label_full)    