"""
Lesson 22
Exercise 1

Use an output element to print the numbers 2 to 500
Print the prime numbers as white on red background
Print all the other numbers normally with no color change than the default
Instructions

    Use a Multiline element as an output element
        In your layout, set parameter so that no values are returned for the element when window is read
        Make the size of your Multliline be 10 chars wide by 25 rows high
    Use the Multiline Element's print method for the output
    If you can't figure out how to determine a prime number, check the hints
    Use a Button (e.g. named "Start") to start the printing
    At the top of the window show the text "Prime numbers 2 to 500". Use the same text for the Window's title
    Remember to always check to see if the window has been closed after you read it.
import PySimpleGUI as sg

layout = [  ]

window = sg.Window('', layout)

while True:
    event, values = window.read()

window.close()
"""
import PySimpleGUI as sg

# # Solution 1:
#
# layout = [  [sg.Text('Prime Numbers 2 to 500')],
#             [sg.Multiline(size=(10, 25), write_only=True, key='-MLINE-')],
#             [sg.Button('Start')]  ]
#
# window = sg.Window('Prime Numbers 2 to 500', layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event == 'Start':
#         for num in range(2, 501):
#             prime=True
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     prime = False
#                     break
#             if prime:
#                 window['-MLINE-'].print(num, colors='white on red')
#             else:
#                 window['-MLINE-'].print(num)
#
# window.close()

# Solution 2:
layout = [  [sg.Text('Prime Numbers 2 to 500')],
            [sg.Multiline(size=(10, 25), write_only=True, key='-MLINE-')],
            [sg.Button('Start')]  ]

window = sg.Window('Prime Numbers 2 to 500', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Start':
        for num in range(2, 501):
            for i in range(2, num):
                if (num % i) == 0:
                    window['-MLINE-'].print(num)
                    break
            else:   # executed if the for loop completed NORMALLY (no break statement)
                window['-MLINE-'].print(num, colors='white on red')
window.close()