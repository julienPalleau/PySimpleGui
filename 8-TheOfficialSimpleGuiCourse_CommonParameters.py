"""
The Official Python GUI Programming with PySimpleGUI Course

Parameter definition found here:
    Online documentation
    Docstrings (in IDE)
    sg.main's SDK reference button

Parameters in PySimpleGUI used when:
    Create Elements
    Call update() for Elements

Common Element Parameters
    key
    font
    pad
    visible
    size
    colors (text, background, button, etc)
    enamble_events
    right_click_menu
    tooltips
    metadata

Defaults valeues set / chosen from:
    Element
    Window
    Program (set_options)

Color defaults are from theme

Parameters in documnetation, doc strings, or call sg.main_sdk_help()
http://www.PySimpleGUI.org
"""
import PySimpleGUI as sg
# sg.set_options(font='Helvetica 18')
# sg.main_sdk_help()

def main():
    right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties::KEY']]

    font1 = 'Courier 18'
    font2 = 'Courier 18 underline italic'
    font3 = ('Courier, 18')
    font4 = ('Courier', 18, 'underline italic overstrike')

    layout = [[sg.Text('Test of fonts', font=font1)],
              [sg.Text('Test of fonts', font=font2)],
              [sg.Text('Test of fonts', font=font3)],
              [sg.Text('Test of fonts', font=font4)],
              [sg.Text('Padding', pad=(0, 0)), sg.Text('Padding', pad=(0,0))],
              [sg.Text('Padding'), sg.Text('Padding')],
              [sg.Text('Padding', pad=((5, 50), (10, 20))), sg.Text('Padding')],
              [sg.Text('Invisible', visible=False), sg.Text('Visible', visible=True)],
              [sg.Text('Right Click Me', right_click_menu=right_click_menu)],
              [sg.Text('Left Click Me', enable_events=True, key='-Text-')],
              [sg.Text('Colors parms', background_color='white', text_color='#FF0000')],
              [sg.Text('Metadata', metadata='MY METADATA', key='-META-', tooltip='has metadata')],
              [sg.Text()],
              [sg.Text(size=(40,1), key='-OUT-', font='Courier 18')],
              [sg.Button('Go'), sg.Button('Exit')]

    ]

    window = sg.Window('Window Title', layout, keep_on_top=True)

    while True:         # Event loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT-'].update(f'Event={event}')
        print(window['-META-'].metadata)

    window.close()

if __name__ == '__main__':
    main()
