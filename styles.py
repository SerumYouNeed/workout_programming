import tkinter as tk
from tkinter import ttk

style = ttk.Style()
style.configure("MainFrame.TFrame", background="black")
style.configure("Grittings.TLabel", background="black", foreground="white", font=("Helvatica, 22"), padding="5mm")
style.configure("Frequency.TLabel", background="black", foreground="white", font=("Helvatica, 18"), padding="5mm")
style.configure("DayNr.TLabel", background="black", foreground="white", font=("Helvatica, 15"), padding="5mm")