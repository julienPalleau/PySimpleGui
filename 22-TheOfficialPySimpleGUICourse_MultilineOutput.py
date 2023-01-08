"""
The Official PythonGUI Programming with PySimpleGUI Course
Multiline Element
    Scrolled text input/output

Multiline Output
cprint

Docs: https://www.pysimplegui.org/en/latest/call%20reference/#multiline-element
Built-in hlep: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 18')

example_number = 1


# ================================== 1 - MULTILINE update & "print" EXAMPLE ============================================
def main_mline_update():
    mkey = '-MLINE-'

    layout = [[sg.T('Multiline Output Using .update')],
              [sg.Multiline(size=(40, 15), key=mkey)],
              [sg.B('Go'), sg.B('Erase'), sg.B('Reroute'), sg.B('Restore'), sg.B('Exit')]]
    

