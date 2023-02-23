"""
The Official Python GUI Programming with PySimpleGUI Course

Tab & TabGroup Elements - Container Elements
    (Others container Elements - Column, Frame, Pane)
Aliases:
    None

Docs: http://wwww.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#tab-element
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 1

sg.set_options(font='Default 16', keep_on_top=True)


def main_example1():
    tab1 = sg.Tab('Tab 1', [[sg.T('Row A')],
                            [sg.T('Row B')],
                            [sg.T('Row C')]])

    tab2 = sg.Tab('Tab 2', [[sg.Text('Row 1')],
                            [sg.Text('Row 2')]])

    layout = [[sg.TabGroup([[tab1, tab2]])],
              [sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


if __name__ == "__main__":
    example = [main_example1]
    example[example_number - 1]()