"""
The Official Python GUI Programming with PySimpleGUI Course
Menu Element - The standard Menubar
    Menu
    Aliases = MenuBar, Menubar

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""

import PySimpleGUI as sg

example_number = 2

# sg.theme('Dark Red')
# sg.theme('Dark Gray 13')

sg.set_options(font='Default 18')
sg.Print('', font='Default 18', keep_on_top=True, size=(45, 8), location=(1000, 500))


# ================================ 1 - Menubar Basic Operation EXAMPLE =================================================
def main_menu():
    sg.sdk_help()
    menu_def = [['&File', ['&Open', '&Save', '&Properties', '---', 'E&xit']],
                ['&Edit', ['Copy', 'Paste', ['Paste', 'As Plain Text'], 'Undo'], ],
                ['&Options', ['Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['!Disabled', ['Will not be visible', 'Because disabled']],
                ['&Help', ['&About...']]]

    layout = [[sg.MenuBar(menu_def, key='-MENU BAR-')],
              [sg.Text('MenuBar test                ')],
              [sg.B('Exit')], ]
    window = sg.Window("Menubar Lesson", layout, keep_on_top=True, margins=(0, 0), finalize=True, size=(400, 100))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event={event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

    window.close()


# ================================ 2 - Menubar Updates EXAMPLE =========================================================
def main_menu_updates():
    sg.theme('Dark Red')

    menu_def = [['&File', ['&Open', '&Save', '&Properties', '---', 'E&xit', '!Disabled']],
                ['&Edit', ['Copy', 'Paste', ['Paste', 'As Plain Text'], 'Undo'], ],
                ['&Opitons', ['Command &1::Command_key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['About...']]]

    layout = [[sg.MenuBar(menu_def, key='-MENU BAR-', disabled_text_color='yellow', tearoff=True)],
              [sg.Text('MenuBar Update Operations')],
              [sg.B('Go'), sg.B('Invisible'), sg.B('Visible'), sg.B('Disable Edit'), sg.B('Enable Edit'),
               sg.B('Exit')], ]

    window = sg.Window("Menu Lesson", layout, keep_on_top=True, margins=(0, 0), finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'Invisible':
            window['-MENU BAR-'].update(visible=False)
        elif event == 'Visible':
            window['-MENU BAR-'].update(visible=True)

        elif event == 'Disable Edit':
            menu_def[1][0] = '!Edit'
            window['-MENU BAR-'].update(menu_def)
        elif event == 'Enable Edit':
            menu_def[1][0] = '&Edit'
            window['-MENU BAR-'].update(menu_def)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f' {k}={values[k]}' for k in values], sep='\n')


if __name__ == "__main__":
    example = [main_menu, main_menu_updates]
    example[example_number - 1]()
