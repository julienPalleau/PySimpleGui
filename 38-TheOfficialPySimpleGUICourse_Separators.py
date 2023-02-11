"""
The Official Python GUI Programming with PySimpleGUI Course
Separator Elements - Draws a horizontal or vertical line
HorizontalSeparator
    Aliases = HSeparator, HSep
VerticalSeparator
    Aliases = VSeparator, VSep

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3
sg.set_options(font='Default 18')


# ================================ 1 - Horizontal Separator EXAMPLE ====================================================
def main_horizontal():
    layout = [[sg.Text('Horizontal Separators')],
              [sg.Text('The original way...')],
              [sg.T('_' * 40, font='courier 18')],  # old way to proceed with separator
              [sg.Text('The TTk way...')],
              [sg.HorizontalSeparator()],  # new way to proceed and thay automatically adapt to window width
              [sg.Button('Exit')], ]

    window = sg.Window("Horizontal Separators", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ================================ 2 - Vertical Separator EXAMPLE ======================================================
def main_vertical():
    sg.theme('dark green')

    layout = [[sg.Listbox([f'file [i]' for i in range(30)], k='-LB-', size=(10, 15), enable_events=True),
               sg.VerticalSeparator('red'),
               sg.Multiline(size=(30, 10), reroute_cprint=True, write_only=True, k='-ML-')],
              [sg.Button('Exit')]]

    window = sg.Window("Vertical Separator", layout, keep_on_top=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-LB-':
            sg.cprint('You chose: ', c='white on red', end='')
            sg.cprint(values[event][0], c='white on purple')

    window.close()


# ================================ 3 - Vertical Separator Using Columns EXAMPLE ========================================
def main_vertical_columns():
    col1 = [[sg.T('one')],
            [sg.T('two')],
            [sg.T('three')]]

    col2 = [[sg.B('123', size=(15, 1))],
            [sg.B('456', size=(15, 1))]]

    # Make a final laoyt using concatenation of 3 layouts
    layout = [[sg.Column(col1), sg.VerticalSeparator(), sg.Column(col2)],
              [sg.HorizontalSeparator(color='red')],
              [sg.Text('1', s=3), sg.VerticalSeparator(pad=(0, 0)), sg.Text('Name')],
              [sg.Text('2', s=3), sg.VerticalSeparator(p=0), sg.Text('Adress')],
              [sg.Text('3', s=(3,1)), sg.VerticalSeparator(p=0), sg.Text('Phone')]]

    window = sg.Window('Vertical Separators Using Columns', layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break


if __name__ == "__main__":
    example = [main_horizontal, main_vertical, main_vertical_columns]
    example[example_number - 1]()
