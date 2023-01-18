"""


Problemes avec PySimpleGUIQt qui requere pyside2 qui n'est plus dispo pour python 3.11...





The Official Python GUI Programmming with PySimpleGUI Course

Slider Element + PySimpleGUIQT's Dial Element
    Variable amount input/output
    Aliases = Sl
PySimpleGUI & PySimpleGUIQt
    PySimpleGUI & PySimpleGUIQt Slider more than other elements
    Visually different feautres
    PySimpleGUI Sliders support float & ints
    PySimpleGUIQt's sliders are in only (not a big problem as you'll see)

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

# sg.main_sdk_help()


sg.set_options(font='Default 14')

# example_number = 2
#
#
# # ==================================== 1 - Basic Slider EXAMPLE ========================================================
# def main_slider():
#     sg.Print('', font='Default 12', keep_on_top=True, size=(15, 7), location=(1700, 350))
#
#     sg.theme_slider_color('purple')
#     sg.theme_slider_border_width(3)
#
#     layout = [
#         [sg.T('Default Horiz')],
#         [sg.Slider((10, 150), orientation='h', enable_events=True, key='-HORIZ 1-')],
#         [sg.Slider((10, 150), orientation='h', disable_number_display=True, enable_events=True, key='-HORIZ 2-')],
#         [sg.T('Default Vert')],
#         [sg.Slider((10, 150), size=(5, 20), orientation='v', enable_events=True, key='-VERT-'),
#          sg.T('Text', size=(4, 1), k='-TEXT-')],
#         [sg.T('Raised - res 20, ticks 40')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_RAISED, tick_interval=40, resolution=10, orientation='h',
#                    key='-RAISED-')],
#         [sg.T('Sunken - resolution =.3')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_SUNKEN, resolution=.3, orientation='h', key='-SUNKEN-')],
#         [sg.T('Ridge')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_RIDGE, orientation='h', key='-RIDGE-')],
#         [sg.T('Flat')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_FLAT, orientation='h', key='-FLAT-')],
#         [sg.T('Solid')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_SOLID, orientation='h', key='-SOLID-')],
#         [sg.T('Groove')],
#         [sg.Slider((10, 150), relief=sg.RELIEF_GROOVE, orientation='h', key='-GROOVE-')],
#         [sg.B('Go'), sg.B('Exit')]
#     ]
#
#     window = sg.Window("Sliders", layout, keep_on_top=True)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#         sg.Print(f'event = {event}', c='white on red', erase_all=True)
#         sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
#         window['-TEXT-'].update(font=f'_ {int(values["-VERT-"])}')
#     window.close()


# ==================================== 2 - Qt Basic Slider EXAMPLE =====================================================

import PySimpleGUIQt as sg


def main_slider_qt():
    sg.theme('Dark Red')
    sg.Print('', font='Default 18', keep_on_top=True, size=(30, 20), location=(170, 350))

    # sg.theme_slider_border_width(1)

    layout = [
        [sg.T('Default Horiz')],
        [sg.Slider((0, 150), resolution=10, tick_interval=10, orientation='h', size=(40, 30), enable_events=True,
                   key='-S7-')],
        [sg.T('Default Vert')],
        [sg.Slider((0, 150), orientation='v', key='-S8-')],
        [sg.T('Above')],
        [sg.Slider((1, 10), resolution=1, enable_events=True, orientation='h',
                   key='-S1-')],
        [sg.T('Below')],
        [sg.Slider((0, 150), orientation='h', key='-S4-')],
        [sg.T('Right'),
         sg.Slider((0, 100), enable_events=True, orientation='v', key='-S2-'),
         sg.T('Left (float)\n0.0 to 3.0'),
         sg.Slider((0, 100), enable_events=True, orientation='v', key='-S3-'),
         sg.Text(size=(8, 1), key='-TEXT-'),
         sg.Stretch()],
        [sg.T('Both Sides')],
        [sg.Slider((0, 150), orientation='h', key='-S6-')],
        [sg.T('No Ticks')],
        [sg.Slider((0, 150), orientation='h', key='-S5-')],
        [sg.B('Go'), sg.B('Exit')],

    ]
    window = sg.Window("Sliders", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'   {k} = {values[k]}' for k in values], sep='\n')

        window['-TEXT-'].update(3 * values['-S3-'] / 100)
        # font_size = int(values['-SLIDER-'])
        # window['-TEXT-'].update(font=("Helvetica", font_size))
        # window['-SLIDER-'].update(font_size)

        # sg.cprint(f'event = {event}', c='white on red')
        # sg.cprint(*[f'   {k} = {values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    main_slider_qt()
#     example = [main_slider, main_slider_qt]
#     example[example_number - 1]()
