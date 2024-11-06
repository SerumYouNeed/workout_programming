import customtkinter as ctk
from programming_frame import ProgrammingFrame

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid(row=0, column=0, sticky="ewns")

    def create_widgets(self, parent):
        # create the grid
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)

        # create widgets
        self.next_frame = ProgrammingFrame(self)
        grittings = ctk.CTkLabel(self, 
                                 text="Welcome in workout creator!",
                                 fg_color="black",
                                 text_color="white",
                                 font=("Helvatica", 27))
        frecquency_q = ctk.CTkLabel(self, 
                                    text="Training days:",
                                    fg_color="black",
                                    text_color="white",
                                    font=("Helvatica", 22))
        
        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            parent.switch_frame(ProgrammingFrame)

        frecquency_selector = ctk.CTkComboBox(self, 
                                              values=["1", "2", "3", "4", "5", "6" , "7"], 
                                              command=combobox_callback)

        # place widgets
        # Sticky pin frame to east, west, north, south 
        grittings.grid(row=0, column=0, columnspan=2)
        frecquency_q.grid(row=1, column=0, sticky="e")
        frecquency_selector.grid(row=1, column=1, sticky="w")



# combobox_var = ctk.StringVar(value="2")
# combobox_var.set("2")


        
