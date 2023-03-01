"""
The Official Python GUI Programming with PySimpleGUI Course

Extending PySimpleGUI
How you can add features without changing the PySimpleGUI source

Element.Widget
Window.TKroot

tkinter documentation:
    https://www.tcl.tk.man/tcl8.6/TkCmd/contents.html

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 2
sg.set_options(font='Default 16', keep_on_top=True)
sg.theme('dark red')


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300))
    color_names = ('red', 'green', 'blue', 'yellow + orange = amber')

    layout = [
        [sg.Listbox(color_names, size=(20, 4), k='-LBOX-')],
        [sg.B('Go'), sg.B('Exit')],
    ]

    window = sg.Window('Extending PySimpleGUI 1', layout, finalize=True)
    widget = window['-LBOX-'].Widget  # type: sg.tk.Listbox
    sg.Print(f'The Spin uses the widget: {type(widget)}')

    widget.config(borderwidth=8, relief=sg.RELIEF_RAISED)
    # Element.ttk_style_name
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')
    window.close()


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300))
    layout = [
        [sg.B('Go'), sg.B('Exit')],
    ]

    window = sg.Window('Extending PySimpleGUI 2', layout, finalize=True)
    root = window.TKroot    # type: sg.tk.Toplevel
    sg.Print(f'The window has root object of type: {type(root)}')
    sg.Print(root.winfo_geometry())

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2]
    example[example_number - 1]()
