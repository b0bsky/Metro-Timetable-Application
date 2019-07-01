# Program: Take data and put it into the details datavse
# Author: Bobbutnotbob and b0bsky(Reuben)
# Date: 1/07/2019
# Version: 1.30

import csv
import sqlite3

# Grab the data from the csv
reader = csv.reader(open('stop_details.csv', 'r'))

# Create array for all columns
latitudes = []
longitudes = []
plat_nums = []
names = []

# Connect to sql
connection = sqlite3.connect("stop_details.db")
cursor = connection.cursor()

# Creates the details query or
create_table_query = ('''CREATE TABLE IF NOT EXISTS details (
               id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
               latitude DOUBLE,
               longitude DOUBLE,
               platform_number CHAR (5),
               stop VARCHAR (64))''')

cursor.execute(create_table_query)

# Loop throw all rows removing the titles and adding the records in each corresponding row to their lists
for row in reader:

    if 'ï»¿Latitude' not in row:
        latitudes.append(float(row[0]))
    if 'Longitude' not in row:
        longitudes.append(float(row[1]))
    if 'Platform Num' not in row:
        plat_nums.append(row[2])
    if 'Road' not in row:
        names.append(row[3])

# Fills database
for i in range(len(latitudes)):
    cursor.execute("INSERT INTO details (id, latitude, longitude, platform_number, stop) VALUES (?, ?, ?, ?, ?)", (i + 1, latitudes[i], longitudes[i], plat_nums[i], names[i]))
    connection.commit()

# Closes connection with database
connection.close()

