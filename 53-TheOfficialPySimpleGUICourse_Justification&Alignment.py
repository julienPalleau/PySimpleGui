"""
The Official Python GUI Programming with PySimpleGUI Course

Element Justification and Alignment
    Positionning of elements within a row, contaniner, and window

Containers:
    Column & Frame

Layout Helpful Funcs:
    vtop, vcenter, vbottom

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3
sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    layout = [[sg.Text('My Group of Elements')],
              [sg.In(size=25)],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    layout = [[sg.VPush()]] + \
             layout + \
             [[sg.VPush()]]

    window = sg.Window('Element Justification & Alignment 1', layout, element_justification='c', size=(500, 500))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    layout = [[sg.Col([[]], size=(500, 20), p=0, background_color='red')],
              [sg.Text('My Group of Elements')],
              [sg.In(size=25)],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # layout = [[sg.Col([[]], size=(500, 20), p=0, background_color='red')]] + layout
    centered_layout = sg.Column(layout, element_justification='c', pad=0)
    layout = [[sg.Col([[]], size=(20, 500), p=0, background_color='yellow'), centered_layout]]
    window = sg.Window('Element Justification & Alignment 2', layout, margins=(0, 0))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


# ========================== 3 - EXAMPLE ===============================================================================
def main_example3():
    layout = [[sg.pin(sg.Text('A Row of Various Elements'), vertical_alignment='t'), sg.vtop(sg.Listbox(list(range(10)), size=(5, 4))), sg.Multiline(size=(20, 8))]]
    window = sg.Window('Justification & Alignment 3', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
