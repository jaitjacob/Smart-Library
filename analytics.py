import sqlite3
#import leather
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

# Connect to SQLite datbase
conn = sqlite3.connect('sensor.db')
cursor = conn.cursor()

# This checks that we can read and print
# the contents from the DB without any issues
# via SQL query
def read_from_db():
        cursor.execute('SELECT * FROM sensor')
        data = cursor.fetchall()
        print(data)
        for row in data:
                print(row)

# This is responsible for the generation and
# plotting of the DB data that is fetched
# via SQL query
def graph_data_1():
        # SQL query to gather DB data
        cursor.execute('SELECT * FROM sensor')
        data = cursor.fetchall()

        # Get current size
        fig_size = plt.rcParams["figure.figsize"]

        # Set figure width to 9 and height to 15
        fig_size[0] = 12
        fig_size[1] = 9

        # Set font for x-axis and y-axis values
        font = {'family' : 'normal',
                'size' : 10}

        matplotlib.rc('font', **font)
		plt.rcParams["figure.figsize"] = fig_size

        # Intialize x and y variables for the graph
        x = []
        y = []

        # Append timestamps to x-axis, and append
        # temperatures to y-axis
        for row in data:
                x.append(row[0])
                y.append(row[1])

        # Generate and plot the data as a Scatter
        # plot
        fig = plt.figure()
        plt.xlabel('Timestamps')
        plt.ylabel('Temperature')
        plt.title('Scatter plot - Temperature data')
        plt.clf()
        plt.scatter(x,y)
        plt.plot(x,y)
        plt.draw()
		plt.show()
        print ("Graph generated!")
        fig.autofmt_xdate()

        # Save the generated plot as a png file
        fig.savefig('graph1.png')

# Call methods
read_from_db()
graph_data_1()

# Close connections
cursor.close()
conn.close()

