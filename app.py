import customtkinter as ctk

from main_frame import MainFrame


class App(ctk.CTk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.minsize(geometry[0], geometry[1])
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._frame = None
        self.resizable(width=True, height=True)
        self.number_of_training_days = None

        self.switch_frame(MainFrame)

        self.mainloop()

        ctk.set_appearance_mode("dark")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(sticky="NSEW")
        self._frame.create_widgets(self)
