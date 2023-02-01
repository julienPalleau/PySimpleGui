"""
Lesson 29

Slider Element
Exercise 1

Make an equalizer GUI with Bass, Mid and Treble settings
Instructions:

    Make a window that implements a basic equalizer
    Use 3 sliders that have a range of 0 to 100
    Add a label under each slider
        You don't have to be precise, a single Text element with spaces between each label is fine
    Include 1 buttons
        Ok - Shows a popup of the values dictionary returned from window.read()
        Reset - Sets the values to 0 for all sliders

Slider in the Call Reference Documentation

import PySimpleGUI as sg

layout = [[sg.Text('Mixer', font='Default 15')],
          # Your part goes here.....
          [sg.Button('Ok'), sg.Button('Reset')]]

window = sg.Window('Equalizer', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        sg.popup(values, title='Values')


window.close()
"""
import PySimpleGUI as sg

layout = [[sg.Text('Mixer', font='Default 15')],
          # Your part goes here.....
          [sg.Button('Ok'), sg.Button('Reset')]]

window = sg.Window('Equalizer', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        sg.popup(values, title='Values')


window.close()