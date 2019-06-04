'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QStyleFactory, QLabel, QFrame, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Main window class
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setup_main_window()
        self.title_frame()

        self.show()

    # Setup main window options
    def setup_main_window(self):

        # Window settings
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.showMaximized()
        self.setWindowTitle("Test")

    def title_frame(self):
        # Box layout
        hbox = QHBoxLayout(self.central_widget)

        # Title frame
        self.title_frame = QFrame()
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setLineWidth(0.6)

        hbox.addWidget(self.title_frame)

        self.setLayout(hbox)

def main():
    # Initiating program
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Cleanlooks'))
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
