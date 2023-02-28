"""
The Official Python GUI Programming with PySimpleGUI Course
Element Expansion
    The Element .expand method
    The expand_x & expand_y parms

Docs:
    http://www.PySimpledGUI.org

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 4

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE - A static window =============================================================
def main_example1():
    layout = [[sg.Text('A static PySimpleGUI Window', key='-TEXT-', background_color='red',
                       justification='c')],
              [sg.Multiline(size=(40, 15), key='-MLINE-')],
              [sg.Button('Go'), sg.Button('Exit')], ]

    window = sg.Window('Expansion 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 2 - EXAMPLE - Expansion without resize ====================================================
def main_example2():
    layout = [[sg.Text('A Resizable window', key='-TEXT-', background_color='red', justification='c')],
              [sg.Multiline(size=(40, 15), key='-MLINE-')],
              [sg.Button('Go'), sg.Button('Exit')], ]

    window = sg.Window('Expansion 2', layout, finalize=True, resizable=True)
    window['-TEXT-'].expand(True, False, False)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 3 - EXAMPLE - The "Old Way" - Call Element.expand =========================================
def main_example3():
    layout = [[sg.Text('A Resizable Window 1', key='-TEXT-', background_color='red', justification='c')],
              [sg.Multiline(size=(40, 15), key='-MLINE-')],
              [sg.Button('Go'), sg.Button('Exit')], ]

    window = sg.Window('Expansion 3', layout, resizable=True, finalize=True)
    window['-MLINE-'].expand(True, True, True)
    window['-TEXT-'].expand(True, False, False)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 4 - EXAMPLE - expand_x, expand_y - the new way ============================================
def main_example4():
    layout = [[sg.Text('A Resizable Window', key='-TEXT-', background_color='red', expand_x=True, justification='c')],
              [sg.Multiline(size=(40, 15), key='-MLINE-', expand_x=True, expand_y=True)],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Expansion 4', layout, resizable=True, finalize=True)
    window.set_min_size(window.size)

    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3, main_example4]
    example[example_number - 1]()
