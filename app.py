import customtkinter as ctk
from main_frame import MainFrame
from data.sqlite import SQLHandler

class App(ctk.CTk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        self.minsize(geometry[0], geometry[1])
        # This tells to use as much space as possible
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._frame = None
        self.resizable(width=True, height=True)

        self.sql_handler = SQLHandler()

        self.switch_frame(MainFrame)

        self.mainloop()

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)
        self._frame.create_widgets(self)