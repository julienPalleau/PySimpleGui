"""
Lesson 38

Separator Element
Exercise 1

Use vertical and horizontal Separator Elements to divide up a window's layout
Instructions:

    In this exercise, you're simply trying to break up the visual parts of the interface so they're more easily visible
    You are to make a layout with 3 rows. Between the elements, add Separators.
    The rows are as follows:
        Listbox (size of 20 x 10), Multiline (size 30 x 10)
        Multiline (size 60 x 10)
        Exit Button

Horizontal Separator Element in the Call Reference Documentation

Vertical Separator Element in the Call Reference Documentation

import PySimpleGUI as sg

# Add your layout
layout = [  []  ]

window = sg.Window('Separator Elements', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
"""
import PySimpleGUI as sg

# Add your layout
layout = [[sg.Listbox([1,2,3,4], size=(20, 10)),  sg.VerticalSeparator(), sg.Multiline(size=(30, 10))],\
    [sg.HorizontalSeparator()],\
    [sg.Multiline(size=(60, 10))],\
    [sg.HorizontalSeparator()],\
    [sg.B('Exit')]
    ]
window = sg.Window('Separator Elements', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()