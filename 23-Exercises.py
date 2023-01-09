"""
Lesson 23

Output Element
Exercise 1

Print numbers 0 to 999 in an Output Element
Instructions:

While not recommended as the preferred way to re-route stdout, the Output element is still fine to use.

    Make your Output element have a size of 40 chars wide by 20 rows high
    Print the numbers 0 to 999 when a "Count" button is clicked

Output Element in the Call Reference Documentation

import PySimpleGUI as sg

layout = [[sg.Text('Prints go here:')],
          # This is whwere you'll add your part....
          ]

window = sg.Window('Output Element', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
"""
import PySimpleGUI as sg

layout = [[sg.Text('Prints go here:', size=(40, 20))],
          [sg.B('Count')]
          # This is whwere you'll add your part....
          ]

window = sg.Window('Output Element', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Count':
        for i in range(1000):
            sg.Print(i)

window.close()