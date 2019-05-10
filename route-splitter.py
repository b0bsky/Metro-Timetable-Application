# Program: Take data and refine it for easy entry into the database
# Author: Bobbutnotbob (Emile)
# Date: 10/05/2019
# Version: 1.20
import pandas as pd
import requests

# Grab the data from our GitHub repository and store it locally so Panda can read it
bus_stops_file = requests.get('https://raw.githubusercontent.com/b0bsky/Metro-Timetable-Application/map-database/Bus_Stops.csv', allow_redirects=True)
open('bus_stops.csv', 'wb').write(bus_stops_file.content)
data = pd.read_csv('bus_stops.csv', dtype={"Routes":str}, index_col='Road')

# Iterate through every row in the CSV and append each tuple with a "|" character into a list to make it easier to work with
processed_rows = []
for row in data.itertuples():
    routes_column = row[4]
    if "|" in routes_column:
        current_routes = routes_column.split("|")
        print(current_routes)
        for route in current_routes:


