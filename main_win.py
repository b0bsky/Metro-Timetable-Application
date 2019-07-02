'''
    Main Window Program, deals with the frontend of the program
    Developer: Reuben Maddock
'''

# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
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

        # Max number of columns to add
        self.col_total = 0

        # Function to print each row in the table
        def print_row(self, stop, route):

            # Gets id of current route
            route_id_result = connection.execute("select id from route where name = ?", [route])
            route_id = (route_id_result.fetchall())[0][0]

            # Gets name of current route
            self.route_name_result = connection.execute("select name from route where id = ?", [route_id])
            self.route_name = (self.route_name_result.fetchall())[0][0]

            # Gets stop name of current stop
            self.stop_name_result = connection.execute("select name from stop where id = ?", [stop + 1])
            self.stop_name = self.stop_name_result.fetchall()[0][0]

            # Gets id of current stop and puts all stops for a route in a list
            self.stop_id_result = connection.execute("select id from stop where name = ?", [self.stop_name])
            self.stop_id = (self.stop_id_result.fetchall())[0][0]

            # Gets all times for each stop and puts it in a list
            self.times_result = connection.execute("select stop_time from route_stop where route_id = ? and stop_id = ? and stop_day = ?", [route_id, self.stop_id, current_days])
            self.times = (self.times_result.fetchall())

            if len(self.times) > self.col_total:
                self.col_total = len(self.times)


            # If there aren't any stops in this route, then empty table
            if self.col_total is not 0:

                # Inserts column for each stop and sets rows
                self.route_search_table.setColumnCount(self.col_total + 1)
                self.route_search_table.setRowCount(stop + 1)


                # Set first column in table to name of stop if stop in route
                self.route_search_table.setItem(stop, 0, QtWidgets.QTableWidgetItem(self.stop_name))

                # Makes table uneditable
                self.route_search_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

                # Loops through times, adding each time to table
                for time in self.times:

                    index = self.times.index(time)

                    self.route_search_table.setItem(stop, index + 1, QtWidgets.QTableWidgetItem(time[0]))
            else:
                self.route_search_table.setColumnCount(0)
                self.route_search_table.setRowCount(0)

        # Gets length of number of stops in current route
        stops_num_result = connection.execute("select distinct stop_id from route_stop "
                                              "inner join route on route_stop.route_id = route.id "
                                              "inner join stop on route_stop.stop_id = stop.id "
                                              "where route_stop.route_id = route.id "
                                              "and route_stop.stop_id = stop.id" )

        stops_num = stops_num_result.fetchall()

        # Loops through each stop displaying all times
        for stop in range(len(stops_num)):

            print_row(self, stop, current_route)

    # Deals with all the UI and window settings
    def setup_ui(self, MainWindow):

        # Sets up the main windows settings such as title etc...
        MainWindow.setObjectName("RETRO TRANSPORT")
        MainWindow.setFixedSize(1400, 810)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowTitle("MainWindow")

        # Sets the window widget as the programs main object
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # App title function, deals with drawing the app title bar
        def app_title():

            # All title frame settings, colours, position etc...
            title_frame = QtWidgets.QFrame(self.centralwidget)
            title_frame.setGeometry(QtCore.QRect(0, 0, 1400, 111))
            title_frame.setStyleSheet("background-color: rgb(146, 0, 117)")
            title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            title_frame.setObjectName("title_frame")

            # All title label settings
            title_label = QtWidgets.QLabel(title_frame)
            title_label.setGeometry(QtCore.QRect(540, 40, 331, 31))
            title_label.setText("RETRO TRANSPORT")
            font = QtGui.QFont()
            font.setPointSize(24)
            font.setBold(True)
            font.setWeight(75)
            title_label.setFont(font)
            title_label.setStyleSheet("color: rgb(255,255,255); font: bold")
            title_label.setObjectName("title_label")

        # Route search frame
        def route_search():

            # Route search frame settings
            route_search_frame = QtWidgets.QFrame(self.centralwidget)
            route_search_frame.setGeometry(QtCore.QRect(0, 111, 411, 441))
            route_search_frame.setStyleSheet("background-color: rgb(38, 20, 71)")
            route_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            route_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            route_search_frame.setObjectName("route_search_frame")

            # Route search title settings
            route_search_title = QtWidgets.QFrame(route_search_frame)
            route_search_title.setGeometry(QtCore.QRect(0, 0, 411, 41))
            route_search_title.setStyleSheet("background-color: rgb(45,226, 230)")
            route_search_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
            route_search_title.setFrameShadow(QtWidgets.QFrame.Raised)
            route_search_title.setObjectName("route_search_title")

            # Route search text display settings
            route_search_label = QtWidgets.QLabel(route_search_title)
            route_search_label.setGeometry(QtCore.QRect(120, 10, 181, 21))
            route_search_label.setText("ROUTE SEARCH")

            # Route search text, font and display settings
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)

            # Route search text continued
            route_search_label.setFont(font)
            route_search_label.setStyleSheet("color: rgb(255,255,255); font: bold")
            route_search_label.setObjectName("route_search_label")

            # Route selection text display settings
            route_selection_label = QtWidgets.QLabel(route_search_frame)
            route_selection_label.setGeometry(QtCore.QRect(20, 90, 71, 21))
            route_selection_label.setText("ROUTE:")
            route_selection_label.setStyleSheet("font: 12pt; color: rgb(255,255, 255)")
            route_selection_label.setObjectName("route_selection_label")

            # Route selection combobox display settings
            self.route_selection_combobox = QtWidgets.QComboBox(route_search_frame)
            self.route_selection_combobox.setGeometry(QtCore.QRect(90, 90, 111, 22))
            self.route_selection_combobox.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.route_selection_combobox.setObjectName("route_selection_combobox")

            # Route search table display settings
            self.route_search_table = QtWidgets.QTableWidget(route_search_frame)
            self.route_search_table.setGeometry(QtCore.QRect(20, 180, 371, 230))
            self.route_search_table.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.route_search_table.setObjectName("route_search_table")
            self.route_search_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.route_search_table.setColumnCount(0)
            self.route_search_table.setRowCount(0)

            # Setting up the vertical and horizontal scroll bar for the route search table
            self.route_search_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.route_search_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
            self.route_search_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

            # Stretch horizontal header so that all text is in view and not cut out
            horizontal_header = self.route_search_table.horizontalHeader()
            vertical_header = self.route_search_table.verticalHeader()
            vertical_header.setVisible(False)
            horizontal_header.setVisible(False)
            horizontal_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

            # Route search enter button display settings
            search_button = QtWidgets.QPushButton(route_search_frame)
            search_button.setGeometry(QtCore.QRect(160, 140, 75, 23))
            search_button.setText("SEARCH")
            search_button.setStyleSheet("background-color: rgb(255, 108, 17)")
            search_button.setObjectName("search_button")

            # Display table when clicked
            search_button.clicked.connect(self.load_data)

            # Select day label
            day_selection_label = QtWidgets.QLabel(route_search_frame)
            day_selection_label.setGeometry(QtCore.QRect(220, 90, 71, 21))
            day_selection_label.setText("DAY:")
            day_selection_label.setStyleSheet("font: 12pt; color: rgb(255,255, 255)")
            day_selection_label.setObjectName("day_selection_label")

            # Combobox to select what day user wants to travel on
            self.day_selection_combobox = QtWidgets.QComboBox(route_search_frame)
            self.day_selection_combobox.setGeometry(QtCore.QRect(280, 90, 101, 22))
            self.day_selection_combobox.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.day_selection_combobox.setObjectName("day_selection_combobox")

            # Displays route search label
            route_search_label.setFont(font)
            route_search_label.setStyleSheet("color: rgb(255,255,255); font: bold")
            route_search_label.setObjectName("route_search_label")

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
        def route_query():
            # Creates and sets settings for the frame of the route queries
            route_query_frame = QtWidgets.QFrame(self.centralwidget)
            route_query_frame.setGeometry(QtCore.QRect(0, 545, 411, 471))
            route_query_frame.setStyleSheet("background-color: rgb(38, 20, 71)")
            route_query_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            route_query_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            route_query_frame.setObjectName("route_query_frame")

            # Sets settings for the route query title
            route_query_title = QtWidgets.QFrame(route_query_frame)
            route_query_title.setGeometry(QtCore.QRect(0, 10, 431, 41))
            route_query_title.setStyleSheet("background-color: rgb(45,226, 230)")
            route_query_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
            route_query_title.setFrameShadow(QtWidgets.QFrame.Raised)
            route_query_title.setObjectName("route_query_title")

            # Sets settings for the route query tile label
            route_query_label = QtWidgets.QLabel(route_query_title)
            route_query_label.setGeometry(QtCore.QRect(110, 10, 191, 21))
            route_query_label.setText("ROUTE OPTIONS")

            # Deals with font and labels
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            route_query_label.setFont(font)
            route_query_label.setStyleSheet("color: rgb(255,255,255)")
            route_query_label.setObjectName("route_query_label")

            # Deals with the from location label part of the route options querys
            from_location_label = QtWidgets.QLabel(route_query_frame)
            from_location_label.setGeometry(QtCore.QRect(30, 100, 61, 16))
            from_location_label.setText("FROM:")
            font = QtGui.QFont()
            font.setPointSize(14)
            from_location_label.setFont(font)
            from_location_label.setStyleSheet("color: rgb(255,255,255)")
            from_location_label.setObjectName("from_location_label")

            # --------------- FROM SEARCH AUTOCOMPLETE ---------------- #

            # Opens a connection to the stops database
            location_connection = sqlite3.connect("stop_details.db")
            get_location_query = location_connection.execute("select stop from details")
            location_results = get_location_query.fetchall()

            # Convert all locations to strings
            location_results = [(str(result[0])) for result in location_results]

            # Makes the autocompleter for the from search box
            from_line_completer = QtWidgets.QCompleter(location_results)
            from_line_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

            # Deals with the from locations search box
            from_line_edit = QtWidgets.QLineEdit(route_query_frame)
            from_line_edit.setGeometry(QtCore.QRect(110, 100, 231, 21))
            from_line_edit.setStyleSheet("background-color: rgb(255,255,255)")
            from_line_edit.setObjectName("from_line_edit")
            from_line_edit.setCompleter(from_line_completer)

            # Deals with the to location label part of the route options querys
            to_location_label = QtWidgets.QLabel(route_query_frame)
            to_location_label.setGeometry(QtCore.QRect(50, 150, 51, 21))
            to_location_label.setText("TO:")
            font = QtGui.QFont()
            font.setPointSize(14)
            to_location_label.setFont(font)
            to_location_label.setStyleSheet("color: rgb(255,255,255)")
            to_location_label.setObjectName("to_location_label")

            # --------------- TO SEARCH AUTOCOMPLETE ---------------- #

            # Makes the autocompleter for the to search box
            to_line_completer = QtWidgets.QCompleter(location_results)
            to_line_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

            # Deals with the to locations search box
            to_line_edit = QtWidgets.QLineEdit(route_query_frame)
            to_line_edit.setGeometry(QtCore.QRect(110, 150, 231, 21))
            to_line_edit.setStyleSheet("background-color: rgb(255,255,255)")
            to_line_edit.setObjectName("to_line_edit")
            to_line_edit.setCompleter(to_line_completer)

            # Calculate route button
            calculate_route_button = QtWidgets.QPushButton(route_query_frame)
            calculate_route_button.setGeometry(QtCore.QRect(130, 210, 141, 23))
            calculate_route_button.setText("CALCULATE BEST ROUTE")
            calculate_route_button.setStyleSheet("background-color: rgb(255, 108, 17)")
            calculate_route_button.setObjectName("calculate_route_button")

            # Calculates route once calculate route button is pressed
            def calculate_route():

                # Gets current text from the for and to location line edits
                from_location = from_line_edit.text()
                to_location = to_line_edit.text()

                # Gets all stops and puts them into a list
                locations_query = location_connection.execute("select stop from details")
                old_locations = locations_query.fetchall()
                new_locations = []

                # Takes the coordinates of the selected origin and destination
                origin_location_query = location_connection.execute("SELECT latitude, longitude FROM details WHERE stop = ?", [from_location])
                origin_location = origin_location_query.fetchall()

                destination_location_query = location_connection.execute("SELECT latitude, longitude FROM details WHERE stop = ?", [to_location])
                destination_location = destination_location_query.fetchall()

                for location in old_locations:
                    new_locations.append(location[0])

                # If the users input isn't an actual stop, throw tantrum
                if from_location not in new_locations or to_location not in new_locations:

                    # Tantrum settings
                    error_message = QtWidgets.QMessageBox()
                    error_message.setIcon(QtWidgets.QMessageBox.Critical)
                    error_message.setWindowTitle("SORRY MATE")
                    error_message.setText("IT APPEARS THAT YOU HAVENT FILLED OUT THE CORRECT LOCATIONS PUNK")
                    error_message.setInformativeText("Get it right next time tough guy")

                    # Throw tantrum
                    error_message.exec()



            # Runs when calculate button is clicked
            calculate_route_button.clicked.connect(calculate_route)

        # Function that draws all the border frames around the map api
        def border_frames():

            # Vertical border 1
            vertical_border_frame_1 = QtWidgets.QFrame(self.centralwidget)
            vertical_border_frame_1.setGeometry(QtCore.QRect(410, 110, 51, 701))
            vertical_border_frame_1.setStyleSheet("background-color: rgb(0, 0, 0)")
            vertical_border_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            vertical_border_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            vertical_border_frame_1.setObjectName("vertical_border_frame_1")

            # Horizontal border 1
            horizontal_border_frame_1 = QtWidgets.QFrame(self.centralwidget)
            horizontal_border_frame_1.setGeometry(QtCore.QRect(460, 110, 941, 51))
            horizontal_border_frame_1.setStyleSheet("background-color: rgb(0, 0, 0)")
            horizontal_border_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            horizontal_border_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            horizontal_border_frame_1.setObjectName("horizontal_border_frame_1")

            # Vertical border 2
            vertical_border_frame_2 = QtWidgets.QFrame(self.centralwidget)
            vertical_border_frame_2.setGeometry(QtCore.QRect(1350, 150, 51, 661))
            vertical_border_frame_2.setStyleSheet("background-color: rgb(0, 0, 0)")
            vertical_border_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            vertical_border_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            vertical_border_frame_2.setObjectName("vertical_border_frame_2")

            # Horizontal border 2
            horizontal_border_frame_2 = QtWidgets.QFrame(self.centralwidget)
            horizontal_border_frame_2.setGeometry(QtCore.QRect(410, 760, 941, 51))
            horizontal_border_frame_2.setStyleSheet("background-color: rgb(0, 0, 0)")
            horizontal_border_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            horizontal_border_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            horizontal_border_frame_2.setObjectName("horizontal_border_frame_2")

        # Function that displays the map into the middle of the
        def map():
            # Creates a vertical box layout for the map to attach too
            vbox_layout = QtWidgets.QVBoxLayout()

            # Map Frame setup
            map_frame = QtWidgets.QFrame(self.centralwidget)
            map_frame.setGeometry(QtCore.QRect(460, 152, 900, 620))
            map_frame.setStyleSheet("background-color: rgb(0, 0, 0)")
            map_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            map_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            map_frame.setObjectName("map_frame")

            # ---------------- JAVASCRIPT CODE CONNECTING TO THE MAP API---------------- #

            transport = "TRANSIT"
            origin_lat, origin_lng = "-43.64270682", "172.4676911"
            destination_lat, destination_lng = "-43.51859929", "172.5919908"
            raw_html = f'''
            <!DOCTYPE html>
            <html>
              <head>
                <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                <meta charset="utf-8">
                <title>Travel Modes in Directions</title>
                <style>
                  /* Always set the map height explicitly to define the size of the div
                   * element that contains the map. */
                  #map {{
                    height: 100%;
                  }}
                  /* Optional: Makes the sample page fill the window. */
                  html, body {{
                    height: 100%;
                    margin: 0;
                    padding: 0;
                  }}
                  #floating-panel {{
                    position: absolute;
                    top: 10px;
                    left: 25%;
                    z-index: 5;
                    background-color: #fff;
                    padding: 5px;
                    border: 1px solid #999;
                    text-align: center;
                    font-family: 'Roboto','sans-serif';
                    line-height: 30px;
                    padding-left: 10px;
                  }}
                </style>
              </head>
              <body>
                <div id="map"></div>
                <script>
                  function initMap() {{
                    var directionsDisplay = new google.maps.DirectionsRenderer;
                    var directionsService = new google.maps.DirectionsService;
                    var map = new google.maps.Map(document.getElementById('map'), {{
                      zoom: 14,
                      center: {{lat: -43.53425805, lng: 172.6370746}}
                    }});
                    directionsDisplay.setMap(map);
                    calculateAndDisplayRoute(directionsService, directionsDisplay);
                  }}
                  function calculateAndDisplayRoute(directionsService, directionsDisplay) {{
                    directionsService.route({{
                      origin: {{lat: {origin_lat}, lng: {origin_lng}}},  // Lincoln University.
                      destination: {{lat: {destination_lat}, lng: {destination_lng}}},  // Bus Interchange.
                      // Note that Javascript allows us to access the constant
                      // using square brackets and a string value as its
                      // "property."
                      travelMode: google.maps.TravelMode['{transport}']
                    }}, function(response, status) {{
                      if (status == 'OK') {{
                        directionsDisplay.setDirections(response);
                      }} else {{
                        window.alert('Directions request failed due to ' + status);
                      }}
                    }});
                  }}
                </script>
                <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=REDACTED">
                </script>
              </body>
            </html>
            '''
            # --------------------------- --------------------------- #

            # Creates a QWebengineview widget for the map
            map_view = QWebEngineView()
            map_view.setHtml(raw_html)

            # Adds the map to the layout and sets it into the frame
            vbox_layout.addWidget(map_view)
            map_frame.setLayout(vbox_layout)

        # Menu bar function
        def menu_bar():

            # Draws menu bar
            menubar = QtWidgets.QMenuBar(MainWindow)
            menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
            menubar.setObjectName("menubar")
            MainWindow.setMenuBar(menubar)

        #----------------------- Status bar for menu, might use later -------------------- #
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        #---------------------------------------------------------------------------------- #

        # Runs all of the display functions
        title_bar = app_title()
        route_search_bar = route_search()
        route_query_bar = route_query()
        border_frames = border_frames()
        menu_frame = menu_bar()
        map_frame = map()

# Runs at the beginning of the program, creating the window and doing any preprogram initializations
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setup_ui(MainWindow)
    MainWindow.show()
sys.exit(app.exec_())