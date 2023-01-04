"""
Lesson 4

Window Types
Exercise 1

Create a 1-shot window that displays your name as Text and an OK button
Instructions

    Create a layout with 2 rows
        Row 1 - Text element that has your name
        Row 2 - Button element with text "Ok"
    Create a Window
    Read the window storing the return value in 2 variables event, values
    Close the window immediately after the read

import PySimpleGUI as sg

# Finish the layout
layout = [[sg.Text('')],
          [sg.Button('')]]

# Create the window
window = sg.Window('Title',)

# Add the call to read the window
event, values =

# close window
"""
import PySimpleGUI as sg

# Finish the layout
layout = [[sg.Text('Julien')],
          [sg.Button('Ok')]]

# Create the window
window = sg.Window('Title', layout)

# Add the call to read the window
event, values = window.read()

# close window
window.close()