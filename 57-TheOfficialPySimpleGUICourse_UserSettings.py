"""
The Official Python GUI Programing with PySimpleGUI Course
UserSettings

Class:
    UserSettings

Functions:
    main_global_pysimplegui_settings
    main_global_pysimplegui_sttings_erase
    user_settings
    user_settings_delete_entry
    user_settings_delete_filename
    user_settings_file_exists
    user_settings_filename
    user_settings_get_entry
    user_settings_load
    user_settings_object
    user_setting_save
    user_settings_set_entry
    user_settings_silent_on_error
    user_settings_write_row_dictionary

Object:
    UserSettings

Docs:
    http://www.PySimpleGUI.org
    https://pysimplegui.redthedocs.io/en/latest/call%20reference/#user-settings-api-function-interface
    https://pysimplegui.redthedocs.io/en/latest/call%20reference/#usersettings-api-class-interface
    https://www.pysimplegui.org/en/latest/#user-settings-api
    https://www.pysimplegui.org/en/latest/cookbook/#recipe-save-and-load-program-settings

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 4

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE - UserSettings functions ======================================================
def main_example1():
    sg.Print(font='Default 16', keep_on_top=True, size=(60, 14), relative_location=(600, -300))

    py_dict = {}
    py_dict.setdefault('-test-', 123)
    sg.Print(py_dict)
    sg.Print(py_dict.get('-test-'))
    sg.Print(py_dict.get('-not there-', 'default value'))

    sg.user_settings_filename(path='.')
    sg.user_settings_silent_on_error(True)

    layout = [[sg.Text('Setting Functions')],
              [sg.Text('Key:'), sg.Input(key='-KEY-', size=15, do_not_clear=False), sg.Text('Value:'),
               sg.Input(key='-VALUE-', size=15, do_not_clear=False), sg.Button('Set')],
              [sg.Text('Key:'), sg.Input(key='-GET-', size=15), sg.Button('Get'), sg.Text(key='-OUT-')],
              [sg.Text('Key:'), sg.Input(key='-DELETE-', size=15, do_not_clear=False), sg.Button('Delete')],
              [sg.Button('Print'), sg.Button('Filename'), sg.Exit()], ]

    window = sg.Window('User Settings 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Print':
            sg.Print(sg.user_settings())
        elif event == 'Set':
            sg.user_settings_set_entry(values['-KEY-'], values['-VALUE-'])
        elif event == 'Get':
            setting_value = sg.user_settings_get_entry(values['-GET-'], 'DEFAULT VALUE')
            window['-OUT-'].update(setting_value)
        elif event == 'Delete':
            sg.user_settings_delete_entry(values['-DELETE-'])
        elif event == 'Filename':
            sg.Print(sg.user_settings_filename())
    window.close()


# ========================== 2 - EXAMPLE - UserSettings Object =========================================================
def main_example2():
    sg.Print(font='Default 16', keep_on_top=True, size=(60, 14), relative_location=(600, -400))

    settings = sg.UserSettings(r'./settings.json')
    settings['-new-'] = 'my new setting'

    layout = [[sg.Text('Settings Functions')],
              [sg.Text('Key:'), sg.Input(key='-KEY-', size=15, do_not_clear=False), sg.Text('Value:'),
               sg.Input(key='-VALUE-', size=15, do_not_clear=False), sg.Button('Set')],
              [sg.Text('Key:'), sg.Input(key='-GET-', size=15), sg.Button('Get'), sg.Text(key='-OUT-')],
              [sg.Text('Key:'), sg.Input(key='-DELETE-', size=15, do_not_clear=False), sg.Button('Delete')],
              [sg.Button('Print'), sg.Button('Filename'), sg.Exit()]]

    window = sg.Window('User Settings 2', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Print':
            sg.Print(settings)
        elif event == 'Set':
            settings[values['-KEY-']] = values['-VALUE-']
        elif event == 'Get':
            # setting_value = settings[values['-GET-']]
            setting_value = settings.get(values['-GET-'], 'DEFAULT VALUE')
            window['-OUT-'].update(str(setting_value))
            sg.Print(f'Get value = {setting_value}')
        elif event == 'Get':
            # del settings[values['-DELETE-']]
            setting_value = settings.get(values['-GET-'], 'DEFAULT VALUE')
            window['-OUT-'].update(str(setting_value))
            sg.Print(f'Get value = {setting_value}')
        elif event == 'Delete':
            # del settings[values['-DELETE-']]
            settings.delete_entry(values['-DELETE-'])
        elif event == 'Filename':
            sg.Print(settings.full_filename)
    window.close()


# ========================== 3 - EXAMPLE - UserSettings INI Files ======================================================
def main_example3():
    sg.Print(font='Default 16', keep_on_top=True, size=(60, 14), relative_location=(600, -300))

    settings = sg.UserSettings(r'./settings.ini')

    layout = [[sg.Text('Settings Functions')],
              [sg.Text('Section:'), sg.Input(key='-SECTION-', size=15)],
              [sg.Text('Key:'), sg.Input(key='-KEY-', size=15, do_not_clear=False), sg.Text('Value:'),
               sg.Input(key='-VALUE-', size=15, do_not_clear=False), sg.Button('Set')],
              [sg.Text('Key:'), sg.Input(key='-GET-', size=15), sg.Button('Get'), sg.Text(key='-OUT-')],
              [sg.Text('Key:'), sg.Input(key='-DELETE-', size=15, do_not_clear=False), sg.Button('Delete')],
              [sg.Button('Print'), sg.Button('Print Section'), sg.Button('Filename'), sg.Exit()]]

    window = sg.Window('User Settings 3', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Print Section':
            sg.Print(settings[values['-SECTION-']])
        if event == 'Print':
            sg.Print(settings)
        elif event == 'Set':
            settings[values['-SECTION-']][values['-KEY-']] = values['-VALUE-']
        elif event == 'Get':
            section = values['-SECTION-']
            key = values['-GET-']
            # setting_value = settings[section][key]
            setting_value = settings.get(values['-GET-'], 'DEFAULT VALUE')
            window['-OUT-'].update(str(setting_value))
            sg.Print(f'Get value = {setting_value}')
        elif event == 'Delete':
            section = values['-SECTION-']
            key = values['-DELETE-']
            del settings[section][key]
            # settings.delete_entry(values['-DELETE-'])
        elif event == 'Filename':
            sg.Print(settings.full_filename)

    window.close()


# ========================== 4 - EXAMPLE - UserSettings - Simple Use ===================================================
def main_example4():
    sg.Print(font='Default 16', keep_on_top=True, size=(60, 14), relative_location=(300, 150))

    layout = [[sg.Text('User Settings - Save Window Location')],
              [sg.Button('Go'), sg.Button('Exit')], ]

    location = sg.user_settings_get_entry('-location-', (None, None))
    sg.Print(sg.user_settings_filename())
    window = sg.Window('User Settings - Window Location', layout, location=location, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
            sg.user_settings_set_entry('-location-', window.current_location())
            break
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3, main_example4]
    example[example_number - 1]()
