"""
The Official Python GUI Programming with PySimpleGUI Course

Multiline Element
    Scrolled text input/Output

Multiline Input
    Docs: http://www.PySimpleGUI.org
    Buit-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 18')
sg.Print('Multiline Input', c='white on red', font='Default 14', keep_on_top=True, size=(60, 10), location=(1400, 130))
example_number = 1


# ================================== TEXT, INPUT, MULTILINE EXAMPLE ====================================================

def main_text_input_multiline():
    # -------------------- Layout & Window
    layout = [
        [sg.Text('This is multiple line\nof text, but no\nscrollbar')],
        [sg.Input(size=(30, 1), key='-IN-')],
        [sg.Multiline(size=(30, 10), k='-MLINE IN-')],
        [sg.Button('Go'), sg.Button('Exit')]
    ]

    window = sg.Window('Basic Multiline Comparison', layout, keep_on_top=True)

    # -------------------- Event loop
    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end='')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()


if __name__ == '__main__':
    main_text_input_multiline()


# ================================== NOTEPAD EXAMPLE ===================================================================
def main_notepad():
    # ---------------------------- Layoue & Window
    layout = [
        [sg.Multiline(size=(80, 25), k='-MLINE IN-')],
        [sg.Button('Open'), sg.Button('Save'), sg.Button('Exit')],
    ]
    window = sg.Window('Mini-Notepad', layout, keep_on_top=True, finalize=True, location=(260, 120))

    # ---------------------------- Event Loop
    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end='')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Open':
            with open(__file__, 'r') as f:
                window['-MLINE IN-'].update(value=f.read())

    window.close()


if __name__ == '__main__':
    main_notepad()
