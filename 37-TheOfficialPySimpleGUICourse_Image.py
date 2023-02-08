"""
    The Official Python GUI Programming with PySimpleGUI Course

    Image Element - Display PNG & GIF Images
        Aliases = Image, Im

        Additional methods = update_animation, update_animation_no_buffering

    Docs: http://www.PySimpleGUI.org
    Built-in help: sg.sdk_help()

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg

example_number = 1

sg.set_options(font='Default 18', keep_on_top=True)

sg.Print('', font='Default 18', size=(45, 8), location=(1980, 500))


# ========================== 1 - Image Basic Operation EXAMPLE ==========================

def main_image():
    sg.theme('light green 3')

    layout = [[sg.Image(key='-IMAGE1-', background_color='red', enable_events=True)],
              [sg.Image(sg.EMOJI_BASE64_HAPPY_BIG_SMILE, key='-IMAGE2-', background_color='red', enable_events=True)],
              [sg.Image(sg.DEFAULT_BASE64_ICON, key='-IMAGE4-')],
              [sg.Image(sg.DEFAULT_BASE64_ICON, subsample=2)],
              [sg.B('Happy'), sg.B('Sad'), sg.B('Logo'), sg.B('Erase'), sg.B('Exit')]]

    window = sg.Window("Image Lesson", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Sad':
            window['-IMAGE1-'].update(sg.EMOJI_BASE64_SAD)
        elif event == 'Happy':
            window['-IMAGE1-'].update(sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
        elif event == 'Logo':
            window['-IMAGE1-'].update(r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\logo200.png')
        elif event == 'Erase':
            window['-IMAGE1-'].update(sg.BLANK_BASE64)
            window['-IMAGE2-'].update()

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# window['-IMAGE1-'].update(r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\logo200.png')
if __name__ == '__main__':
    example = [main_image]
    example[example_number - 1]()
