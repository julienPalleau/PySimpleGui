"""
The Official Python GUI Programmming with PySimpleGUI Course
Tkinter Event Binding
Windows-level:
    Window.bind
Element-level:
    Element.bind
Docs:
    https://pysimplegui.readthedocs.is/en/latest/#binding-tkinter-events

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3
sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE - Displaying Objects ==========================================================
def main_example1():
    sg.Print(font='Default 14', keep_on_top=True, size=(60, 30), relative_location=(400, -200))

    layout = [[sg.Text('Displaying Objects')],
              [sg.Button('Show Window.Tkroot'), sg.Button('Exit')],
              ]

    window = sg.Window('Tkinter Bindings 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Show Window.Tkroot':
            sg.Print(f'TKroot = {window.TKroot.x}', c='white on green')
            sg.Print(f'TKroot = {type(window.TKroot)}', c='white on green')
            sg.Print(f'TKroot = {sg.obj_to_string_single_obj(window.TKroot)}', c='white on green')

    window.close()


# ========================== 2 - EXAMPLE - Window-level binding ========================================================
def main_example2():
    sg.Print(font='Default 14', keep_on_top=True, size=(60, 30), relative_location=(300, -150))

    layout = [[sg.Text('Binding At Window-level')],
              [sg.Button('Bind'), sg.Button('Exit')], ]

    window = sg.Window('Tkinter Bindings 2', layout, finalize=True)
    window.bind('<Button-3>', 'Mouse Event')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Bind':
            window.bind('<Button-1>', 'Mouse Event')

        sg.Print(f'event = {event}', c='white on red')
        sg.Print(f'values = {values}', c='white on red')

        if window.user_bind_event is not None:
            sg.Print(f'Event = {sg.obj_to_string_single_obj(window.user_bind_event)}', c='white on green')
    window.close()


# ========================== 3 - EXAMPLE - Element-level binding ========================================================
def main_example3():
    sg.Print(font='Default 16', keep_on_top=True, size=(60, 14), relative_location=(850, -150))

    layout = [[sg.Text('Binding At Element-level')],
              [sg.Multiline(size=(40, 10), key='-MLINE-')],
              [sg.Multiline(size=(40, 10), key=('-MLINE-', 2))],
              [sg.Button('Exit')], ]

    window = sg.Window('Tkinter Binding 3', layout, finalize=True)

    window['-MLINE-'].bind('<Control-x>', '+X')
    window['-MLINE-', 2].bind('<Enter>', 'Enter Tuple Addition')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-MLINE-+X':
            sg.Print('CONTROL X FOUND')

        sg.Print(f'event = {event}', c='white on red')
        sg.Print(f'values = {values}', c='white on red')

        if window['-MLINE-'].user_bind_event is not None:
            sg.Print(f'Event = {sg.obj_to_string_single_obj(window["-MLINE-"].user_bind_event)}', c='white on green')

    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
