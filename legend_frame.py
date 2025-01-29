import customtkinter as ctk

class LegendFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.configure(fg_color="black")

        self.legend_white = ctk.CTkLabel(master=self, text_color="white", font=("Helvatica", 18), text="White color means that you have room for few more sets.")
        self.legend_green = ctk.CTkLabel(master=self, text_color="green", font=("Helvatica", 18), text="Between 5 - 15 sets. This is where you want to be.")
        self.legend_orange = ctk.CTkLabel(master=self, text_color="orange", font=("Helvatica", 18), text="You are getting closer to overtrain area.")
        self.legend_red = ctk.CTkLabel(master=self, text_color="red", font=("Helvatica", 18), text="You should stay alert. Over 25 sets per muscle. Better evaluate what are you doing.")
        
        self.legend_white.grid(column=1)
        self.legend_green.grid(column=1)
        self.legend_orange.grid(column=1)
        self.legend_red.grid(column=1)