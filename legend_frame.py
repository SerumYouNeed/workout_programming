import customtkinter as ctk

class LegendFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.configure(fg_color='transparent')

        self.legend = ctk.CTkLabel(master=self, text_color='white', font=('', 18), text='LEGEND:')
        self.legend_white = ctk.CTkLabel(master=self, text_color='white', font=('', 14), text='White - you have room for few more sets.')
        self.legend_green = ctk.CTkLabel(master=self, text_color='green', font=('', 14), text='Green - between 5 and 15 sets.')
        self.legend_orange = ctk.CTkLabel(master=self, text_color='orange', font=('', 14), text='Orange - you are getting closer to overtrain area.')
        self.legend_red = ctk.CTkLabel(master=self, text_color='red', font=('', 14), text='Red - over 25 sets per muscle.')

    def create_widgets(self):
        self.legend.grid()
        self.legend_white.grid()
        self.legend_green.grid()
        self.legend_orange.grid()
        self.legend_red.grid()