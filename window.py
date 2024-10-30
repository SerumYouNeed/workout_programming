import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Workout creator')
        self.geometry('700x700')
        # This tells to use as much space as possible
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Styles
        style = ttk.Style()
        style.configure("MainFrame.TFrame", background="black")
                
        # Create widgets        
        frame_main = ttk.Frame(self, style="MainFrame.TFrame")

        # Put widgets on the screen
        # Sticky pin frame to east, west, north, south 
        frame_main.grid(column=0, row=0, sticky="ewns")
    
        # grittings = ttk.Label(frame_main, text="Welcome in workout creator!")
        # grittings.grid(column=1, row=1, columnspan=2)

        # def submit():
        #     frecquency_a = frecquency_selector.get()
        #     print(f'frequency: {frecquency_a}')
        #     if self.grittings.winfo_viewable():
        #         self.grittings.grid_forget()


        # frecquency_q = ttk.Label(content, text="Training days:")
        # frecquency_q.grid(column=1, row=2)
        # frecquency_selector = ttk.Spinbox(from_=1, to=6)
        # frecquency_selector.grid(column=2, row=2)

        # submit_btn = ttk.Button(content, text="Submit", command=submit)
        # submit_btn.grid(column=1, row=3, columnspan=2)

    