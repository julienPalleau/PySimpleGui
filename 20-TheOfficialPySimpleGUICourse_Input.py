"""
The Official Python GUI Programmming with PySimpleGUI Course

Input Element - Input, In, I, InputText
Uses:
    * Simple single line input
    * Chooser target
    * Password input
    * Small/short field input

https://www.pysimplegui.org/en/latest/call%20reference/#input-element
sg.main_sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='default 18')


def main():
    layout = [[sg.Text('The Input Element')],
              # [sg.Input('default', key='-IN1-')],
              # [sg.Input(password_char='*', key='-IN1-')],
              [sg.Input(key='-IN1-'), sg.FileBrowse(target='-IN1-')],
              [sg.Input(key='-IN2-')],
              [sg.Text(size=(30, 1), key='-OUT EVENT-', text_color='yellow')],
              [sg.Text(size=(40, 1), key='-OUT VALUES-', text_color='green1')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Input Element Window', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT EVENT-'].update(f'Event = {event}')
        window['-OUT VALUES-'].update(window['-IN2-'].get())

    window.close()


if __name__ == '__main__':
    main()
