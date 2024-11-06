import customtkinter as ctk
from main_frame import MainFrame

class App(ctk.CTk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        self.minsize(geometry[0], geometry[1])
        # This tells to use as much space as possible
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.create_widgets()

        self.mainloop()
        
        
        

    