"""
The Official Python GUI Programming with PySimpleGUI Course
PSG Distribution Utilities
    Programs to help you distribute and use PySimpleGUI programs (by creating EXE files for example)

Utilities:
    psgcompiler - Front-end to PyInstaller
    psgshortcut - Create double-clickable icons for your Python programs
    psgresizer - Convert and resize images
    sgfiglet - Make figlets for your code

Comes with pip install of PySimpleGUI:
    psgmain - Same as calling
    psgissue - Open GitHub issue
    psgupgrade - Upgrade to use latest from GitHub
    psghelp - SDK Help Window
    psgver - Show version information
    psgsettings - Show settings window

Docs:
    http://www.PySimpleGUI.org
    https://pysimplegui.readthedocs.io/en/latest/call%20reference/#exec-apis-launching-subprocesses

Built-in help: sg.sdk_help()

Copyright 2021 PySimpleGUI
"""
import PySimpleGUI as sg

example_number = 0

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    psg_apps = ['psgcompiler', 'psgshortcut', 'psgresizer', 'psgfiglet']
    psg_builtins = ['psgmain', 'psgissue', 'psgupgrade', 'psghelp', 'psgver','psgsettings']

    layout = [[sg.Text('PSG Applications - Launcher')],
              [sg.Button(app) for app in psg_apps],
              [sg.Button(app, button_color='yellow on green') for app in psg_builtins],
              [sg.Button('Main'), sg.Button('Exit')]]

    window = sg.Window('psg utilities', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Main':
            sg.main()
        else:
            sg.execute_command_subprocess(event)


    window.close()

if __name__ == "__main__":
    example=[main_example1]
    example[example_number - 1]()