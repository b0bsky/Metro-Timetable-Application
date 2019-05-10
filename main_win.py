'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label

# Creating main window and setting window options
root = Tk(className=" Metro Application")
root.state("zoomed")

# -------- METRO TITLE --------- #
# Metro title frame
title_frame = Frame(root, height = "100", width = "1920", bg = "dark orchid")
title_frame.grid(row = 0, columnspan = 8)

# Metro title text
title_text = Label(root, text = "RETRO TRANSPORT", fg = "maroon3", bg = "dark orchid", font = ("arial", 40))
title_text.place(x = 500, y = 20)

# ----- SEARCH BAR ------ #

# Search bar frame
search_bar_frame = Frame(root, height = "50", width = "499", borderwidth = 2, relief = "groove")
search_bar_frame.grid(row = 1, column = 0, sticky = "nw")

# ----- RESULTS BAR ----- #

# Results bar frame
results_bar_frame = Frame(root, width = "500", height = "300", borderwidth = 3, relief = "groove")
results_bar_frame.grid(row = 2, column = 0, sticky = "nw")

# ----- QUERY BAR ------- #

# Query bar frame
query_bar_frame = Frame(root, width = "500", height = "390", borderwidth = 3, relief = "groove")
query_bar_frame.grid(row = 3, column = 0, sticky = "nw")

# Main window loop
root.mainloop()
