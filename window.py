from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, geometry, title):
        self.__root = Tk()
        # geometry in format: "widthxheight"
        self.__root.geometry(geometry)
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, bg="black")
        self.__canvas.pack(fill=BOTH, expand=1)
   
        self.__root.mainloop()