"""
The Official Python GUI Programming with PySimpleGUI Course
Spin Element (Spinbox)
    "Choose one" type of element
    Aliases = Sp

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.Print('', font='Default 18', keep_on_top=True, size=(50, 10), location=(1450, 250))
sg.set_options(font='Default 18')
example_number = 2


# ====================================== 1 - Basic Spinner Example =====================================================
def main_spin():
    sg.sdk_help()
    color_names = ('red', 'green', 'blue', 'yellow + orange = amber')
    layout = [
        [sg.Spin(color_names, k='-SPIN-')],
        [sg.B('Go'), sg.B('Exit')],
    ]

    window = sg.Window("Spin", layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')


# ====================================== 2 - Basic Spinner Example =====================================================
def main_mixed():
    mixed = ('red', 1_000_000, 3, 1415, sg.Text())
    layout = [
        [sg.Spin(mixed, readonly=True, disabled=True, size=(40, 1), k='-SPIN MIXED-')],
        [sg.B('Go'), sg.B('Enable'), sg.B('Exit')],
    ]
    window = sg.Window("Spin Mixed", layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == 'Enable':
            window['-SPIN MIXED-'].update(disabled=False)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

        sg.Print(type(values['-SPIN MIXED-']))

    window.close()


if __name__ == "__main__":
    example = [main_spin, main_mixed]
    example[example_number - 1]()
