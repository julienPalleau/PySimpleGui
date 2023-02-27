"""
The Official Python GUI Programming with PySingleGUI Course
Titlebar, MenubarCustom Element
Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 2
# sg.theme('light green 5')
# sg.theme('dark red')
sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE - Custom Titlebar =============================================================

def main_example1():
    # sg.Print(font='Default 16', keep_on_top=True, size=(,)

    # sg.theme('dark green 7')
    # sg.theme('dark gray 13')
    sg.theme('dark blue 13')
    color_pairs = [['1 - Button Colors', sg.theme_button_color()[0], sg.theme_button_color()[1]],
                   ['2 - Reversed Button Colors', sg.theme_button_color()[1], sg.theme_button_color()[0]],
                   ['3 - Input Colors', sg.theme_text_color(), sg.theme_input_background_color()],
                   ['4 - Reversed Input Colors', sg.theme_input_background_color(), sg.theme_input_text_color()],
                   ['5 - Reversed background & Text', sg.theme_background_color(), sg.theme_text_color()],
                   ['6 - Button Background & Slider', sg.theme_button_color()[1], sg.theme_slider_color()],
                   ['7 - Slider & Button Text', sg.theme_slider_color(), sg.theme_button_color()[0]]
                   ]

    sg.set_options(use_custom_titlebar=True)
    # sg.set_options(titlebar_font = 'default 18', titlebar_icon=sg.DEFAULT_BASE64_ICON)
    # sg.set_options(titlebar_background_color='red', titlebar_text_color='white', titlebar_font='courier 18',
    # titlebar_icons=sg.DEFAULT_BASE64_ICON)

    layout = [
        # [sg.Titlebar('My Custom Titlebar')],
        # [sg.Titlebar('My Custom Titlebar', background_color='red', text_color='white', icon=sg.DEFAULT_BASE64_ICON,
        #              font='_ 18')],
        # [[sg.Titlebar(cp[0], text_color=cp[1], background_color=cp[2])] for cp in color_pairs],
        [sg.Text('My Window')],
        [sg.Input(k='-IN1-')],
        [sg.Input(k='-IN2-')],
        [sg.Input(k='-IN3-')],
        [sg.Button('Popup'), sg.Button('Exit')]
    ]

    # Use the same title so that when the window minimizes, the title will be the same as the custom titlebar title
    # window = sg.Window('My Custom Titlebar', layout)
    window = sg.Window('My Custom Titlebar', layout, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Popup':
            sg.popup('This is a popup')
    window.close()

# ========================== 1 - EXAMPLE - MenubarCustom ===============================================================
def main_example2():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(750, -300))

    sg.theme('dark green 7')

    menu_def = [['&File', ['&Open   Ctrl-0', '&Save Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', ['Me', 'Special', 'Normal',['Normal1', 'Normal2'], 'Undo']],
                ['&Toolbar', ['---', 'Command &1::Command_key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&About...']], ]

    layout = [
                # [sg.Menu(menu_def, background_color='red')],
                [sg.Titlebar(title='This is the custom titlebar', icon=sg.EMOJI_BASE64_HAPPY_BIG_SMILE, font='_ 18')],
                [sg.MenubarCustom(menu_def, pad=(0,0), k='-CUST MENUBAR-')],
                [sg.ButtonMenu('Button Menu', menu_def[1], k='-BUTTON MENU-')],
                [sg.Multiline(size=(70, 20), reroute_cprint=True, write_only=True, no_scrollbar=True, k='-MLINE-')]]

    window = sg.Window("Custom Titlebar with Custom (Simulated) Menubar", layout, finalize=True)

    # ----- Event Loop ----- #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.cprint(f'event = {event}', c=(sg.theme_background_color(), sg.theme_text_color()))
        sg.cprint(f'values = {values}', c=(sg.theme_input_text_color(), sg.theme_input_background_color()))

        # ----- Process menu choices ----- #
        if event == "About...":
            window.disappear()
            sg.popup('About this program', 'Simulated Menubar to accompany a simulated Titlebar', 'PySimpleGUI Version',
                     sg.get_versions(), grab_anywhere=True, keep_on_top=True)

    window.close()


if __name__ == "__main__":
    example = [main_example1, main_example2]
    example[example_number - 1]()
