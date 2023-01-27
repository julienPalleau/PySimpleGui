"""
Lesson 34

Button Element - Shortcuts
Exercise 1

Replace conventional Buttons with shortcut equivalents
Instructions:

    Replace the Button Elements in the layout with their shortcut alias
    Print the event each time through your event loop to see what is generated when you click the Button
    Break from your event loop if the window is closed or one of the 3 Buttons in the example that would logically close a window is clicked.

"Predefined Buttons" in the Call Reference Documentation

import PySimpleGUI as sg

# Replace these Buttons with their "Shorttcut" version
layout = [  [sg.Text('Button Shortcuts')],
            [sg.Button('OK'), sg.Button('Cancel'), sg.Button('Yes'), sg.Button('No')],
            [sg.Button('Open'), sg.Button('Save'), sg.Button('Quit'), sg.Button('Exit')],
            [sg.Button('Submit'), sg.Button('Help')],]

window = sg.Window('Button Shortcuts', layout)

# In the event loop, check for window closed and other buttons that maybe should close a window
# Also print the event each time through the loop
while True:
    event, values = window.read()

window.close()
"""
import PySimpleGUI as sg

# Replace these Buttons with their "Shorttcut" version


layout = [[sg.Text('Button Shortcuts')],
          [sg.Ok(), sg.Cancel(), sg.Yes(), sg.No()],
          [sg.Open(), sg.Button('Save'), sg.Button('Quit'), sg.Button('Exit')],
          [sg.Button('Submit'), sg.Button('Help')], ]

window = sg.Window('Button Shortcuts', layout)

# In the event loop, check for window closed and other buttons that maybe should close a window
# Also print the event each time through the loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.Print(f'event = {event}', c='white on red', erase_all=True)
    sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

window.close()
