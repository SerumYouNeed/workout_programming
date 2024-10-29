from tkinter import Tk, BOTH, Canvas, Label, Spinbox

class Window:
    def __init__(self, geometry, title):
        self.__root = Tk()
        # geometry in format: "widthxheight"
        self.__root.geometry(geometry)
        self.__root.title(title)

        # self.__canvas = Canvas(self.__root, bg="black")
        # self.__canvas.pack(fill=BOTH, expand=1)

        grittings = Label(self.__root, background="black", foreground="white", height=3, text="Welcome in workout creator!")
        grittings.pack()

        frecquency_selector = Spinbox(self.__root, from_=1, to=6)
        frecquency_selector.pack()

        
   
        self.__root.mainloop()