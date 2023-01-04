"""
Lesson 7

Themes
Exercise 1
Instructions

    Use popup to get a list of themes.
    Make a window using a theme of your choice.

import PySimpleGUI as sg

sg.popup(sg.theme_list(), title='Theme List')

exit()    # Comment out to continue

sg.theme('')    # Add your theme name
layout = [[sg.Text('This is my theme')],
          [sg.Button('Exit')]]

window = sg.Window('Theme', layout)

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED or event == 'Exit':
    break

window.close()
"""
import PySimpleGUI as sg

sg.popup(sg.theme_list(), title='Theme List')

exit()  # Comment out to continue

sg.theme('Light Green 5')  # Add your theme name
layout = [[sg.Text('This is my theme')],
          [sg.Button('Exit')]]

window = sg.Window('Theme', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()