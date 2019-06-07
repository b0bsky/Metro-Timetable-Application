'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

# imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Main Window Class
class Window(object):

    # Init function
    def __init__(self):
        super(Window, self).__init__()

        self.setup_ui(MainWindow)

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

            # Route search text
            self.label = QtWidgets.QLabel(self.route_search_title)
            self.label.setGeometry(QtCore.QRect(120, 10, 181, 21))

            # Route search text, font and display settings
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("color: rgb(255,255,255); font: bold")
            self.label.setObjectName("label")

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
            self.label_2 = QtWidgets.QLabel(self.route_query_title)
            self.label_2.setGeometry(QtCore.QRect(110, 10, 191, 21))

            # Deals with font and labels
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color: rgb(255,255,255)")
            self.label_2.setObjectName("label_2")

        # Function that draws all the border frames around the map api
        def border_frames(self):

            # Horizontal border
            self.border_frame_1 = QtWidgets.QFrame(self.centralwidget)
            self.border_frame_1.setGeometry(QtCore.QRect(410, 150, 61, 881))
            self.border_frame_1.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.border_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.border_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.border_frame_1.setObjectName("border_frame_1")

            # Vertical border
            self.border_frame_2 = QtWidgets.QFrame(self.centralwidget)
            self.border_frame_2.setGeometry(QtCore.QRect(470, 150, 1451, 51))
            self.border_frame_2.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.border_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.border_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.border_frame_2.setObjectName("border_frame_2")

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

        title_bar = app_title(self)
        route_search_bar = route_search(self)
        route_query_bar = route_query(self)
        border_frames = border_frames(self)
        menu_frame = menu_bar(self)

        # Deals with any text in the programs and deals with multilanguage switching from C++ to Python when coding
        def retranslateUi(MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "ROUTE SEARCH"))
            self.label_2.setText(_translate("MainWindow", "ROUTE OPTIONS"))

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

