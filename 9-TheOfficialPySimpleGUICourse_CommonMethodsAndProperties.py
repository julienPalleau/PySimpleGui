"""
    The Official Python GUI Programming with PySimpleGUI Course

    Basic Element Methods & Properties

    1 - 12 Element Methods (available for all elements):
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

    2 - Properties
        metadata - read/write anything
        visible - readonly bool

    3 - Available cursors
    X_cursor                dotbox          man                 sizing
    arrow                   double_arrow    midlebutton         spider
    based_arrow_down        draft_large     mouse               spraycan
    based_arrow_up          draft_small     pencil              start
    boat                    draped_box      pirate              target
    bogsity                 exchange        plus                tcross
    bottom_left_corner      fleur           question_arrow      top_left_arrow
    bottom_right_corner     gobbler         right_ptr           top_left_corner
    bottom_side             gumby           right_side          top_right_corner
    bottom_tee              hand1           right_tee           top_side
    box_spiral              hand2           rightbutton         top_edd
    cetenr_ptr              heart           rtl_logo            treck
    circle                  icon            sailboat            ul_angle
    clock                   iron_cross      sb_down_arrow       umbrella
    coffee_mug              left_ptr        sb_h_double_arrow   ur_angle
    cross                   left_side       sb_left_arrow       watch
    cross_reverse           left_tee        sb_right_arrow      xterm
    crosshair               lefbutton       sb_up_arrow
    diamond_cross           ll_angle        sb_v_double_arrow
    dot                     lr_angle        shuttle


    http://www.PySimpleGUI.org
"""

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
              [sg.Button('Go'), sg.B('Visible'), sg.B('Scroll'), sg.B('Focus2'),sg.B('Expand2'), sg.B('Size'),
               sg.B('Tooltip'), sg.Button('Exit')],
              ]

    window = sg.Window('Window Title', layout, keep_on_top=True, font='Default 16', finalize=True, resizable=True)
    # window['-IN2-'].bind('<FocusIn>', '+FOCUSIN2+')
    # window['-IN2-'].bind('<END>', '+END+'
    txt.set_cursor('hand1')

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
        if event == 'Visible':
            print(f"visible={window['-IN1-'].visible}")
        if event == 'Scroll':
            window['-ML-'].set_vscroll_position(.5)

        window['-OUT-'].update(f'EVENT: {event}')
        window['-VALUES-'].update(f'VALUES: {values}')

    window.close()


if __name__ == '__main__':
    main()
