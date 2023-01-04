"""
Lesson 12

Shortcuts and Aliases
Exercise 1
Instructions

Recreate the window using only the aliases of elements and call Window.read using the alternate shortcut technique.

    Replace the Elements in the provided layout with one of their Aliases/Shortcuts
    You should notice no difference in how the window looks and operates

Bonus Points

    Replace parameters with their alias form too so your code is as short as possible

import PySimpleGUI as sg

PASSWORD = 'Easy is FUN!'

layout = [  [sg.Text('Enter Your ID and Password')],
            [sg.Text('ID', size=(10,1)), sg.Input(key='-ID-', size=(15,1))],
            [sg.Text('Password', size=(10,1)), sg.Input(password_char='*', key='-PASSWORD-', size=(15,1))],
            [sg.Button('Login'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Login':
        if values['-PASSWORD-'] == PASSWORD:
            sg.popup('Login complete!', button_color='white on green')
            break
        else:
            sg.popup_error('Incorrect Password')

window.close()
"""
import PySimpleGUI as sg

PASSWORD = 'Easy is FUN!'

layout = [  [sg.T('Enter Your ID and Password')],
            [sg.T('ID', size=(10,1)), sg.I(key='-ID-', size=(15,1))],
            [sg.T('Password', size=(10,1)), sg.I(password_char='*', key='-PASSWORD-', size=(15,1))],
            [sg.B('Login'), sg.B('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Login':
        if values['-PASSWORD-'] == PASSWORD:
            sg.popup('Login complete!', button_color='white on green')
            break
        else:
            sg.popup_error('Incorrect Password')

window.close()