"""
The Official Python GUI Programming with PySimpleGUI Course

Radio Element (i.e RadoButton)
    Binary input element (checkbox is another)
    Radio, Rad, R

    Docs: http://www.PySimpleGUI.org
    https://www.pysimplegui.org/en/latest/call%20reference/#radio-element

    Buit-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 18')
# sg.theme('dark red')
example_number = 2


# ================================== 1 - Basic Radio Button EXAMPLE ====================================================
def main_checkbox():
    layout = [[sg.T('The Radio [Button] Element')],
              [sg.MLine(size=(60, 10), write_only=True, reroute_cprint=True, k='-ML-')],
              [sg.Radio('Radio 1', 'Group 1', k='-R1-')],
              [sg.Radio('Radio 2', 'Group 1', k='-R2-')],
              [sg.Radio('Radio 3', 'Group 1', k='-R3-')],
              [sg.B('Go'), sg.B('Reset'), sg.B('Exit')]]

    window = sg.Window('RadioButton Element', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        sg.cprint(f'event = {event}', c='white on red')
        sg.cprint(*[f'{k}={values[k]}' for k in values], sep='\n')

    window.close()


# ================================== 2 - Multiple Choice Test EXAMPLE ==================================================
def main_checkbox_simulating_radios():
    color_names = ('red', 'green', 'blue', 'yellow')
    layout = [
        [sg.MLine(size=(60, 10), write_only=True, reroute_cprint=True, reroute_stdout=True, k='-ML-')],
        [sg.Text('Chosse text color')],
        [sg.Radio(name, group_id=1, k=name, enable_events=True) for name in color_names],
        [sg.Button('Go'), sg.B('Reset'), sg.Button('Exit')]]

    window = sg.Window('RadioButton Element', layout, keep_on_top=True)

    while True:  # Event loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Reset':
            window['red'].reset_group()

        sg.cprint(f'event = {event}', c='white on red')
        sg.cprint(*[f'  {k} = {values[k]}' for k in values], sep='\n')
    window.close()


if __name__ == "__main__":
    examples = [main_checkbox, main_checkbox_simulating_radios]
    print(examples[example_number-1].__name__)

    examples[example_number-1]()
