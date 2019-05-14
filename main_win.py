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

class Query(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.query_widgets()

    def query_widgets(self):

        # Updating the listbox with all options
        self.users_search = StringVar()
        self.users_search.trace("w", self.updateList)

        # Query bar frame
        self.query_bar_frame = Frame(root, width="500", height="500", bg="dodgerblue3", borderwidth=3, relief="groove")
        self.query_bar_frame.grid(row=3, column=0, sticky="nw")

        # Trip options label
        self.trip_options_label = Label(root, text="TRIP OPTIONS:", fg="black", bg="dodgerblue3", font=("verdana", 17))
        self.trip_options_label.grid(row=3, column=0, sticky="nw", padx=150, pady=25)

        # From query
        self.from_label = Label(root, text="FROM: ", fg="black", bg="dodgerblue3", font=("verdana 12 bold"))
        self.from_label.place(x=35, y=630)

        self.from_query = Entry(root, textvariable = self.users_search)
        self.from_query.place(x = 100, y = 632)

        self.from_query.bind("<Key>", self.updateList)
        self.from_query.bind("<FocusIn>", self.toggle_visibility)
        self.from_query.bind("<FocusOut>", self.toggle_visibility)


    def updateList(self, *args):

        search_term = self.users_search.get()

        self.from_listbox = Listbox(root)
        self.from_listbox.place(x=100, y=652)
        self.from_listbox.pi = self.from_listbox.place_info()

        self.from_listbox.config(highlightbackground="red")

        test_lbox = ['Adam', 'Lucy', 'Barry', 'Bob', 'James', 'Frank', 'Susan', 'Amanda', 'Christie']

        self.from_listbox.delete(0, END)

        for item in test_lbox:
            if search_term.lower() in item.lower():
                self.from_listbox.insert(END, item)

    def toggle_visibility(self):
        if self.from_query.visible:
            self.from_listbox.place_forget()
        else:
            self.from_listbox.place(self.from_listbox.pi)

Query(master = root)


# Main window loop
root.mainloop()