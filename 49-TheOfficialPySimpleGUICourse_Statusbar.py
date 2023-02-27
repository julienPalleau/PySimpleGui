"""
The Official Python GUI Programming with PySimpleGUI Course
StatusBar Element - Show a "status bar" (normally at the bottom of the window)
Aliases: Sbar
Additional methods:

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 1

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(850, -300))

    menu_def = [['&File', ['&Open', '&Save', ['A', 'B'], '&Properties', '---', 'E&xit']],
                ['&Edit', ['Copy', 'Paste', ['Paste', 'As Plain Text'], 'Undo'], ],
                ['&Options', ['Command &1::Command key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['!Disabled', ['Will not be visible', 'Because disabled']],
                ['&Help', ['&About...']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Multiline(size=(80, 20), key='-MLINE-', expand_x=True, expand_y=True, enable_events=True,
                            rstrip=False)],  # if rstrip is put to true il won't count the number of lines correctly
              [sg.StatusBar('My Statusbar', key='-STATUS-')],
              [sg.Text('My Statusbar', expand_x=True, relief=sg.RELIEF_SUNKEN, key='-TEXT-')]]
    # the two lines above sg.StatusBar and sg.Text are doing the same thing, it is however recommended to use sg.Text
    # because the text element is going to continue to be enhanced over time while StatusBar mostly will not

    window = sg.Window('Statusbar', layout, margins=(0, 0), resizable=True, finalize=True)

    window.set_min_size(window.size)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        lines = len(values["-MLINE-"].split("\n")) - 1

        window['-STATUS-'].update(f'Lines: {lines}')
        window['-TEXT-'].update(f'Lines: {lines}')

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)


if __name__ == "__main__":
    example = [main_example]
    example[example_number - 1]()
