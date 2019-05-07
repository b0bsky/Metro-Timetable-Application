'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label

# Creating main window and setting window options
root = Tk(className=" Metro Application")
root.state("zoomed")

# Metro title
title_frame = Frame(height = "100", width = "1920", bg = "dark orchid")
title_frame.grid(columnspan = 10)

title_text = Label(root, text = "RETRO TRANSPORT", fg = "maroon3", bg = "dark orchid", font = ("arial", 30))
title_text.grid(row = 0, column = 3)

# Main window loop
root.mainloop()
