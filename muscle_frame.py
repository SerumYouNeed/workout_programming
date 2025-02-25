import customtkinter as ctk

class MuscleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure((0,1,2), weight=1)
        self.configure(fg_color='transparent')
        self.entry = []

    def update_table_total_load(self, parent):
        if self.entry:
            for i in self.entry:
                i.destroy()
            self.entry.clear()
        for k, v in parent.total_load_per_muscle.items():
            self.entry_lbl = ctk.CTkLabel(master=self, font=('', 18))
            if v > 1:
                text = f'{k}: {v}sets\n'
            else: 
                text = f'{k}: {v}set\n'
            self.entry_lbl.configure(text=text)    
            if v > 25:
                self.entry_lbl.configure(text_color='red')
            elif v > 15:   
                self.entry_lbl.configure(text_color='orange')
            elif v > 5:
                self.entry_lbl.configure(text_color='lime green')
            self.entry.append(self.entry_lbl)
        for i in self.entry:
            i.grid(column=1, sticky='NSEW')
