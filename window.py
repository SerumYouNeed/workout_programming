from tkinter import Tk
from tkinter.font import Font
from tkinter import ttk

class Window:
    def __init__(self):
        self.__root = Tk()
        content = ttk.Frame(self.__root)
        frame = ttk.Frame(content, width=700, height=700)
        content.grid(column=1, row=1)
        frame.grid(column=1, row=1, columnspan=2, rowspan=3)

        gritting_font = Font(family="Helvetica", size=32)
        text_font = Font(family="Helvetica", size=22)

        grittings = ttk.Label(content, text="Welcome in workout creator!")
        grittings.grid(column=1, row=1, columnspan=2)

        frecquency_q = ttk.Label(content, text="Training days:")
        frecquency_q.grid(column=1, row=2)
        frecquency_selector = ttk.Spinbox(content, from_=1, to=6)
        frecquency_selector.grid(column=2, row=2)

        submit_btn = ttk.Button(content, text="Submit")
        submit_btn.grid(column=1, row=3, columnspan=2)

        
   
        self.__root.mainloop()