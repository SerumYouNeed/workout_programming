import customtkinter as ctk

class ProgrammingFrame1(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")

    # create widgets
    def create_widgets(self, parent):
        # packed frame with mini frames: exercises selector frames, set selector frames        
        day_frame = ctk.CTkFrame(self, fg_color="black")
        day_frame.pack(expand=True, fill="both")

        # frame with day label
        day_label_frame = ctk.CTkFrame(day_frame, fg_color="black")
        day_label_frame.pack(expand=True, fill="both")
        day_lbl = ctk.CTkLabel(master=day_label_frame, text="Day 1",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 27))

        # frame with exercises and set labels
        etq_frame = ctk.CTkFrame(day_frame, fg_color="black")
        etq_frame.pack(expand=True, fill="both")
        ex_lbl = ctk.CTkLabel(master=etq_frame, text="Exercise",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        st_lbl = ctk.CTkLabel(master=etq_frame, text="Sets",
                              fg_color="black",
                              text_color="white",
                              font=("Helvatica", 22))
        
        choice_frame_ex = ctk.CTkFrame(day_frame, fg_color="black")
        choice_frame_ex.pack(side="left", expand=True, fill="both")
        choice_frame_set = ctk.CTkFrame(day_frame, fg_color="black")
        choice_frame_set.pack(side="right", expand=True, fill="both")

        # place widgets
        day_lbl.pack(expand=True, fill="both")

        ex_lbl.pack(side="left", expand=True, fill="both")
   
        st_lbl.pack(side="left", expand=True, fill="both")
        
        for i in range(7):    
            exercise = ctk.CTkComboBox(master=choice_frame_ex, values=["press", "2", "3", "4", "5", "6"])
            set = ctk.CTkComboBox(master=choice_frame_set, values=["1", "2", "3", "4", "5"])
            exercise.pack()
            set.pack()