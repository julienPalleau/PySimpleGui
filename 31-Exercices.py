"""
Lesson 31

Button Element - Choosers
Exercise 1

Make a GUI that enables choosing 2 files - an input file and an output file
Instructions:

    Make a Window with 2 filename inputs. Each input row should have:
        A Text element that tells the user what the item is (e.g. "Input File")
        An Input element for the filename to be entered
        A chooser button to allow user to browse for a filename
    Use "File Browse" type of chooser buttons with an Input element to create your GUI
    Include an OK button and a Cancel button
        OK will print the names of the files chosen
        Cancel closes the window and exits the program
    Limit the files shown to the user to be only those with a .txt extension
    Write your GUI so that the user is prompted to "overwrite" if the output file already exists
    Make your Input elements line up visually in a nice way

"Predefined Buttons" in the Call Reference Documentation
import PySimpleGUI as sg

layout = [  [sg.Text('Choose your Input and Output Files')],
            # this is where you'll add your part....
            [sg.Button('Ok'), sg.Button('Cancel')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    # finish the event loop's code according to the directions

window.close()
"""
import PySimpleGUI as sg
starting_value = ''
layout = [[sg.Text('Choose your Input and Output Files')],
          # this is where you'll add your part....
          [sg.T('Input File:', size=(9,1)), sg.Input(starting_value, size=(len(starting_value), 1), k='-IN-'),
           sg.FileBrowse(file_types=(('Text Files', '*.txt'),))],
          [sg.T('Output File:', size=(9,1)), sg.Input(key='-OUT-'),
           sg.FileSaveAs(file_types=(('Text Files', '*.txt'),))],
          [sg.Button('Ok'), sg.Button('Cancel')]
        ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Ok':
        sg.popup(f'Input file = {values["-IN-"]}', f'Output File = {values["-OUT-"]}', title='Chosen files')

    # finish the event loop's code according to the directions

window.close()