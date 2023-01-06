"""
The Official Python GUI Programming with PySimpleGUI Course

popup_get_date

There are 4 popups that collect user input
    popup_get_date
    popup_get_file
    popup_get_folder
    popup_get_text

https://www.pysimplegui.org/en/latest/#high-level-api-calls-popups
sg.main_sdk_help()
"""
import PySimpleGUI as sg

sg.set_options(font='Default 14')  # set system-wide default
sg.Print('Output from popup_get_date', font='Default 16', keep_on_top=True, size=(30, 10), location=(1700, 350))
# sg.Print(sg.popup_get_date(no_titlebar=False, start_year=1975, start_mon=5, start_day=8)) # set up a start date
# sg.Print(sg.popup_get_date(close_when_chosen=True)) # close automatically after you choose a date
sg.Print(sg.popup_get_date(locale='en'))  # locale='langue' permet definir la langue du calendrier here english.
sg.popup('Exit')
