# Program: Take data and refine it for easy entry into the database
# Author: Bobbutnotbob (Emile)
# Date: 03/05/2019
# Version: 1.00
import pandas as pd
import requests

# Grab the data from our GitHub repository and store it locally so Panda can read it
bus_stops_file = requests.get('https://raw.githubusercontent.com/b0bsky/Metro-Timetable-Application/map-database/Bus_Stops.csv', allow_redirects=True)
open('bus_stops.csv', 'wb').write(bus_stops_file.content)
data = pd.read_csv('bus_stops.csv', usecols=['Road', 'Routes'], dtype={"Road":str,"Routes":str})