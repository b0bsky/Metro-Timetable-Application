'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QStyleFactory, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.showMaximized()
        self.setWindowTitle("Test")

    def titleFrame(self):

        self.title_label = QLabel(self)
        self.title_label.setText("RETRO TRANSPORT")
        self.title_label.setAlignment()

app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create('Cleanlooks'))
GUI = Window()
sys.exit(app.exec_())
