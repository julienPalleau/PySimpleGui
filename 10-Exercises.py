"""
Lesson 10

Element.update method
Exercise 1
Instructions

You are going to use the update method for Text and Button elements

    Make a Text Element and a Button Element and store into 2 variables
    Create your layout using these 2 variables, one per row
    Increment a counter every time through your event loop
    Call the update method for the Text Element:
        Set it to the counter value
    Call the update method for the Button Element
        Set the button text to be the counter * 1000

"Text Element" in the Call Reference Documentation

"Button Element" in the Call Reference Documentation
"""

import PySimpleGUI as sg

text_elem = sg.Text("Hello Julian", key='-Text-')
button_elem = sg.Button('Element', key='-ButtonE-')


layout = [ [text_elem],
           [button_elem]]

window = sg.Window('Update Method Exercise', layout)

counter = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    text_elem.update(counter)
    button_elem.update(counter*1000)


    if event == '-ButtonE-':
        counter += 1

window.close()