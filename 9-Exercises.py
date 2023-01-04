"""
    The Official Python GUI Programming with PySimpleGUI Course

    Basic Element Methods & Properties

    12 Element Methods (available for all elements):
        SetFocus (don't use... use set_focus instead)
        SetTooltip (don't use.... use set_tooltip instead)
        bind - enables specific tkinter events for an element
        expand - controls how elements resize themselves
        get_size - returns element size
        hide_row - hides the row an element is on
        set_cursor - shows this cursor when mouse is over element
        set_focus - moves the input focus to the element
        set_size - changes size for element
        set_tooltip - changes tooltip for element
        set_vscroll_position - if element has scrollbar, changes position
        unbind - unbind a previous bind
        unhide_row - unhide a previously hidden row
        update - changes an element (each element has a UNIQUE update method)

    2 Properties
        metadata - read/write anything
        visible - readonly bool

    http://www.PySimpleGUI.org

import PySimpleGUI as sg



def main():
    txt = sg.Text('An element to update', k='-TXT-')

    layout = [
              [txt],
              [sg.Input(key='-IN1-', tooltip='Initial tooltip')],
              [sg.Input(key='-IN2-', size=(10,1))],
              [sg.Multiline(size=(40,10), k='-ML-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Text(size=(40, 1), key='-VALUES-')],
              [sg.Button('Go'), sg.B('Scroll'), sg.B('Focus2'),sg.B('Expand2'), sg.B('Size'), sg.B('Tooltip'), sg.Button('Exit')],
              ]

    window = sg.Window('Window Title', layout, keep_on_top=True, font='Default 16', finalize=True, resizable=True)


    while True:             # Event Loop
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Focus2':
            window['-IN2-'].set_focus()
        if event == 'Expand2':
            window['-ML-'].expand(True, True)
        if event == 'Size':
            window['-IN2-'].set_size((30,None))
            window.refresh()
            print(f"size = {window['-IN2-'].get_size()}")
        if event == 'Tooltip':
            window['-IN1-'].set_tooltip('New tooltip')
        if event == 'Scroll':
            window['-ML-'].set_vscroll_position(.5)

        window['-OUT-'].update(f'EVENT: {event}')
        window['-VALUES-'].update(f'VALUES: {values}')

    window.close()


if __name__ == '__main__':
    main()
"""
import PySimpleGUI as sg


layout = [  [sg.Text(r'http://www.PySimpleGUI.org', key='-TEXT-')],
            [sg.Input(size=(10,1), tooltip='Input text', key='-IN-')],
            [sg.Multiline(size=(30,10), key='-ML-')],
            [sg.Button('Tooltip'), sg.Button('Focus')]
        ]   # Add your layout

window = sg.Window('Lesson 9 - Common Methods', layout, finalize=True)

window.set_cursor('hand1')
window['-IN-'].bind('<Escape>', '+escape')

# You'll be adding some code here
while True:
    event, values = window.read()
    # something goes here
    print(event)
    # and you'll add your event processing here
    if event == sg.WIN_CLOSED:
        break
    if event == 'Focus':
        window['-ML-'].set_focus()
    if event == 'Tooltip':
        window['-IN-'].set_tooltip('New Tooltip')

window.close()