import tkinter as tk
from tkinter import ttk

class SubBtn(tk.Button):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.btn = ttk.Button(self.frame, text="Submit")
        self.btn.grid(row=2, column=0, columnspan=2, sticky="n")


        # def submit():
        #     frecquency_a = MainWindow.frecquency_selector.get()
        #     print(f'frequency: {frecquency_a}')
        #     if self.grittings.winfo_viewable():
        #         self.grittings.grid_forget()



    
