"""
The Official Python GUI Programming with PySimpleGUI Course
Text Element
Uses:
    * Initial Text
    * Clickable Text
    * Output Text
    * Grabbable spot to move window
    * Expands to fill space (covvered in Justification Lesson)

    https://www.pysimplegui.org/en/latest/call%20reference/#text-element
    sg.main_sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 14')


def main():
    layout = [[sg.Text('The Text Element', grab=True), sg.T(' '*60), sg.T(sg.SYMBOL_X, enable_events=True, k='Exit')],
              [sg.T('www.PySimpleGUI.org', font='_ 18 underline', k='-URL-', enable_events=True)],
              [sg.Input(key='-IN-')],
              [sg.T()],
              [sg.Text(size=(30, 1), key='-OUT EVENT-', text_color='yellow')],
              [sg.Text(size=(30, 1), key='-OUT VALUES-', text_color='green1')],
              [sg.Button('Go')]]

    window = sg.Window('Window Title', layout, keep_on_top=True, no_titlebar=True,finalize=True)
    window['-URL-'].set_cursor('hand1')

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT EVENT-'].update(f'event = {event}')
        window['-OUT VALUES-'].update(f'values = {values}')

    window.close()


if __name__ == '__main__':
    main()
