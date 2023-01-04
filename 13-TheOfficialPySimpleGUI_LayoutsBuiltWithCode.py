"""
    The Official Python GUI Programming with PySimpleGUI Course

    Building Layouts
        Using code to create and extend layouts

    Docs: http://www.PySimpleGUI.org
    Built-in help: sg.sdk_help()

    Copyright 2021 PySimpleGUI

    PySimpleGUI Demo Program: psgdemos from terminal
"""

import PySimpleGUI as sg

example_number = 1

sg.set_options(font='Default 16', keep_on_top=True)



#========================== 1 - EXAMPLE - for loop  ==========================

# def main_example1():
#
#     row = []
#     for i in range(4):
#         row.append(sg.Button(i))
#
#     layout = [row]
#
#     window = sg.Window('Generated Layouts 1', layout)
#
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break
#
#     window.close()
#
# if __name__ == '__main__':
#     main_example1()


#========================== 2 - EXAMPLE - List Comprehension  ==========================
# example_number = 2
#
# def main_example2():
#     window = sg.Window('Generated Layouts 2', [[sg.Button(i) for i in range (4)]])
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break
#
#     window.close()
#
# if __name__ == '__main__':
#     main_example2()

# ========================== 3 - EXAMPLE - List Comprehension  ==========================
# example_number = 3
# def main_example3():
#     layout = [[sg.Button(i)] for i in range (4)]
#     window = sg.Window('Generated Layouts 3', layout)
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break
#
#         window.close()
#
# if __name__ == '__main__':
#     main_example3()

# # ========================== 4 - EXAMPLE - List Comprehension - dual  ==========================
# example_number = 4
# def main_example4():
#     layout = [[sg.Button(f'row {row} col {col}') for col in range(4)] for row in range(5)]
#     window = sg.Window('Generated Layout 4', layout)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break
#     window.close()
#
# if __name__ == '__main__':
#     main_example4()

# # ========================== 5 - EXAMPLE - Addition of lists - one a row  ==========================
# example_number = 5
# def main_example5():
#     # [a] + [b] = [a, b]
#
#     # the two lines below are identical only the syntax change but you got the same result
#     layout = [[sg.Text('Row 1')] + [sg.Text('Also row 1')]]
#     # layout = [[sg.Text('Row 1')], [sg.Text('Also row 1')]]
#
#     window = sg.Window('Generated Layouts 5', layout)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break
#     window.close()
#
# if __name__ == '__main__':
#     main_example5()

# # ========================== 6 - EXAMPLE - Addition of layouts  ==========================
# example_number = 6
# def main_example6():
#
#     use_ok = True
#     layout = [[sg.Text('My Group of Elements')],
#               [sg.In(size=25)]]
#
#     if use_ok:
#         layout += [[[sg.In()], sg.Button('Ok'), sg.Button('Cancel')]]
#     else:
#         layout += [[sg.Button('Go'), sg.Button('Exit')]]
#
#     window = sg.Window('Generated Layout 6', layout)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
#             break
#     window.close()
#
# if __name__ == '__main__':
#     main_example6()

# # ========================== 7 - EXAMPLE - Addition of layouts  ==========================
example_number = 7
def main_example7():

    use_ok = True
    layout = [[sg.Text('My Group of Elements')],
              [sg.In(size=25)],
              [sg.Column([[]], key='-COL-')],
              # [sg.Frame('Frame', [[]], key='-COL-')],
              [sg.Button('Go'), sg.Button('Exit')]
             ]

    window = sg.Window('Generated Layout 7', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
            break
        if event == 'Go':
            window.extend_layout(window['-COL-'], [[sg.Text('My New Row1!')],
                                                   [sg.Text('My New Row2!')]])
    window.close()

if __name__ == '__main__':
    main_example7()