"""
The Official Python GUI Programming with PySimpleGUI Course
Checkbox Element
    A binary input element

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#checkbox-element

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.sdk_help()
sg.set_options(font='Default 18')

# sg.theme('dark red')

example_number = 2


# ================================== 1 - Basic Checkbox EXAMPLE ========================================================
def main_checkbox():
    layout = [[sg.T('The Checkbox Element')],
              [sg.MLine(size=(60, 10), write_only=True, reroute_stdout=True, reroute_cprint=True, k='-ML-')],
              [sg.Checkbox('Checkbox 1', k='-CBOX1')],
              [sg.Checkbox('Checkbox 2', default=True, k='-CBOX2)')],
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


# ================================== 2 - Simulated Radio Button EXAMPLE ================================================

def main_checkbox_simulating_radios():
    color_names = ['red', 'green', 'blue', 'yellow']
    layout = [[sg.Text('Simulated Radio Buttons')],
              [sg.MLine(size=(60, 10), write_only=True, reroute_stdout=True, reroute_cprint=True, k='-ML-')],
              [sg.Checkbox(name, k=name, enable_events=True, checkbox_color='black') for name in color_names],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Checkbox', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event in color_names:
            for k in color_names:
                window[k].update(False, checkbox_color='black')
            window[event].update(True, checkbox_color='red')

    window.close()


if __name__ == "__main__":
    examples = [main_checkbox, main_checkbox_simulating_radios]
    print(examples[example_number - 1].__name__)

    examples[example_number - 1]()
