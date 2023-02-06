"""
The Official Python GUI Programming with PySimpleGUI Course

ButtonMenu Element - Button the appears like a right click menu
    Aliases = BMenu, BM

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""

import PySimpleGUI as sg

example_number = 2

sg.theme('Dark Red')
# sg.theme('Dark Gray 13')

sg.set_options(font='Default 18')
sg.Print('', font='Default 18', keep_on_top=True, size=(45, 8), location=(198, 50))


# ================================ 1 - ButtonMenu Basic Operation EXAMPLE ==============================================
def main_menu():
    menu_def = ['not used', ['Item 1', 'Has Submenu', ['1', '2'], '!Disabled', '---', 'WithKey::KeyIsHere', 'Exit']]
    menubar_def = [['&File', ['&Open', '&Save', ['A', 'B'], '&Properties', '---', 'E&xit']],
                   ['&Edit', ['Copy', 'Paste', ['Paste', 'As Plain Text'], 'Undo'], ],
                   ['&Options', ['Command &1::Command_key', 'Command &2', '---', 'Command &3', 'Command &4']],
                   ['&Help', ['&About...']]]

    layout = [[sg.Menu(menubar_def, key='-MENU BAR-')],
              [sg.MenubarCustom(menubar_def)],
              [sg.Text('ButtonMenu - Right click here', right_click_menu=menu_def)],
              [sg.ButtonMenu('Button Menu', menu_def, border_width=0, key='-BUTTON MENU-',
                             background_color=sg.theme_background_color(),
                             text_color=sg.theme_text_color())]]

    window = sg.Window("Menubar Lesson", layout, keep_on_top=True, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


# ================================ 2 - ButtonMenu Updates EXAMPLE ======================================================
def main_menu_updates():
    sg.theme('Dark Red')

    menu_def = ['', ['Item 1', 'Has Submenu', ['1', '2'], '!Disabled', 'WithKey::KeyIsHere', 'Exit']]

    layout = [[sg.Text('ButtonMenu')],
              [sg.pin(sg.ButtonMenu('Button Menu', menu_def, key='-BUTTON MENU-'))],
              [sg.B('Go'), sg.B('Invisible'), sg.B('Visible'), sg.B('Change Disable'), sg.B('Exit')]]

    window = sg.Window("Menubar_Lesson", layout, keep_on_top=True, finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Invisible':
            window['-BUTTON MENU-'].update(visible=False)
        elif event == 'Visible':
            window['-BUTTON MENU-'].update(visible=True)
        elif event == 'Change Disable':
            menu_def[1][3] = 'Enabled'
            window['-BUTTON MENU-'].update(menu_def)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')
    window.close()


if __name__ == "__main__":
    example = [main_menu, main_menu_updates]
    example[example_number - 1]()