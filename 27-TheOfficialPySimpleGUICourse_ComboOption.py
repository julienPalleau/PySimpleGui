"""
The Official Python GUI Programming with PySimpleGUI Course
Combo and OptionMenu Elements
    "Choose one" type of elements
Combo (Combobox)
    Aliases = DD, Drop, DropDown, InputCombo
OptionMenu = unique to tkinter
    Alias = InputOptionMenu

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.Print('', font='Default 18', keep_on_top=True, size=(50, 10), location=(1450, 250))
sg.set_options(font='Default 18')
example_number = 2


# ================================= 1 - Basic Combo EXAMPLE ============================================================
def main_combo_option_menu():
    color_names = ('red', 'green', 'blue', 'yellow + orange = amber')
    feeling_blue = ('blue', 'dark blue', 'sky blue', 'blue + blue = blue')

    layout = [[sg.T('    ')],
              [sg.Combo(color_names, default_value=color_names[0], enable_events=True, k='-COMBO-')],
              [sg.OptionMenu(color_names, default_value=color_names[0], k='-OPTION-')],
              [sg.B('Go'), sg.B('Change'), sg.B('Exit')],
              ]

    window = sg.Window('Combo', layout, keep_on_top=True, button_color=('red', 'white'),
                       right_click_menu=[[], list(color_names)])

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Change':
            window['-COMBO-'].update(values=feeling_blue, value='test')
            window['-OPTION-'].update(values=feeling_blue, value='123')

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'    {k} = {values[k]}' for k in values], sep='\n')


# ================================= 2 - Combo Read Only EXAMPLE ========================================================
def main_combo_readonly():
    sg.sdk_help()
    color_names = ('red', 'green', 'blue', 'yelllow', 'green + green = green')
    feeling_blue = ('blue', 'dark blue', 'sky blue', 'blue + blue = blue')
    layout = [
        [sg.Combo(color_names, default_value=color_names[0], readonly=True, k='-COMBO0-')],
        [sg.DropDown(list(range(1, 100)), default_value='Not chosen', size=(10, 12), readonly=True, k='-COMBO1-')],
        [sg.OptionMenu(color_names, default_value=color_names[0], size=(20, 2), k='-OPTION-')],
        [sg.B('Go'), sg.B('Change'), sg.B('Exit')]
    ]

    window = sg.Window("Combo", layout, keep_on_top=True, font='Default 18')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Change':
            window['-COMBO0-'].update(values=feeling_blue,)
            window['-COMBO1-'].update(values=feeling_blue, size=(30, 2))
            window['-OPTION-'].update(values=feeling_blue, size=(2, 2))

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'   {k}={values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    example = [main_combo_option_menu, main_combo_readonly]
    example[example_number - 1]()
