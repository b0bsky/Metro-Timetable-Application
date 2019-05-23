'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label, Entry, Listbox, StringVar, END, ttk, ACTIVE
import re

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

# Query bar frame
query_bar_frame = Frame(root, width="500", height="500", bg="dodgerblue3", borderwidth=3, relief="groove")
query_bar_frame.grid(row=3, column=0, sticky="nw")

# Trip options label
trip_options_label = Label(root, text="TRIP OPTIONS:", fg="black", bg="dodgerblue3", font=("verdana", 17))
trip_options_label.grid(row=3, column=0, sticky="nw", padx=150, pady=25)

# ----- RESULTS BAR ----- #

# Results bar frame
results_bar_frame = Frame(root, width = "500", height = "325", borderwidth = 3, relief = "groove")
results_bar_frame.grid(row = 2, column = 0, sticky = "nw")

# Listbox visibility variables
from_listbox_is_showing = False
to_listbox_is_showing = False

# From query
from_label = Label(root, text="FROM: ", fg="black", bg="dodgerblue3", font=("verdana 12 bold"))
from_label.place(x=35, y=555)
from_query_search = StringVar()
from_query = Entry(root, width = "35", textvariable = from_query_search)

# To query
to_label = Label(root, text = "TO: ", fg = "black", bg = "dodgerblue3", font = ("verdana 12 bold"))
to_label.place(x=55, y=615)
to_query_search = StringVar()
to_query = Entry(root, width = "35", textvariable = to_query_search)

# ----- QUERY BAR ------- #

# Query class which holds everything in the query frame
class Query(Frame):

    # Initiation function
    def __init__(self, autocompleteentry, listbox_x, listbox_y, query, query_x, query_y, query_search, listbox_is_showing, *args, **kwargs):
        Frame.__init__(self)

        self.query = query
        self.listbox_x = listbox_x
        self.listbox_y = listbox_y
        self.query_x = query_x
        self.query_y = query_y
        self.query_search = query_search
        self.listbox_is_showing = listbox_is_showing

        # Updating the listbox with all options
        self.query_search.trace("w", self.updateList)
        self.query.place(x=self.query_x, y=self.query_y)

        # Dynamically updates queries search
        self.query.bind("<FocusIn>", self.updateList)

        # Custom matches function
        if 'matches_function' in kwargs:
            self.matchesFunction = kwargs['matches_function']
            del kwargs['matches_function']

    # Dynamically updates the query frames listboxes
    def updateList(self, *args):

        # Gets users search when there is text in listbox
        if self.query_search.get() == '':
            if self.listbox_is_showing:
                self.listbox.destroy()
                self.listbox_is_showing = False
        else:
            word_matched = self.search_compare(self.query_search)

            # Dynamic search filtering the from query
            if word_matched:
                if not self.listbox_is_showing:

                    # Puts listboxes on screen
                    self.listbox = Listbox(root, width = "32")
                    self.listbox.place(x=self.listbox_x, y=self.listbox_y)
                    self.listbox_is_showing = True

                    # Search suggestion navigation
                    self.listbox.bind("<Return>", self.selection)
                    self.listbox.bind("<<ListboxSelect>>", self.selection)

                    # Toggles listboxes visibility when entry isn't being used
                    self.query.bind("<FocusOut>", self.toggle_visibility)

                # Removes any past data left on from listbox
                self.listbox.delete(0, END)

                # Dynamically prints out listbox items matching users search
                for item in word_matched:
                    if self.query_search.get().lower() in item.lower():
                        self.listbox.insert(END, item)
            else:
                if self.listbox_is_showing:
                    self.listbox.destroy()
                    self.listbox_is_showing = False


    # Compares users search to search terms in database
    def search_compare(self, query):

        # Compares users search with every item in list
        return [w for w in search_queries if matches(self.query.get(), w)]

    # Toggles listboxes visibility on screen
    def toggle_visibility(self, event=None):

        if self.listbox_is_showing and self.listbox is not self.listbox.focus_get():
            self.listbox.destroy()
            self.listbox_is_showing = False

    # Deals with the selection of search suggestions
    def selection(self, *args):
        if self.listbox_is_showing:
            self.query_search.set(self.listbox.get(self.listbox.curselection()))
            self.listbox.destroy()
            self.listbox_is_showing = False
            self.query.icursor(END)

if __name__ == "__main__":

    # Possible search queries
    search_queries = ['Adam', 'Lucy', 'Barry', 'Bob', 'James', 'Frank', 'Susan', 'Amanda', 'Christie']

    # Uses regular expressions to test for a match
    def matches(row_value, ac_list_entry):
        pattern = re.compile(re.escape(row_value) + '.*', re.IGNORECASE)
        return re.match(pattern, ac_list_entry)

# def __init__(self, autocompleteentry, listbox, listbox_x, listbox_y, query, query_x, query_y, query_search, listbox_is_showing, *args, **kwargs):
 #self.listbox.place(x=120, y=577)
# self.query.place(x = 120, y = 557), query.place(x = 120, y = 617)
# Creating the from and to query instances
from_query_instance = Query(search_queries, 120, 577, from_query, 120, 557, from_query_search, from_listbox_is_showing, matches_function = matches)
to_query_instance = Query(search_queries, 120, 633, to_query, 120, 617, to_query_search, to_listbox_is_showing, matches_function = matches)


# Main window loop
root.mainloop()