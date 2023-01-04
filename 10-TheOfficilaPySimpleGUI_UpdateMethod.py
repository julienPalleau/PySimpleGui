"""
The Official Python GUI Programming with PySimpleGUI Course
The Element.update method
The most commonly used of the Element method. If you want to change an element in your window, you will use its update
method.
Other then the set_tooltip & set_size methods, all changes are made through update
https://www.pysimplegui.org/en/latest/call%20reference/

http://www.PySimpleGUI.org
"""
import PySimpleGUI as sg
import random

def main():
    txt = sg.Text('Text Element Updating')
    layout = [[txt],
              [sg.Text(size=(30, 1), key='-OUT-', )],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, font='_ 20')

    while True:         # Event Loop
        event, values = window.read(timeout=200)
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window['-OUT-'].update(sg.SYMBOL_CIRCLE_OUTLINE if random.randint(0,100)<50 else sg.SYMBOL_CIRCLE)

    window.close()

if __name__ == '__main__':
    main()