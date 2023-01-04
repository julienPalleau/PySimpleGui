import PySimpleGUI as sg

# when creating keys, keep in mind to follow the coding convention '-ELEMENT-'
layout = [[sg.Input(key='-INPUT-')],
          [sg.Button('Print')]]

window = sg.Window('Keys!', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Print':
        # the values variable is a dictionary that holds the values of capable elements
        # access the value using the element's key
        print(values['-INPUT-'])

window.close()