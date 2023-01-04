"""
    The Official Python GUI Programming with PySimpleGUI Course

    themes

    The 1-line windows beautification.

    Choose from 151 pre-defined themes or create your own

    <"Dark" | "Light"> <Color> [#]

    Color is one of: Black, Blue, Green, Teal, Brown, Yellow, Gray, Purple

    http://www.PySimpleGUI.org

    you can call in the terminal: psgdemos, psgmain
"""

import PySimpleGUI as sg

def make_window():
    layout = [[sg.Text('My Window')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, keep_on_top=True)
    return window

def main():
    sg.set_options(font='Default 18')

    new_theme = {'BACKGROUND': '#32414B',
                 'TEXT': '#ffffff',
                 'INPUT': '#32414B',
                 'TEXT_INPUT': '#ffffff',
                 'SCROLL': '#505F69',
                 'BUTTON': ('#ffffff', '#32414B'),
                 'PROGRESS': ('#505F69', '#32414B'),
                 'BORDER': 4, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 }

    sg.theme_add_new('Your New Theme', new_theme)

    sg.theme('Your New Theme')
    # sg.theme_background_color('#FF0000')
    # sg.popup(sg.theme_background_color())

    window = make_window()



    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Go':
            sg.theme('Dark Grey 13')
            window.close()
            window = make_window()
        else:
            window['-OUT-'].update(f'You clicked {event}')

    window.close()


if __name__ == '__main__':
    main()
