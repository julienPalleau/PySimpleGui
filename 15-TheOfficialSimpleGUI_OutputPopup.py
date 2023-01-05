"""
The Official Python GUI Programming with PySimpleGUI Course

Popups - "Windows with triningwheels"

Basic popup
    popup
Variant popups
    popup_auto_close
    popup_cancel
    popup_error
    popup_no_buttons
    popup_no_titlebar
    popup_ok
    popup_ok_cancel
    popup_yes_non
Non-blocking pupups
    popup_non_blocking
    popup_quick
    popup_quick_message
Scrolled popups
    popup_scrolled
Notification window from SystemTray SDK
    popup_notify
Output an animatoin (GIF) one frame at a time
    popup_animated

Input popups (returns information)
    popup_get_date
    popup_get_file
    popup_get_folder
    popup_get_text
"""

import PySimpleGUI as sg
import inspect

sg.popup('Vanilla popup', any_key_closes=True)
sg.Window('Title', [[sg.T('Vanilla popup')], [sg.Ok()]]).read(close=True)
exit()

# sg.popup('Vanilla popup')
sg.set_options(font='Default 15')   # set the font so lesson viewer can easily see

# Animation for splash and loading screens
for i in range(1000):
    sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, 'loading...', time_between_frames=30, keep_on_top=True)
sg.popup_animated(None)

sg.popup('After system-wide font set')
sg.theme('dark red')
sg.popup('Following Dark Red theme')
if sg.popup_yes_no('Do you want to continue') == 'No':
    exit()

sg.theme(sg.OFFICIAL_PYSIMPLEGUI_THEME)
sg.popup('This is you planin vanilla popup'
         'I is the easiest way to make a Window',
         title='Title is after the parms')
sg.popup('A popup with not title uses the first parm for the title')
sg.popup('The return value was', sg.popup('My own buttons', custom_text=('Button1', 'Button2')))

sg.popup_scrolled(inspect.getdoc(sg.popup), font='Courier 14', size=(80,40))

sg.popup_quick('The Quick Popup autocloses', 'The user can also close it with the button', location=(1100, 500),
               auto_close_duration=15)

sg.popup('Follows the "quick" popup', modal=False)

sg.popup_quick_message('Please wait while your operation completes', background_color='red', text_color='white',
                       keep_on_top=True, auto_close_duration=5, location=(1100, 500))

sg.popup('Follows the "quick_message" popup', modal=False)

sg.popup_non_blocking('Non-blocking does not wait for the user.',
                      'But still has a button to close it', location=(1100, 500))

sg.popup('Follows the "non-blocking" popup', modal=False)

# Notification popup - part of the SystemTray APIs. Toaster-style window
sg.popup_notify('Notification Style Popup critical', location=(1200, 600), icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)
sg.popup_notify('Notification Style Popup Info', location=(1200, 600), icon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION)

