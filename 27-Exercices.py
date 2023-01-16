"""
Lesson 27

ComboBox and OptionMenu Elements
Exercise 1

Make a Pick a Color & Pick a Number GUI
Instructions:

In this window, you're using 2 Combo Elements to get a Color and a Number

    The color can be either typed in or chosen from the Combo's list
    The number is to be chosen only (cannot be typed in)
        The range should be 0 to 99
        Make 15 of them at a time visible to the user
        Set the default value initially shown to be 10
    Include an "OK" button
        When clicked, show the values chosen in the Debug Print window

Suggested widths for your Combos - 15 for the colors, 3 for the numbers.

Reminder - Always be sure and check for a window being closed and always close your windows at the end of the program

Combo Element in the Call Reference Documentation

Option Menu Element in the Call Reference Documentation

import PySimpleGUI as sg

color_names = ('red', 'green', 'blue', 'yellow')
number_choices =

layout = [  [sg.Text('Choose a color, choose a number')],
            # Insert your Combo Elements here
            [sg.Button('OK')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
"""
import PySimpleGUI as sg

color_names = ('red', 'green', 'blue', 'yellow')
# number_choices =

layout = [  [sg.Text('Choose a color, choose a number')],
            # Insert your Combo Elements here
            [sg.Combo(color_names, default_value=color_names[0], size=(15, 1), k='-COLOR-')],
            [sg.Combo(list(range(0, 100)), default_value=10, readonly=True, size=(3, 15), k='-NUMBER-')],
            [sg.Button('OK'), sg.Button('Exit')]
        ]
window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'OK':
        sg.Print(values['-COLOR-'], values['-NUMBER-'])

window.close()