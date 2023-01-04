"""
The official python GUI programming with PySimpleGUI Course
Lesson 1

Documentation
    https://www.pysimplegui.org/en/latest/
Built in Help:
    Built-in help: sg.sdk_help()
"""

# 1 - Import
import PySimpleGUI as sg
sg.set_options(font='Default 18', keep_on_top=True)

# 2 - Layout
layout = [
            [sg.Text('Hello, World!')],
            [sg.Button('Ok')],
        ]

# 3 - Window
window = sg.Window('Title', layout)

# 4 - Event loop / handling
event, value = window.read()

# 5 - Close
window.close()