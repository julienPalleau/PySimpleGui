"""
Lesson 25

Radio Button Element
Exercise 1

Make a GUI to select a "Player Character Type" for a game
Instructions:

You're making a game and the user has these choices of player types:

    Warrior
    Wizard
    Ninja
    Archer
    Cleric

    Make a window that uses Radio Buttons to enable players to choose a type.
    All of the choices should be on 1 row in your Window.
    Include 2 buttons
        Ok - Shows a popup of the values dictionary returned from window.read()
        Clear - Clears the choices

Radio Button in the Call Reference Documentation
"""
import PySimpleGUI as sg

char_types = ['Warrior', 'Wizard', 'Ninja', 'Archer', 'Cleric']

layout = [[sg.Text('Character type:', font = 'Default 15')],
          [sg.Radio(char_type, group_id=1, key=char_type) for char_type in char_types],
          [sg.Button('Ok', k='-Button1-'), sg.Button('Clear', k='-Button2-')]]


window = sg.Window('Player Character Type', layout)

while True:     # Event Loop
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break
    if event == '-Button1-':
        sg.popup(values, title='values')
    elif event == '-Button2-':
        window[char_types[0]].reset_group()

window.close()
