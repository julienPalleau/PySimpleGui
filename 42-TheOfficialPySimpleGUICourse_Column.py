"""
The Official Python GUI Programming with PySimpleGUI Course

Column Element - Most Basic of Container Elements
    (Others are Frame, Tab,TabGroup, Pane)
Aliases:
    Column = Col

Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#column-element
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 7

sg.set_options(font='Default 18', keep_on_top=True)


# ========================== 1 - Example  ==============================================================================
def main_example1():
    right_col = sg.Column([[sg.Text('Row 1')],
                           [sg.Text('Row 2')]], vertical_alignment='t')  # t means top and we can use b for bottom

    c = [[sg.T('Row A')],
         [sg.T('Row B')],
         [sg.T('Row C')]]

    layout = [[sg.Text('This layout shows why a Column Element is needed')],
              # [sg.Column(c), right_col],
              # [sg.Listbox((1, 2, 3, 4, 5, 6), size=(10, 6), no_scrollbar=True), sg.Text('How do I get 2 rows here??')],
              [sg.Column(c), right_col],
              [sg.Button('Exit')], ]

    window = sg.Window('Column Element - Example 1', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break


# ========================== 2 - Example - Nested Columns  =============================================================
def main_example2():
    col_layout = [[sg.Text('Row 1', background_color='blue')],
                  [sg.Text('Row 2', background_color='blue')]]
    col_layout = [[sg.Col(col_layout, background_color='purple', pad=(0, 0))]]
    col_layout = [[sg.Col(col_layout, background_color='purple', pad=(0, 0))]]
    col_layout = [[sg.Col(col_layout, background_color='purple', pad=(0, 0))]]
    col_layout = [[sg.Col(col_layout, background_color='purple', pad=(0, 0))]]

    col_layout = [[sg.Col(col_layout, background_color='purple', pad=(0, 0))]]
    col_layout = [[sg.Col(col_layout, background_color='purple')]]

    col_layout = [[sg.Col(col_layout, background_color='yellow')]]

    layout = [[sg.Titlebar('This layout shows why a Column Element is needed')],
              [sg.Listbox((1, 2, 3, 4, 5, 6), size=(10, 6)), sg.Column(col_layout, background_color='red')],
              [sg.Button('Start'), sg.Button('Stop'), sg.Button('Exit')], ]

    window = sg.Window('Column Element - Example 2', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 3 - Example - Window's Layout in Column  ==================================================
def main_example3():
    col1 = [[sg.Text('123' * i)] for i in range(5)]
    col2 = [[sg.In(s=i * 10)] for i in range(5)]

    layout = [[sg.Text('Columns as columns')],
              [sg.Col(col1), sg.Col(col2)],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Column Element - Example 3', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event={event}', c='white on red', erase_all=True, font='Default 18', keep_on_top=True, size=(30, 14),
                 location=(500, 500))
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='/n')
    window.close()


# ========================== 4 - Example - Window's Layout in Column  ==================================================
def main_example4():
    layout = [[sg.Text('Column for entire window')],
              [sg.Input()],
              [sg.Button('Go'), sg.Button('Exit')]]

    layout = [[sg.Column(layout, pad=(0, 0), element_justification='c')]]

    window = sg.Window('Column Element - Example 4', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 5 - Example - Hide Sections  ==============================================================
def main_example5():
    layout1 = [[sg.Text('SECTION 1', text_color='white', background_color='red')],
               [sg.Text('Name'), sg.Input(k='-NAME-')],
               [sg.Button('Next')]]

    layout2 = [[sg.Text('SECTION 2', text_color='white', background_color='blue')],
               [sg.Text('Password'), sg.Input(k='-PW-', password_char='*')],
               [sg.Button('Back'), sg.Button('Submit')]]

    # Below we have two different definition to manage where to put (Right side of window) to see what happens
    # comment the first one and uncomment the second one.
    layout = [[sg.Column(layout1, k='-C1-'), sg.Column(layout2, k='-C2-', visible=False),
               sg.T('Right side of window')]]
    # layout = [[sg.pin(sg.Column(layout1, k='-C1-')), sg.pin(sg.Column(layout2, k='-C2-', visible=False)),
    #            sg.T('Right side of window')]]

    window = sg.Window('Column Element - Example 5', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Next':
            window['-C1-'].update(visible=False)
            window['-C2-'].update(visible=True)
        elif event == 'Back':
            window['-C1-'].update(visible=True)
            window['-C2-'].update(visible=False)

    window.close()


# ========================== 6 - Example - Scrollable Column ===========================================================
def main_example6():
    # instead of None you can put a wide for example 300. In putting none the wide will be automatically adapted.
    long_layout = [[sg.Column([[sg.T(f'Line {i}')] for i in range(50)], size=(None, 400), scrollable=True,
                              vertical_scroll_only=True, )]]

    layout = [[sg.Text('My long window')]]
    layout += long_layout
    layout += [[sg.Button('Go'), sg.Button('Exit')]]

    # layout [[sg.Column(layout, pad=(0,0), element_justification='l')]]
    window = sg.Window('Column Element - Example 6', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True, font='Default 18', keep_on_top=True,
                 size=(30, 14), location=(500, 500))
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')
    window.close()


# ========================== 7 - Example - Sizers ======================================================================
def ColumnFixedSize(layout, size=(None, None), *args, **kwargs):
    # An addition column is needed to wrap the column with the Sizers because the colors will not be set on the space
    # the sizers take
    return sg.Column([[sg.Column([[sg.Sizer(0, size[1] - 1), sg.Column([[sg.Sizer(size[0] - 2, 0)]] + layout,
                                                                       *args, **kwargs, pad=(0, 0))]], *args,
                                 **kwargs)]], pad=(0, 0))


def main_example7():
    col_contents = [[sg.Sizer(500, 0)],
        [sg.T('Row A')],
        [sg.T('Row B')],
        [sg.T('Row C')]]

    layout = [[sg.Sizer(0, 500), sg.Col(col_contents, vertical_alignment='t', element_justification='c')]]
    window = sg.Window('Column Element - Example 7', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True, font='Default 18', keep_on_top=True,
                 size=(30, 14), location=(500, 500))
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

    window.close()


if __name__ == "__main__":
    example = [main_example1, main_example2, main_example3, main_example4, main_example5, main_example6, main_example7]
    example[example_number - 1]()
