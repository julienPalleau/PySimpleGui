"""
The official python GUI programming with PySimpleGUI Course

The PySimpleGui Ports

    http://www.PySimpleGUI.org
"""

import PySimpleGUI as sg

def main():
    layout = [[sg.Text('My Window')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)

    while True:     # Event loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT-'].update(f'You clicked {event}')
    window.close()

main()