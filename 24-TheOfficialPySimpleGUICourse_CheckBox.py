"""
The Official Python GUI Programming with PySimpleGUI Course
Checkbox Element
    A binary input element

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 18')

# sg.theme('dark red')

example_number = 1


# ================================== 1 - Basic Checkbox EXAMPLE ========================================================
def main_checkbox():
    layout = [[sg.T('The Checkbox Element')],
              [sg.MLine(size=(60, 10), write_only=True, reroute_stdout=True, reroute_cprint=True, k='-ML-')],
              [sg.Checkbox('Checkbox 1', k='-CBOX1')],
              [sg.Checkbox('Checkbox 2', k='-CBOX2)')],
              [sg.B('Go'), sg.B('Exit')]
              ]

    window = sg.Window('Checkbox Element', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        sg.cprint(f'event = {event}', c='white on red')
        sg.cprint(f'\n'.join(f'{k} = {values[k]}' for k in values), sep='\n')
    window.close()


if __name__ == "__main__":
    main_checkbox()
