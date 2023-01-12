"""
The Official Python GUI Programming with PySimpleGUI Course

Output Element
    Scrolled stdout/stderr output

Docs: https://www.pysimplegui.org/en/latest/call%20reference/#output-element-no-longer-recommended-use-multiline-instead
Built-in help: sg.sdk_help()
"""
import threading

import PySimpleGUI as sg

sg.set_options(font='Default 18')

example_number = 1


# ================================== 1 - Basic "print" EXAMPLE =========================================================

def main_output():
    layout = [[sg.T('Text Output Using Output Element')],
              [sg.Output(size=(40, 15), echo_stdout_stderr=True, k='-OUTPUT-'),
               sg.B('Go'), sg.B('Erase'), sg.B('Crash'), sg.B('Exit')]]

    window = sg.Window('Multiline Output', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Erase':
            window['-OUTPUT-'].update('')
        elif event == 'Crash':
            sg.bad_call()
    window.close()


# ================================== 2 - print FROM THREAD EXAMPLE =====================================================
import time


def print_thread():
    counter = 0
    sg.popup('Hello')
    while True:
        print(f'Thread counter = {counter}')
        counter += 1
        time.sleep(1)


def main_output_with_thread():
    layout = [
        [sg.Output(size=(40, 15)),
         sg.B('Go'), sg.B('Thread'), sg.B('Exit')]]

    window = sg.Window('Multiline.print()', layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Go':
            pass
        elif event == 'Thread':
            threading.Thread(target=print_thread, daemon=True).start()
    window.close()


if __name__ == "__main__":
    examples = [main_output, main_output_with_thread]
    print(examples[example_number - 1].__name__)

    examples[example_number - 1]()
