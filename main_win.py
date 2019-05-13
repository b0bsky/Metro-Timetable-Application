'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label, Entry, Listbox, StringVar, END

# Creating main window and setting window options
root = Tk(className=" Metro Application")
root.state("zoomed")

# -------- METRO TITLE --------- #
# Metro title frame
title_frame = Frame(root, height = "100", width = "1920", bg = "dark orchid")
title_frame.grid(row = 0, columnspan = 8)

# Metro title text
title_text = Label(root, text = "RETRO TRANSPORT", fg = "maroon3", bg = "dark orchid", font = ("fixedsys", 40))
title_text.grid(row = 0, column = 2)

# ----- SEARCH BAR ------ #

# Search bar frame
search_bar_frame = Frame(root, height = "50", width = "499", borderwidth = 2, relief = "groove")
search_bar_frame.grid(row = 1, column = 0, sticky = "nw")

search_bar_entry = Entry(search_bar_frame)
search_bar_entry.grid(row = 1, column = 0, sticky = "nw")

# ----- RESULTS BAR ----- #

# Results bar frame
results_bar_frame = Frame(root, width = "500", height = "400", borderwidth = 3, relief = "groove")
results_bar_frame.grid(row = 2, column = 0, sticky = "nw")

# ----- QUERY BAR ------- #

# Query bar frame
query_bar_frame = Frame(root, width = "500", height = "500", bg = "dodgerblue3", borderwidth = 3, relief = "groove")
query_bar_frame.grid(row = 3, column = 0, sticky = "nw")

# Trip options label
trip_options_label = Label(root, text = "TRIP OPTIONS:", fg = "black", bg = "dodgerblue3", font = ("verdana", 17))
trip_options_label.grid(row = 3, column = 0, sticky = "nw", padx = 150, pady = 25)

# From query
from_label = Label(root, text = "FROM: ", fg = "black", bg = "dodgerblue3", font = ("verdana 12 bold"))
from_label.place(x = 35, y = 630)

def query_widgets():
    # Updating the listbox with all options
    users_search = StringVar()
    users_search.trace("w", updateList)

    from_query = Entry(root, textvariable = users_search)
    from_query.place(x = 100, y = 630)

    from_query.bind("<Key>", lambda : updateList(users_search))

def updateList(key, users_search):

    from_listbox = Listbox(root)
    from_listbox.place(x=100, y=650)

    search_term = users_search.get()

    lbox_list = ['Adam', 'Lucy', 'Barry', 'Bob',
                 'James', 'Frank', 'Susan', 'Amanda', 'Christie']
    from_listbox.delete(0, END)

    for item in lbox_list:
        if search_term.lower() in item.lower():
            from_listbox.insert(END, item)


# Main window loop
root.mainloop()