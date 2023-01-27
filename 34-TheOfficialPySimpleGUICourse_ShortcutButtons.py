"""
    The Official Python GUI Programming with PySimpleGUI Course

    Button Element - Lesson Part 5- Shortcut Buttons

    Shortcut Buttons (also called "Lazy Buttons") are a set of pre-defined buttons that make your layout appear more
    like your window.

    some examples:
        Ok
        Cancel
        Open
        Save
        Submit
        Quit
        Exit
        Yes
        No
        Help

    Docs: http://www.PySimpleGUI.org
    Built-in: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 18')
sg.Print(font='Default 18', keep_on_top=True, size=(30, 14))

example_number = 3


# =========================== 1 - Shortcut Buttons =====================================================================
def main_button_ok_cancel():
    layout = [[sg.T('Shortcut Buttons... The same old Buttons')],
              [sg.Input(key='-IN-')],
              [sg.Ok(), sg.Cancel()]]

    window = sg.Window("Ok and Cancel", layout, keep_on_top=True, use_default_focus=False)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

        if event == 'Ok':
            sg.Print(f'The Ok button is a:', sg.Ok())
    window.close()


# =========================== 2 - All Shortcuts ========================================================================
def main_button_all_shortcuts():
    layout = [[sg.T('Lots to choose from')],
              [sg.Input(key='-IN-')],
              [sg.Ok('Okay'), sg.Cancel(), sg.Open(), sg.Save(), sg.Submit(), sg.Quit(), sg.Yes(), sg.No(), sg.Help(),
               sg.Exit()]]

    window = sg.Window("All shortcuts", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


# =========================== 3 - Your Own Shortcut Buttons ============================================================
def Ok():
    return sg.Button('Ok', size=(6, 1))


def Cancel():
    return sg.Button('Cancel', size=(6, 1))


def main_your_own_shortcuts():
    layout = [[sg.Text('Your own Shortcuts')],
              [Ok(), Cancel()]]

    window = sg.Window("Toggle Button", layout, keep_on_top=True, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f' {k} = {values[k]}' for k in values], sep='\n')
    window.close()


if __name__ == "__main__":
    example = [main_button_ok_cancel, main_button_all_shortcuts, main_your_own_shortcuts]
    example[example_number - 1]()
