"""
The Official Python GUI Programming with PySimpleGUI Course

popup_get_file
popup_get_folder

There are 4 popups that collect user input
popup_get_date
popup_get_file
popup_get_folder
popup_get_text

https://www.pysimplegui.org/en/latest/#high-level-api-calls-popups
"""
import PySimpleGUI as sg

sg.set_options(font='Default 14')       # set system-wide default
sg.Print('Output from popups', font='Default 14', keep_on_top=True, size=(30, 10), location=(1700, 350))

# Save as window files with image and browse button all you to save multiple files, if you wish to save only 1 file
# just remove multiple_files=True option.
# name = sg.popup_get_file("What is the filename?", 'Filename',
#                          image=r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\the.png',
#                          default_path='default', save_as=True, multiple_files=True)

# Open window files with image and browse button, and in a set initial folder for specific py files
# name = sg.popup_get_file("What is the filename?", 'Filename', # open a window with browse button
#                          image=r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\the.png',
#                          default_path='default',    # default input value
#                          # save_as=True,
#                          initial_folder=r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui',
#                          file_types=(("Py Files", "*.py"), ("All files", "*.*")),
#                          multiple_files=True, files_delimiter='<<>>')

# name = sg.popup_get_file("What is the filename?", 'Filename', no_window=True) # Open directly the explorer

# Open window folders
name = sg.popup_get_folder('What is the folder name', 'Filename')

sg.Print(f'get_file = {name}')  # print in a separate debug window
sg.popup(f'get_file = {name}')  # print in the popup window