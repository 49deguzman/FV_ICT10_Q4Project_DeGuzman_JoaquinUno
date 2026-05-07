from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
# Sample data for the graph (global values for the graph to remember the inputs)
days_labels = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
data = [0,0,0,0,0]

def update_graph(e):
    # Get the values from the HTML inputs
    day_input = int(document.getElementById('days').value)
    absence_input = int(document.getElementById('absences').value)

    # Update the data for the graph
    data[day_input] = absence_input
    # Clear the previous graph
    document.getElementById('output').innerHTML = " "
    # Create a new graph with the updated data
    fig, ax = plt.subplots()
    ax.plot(days_labels, data, marker='o')
    ax.set_title("Student Absences")
    ax.set_xlabel('Days')
    ax.set_ylabel('Number of Absences')
    # Display the graph in the output div
    display(fig, target = 'output')