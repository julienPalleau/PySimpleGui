"""
https://www.pysimplegui.org/en/latest/
"""
import PySimpleGUI as sg

window = sg.Window('Title', [[sg.Text('Do you want to continue?')], [sg.Button('Yes'), sg.Button('No'), sg.Button('Exit')]])

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Yes':
        print("YES!")
    elif event == 'No':
        print('NO!')


window.close()