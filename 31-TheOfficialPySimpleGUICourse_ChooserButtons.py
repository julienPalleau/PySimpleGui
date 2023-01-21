"""
The Official Python GUI Programming with PySimpleGUI Course
Button Element - Lesson Part 2 - Chooser Buttons (type of Button)
    File(s) Browser
    Folder Browser
    Calendar Browser
    Color Chooser

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 12')

example_number = 4


# ============================= 1 - File & Folder Choosers Lessons =====================================================
def main_file_folder_choosers():
    sg.Print('Debug', font='Default 12', keep_on_top=True, size=(30, 12), location=(1200, 350))
    layout = [[sg.Input(k='-IN0-'), sg.FileBrowse()],
              [sg.Input(k='-IN1-'), sg.FileBrowse(file_types=(("All Files", "*.*"), ("Executables", "*.exe")))],
              [sg.Input(k='-IN2-'), sg.FilesBrowse(target='-IN2-', k='-B2-', files_delimiter='+')],
              [sg.Combo(('Folder 1', 'Folder 2'), size=sg.DEFAULT_ELEMENT_SIZE, k='-IN3-'), sg.FileBrowse()],
              [sg.Input(k='-IN4-'), sg.FileSaveAs()],
              [sg.Input(k='-IN5-'), sg.SaveAs()],
              [sg.B('Go'), sg.B('Exit')]
              ]

    window = sg.Window("File & Folder Choosers", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f' {k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ============================= 2 - Color & Calendar Chooser EXAMPLE ===================================================
def main_color_date():
    layout = [
        [sg.Input(k='-IN1-'), sg.ColorChooserButton('Choose Color')],
        [sg.Input(k='-IN2-'), sg.CalendarButton('Date')],
        [sg.B('Go'), sg.B('Exit')]]

    window = sg.Window("Color & Date Chooser", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


# ============================= 3 - Chooser Events EXAMPLE =============================================================
def main_chooser_events():
    layout = [
        [sg.Input(k='-IN1-', enable_events=True), sg.FileBrowse()],
        [sg.Input(k='-IN2-', enable_events=True, visible=False), sg.FileBrowse()],
        [sg.B('Go'), sg.B('Exit')]
    ]

    window = sg.Window('Chooser Events', layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ============================= 4 - Popups Instead of Choosers EXAMPLE =================================================
def main_popup_get_as_chooser():
    starting_value = ''
    layout = [
        [sg.Input(size=(len(starting_value), 1), key='-IN1-', enable_events=True), sg.Button('Browse')],
        [sg.Input(k='-IN2-'), sg.Button('-Date1-')],
        [sg.T('Starting Year:'), sg.Input(size=(5, 1), k='-YEAR-')],
        [sg.Input(k='-IN3-'), sg.Button('-Date2-')],
        [sg.B('Go'), sg.B('Exit')]]

    window = sg.Window("Chooser Using Popups", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Browse':
            filename = sg.popup_get_file('', no_window=True, keep_on_top=True)
            if filename is not None:
                window['-IN1-'].update(filename)
        elif event == '-Date1-':
            date = sg.popup_get_date()
            if date is not None:
                window['-IN2-'].update(date)
        elif event == '-Date2-':
            date = sg.popup_get_date(close_when_chosen=True, start_mon=1, start_day=1, start_year=int(values['-YEAR-']))
            if date is not None:
                window['-IN3-'].update(date)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    example = [main_file_folder_choosers, main_color_date, main_chooser_events, main_popup_get_as_chooser]
    example[example_number - 1]()
