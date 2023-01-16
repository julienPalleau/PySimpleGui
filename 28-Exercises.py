"""
Lesson 41

Listbox
Exercise 1

Make a GUI to manage items on a list
Instructions:

    Make a GUI that has:
        Input Element to enter values to add
        Listbox Element that is 20 chars wide and 10 entries high
        3 Buttons - Add, Delete, Exit
    When the user clicks Add, add the value that is in the input element if there is one
    When the user clicks Delete, delete the highlighted item in the listbox
    When the user clicks Exit, quit the event loop

Listbox documentation:

https://pysimplegui.readthedocs.io/en/latest/call%20reference/#listbox-element

import PySimpleGUI as sg

layout = [  [sg.Text('Manage a list')],
            [],   # Input element goes here
            [],   # Listbox goes here
            []]   # Your 3 buttons goes here

window = sg.Window('Listbox Exercise', layout)

while True:
    event, values = window.read()

    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Add':

    elif event == 'Delete':

window.close()
"""
import PySimpleGUI as sg

layout = [  [sg.Text('Manage a list')],
            [sg.Input(background_color='black', text_color='white',
                      border_width=2, tooltip='input text', focus=True, key='-IN-')],   # Input element goes here
            [sg.Listbox(['test1', 'test2'], size=(20, 10), key='-LB-')],   # Listbox goes here
            [sg.Button('Add'), sg.Button('Delete'), sg.Button('Exit')]]   # Your 3 buttons goes here

window = sg.Window('Listbox Exercise', layout)

while True:
    event, values = window.read()

    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #
    if event == 'Add':
        cur_list = window['-LB-'].get_list_values()
        print(cur_list, values['-IN-'])
        if len(values['-IN-']) != 0:
            cur_list.append(values['-IN-'])
            window['-LB-'].update(values=cur_list)

    # elif event == 'Delete':

window.close()