"""
Lesson 41

ProgressBar Element
Exercise 1

Make a vertical Progress Bar that shows progress increasing using a button
Instructions:

    Your program will display the value of a counter as it counts up to 20
    Create a layout that has 3 elements
        A vertical Progress Bar that is 20 chars (rows) by 30 pixels. The Maximum value for your Progress Bar should be 20
        A Text Element for showing your counter's value
        A Button with the text "Increment"
    When the Increment button is clicked:
        Increment your counter
        Display the current counter value in your Text Element
        Update the Progress Bar using the counter's value

ProgressBar Element in the Call Reference Documentation

import PySimpleGUI as sg

# Create the layout as described in the exercise
layout = [[]]

window = sg.Window("Progress Bars", layout)

counter = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # add your event processing here

window.close()
"""
import PySimpleGUI as sg

# Create the layout as described in the exercise
layout = [[sg.ProgressBar(20, size_px=(20, 30), orientation='v', k='-PB-')],
          [sg.Text(k='-T1-')],
          [sg.B("Increment", k='-B1-')]
          ]

window = sg.Window("Progress Bars", layout)

counter = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # add your event processing here

    if event == '-B1-':
        counter += 1
        window['-PB-'].update(counter)
        window['-T1-'].update(f'counter = {counter}')

window.close()