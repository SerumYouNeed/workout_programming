from tkinter import *
from window import Window
import sqlite3
from data.sqlite import *

def main():

    win = Window("700x700", "Program your workout")

    add_muscle("chest", sqlite.connection)

    

    

main()