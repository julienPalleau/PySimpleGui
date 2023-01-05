"""
The Official Python GUI Programming with PySimpleGUI Course
Input Popups
There are 4 popups that collect user input
    popup_get_date
    popup_get_file
    popup_get_foloder
    popup_get_text

    http://www.PySimpleGUI.org
"""
import PySimpleGUI as sg


def popup_drop_down(title, text, values):
    event, values = sg.Window(title,
                       [[sg.Text(text)],
                        [sg.Combo(values, key='-DROP-')],
                        [sg.OK(), sg.Cancel()]
                        ]).read(close=True)
    return None if event != 'OK' else values['-DROP-']


sg.set_options(font='Default 14')  # set system_wide default
sg.Print('Outoput from popups', font='Default 14', keep_on_top=True, size=(30, 10), location=(1700, 350))
# print in a separate debug window

name = sg.popup_get_text('What is your name?', 'Enter Name', image=sg.EMOJI_BASE64_NOTUNDERSTANDING)
sg.Print(f'get_text = {name}')    # print in a separate debug window

password = sg.popup_get_text('Password', 'Title', password_char='*', image=sg.EMOJI_BASE64_NOTUNDERSTANDING)
sg.Print(f'Password = {password}')    # print in a separate debug window

value = popup_drop_down('Title', 'Choose something', [1, 2, 3, 4])
sg.Print(f'value = {value}')    # print in a separate debug window

sg.popup('Exit')    # print in the popup window
