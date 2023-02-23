"""
The Official Python GUI Programming with PySimpleGUI Course

Tab & TabGroup Elements - Container Elements
    (Others container Elements - Column, Frame, Pane)
Aliases:
    None

Docs: http://wwww.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#tab-element
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 6

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - Example - Tabs  =======================================================================
def main_example1():
    tab1 = sg.Tab('Tab 1', [[sg.T('Row A')],
                            [sg.T('Row B')],
                            [sg.T('Row C')]])

    tab2 = sg.Tab('Tab 2', [[sg.Text('Row 1')],
                            [sg.Text('Row 2')]])

    layout = [[sg.TabGroup([[tab1, tab2]])],
              [sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 2 - Example - Images and Tabs  ============================================================
def main_example2():
    tab_layout1 = [[sg.Text('Row 1 tab 1')],
                   [sg.Text('Row 2 tab 1')]]

    tab_layout2 = [[sg.Text('Row 1 tab 2')],
                   [sg.Text('Row 2 tab 2')]]

    tab_layout3 = [[sg.Text(f'Row {row} tab 3')] for row in range(1, 8)]

    tab1 = sg.Tab('Tab 1', tab_layout1, image_source=sg.HEART_FLAT_BASE64, image_subsample=4)
    tab2 = sg.Tab('Tab 2', tab_layout2, image_source=sg.EMOJI_BASE64_HAPPY_THUMBS_UP, image_subsample=2)
    tab3 = sg.Tab('Tab 3', tab_layout3)

    layout = [[sg.TabGroup([[tab1, tab2, tab3]], tab_location=sg.TAB_LOCATION_LEFT_TOP)],
              [sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 2', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 3 - Example - Tab Colors  =================================================================
def main_example3():
    tab_layout1 = [[sg.Text('Row 1 tab 1')],
                   [sg.Text('Row2 tab 1')]]

    tab_layout2 = [[sg.Text('Row 1 tab 2')],
                   [sg.Text('Row 2 tab 2')]]

    tab_layout3 = [[sg.Text(f'Row {row} tab 3')] for row in range(1, 8)]

    tab1 = sg.Tab('Tab 1', tab_layout1)
    tab2 = sg.Tab('Tab2', tab_layout2)
    tab3 = sg.Tab('Tab3', tab_layout3)

    layout = [[sg.TabGroup([[tab1, tab2, tab3]],
                           title_color='blue',
                           focus_color='yellow',
                           selected_background_color='black',
                           tab_background_color='green',
                           selected_title_color='purple')],
              [sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 3', layout, background_color='light blue')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()


# ========================== 4 - Example - Title Location  =============================================================

def main_example4():
    sg.Print(font='Default 18', keep_on_top=True, size=(35, 15), relative_location=(650, -300))

    def make_tab_layout(tab_key, description):
        return [[sg.Text(f'Location = {description}', font='_ 14')],
                [sg.Text('Middle Row')],
                [sg.Text('last row of tab')],
                [sg.B('Close Tab', k=('Close', tab_key))]]

    title_locations = {'Top': sg.TAB_LOCATION_TOP,
                       'Top Left': sg.TAB_LOCATION_TOP_LEFT,
                       'Top Right': sg.TAB_LOCATION_RIGHT_TOP,
                       'Left': sg.TAB_LOCATION_LEFT,
                       'Left Top': sg.TAB_LOCATION_LEFT_TOP,
                       'Left Bottom': sg.TAB_LOCATION_LEFT_BOTTOM,
                       'Right': sg.TAB_LOCATION_RIGHT,
                       'Right Top': sg.TAB_LOCATION_RIGHT_TOP,
                       'Right Bottom': sg.TAB_LOCATION_RIGHT_BOTTOM,
                       'Bottom': sg.TAB_LOCATION_BOTTOM,
                       'Bottom Left': sg.TAB_LOCATION_BOTTOM_LEFT,
                       'Bottom Right': sg.TAB_LOCATION_BOTTOM_RIGHT
                       }

    tabgroups = []

    for i, (description, title_location) in enumerate(title_locations.items()):
        tab_key = f'{description}'
        group_key = f'-TAB GROUP {i}-'

        tab1_layout = make_tab_layout(tab_key + '1', description)
        tab2_layout = make_tab_layout(tab_key + '2', description)
        tab3_layout = make_tab_layout(tab_key + '3', description)

        tab_group = sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, key=tab_key + '1'),
                                  sg.Tab('Tab 2', tab2_layout, key=tab_key + '2'),
                                  sg.Tab('Tab 3', tab3_layout, key=tab_key + '3')]],
                                tab_location=title_location,
                                font=f'_ {(i % 3) * 2 + 8}',
                                key=f'-TAB GROUP {i}-',
                                selected_background_color='red')

        tabgroups.append(tab_group)

    layout = [[tabgroups[3 * row + col] for col in range(3)] for row in range(4)]

    window = sg.Window('Tab Element - Example 4', layout, background_color='light blue')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'New Title':
            window['Top'].update('NEW Top')
        if isinstance(event, tuple):
            tab_key = event[1]
            window[tab_key].update(visible=False)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


# ========================== 5 - Example - Right Click Menu & Visibility  ==============================================
def main_example5():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(500, -300))

    def make_tab_layout():
        return [[sg.Text('First Row', right_click_menu=sg.MENU_RIGHT_CLICK_DISABLED)],
                [sg.Text('Middle Row')],
                [sg.Text('Last row of tab')]]

    tab1 = sg.Tab('Tab 1', make_tab_layout(), right_click_menu=['', ['Close::Tab 1']], image_source=sg.HEART_3D_BASE64,
                  image_subsample=4)
    tab2 = sg.Tab('Tab 2', make_tab_layout(), right_click_menu=sg.MENU_RIGHT_CLICK_DISABLED)
    tab3 = sg.Tab('Tab 3', make_tab_layout(), right_click_menu=['', ['Close::Tab 3']], image_source=sg.HEART_3D_BASE64,
                  image_subsample=4)

    layout = [[sg.TabGroup([[tab1, tab2, tab3]], right_click_menu=['', ['GROUP Menu']], key='-TAB GROUP')],
              [sg.Button('Select 2'), sg.Button('Disable 3'), sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 7', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event.startswith('Close'):
            tab_key = event[event.index("::") + 2:]
            window[tab_key].update(visible=False)

        if event == 'Select 2':
            window['Tab 2'].select()
        elif event == 'Disable 3':
            window['Tab 3'].update(disabled=True)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f' {k} = {values[k]}' for k in values], sep='\n')

    window.close()


# ========================== 5 - Example - Right Click Menu & Visibility  ==============================================
def main_example6():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(500, -300))

    def make_tab_layout():
        return [[sg.Text('First Row')],
                [sg.Text('Middle Row')],
                [sg.Text('Last row of tab')]]

    tab1 = sg.Tab('Tab 1', make_tab_layout())
    tab2 = sg.Tab('Tab 2', make_tab_layout())
    tab3 = sg.Tab('Tab 3', make_tab_layout())

    layout = [[sg.TabGroup([[tab1, tab2, tab3]], tab_location=sg.TAB_LOCATION_LEFT_TOP, key='-TAB GROUP-',
                           enable_events=True)],
              [sg.Button('Add'), sg.Button('Disable'), sg.Button('Find "Disabled"'), sg.Button('Exit')]]

    window = sg.Window('Tab Element - Example 6', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

        if event == 'Add':
            window['-TAB GROUP-'].add_tab(sg.Tab('New Tab', make_tab_layout(), key='-NEW TAB-'))
        elif event == 'Disable':
            window['Tab 1'].update('Disabled', disabled=True)
        elif event == 'Find "Disabled"':
            sg.Print(f"find tab = {window['-TAB GROUP-'].find_key_from_tab_name('Disabled')}", colors='white on blue')

    window.close()


if __name__ == "__main__":
    example = [main_example1, main_example2, main_example3, main_example4, main_example5, main_example6]
    example[example_number - 1]()
