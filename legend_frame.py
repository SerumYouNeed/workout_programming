import customtkinter as ctk

class LegendFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.configure(fg_color="red")

        self.legend_white = ctk.CTkLabel(master=self, text_color="white", font=("Helvatica", 18), text="White color means that you have room for few more sets.")
        self.legend_green = ctk.CTkLabel(master=self, text_color="green", font=("Helvatica", 18), text="Between 5 - 15 sets. This is where you want to be.")
        self.legend_orange = ctk.CTkLabel(master=self, text_color="orange", font=("Helvatica", 18), text="You are getting closer to overtrain area.")
        self.legend_red = ctk.CTkLabel(master=self, text_color="red", font=("Helvatica", 18), text="You should stay alert. Over 25 sets per muscle.")

    def create_widgets(self):
        self.legend_white.grid()
        self.legend_green.grid()
        self.legend_orange.grid()
        self.legend_red.grid()