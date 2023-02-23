"""
The Official Python GUI Programming with PySimpleGUI Course
Frame Element - Container Element - has optional text and outline
    (Other container Elements - Column, Tab/TabGroup, Pane)
Aliases:
    Frame = Fr
Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#frame-element
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 5

sg.set_options(font='Default 18', keep_on_top=True)


# ========================== 1 - Example - alignement  =================================================================
def main_example1():
    right_frame = sg.Frame('Frame 2', [[sg.Text('Row 1')],
                                       [sg.Text('Row 2')]], vertical_alignment='t')

    frame_layout = [[sg.T('Row A', k='-T-')],
                    [sg.T('Row B')],
                    [sg.T('Row C')]]

    layout = [[sg.Text('Your basic frame example\nthat demonstrates one issue when\nplacing 2 frames on 1 row\n')],
              [sg.Frame('Frame 1', frame_layout, vertical_alignment='t'), right_frame],
              [sg.B('Go'), sg.Button('Exit')], ]

    window = sg.Window('Frame Element - Example 1', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 2 - Example - Size Compare with Column  ===================================================
def main_example2():
    col1 = [[sg.T('Frame', background_color='blue')]] + [[sg.T('123 ' * i, background_color='blue')] for i in
                                                         range(1, 5)]
    col2 = [[sg.T('Column', background_color='red')]] + [[sg.Text('123 ' * i, background_color='red')] for i in
                                                         range(1, 5)]
    col3 = [[sg.T('Frame with 0 Border', background_color='green')]] + [[sg.Text('123 ' * i, background_color='green')]
                                                                        for i in range(1, 5)]

    layout = [
        [sg.Frame('My Frame', col1, size=(300, 300), background_color='blue'),
         sg.Column(col2, size=(300, 300), background_color='red'),
         sg.Frame('', col3, size=(300, 300), border_width=0, background_color='green', element_justification='c')],
        # the element justification works better in a frame than in a column. So that's why somethime you use
        # frame without border and without title as it mimics perfectly the column.
        [sg.Button('Go'), sg.Button('Exit')]]
    window = sg.Window('Frame Element - Example 3', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 3 - Example - Reliefs  ====================================================================
def main_example3():
    reliefs = (sg.RELIEF_GROOVE, sg.RELIEF_RIDGE, sg.RELIEF_SUNKEN, sg.RELIEF_RAISED, sg.RELIEF_SOLID, sg.RELIEF_FLAT)

    frames = []
    for relief in reliefs:
        layout = [[sg.Text(f'This is a {relief} relief')],
                  [sg.Input()]]
        frames.append(sg.Frame(relief, layout, relief=relief, border_width=6))

    layout = [[f] for f in frames]
    window = sg.Window('Frame Element - Example 4', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 4 - Example - Title locations  ============================================================
def main_example4():
    title_locations = {'Top': sg.TITLE_LOCATION_TOP,
                       'Bottom': sg.TITLE_LOCATION_BOTTOM,
                       'Left': sg.TITLE_LOCATION_LEFT,
                       'Right': sg.TITLE_LOCATION_RIGHT,
                       'Top Left': sg.TITLE_LOCATION_TOP_LEFT,
                       'Top Right': sg.TITLE_LOCATION_TOP_RIGHT,
                       'Bottom left': sg.TITLE_LOCATION_BOTTOM_LEFT,
                       'Bottom Right': sg.TITLE_LOCATION_BOTTOM_RIGHT}

    frames = []
    for description, title_location in title_locations.items():
        frames.append(sg.Frame(description, [[sg.Text(f'Another Frame Example...')]],
                               title_location=title_location, title_color='yellow', font='_25', border_width=3,
                               key=description))

    layout = [[f] for f in frames]
    layout += [[sg.B('New Title')]]

    window = sg.Window('Frame Element - Example 5', layout, background_color='Light blue')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'New Title':
            window['Top'].update('NEW TOP')

    window.close()


# ========================== 5 - Example - grabbable Frames  ===========================================================
def main_example5():
    frame_layout1 = [[sg.Text(f'Grab anything {line}', background_color='red')] for line in range(1, 6)]
    frame_layout2 = [[sg.Text(f'Can\'t grab me {line}', background_color='blue')] for line in range(1, 6)]
    frame_layout3 = [[sg.Text(f'Grab any line {line}', background_color='green', grab=True)] for line in range(1, 6)]

    layout = [[sg.Frame('Grab', frame_layout1, grab=True, background_color='red'),
               sg.Frame('No Grab', frame_layout2, background_color='blue'),
               sg.Frame('Line Grab', frame_layout3, background_color='green')]]

    window = sg.Window('Frame Element - Example 6', layout, no_titlebar=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


if __name__ == "__main__":
    example = [main_example1, main_example2, main_example3, main_example4, main_example5]
    example[example_number - 1]()
