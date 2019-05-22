'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

from tkinter import Tk, Frame, Label, Entry, Listbox, StringVar, END, ttk
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

# ----- RESULTS BAR ----- #

# Results bar frame
results_bar_frame = Frame(root, width = "500", height = "325", borderwidth = 3, relief = "groove")
results_bar_frame.grid(row = 2, column = 0, sticky = "nw")

# ----- QUERY BAR ------- #

# Query class which holds everything in the query frame
class Query(Frame):

    # Initiation function
    def __init__(self, autocompleteentry, *args, **kwargs):
        Frame.__init__(self)

        self.from_listbox_is_showing = False

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

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']

    # Dynamically updates the query frames listboxes
    def updateList(self, *args):

        # Gets users search when there is text in listbox
        if self.users_search.get() == '':
            if self.from_listbox_is_showing:
                self.from_listbox.destroy()
                self.from_listbox_is_showing = False
        else:
            word_matched = self.search_compare()

            if word_matched:
                if not self.from_listbox_is_showing:

                    # Puts listboxes on screen
                    self.from_listbox = Listbox(root, width = "35")
                    self.from_listbox.place(x=120, y=577)
                    self.from_listbox_is_showing = True
                    self.from_listbox.pi = self.from_listbox.place_info()
                    self.from_listbox.config(highlightbackground="red")
                    self.from_listbox_is_showing = True

                    # Search suggestion navigation
                    self.from_listbox.bind("<Return>", lambda from_listbox: self.selection(self.from_listbox, self.from_query))
                    self.from_listbox.bind("<<ListboxSelect>>", lambda from_listbox: self.selection(self.from_listbox, self.from_query))

                    # Toggles listboxes visibility when entry isn't being used
                    self.from_query.bind("<FocusOut>", self.toggle_visibility)

                # Removes any past data left on from listbox
                self.from_listbox.delete(0, END)

                # Dynamically prints out listbox items matching users search
                for item in word_matched:
                    if self.users_search.get().lower() in item.lower():
                        self.from_listbox.insert(END, item)
            else:
                if self.from_listbox_is_showing:
                    self.from_listbox.destroy()
                    self.from_listbox_is_showing = False

    # Compares users search to search terms in database
    def search_compare(self):

        # Compares users search with every item in list
        return [w for w in search_queries if matches(self.users_search.get(), w)]

    # Toggles listboxes visibility on screen
    def toggle_visibility(self, event=None):

        if self.from_listbox_is_showing and self.from_listbox is not self.from_listbox.focus_get():
            self.from_listbox.destroy()
            self.from_listbox_is_showing = False

    # Deals with the selection of search suggestions
    def selection(self, listbox, entry):
        if self.from_listbox_is_showing:
            self.users_search.set(listbox.get(listbox.curselection()))
            listbox.destroy()
            self.from_listbox_is_showing = False
            entry.icursor(END)

if __name__ == "__main__":

    # Possible search queries
    search_queries = ['Adam', 'Lucy', 'Barry', 'Bob', 'James', 'Frank', 'Susan', 'Amanda', 'Christie']

    # Uses regular expressions to test for a match
    def matches(row_value, ac_list_entry):
        pattern = re.compile(re.escape(row_value) + '.*', re.IGNORECASE)
        return re.match(pattern, ac_list_entry)


Query(search_queries, root, matchesFunction = matches)

# Main window loop
root.mainloop()