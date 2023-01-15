"""
Lesson 26

Spin Element
Exercise 1

Make a Timer GUI
Instructions:

You are making a GUI that will be used as a timer. Use 2 Spin Elements to enable your user to set the hours and minutes. Each should be values 0 to 59. You do not need to handle "rollover" for the minutes to hours.

There are 2 approaches you may take on this exercise:
1. Use Ints for the values 2. Use strings which will enable you to have leading zeros

In other words, a value of 0 hours and 0 minutes can look like this:
0 : 0

Or like this:
00 : 00

    Make a window that has 3 rows
        Row 1 should read "Timer GUI"
        Row 2 will have your Spin Elements
        Row 3 should have 2 buttons - "Set" and "Clear"
    Button Operation
        Set - Prints the values of the Spin elements in the Debug Window
        Clear - Resets the value to 0 hours 0 minutes
    Set the font for the entire Window to be "Courier" with a size of 40 so that it is easy to see and interact with.

Spin Element in the Call Reference Documentation

import PySimpleGUI as sg

layout = [  [sg.Text('Timer GUI')],
            # Insert your Spin code her
            [sg.Button(), sg.Button()]]   # and complete the reset of the layout

window = sg.Window('Window Title')    # Add your layout and set the font

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Add your code to handle events for buttons

window.close()

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
# sg.sdk_help()
s = ","
hours = [f'{i:02}' for i in range(24)]
minutes = [f'{i:02}' for i in range(60)]

layout = [[sg.Text('Timer GUI')],
          # Insert your Spin code her
          [sg.Text('Hour(s)', font=('Courier 20')), sg.Text('Minute(s)', font=('Courier 20'))],
          [sg.Spin(hours, size=(2, 1), key='-HOURS-'), sg.Text(''), sg.Spin(minutes, size=(2, 1), key='-MINUTES-')],
          [sg.Button('Set'), sg.Button('Clear')]]  # and complete the reset of the layout

window = sg.Window('Window Title', layout, font='Courier 40')  # Add your layout and set the font

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Set':
        sg.Print(event, values)
    if event == 'Clear':
        window['-MINUTES-'].update('00')
        window['-HOURS-'].update('00')

    # Add your code to handle events for buttons

window.close()
