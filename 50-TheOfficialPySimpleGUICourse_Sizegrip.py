"""
The Official Python GUI Programming with PySimpleGUI Course
Sizegrip - Getting a better grip on your risizable windows
alias : SGrip

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#sizegrip-element

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3

sg.theme('Light Green 6')
sg.set_options(font='Default 18', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    layout = [[sg.Text('My Window with a Sizegrip')],
              [sg.Text('Sizegrip -------------------->'), sg.Push(), sg.Sizegrip(background_color='red')]]
    window = sg.Window('Sizegrip Element - Example 1', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in ('Exit', sg.WIN_CLOSED):
            break
    window.close()


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    layout1 = [[sg.Text('Normal window WITHOUT Sizegrip')],
               [sg.Text('Last row')]]

    window1 = sg.Window('Window Title', layout1, finalize=True)

    layout2 = [[sg.Text('Normal window WITH Sizegrip')],
               [sg.Text('Last row'), sg.Sizegrip()]]

    window2 = sg.Window('Window Title', layout2, finalize=True, resizable=True, relative_location=(0, -200),
                        margins=(0, 0))

    while True:
        window, event, values = sg.read_all_windows()
        if event in ('Exit', sg.WIN_CLOSED):
            break

    window.close()


# ========================== 3 - EXAMPLE ===============================================================================
def main_example3():
    layout = [[sg.Text('My Window with a Sizegrip')],
              [sg.Multiline(size=(40, 10), expand_x=True, expand_y=True)],
              [sg.Button('Ok'), sg.Button('Cancel'), sg.Sizegrip()]]

    window = sg.Window('Sizegrip Element - Example 3', layout, resizable=True, margins=(0, 0), finalize=True)
    window.set_min_size(window.size)  # it blocks the resizable to the minimum size of window.size. Without that button
    # will disappear while make the window too small.

    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
