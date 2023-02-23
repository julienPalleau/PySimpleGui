"""
The Official Python GUI Programming with PySimpleGUI Course
Listbox Element
    "Choose 1 or more" type of element
    Aliases = LBox, LB

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#listbox-element

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import os

sg.Print('', font='Default 18', keep_on_top=True, size=(50, 10), location=(1650, 100))
sg.set_options(font='Default 18')
example_number = 1


# ==================================== 1 - Basic Listbox Example =======================================================
def main_listbox():
    sg.theme_text_color('yellow')

    color_names = ('red', 'green', 'blue', 'yellow', 'blue', 'blue green', 'sky blue', 'navy blue')
    mixed_list = (1, 2, 3, 3.1415, sg.Text(), 'yellow + orange = amber')

    layout = [
        [sg.T('SINGLE (default)' + ' ')],
        [sg.Listbox(color_names, size=(25, 7), select_mode=sg.SELECT_MODE_SINGLE, enable_events=True, k='-LBOX1-')],
        [sg.T('MULTIPLE''+')],
        [sg.Listbox(mixed_list, size=(25, 7), select_mode=sg.SELECT_MODE_MULTIPLE, enable_events=True, k='-LBOX2-')],
        [sg.T('BROWSE' + ' ')],
        [sg.Listbox(mixed_list, size=(25, 7), select_mode=sg.SELECT_MODE_BROWSE, enable_events=True, k='-LBOX3-')],
        [sg.T('EXTENDED (best for multiple)')],
        [sg.Listbox(mixed_list, size=(25, 7), select_mode=sg.SELECT_MODE_EXTENDED, no_scrollbar=True,
                    enable_events=True, k='-LBOX4-')],
        [sg.B('Go'), sg.B('Change'), sg.B('Exit')]
    ]

    window = sg.Window('Listbox', layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

        if event == 'Change':
            window['-LBOX1-'].update(values=mixed_list)
        elif event == 'Go':
            sg.Print(window['-LBOX2-'].get_indexes())
            window['-LBOX3-'].set_value((2, 3, 3.1415))

    window.close()


# ==================================== 2 - Listbox with files Example ==================================================
def main_listbox_filename():
    # Create a dictionary with
    folder1 = r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\example_folder1'
    file_list = os.listdir(folder1)
    file_dict = {fname: os.path.join(folder1, fname) for fname in file_list}

    folder2 = r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\example_folder2'
    file_list2 = os.listdir(folder2)
    fild_dict2 = {fname: os.path.join(folder2, fname) for fname in file_list2}

    # add the file lists and dictionaries together
    file_list += file_list2
    file_dict.update(fild_dict2)

    layout = [
        [sg.Listbox(file_list, size=(30, 15), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED, enable_events=True,
                    k='LBOX'),
         sg.Image(k='-I-')],
        [sg.T(size=(35, 2), k='-T-')],
        [sg.B('Exit')]
    ]

    window = sg.Window("Listbox", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        window['-I-'].update(filename=file_dict[values[event][0]])
        window['-T-'].update(file_dict[values[event][0]])

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    example = [main_listbox, main_listbox_filename]
    example[example_number - 1]()
