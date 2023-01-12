"""
The Official Python GUI Programming with PySimpleGUI Course

Multiline Element
    Scrolled text input/Output

Multiline Input
    Docs: http://www.PySimpleGUI.org
    Buit-in help: sg.sdk_help()
"""
import PySimpleGUI as sg


#
sg.set_options(font='Default 18')
sg.Print('Multiline Input', c='white on red', font='Default 14', keep_on_top=True, size=(60, 10), location=(1400, 130))
example_number = 3


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


# ================================== NOTEPAD EXAMPLE ===================================================================
def main_notepad():
    # ---------------------------- Layout & Window
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


# ================================== CHAT EXAMPLE ======================================================================
def main_chat():
    # ---------------------------- Layoue & Window
    layout = [
        [sg.Output(size=(40, 10))],
        [sg.Multiline(size=(40, 4), k='-MLINE IN-', justification='r', focus=True,
                      enable_events=True),
         sg.B('Send', bind_return_key=True), sg.Exit()]
    ]
    window = sg.Window('Chat', layout, keep_on_top=True)

    # ---------------------------- Event loop
    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end=' ')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == '-MLINE IN-':
            window['-MLINE IN-'].update(values['-MLINE IN-'], justification='r')
        if event == 'Send':
            mline_clean = values['-MLINE IN-'][:-2]
            print(f'You entered: "{mline_clean}"')
    window.close()


if __name__ == '__main__':
    examples = [main_text_input_multiline, main_notepad, main_chat]
    print(examples[example_number - 1].__name__)

    examples[example_number - 1]()
