"""
The Official Python GUI Programming with PySimpleGUI Course

Layout Reuse:
    * Reusing a layout (in a safe manner)
    * Changing themes or other "drastic changes"

Docs:
    http://www.PySimpleGUI.org
Built-in help:
    sg.sdk_help()
"""
import PySimpleGUI as sg
example_number = 0
sg.set_options(font='Default 16', keep_on_top=True)

#====================================== 1 - EXAMPLE - Layout reuse =====================================================
# def main_example1():
#     layout = [[sg.Text('My Layout to be Reused')],
#               [sg.Multiline(size=(40,15), key='-MLINE-')],
#               [sg.Button('Go'), sg.Button('Exit')]]
#     window = sg.Window('Layout Reuse 1', layout)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#
#     window.close()
#
#     window = sg.Window('Layout Reuse 1', layout)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#
#     window.close()
#
# if __name__ == '__main__':
#     main_example1()

#====================================== 2 - EXAMPLE - Layout reuse (safely) ============================================
# def main_example1():
#     def make_window():
#         layout = [[sg.Text('My Layout to be Reused')],
#                   [sg.Multiline(size=(40,15), key='-MLINE-')],
#                   [sg.Button('Go'), sg.Button('Exit')]]
#         window = sg.Window('Layout Reuse 2', layout, no_titlebar=True)
#         return window
#
#     window = make_window()
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#
#     window.close()
#
#     window = make_window()
#     while True:
#         event , values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#     window.close()
#
# if __name__ == '__main__':
#     main_example1()

#====================================== 3 - EXAMPLE - Theme change =====================================================
def main_example3():
    def make_window(location=(None, None)):
        layout = [[sg.Text('My Layout to be Reused')],
                  [sg.Multiline(size=(40,15), key='-MLINE-')],
                  [sg.Button('Change Theme'), sg.Button('Exit')]]

        window = sg.Window('Layout Reuse 3', layout, location=location)
        return window

    window = make_window()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Change Theme':
            location = window.current_location()
            window.close()
            sg.theme('dark gray 13')
            window = make_window(location)
    window.close()

if __name__ == '__main__':
    main_example3()