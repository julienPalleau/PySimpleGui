"""
The Official Python GUI Programming with PySimpleGUI Course
Shortcut & Aliases

Types of shortcuts:
    Element names shortened
    PEP8 compliant aliases
    Function/method call replacemnets

Element shortcuts:
    Input I
    Input In
    Input InputText
    Combo DD
    Combo Drop
    Combo DropDown
    Combo InputCombo
    OptionMenu InputOptionMenu
    Listbox LB
    Listbox LBox
    Radio R
    Radio Rad
    Checkbox CB
    Checkbox CBox
    Checkbox Check
    Spin Sp
    Multiline ML
    Multiline MLine
    Text T
    text Txt
    StatusBar SBar
    Button B
    Button Btn
    ButtonMenu BM
    ButtonMenu BMenu
    ProgressBar PBar
    ProgressBar Prog
    ProgressBar Progress
    Image Im
    Graph G
    Frame Fr
    VerticalSeparator VSep
    VerticalSeparator VSeparator
    VerticalSeparator Vseparator
    HorizontalSeparator HSep
    HorizontalSeparator HSeparator
    Slider Sl
    Column Col
    Menu MenuBar

PEP8 Variables
CamelCase =
snake_case = variables, funcs


    https://www.pysimplegui.org/en/latest/#elements
"""
import PySimpleGUI as sg
# sg.main_sdk_help() # the shortcut is at the end of each section i.e Button Input Multiline etc...

# you can create your own shortcut
PBJ = sg.ProgressBar
T = sg.Text


def main():
    layout = [[sg.Text('My Window')],
              [PBJ(10)],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    layout = [[T('My Window')],
              [sg.I(k='-IN-')],
              [T(size=(30, 1), k='-OUT-')],
              [sg.B('Go'), sg.B('Exit')]]

    window = sg.Window('Window Title', layout)

    while True:     # Event loop

        # the two line below are the same the second line use a shortcut without .read()
        event, values = window.read()
        event, values = window()

        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # the two line below are the same the second line on use a shortcut with [] instead of .find_element
        # window.find_element('-OUT-').update(f'You clikcked {event}')
        window['-OUT-'].update(f'You clikcked {event}')

    window.close()

if __name__ == '__main__':
    main()