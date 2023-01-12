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
    mkey = '-MLINE-' + sg.WRITE_ONLY_KEY

    layout = [[sg.T('Multiline Output Using .update')],
              [sg.Multiline(size=(40, 15), key=mkey, disabled=True, autoscroll=True),
               sg.B('Go'), sg.B('Erase'), sg.B('Reroute'), sg.B('Restore'), sg.B('Exit')]]

    window = sg.Window('Multiline Output', layout, keep_on_top=True)

    mline = window[mkey]  # type: sg.Multiline

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Erase':
            mline.update('')
            continue
        elif event == 'Reroute':
            mline.reroute_stdout_to_here()
        elif event == 'Resotre':
            mline.restore_stdout()

        mline.update(f'event = {event} ', append=True)
        mline.update(f'values = {values}\n', append=True)
    window.close()


# ================================== 2 - MULTILINE print EXAMPLE =======================================================
def main_mline_print():
    mkey = '-MLINE-'
    layout = [[sg.T('Multiline Output Using Multiline.print()')],
              [sg.Multiline(size=(40, 15), key=mkey, write_only=True, disabled=True, autoscroll=True),
               sg.B('Go'), sg.B('Right Justified'), sg.B('Exit')]]

    window = sg.Window('Multiline.print()', layout, keep_on_top=True)

    mline = window[mkey]  # type: sg.Multiline
    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Go':
            mline.print(f'event = {event}', text_color='red')
            mline.print(f'values = {values}', background_color='yellow')
        elif event == 'Right Justified':
            mline.print(f'event = {event}', t='red', justification='r')
            mline.print(f'values = {values}', t='green', justification='r')
    window.close()


# ================================== 3 - cprint EXAMPLE ================================================================
def main_cprint():
    # ----------------------------- Layout & Window
    layout = [[sg.Multiline(size=(40, 20), k='-MLINE-', border_width=True, reroute_stdout=True, echo_stdout_stderr=True,
                            write_only=True, autoscroll=True), sg.B('print'), sg.B('cprint')], ]

    window = sg.Window('Multiline cprint', layout, keep_on_top=True)

    sg.cprint_set_output_destination(window, '-MLINE-')

    # ----------------------------- Event Loop
    while True:
        event, values = window.read()
        # print(event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'print':
            print(f'Event = {event} values = {values}')
        elif event == 'cprint':
            sg.cprint(f'Event = {event} values = {values}', c="white on red")  # c stands for color and there are 2
            # syntax possible: c="white on red" or c = ('white', 'red')

    window.close()


if __name__ == "__main__":
    examples = [main_mline_update, main_mline_print, main_cprint]
    print(examples[example_number - 1].__name__)

    examples[example_number - 1]()
