"""
The Official Python GUI Programmming with PySimpleGUI Course
Event Dispatchers
    * If-Else
    * Dictionnaries
    * Functions as keys
http://www.PySimpleGUI.org
"""
import PySimpleGUI as sg


def do_go(window):
    window['-LED-'].update(sg.SYMBOL_CIRCLE, text_color='green')


def do_stop(window):
    window['-LED-'].update(sg.SYMBOL_CIRCLE, text_color='red')


def do_error(window):
    window['-LED-'].update(sg.SYMBOL_X, text_color='red')


def main():
    dispatch_dict = {'Go':do_go, 'Stop':do_stop}

    layout = [[sg.Text('My Window')],
              [sg.Text('Status:'), sg.Text(sg.SYMBOL_CIRCLE_OUTLINE, size=(3, 1), key='-LED-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Button('Go'), sg.B('Stop'), sg.B('Other', key=do_error), sg.B('Exit')]]

    window = sg.Window('Dispatchers', layout, font='Default 16', keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if callable(event):
            event(window)
        else:
            func = dispatch_dict.get(event, do_error)
            func(window)

        window['-OUT-'].update(f'You clicked: {event}')

    window.close()


if __name__ == '__main__':
    main()
