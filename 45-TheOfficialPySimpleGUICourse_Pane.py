"""
The Official Python GUI Programming with PySimpleGUI Course
Pane Element - The sliding Window Pane... a Container Element
Docs: http://www.PySimpleGui.org
https://www.udemy.com/course/pysimplegui/learn/lecture/30060900#questions
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - Example ===============================================================================
def main_example():
    col1 = sg.Column([[sg.Text('Column 1')],
                      [sg.Multiline(s=(20, 10), k='-ML1-')],
                      [sg.Button('Go'), sg.Button('Exit')]])

    col2 = sg.Column([[sg.Text('Column 2')],
                      [sg.Multiline(s=(10, 10), k='-ML2-')],
                      [sg.Button('Go'), sg.Button('Exit')]])

    col3 = sg.Column([[sg.Text('Column 3')],
                      [sg.Multiline(s=(40, 10), k='-ML3-')],
                      [sg.Button('Go'), sg.Button('Exit')]])

    col4 = sg.Column([[sg.Text('Column 4')],
                      [sg.Multiline(s=(30, 10), k='-ML4-')],
                      [sg.Button('Go'), sg.Button('Exit')]])

    layout = [sg.Pane([col1, col2, col3, col4], orientation='h', k='-PANE', background_color='red',
                      border_width=10, show_handle=True, handle_size=15)],

    window = sg.Window('Window Title', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break


# ========================== 2 - Example ===============================================================================
def main_example2():
    col1 = sg.Column([[sg.Text('Column 1')],
                      sg.vbottom([sg.Listbox([i for i in range(20)], s=(20, 20), k='-ML1-'), sg.Button('Exit')]),
                      ])
    col2 = sg.Column([[sg.Text('Column 2')],
                      [sg.Multiline(s=(40, 10), k='-ML2-')],
                      [sg.Button('Go'), sg.Button('Exit')]])

    layout = [sg.Pane([col1, col2], orientation='v', relief=sg.RELIEF_GROOVE, k='-PANE-', background_color=None,
                      handle_size=15)],

    window = sg.Window('Window Title', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 3 - Example ===============================================================================
def main_example3():
    col1 = sg.Column([[sg.Text('Column 1', background_color='green')],
                      [sg.Multiline(size=(1, 1), k='-ML1-', expand_x=True, expand_y=True)],
                      [sg.Button('Go'), sg.Button('Exit', k='E1')]], background_color='green')

    col2 = sg.Column([[sg.Text('Column 2', background_color='blue')],
                      [sg.Multiline(size=(1, 1), k='-ML2-', expand_x=True, expand_y=True)],
                      [sg.Button('Exit', k='E2')]], background_color='blue')

    layout = [sg.Pane([col1, col2], orientation='v', size=(300, 700), border_width=0, k='-PANE-', handle_size=15,
                      expand_x=True, expand_y=True, background_color='red')],

    window = sg.Window('Window Title', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in ('E1', 'E2', sg.WIN_CLOSED):
            break
        if event == 'Go':
            for i in range(50):
                window['-ML1-'].print(i, colors='white on green')
                window['-ML2-'].print(i, colors='white on blue')

    window.close()


if __name__ == '__main__':
    example = [main_example, main_example2, main_example3]
    example[example_number - 1]()
