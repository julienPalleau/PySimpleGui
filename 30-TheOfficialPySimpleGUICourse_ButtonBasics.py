"""
The Official Python GUI Programming with PySimpleGUI Course

Button Element
    A clicked element
    Aliases = B, Btn

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import webbrowser

repl_link = r'http://replit.com/@PySimpleGUI/Udemy-Buttons-Lesson-1#main.py'
sg.set_options(font='Default 18')

example_number = 4
sg.Print('', font='Default 18', keep_on_top=True, size=(30, 14), location=(1700, 350))


# sg.theme('gray gray gray')
# sg.theme('Dark Red')

# ============================= 1 - Button Lessons =====================================================================
def main_button_lessons():
    # sg.Print('', font='Default 18', keep_on_top=True, size=(30, 14), location=(1700, 350))

    layout = [[sg.Button('Button'), sg.Text('1.Button Basics')],
              [sg.Button('Browse'), sg.Text('2. Chossers')],
              [sg.Text(sg.SYMBOL_X, pad=((5, 115), (3, 3))), sg.Text('4. Simultated Buttons')],
              [sg.Button('Ok'), sg.Text('5. Shortcut Buttons (aka Lazy/Predefined Button Functions)')]
              ]

    window = sg.Window("Button Lessons", layout, keep_on_top=True, auto_size_buttons=False,
                       default_button_element_size=(10, 1), use_default_focus=False)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        # sg.Print('event = {event}', c='white on red', erase_all=True)
        # sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n'
    window.close()


# ============================= 2 - Basic Button Lessons ===============================================================
def main_button():
    sg.Print('', font='Default 28', keep_on_top=True, size=(30, 14), location=(1700, 350))

    layout = [
        [sg.T('Plain Buttons TK')],
        [sg.Button('Tk', mouseover_colors='blue on gray')],
        [sg.T('Plain Buttons TTK')],
        [sg.Button('TTk5', use_ttk_buttons=True, button_color=('yellow', 'blue'))],
        [sg.Button('TTk', use_ttk_buttons=True, mouseover_colors='blue on gray', disabled=False)],
        [sg.Button('TTk3', use_ttk_buttons=True, disabled_button_color='blue on green', disabled=False)],
        [sg.Button('TTk2', use_ttk_buttons=True)],
        [sg.HorizontalSeparator()],
        [sg.T('Chooser Buttons')],
        [sg.T('Realtime Buttons')],
        [sg.RealtimeButton(sg.SYMBOL_LEFT, key='-LEFT-'), sg.RealtimeButton(sg.SYMBOL_RIGHT, key='-RIGHT')],
        [sg.T('Image Buttons')],
        [sg.Button(image_data=sg.EMOJI_BASE64_HAPPY_HEARTS, button_color=(sg.theme_background_color(),
                                                                          sg.theme_background_color()), border_width=0,
                   k='-EMOJI-')],
        [sg.HorizontalSeparator()],
        [sg.T('Button Shortcuts')],
        [sg.Ok(), sg.Cancel()],
        [sg.HorizontalSeparator()],
        [sg.T('Special Circumstance Close & Dummy Buttons')],
        [sg.CloseButton('CloseButton')],
        [sg.DummyButton('Dummy')],
        [sg.B('REPL')],
        [sg.ButtonMenu(sg.SYMBOL_DOWN_ARROWHEAD, sg.MENU_RIGHT_CLICK_EDITME_EXIT, k='-MENU-')],
    ]
    window = sg.Window("Buttons", layout, keep_on_top=True, finalize=True,
                       right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT, ttk_theme='alt')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'REPL':
            webbrowser.open_new(repl_link)
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')
    window.close()


# ============================= 3 - Button Bind EXAMPLE ================================================================
def main_button_bind():
    layout = [[sg.Text('Key Binding')],
              [sg.Input(k='-IN-')],
              [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel'), sg.Button('Disabled', disabled=True)]
              ]
    window = sg.Window("Bind Example", layout, keep_on_top=True, finalize=True)
    window.bind('<F10>', 'Cancel')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ============================= 3 - Button Bind EXAMPLE ================================================================
def main_button_focus():
    layout = [[sg.Text('Removing Focus From Buttons')],
              [sg.Button('Ok')]]

    window = sg.Window("Bind Example", layout, keep_on_top=True, use_default_focus=False, finalize=True)
    window['Ok'].block_focus()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ============================= 5 - Button Grid EXAMPLE ================================================================
def main_button_grid():
    sg.Print('', font='Default 18', keep_on_top=True, size=(30, 14), location=(1700, 350))

    layout = [[sg.Button(f'({r}, {c})', key=(r, c), pad=(0, 0), border_width=1) for c in range(10)] for r in range(8)]

    window = sg.Window("Grid-0-Buttons", layout, keep_on_top=True, margins=(0, 0))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    example = [main_button_lessons, main_button, main_button_bind, main_button_focus, main_button_grid]
    example[example_number]()