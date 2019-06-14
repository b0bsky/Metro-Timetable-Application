'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

# imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

# Main Window Class
class Window(object):

    # Init function
    def __init__(self):
        super(Window, self).__init__()

        # Runs programs main functions
        self.setup_ui(MainWindow)
        self.load_data()

    # Connects to database
    def load_data(self):

        # Opens a connection to the database
        connection = sqlite3.connect('buses.db')

        # Gets currently selected route and day in comboboxes
        current_route = self.route_selection_combobox.currentText()
        current_days = self.day_selection_combobox.currentText()

        # Gets id of current route
        id_result = connection.execute("select id from route where name = ?", [current_route])
        id = (id_result.fetchall())[0][0]

        # Deals with time part of database
        times_result = connection.execute("select stop_time from route_stop where route_id = ? and stop_day = ?", [id, current_days])
        times = times_result.fetchall()

        stops_result = connection.execute("select name from stop where id = ?", [id])
        stop = stops_result.fetchall()

        # Emptys table to remove old data and if route has no times, empty table else, print it
        self.route_search_table.setColumnCount(0)
        self.route_search_table.setRowCount(0)

        # Sets row and column
        self.route_search_table.setColumnCount(1)
        self.route_search_table.setRowCount(1)

        print(str(stop))

        # Loops through times, printing them into the search table
        for time in times:
            index = times.index(time)
            self.route_search_table.insertColumn(index)

            # add more if there is more columns in the database.
            self.route_search_table.setItem(0, index, QtWidgets.QTableWidgetItem(str(time[0])))
            self.route_search_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.route_search_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(stop[0][0])))
    # Deals with all the UI and window settings
    def setup_ui(self, MainWindow):

        # Sets up the main windows settings such as title etc...
        MainWindow.setObjectName("RETRO TRANSPORT")
        MainWindow.showMaximized()
        MainWindow.setStyleSheet("")

        # Sets the window widget as the programs main object
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # App title function, deals with drawing the app title bar
        def app_title(self):
            # All title frame settings, colours, position etc...
            self.title_frame = QtWidgets.QFrame(self.centralwidget)
            self.title_frame.setGeometry(QtCore.QRect(0, 0, 2101, 151))
            self.title_frame.setStyleSheet("background-color: rgb(146, 0, 117)")
            self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.title_frame.setObjectName("title_frame")

        # Route search frame
        def route_search(self):

            # Route search frame settings
            self.route_search_frame = QtWidgets.QFrame(self.centralwidget)
            self.route_search_frame.setGeometry(QtCore.QRect(0, 150, 411, 421))
            self.route_search_frame.setStyleSheet("background-color: rgb(38, 20, 71)")
            self.route_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.route_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.route_search_frame.setObjectName("route_search_frame")

            # Route search title settings
            self.route_search_title = QtWidgets.QFrame(self.route_search_frame)
            self.route_search_title.setGeometry(QtCore.QRect(0, 0, 411, 41))
            self.route_search_title.setStyleSheet("background-color: rgb(45,226, 230)")
            self.route_search_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.route_search_title.setFrameShadow(QtWidgets.QFrame.Raised)
            self.route_search_title.setObjectName("route_search_title")

            # Route search text display settings
            self.route_search_label = QtWidgets.QLabel(self.route_search_title)
            self.route_search_label.setGeometry(QtCore.QRect(120, 10, 181, 21))

            # Route search text, font and display settings
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)

            # Route search text continued
            self.route_search_label.setFont(font)
            self.route_search_label.setStyleSheet("color: rgb(255,255,255); font: bold")
            self.route_search_label.setObjectName("route_search_label")

            # Route selection text display settings
            self.route_selection_label = QtWidgets.QLabel(self.route_search_frame)
            self.route_selection_label.setGeometry(QtCore.QRect(20, 90, 71, 21))
            self.route_selection_label.setStyleSheet("font: 12pt; color: rgb(255,255, 255)")
            self.route_selection_label.setObjectName("route_selection_label")

            # Route selection combobox display settings
            self.route_selection_combobox = QtWidgets.QComboBox(self.route_search_frame)
            self.route_selection_combobox.setGeometry(QtCore.QRect(90, 90, 111, 22))
            self.route_selection_combobox.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.route_selection_combobox.setObjectName("route_selection_combobox")

            # Route search table display settings
            self.route_search_table = QtWidgets.QTableWidget(self.route_search_frame)
            self.route_search_table.setGeometry(QtCore.QRect(20, 180, 371, 251))
            self.route_search_table.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.route_search_table.setObjectName("route_search_table")
            self.route_search_table.horizontalHeader().setVisible(False)
            self.route_search_table.verticalHeader().setVisible(False)
            self.route_search_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)


            # Route search enter button display settings
            self.search_button = QtWidgets.QPushButton(self.route_search_frame)
            self.search_button.setGeometry(QtCore.QRect(160, 140, 75, 23))
            self.search_button.setStyleSheet("background-color: rgb(255, 108, 17)")
            self.search_button.setObjectName("search_button")

            # Display table when clicked
            self.search_button.clicked.connect(self.load_data)

            # Select day label
            self.day_selection_label = QtWidgets.QLabel(self.route_search_frame)
            self.day_selection_label.setGeometry(QtCore.QRect(220, 90, 71, 21))
            self.day_selection_label.setStyleSheet("font: 12pt; color: rgb(255,255, 255)")
            self.day_selection_label.setObjectName("day_selection_label")

            # Combobox to select what day user wants to travel on
            self.day_selection_combobox = QtWidgets.QComboBox(self.route_search_frame)
            self.day_selection_combobox.setGeometry(QtCore.QRect(280, 90, 101, 22))
            self.day_selection_combobox.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.day_selection_combobox.setObjectName("day_selection_combobox")

            # Displays route search label
            self.route_search_label.setFont(font)
            self.route_search_label.setStyleSheet("color: rgb(255,255,255); font: bold")
            self.route_search_label.setObjectName("route_search_label")

            # Opens a connection to the database as to load in routes into combobox
            connection = sqlite3.connect('buses.db')

            # Deals with routes part of database in routes combobox
            get_routes_query = "select name from route"
            routes_result = connection.execute(get_routes_query)
            routes = routes_result.fetchall()

            # Deals with stop days part of database in days combobox
            get_day_query = "select days from day"
            days_result = connection.execute(get_day_query)
            days = days_result.fetchall()

            # updates routes combobox with all routes
            for route in routes:
                self.route_selection_combobox.addItem(route[0])

            # updates days combobox with all days
            for day in days:
                self.day_selection_combobox.addItem(day[0])

        # Route query frame
        def route_query(self):
            # Creates and sets settings for the frame of the route queries
            self.route_query_frame = QtWidgets.QFrame(self.centralwidget)
            self.route_query_frame.setGeometry(QtCore.QRect(0, 560, 411, 471))
            self.route_query_frame.setStyleSheet("background-color: rgb(38, 20, 71)")
            self.route_query_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.route_query_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.route_query_frame.setObjectName("route_query_frame")

            # Sets settings for the route query title
            self.route_query_title = QtWidgets.QFrame(self.route_query_frame)
            self.route_query_title.setGeometry(QtCore.QRect(0, 60, 411, 41))
            self.route_query_title.setStyleSheet("background-color: rgb(45,226, 230)")
            self.route_query_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.route_query_title.setFrameShadow(QtWidgets.QFrame.Raised)
            self.route_query_title.setObjectName("route_query_title")
            self.route_query_label = QtWidgets.QLabel(self.route_query_title)
            self.route_query_label.setGeometry(QtCore.QRect(110, 10, 191, 21))

            # Deals with font and labels
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.route_query_label.setFont(font)
            self.route_query_label.setStyleSheet("color: rgb(255,255,255)")
            self.route_query_label.setObjectName("route_query_label")

        # Function that draws all the border frames around the map api
        def border_frames(self):

            # Vertical border 1
            self.horizontal_border_frame_1 = QtWidgets.QFrame(self.centralwidget)
            self.horizontal_border_frame_1.setGeometry(QtCore.QRect(410, 150, 51, 881))
            self.horizontal_border_frame_1.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.horizontal_border_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.horizontal_border_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.horizontal_border_frame_1.setObjectName("horizontal_border_frame_1")

            # Horizontal border 1
            self.vertical_border_frame_1 = QtWidgets.QFrame(self.centralwidget)
            self.vertical_border_frame_1.setGeometry(QtCore.QRect(460, 150, 1461, 51))
            self.vertical_border_frame_1.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.vertical_border_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.vertical_border_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.vertical_border_frame_1.setObjectName("vertical_border_frame_1")

            # Vertical border 2
            self.vertical_border_frame_2 = QtWidgets.QFrame(self.centralwidget)
            self.vertical_border_frame_2.setGeometry(QtCore.QRect(1870, 200, 51, 781))
            self.vertical_border_frame_2.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.vertical_border_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.vertical_border_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.vertical_border_frame_2.setObjectName("vertical_border_frame_2")

            # Horizontal border 2
            self.horizontal_border_frame_2 = QtWidgets.QFrame(self.centralwidget)
            self.horizontal_border_frame_2.setGeometry(QtCore.QRect(460, 980, 1461, 51))
            self.horizontal_border_frame_2.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.horizontal_border_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.horizontal_border_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.horizontal_border_frame_2.setObjectName("horizontal_border_frame_2")

        # Menu bar function
        def menu_bar(self):

            # Draws menu bar
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)

        #----------------------- Status bar for menu, might use later -------------------- #
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        #---------------------------------------------------------------------------------- #

        # Runs all of the display functions
        title_bar = app_title(self)
        route_search_bar = route_search(self)
        route_query_bar = route_query(self)
        border_frames = border_frames(self)
        menu_frame = menu_bar(self)

        # Deals with any text in the programs and deals with multilanguage switching from C++ to Python when coding
        def retranslateUi(MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.route_search_label.setText(_translate("MainWindow", "ROUTE SEARCH"))
            self.route_selection_label.setText(_translate("MainWindow", "ROUTE:"))
            self.day_selection_label.setText(_translate("MainWindow", "DAY:"))
            self.search_button.setText(_translate("MainWindow", "SEARCH"))
            self.route_query_label.setText(_translate("MainWindow", "ROUTE OPTIONS"))

        retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Runs at the beginning of the program, creating the window and doing any preprogram initializations
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
