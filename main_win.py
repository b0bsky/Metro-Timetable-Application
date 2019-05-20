'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label, Entry, Listbox, StringVar, END, ttk

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

search_bar_style = ttk.Style()
search_bar_style.configure("TEntry", )

search_bar_entry = Entry(search_bar_frame, width = "45", font = ("Helvetica 14"))
search_bar_entry.grid(row = 1, column = 0, sticky = "w")

# ----- RESULTS BAR ----- #

# Results bar frame
results_bar_frame = Frame(root, width = "500", height = "325", borderwidth = 3, relief = "groove")
results_bar_frame.grid(row = 2, column = 0, sticky = "nw")

# ----- QUERY BAR ------- #

# Query class which holds everything in the query frame
class Query(Frame):

    # Initiation function
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.query_widgets()
        self.listbox_is_showing = False

    # Function that controls all query widgets
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
        self.from_label.place(x=35, y=555)
        self.from_query = Entry(root, width = "35", textvariable = self.users_search)
        self.from_query.place(x = 120, y = 557)

        # Dynamically updates the from queries search
        self.from_query.bind("<FocusIn>", self.updateList)

    # Dynamically updates the query frames listboxes
    def updateList(self, *args):

        # Gets users search(live)
        search_term = self.users_search.get()

        # Puts listboxes on screen and makes them disapear if users not using entry
        self.from_listbox = Listbox(root, width = "35")
        self.from_listbox.place(x=120, y=577)
        self.listbox_is_showing = True
        self.from_listbox.pi = self.from_listbox.place_info()
        self.from_listbox.config(highlightbackground="red")
        self.from_query.bind("<FocusOut>", self.toggle_visibility)
        self.from_listbox.bind("<FocusOut>", self.toggle_visibility)

        test_lbox = ['Adam', 'Lucy', 'Barry', 'Bob', 'James', 'Frank', 'Susan', 'Amanda', 'Christie']

        # Removes any past data left on from listbox
        self.from_listbox.delete(0, END)

        # Dynamically prints out listbox items matching users search
        for item in test_lbox:
            if search_term.lower() in item.lower():
                self.from_listbox.insert(END, item)

    # Toggles listboxes visibility on screen
    def toggle_visibility(self, event=None):
        if self.listbox_is_showing and self.from_listbox is not self.from_listbox.focus_get():
            self.from_listbox.place_forget()
            self.listbox_is_showing = False
        else:
            self.from_listbox.place(x=120, y=577)
            self.listbox_is_showing = True

Query(master = root)

# Main window loop
root.mainloop()