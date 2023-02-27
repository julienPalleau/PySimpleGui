"""
The Official Python GUI Programming with PySimpleGUI Course
Push and VPush Elements - Use to "Push" your elements around in your layouts

Aliases:    Push - Stretch, P
            VPush - VStretch, VP

Additional methods:

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#push-element-alias-include-p-and-stretch

Built-in help: sg.sdk_help()
"""

import PySimpleGUI as sg

example_number = 3
sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    layout = [[sg.Text('Left justified element')],
              [sg.Push(background_color='red'), sg.Text('Right justified element')],
              [sg.Push(), sg.Text('Centered element'), sg.T('1234'), sg.Push()],
              [sg.Button('Ok'), sg.Button('Cancel')],
              [sg.VPush(), sg.Sizegrip()]]

    window = sg.Window('Push Element 1', layout, resizable=True, background_color='red')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)

    window.close()


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    layout = [[sg.VPush()],
              [sg.Push(), sg.Text('Centered in the window'), sg.Push()],
              [sg.Push(), sg.Button('Ok'), sg.Button('Cancel'), sg.Push()],
              [sg.VPush(), sg.Sizegrip()]]

    window = sg.Window('flush Element 2', layout, resizable=True, size=(500, 500))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)

    window.close()


# ========================== 3 - EXAMPLE ===============================================================================
def main_example3():
    layout = [[sg.Text('Using Push For Alignment')],
              [sg.Text('Mame'), sg.P(), sg.In(size=15)],
              [sg.Text('Address'), sg.P(), sg.In(size=15)],
              [sg.Text('Phone'), sg.P(), sg.In(size=15)],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    window = sg.Window('Push Element 3', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
