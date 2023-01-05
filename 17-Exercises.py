"""
    Lesson 17

Popups - Get File & Folder
Exercise 1
Instructions

Get a filename of a TXT file using popup (NOTE Trinket has the full solution)
# Use a popup to get a text file filename
# Limit the files shown to only those with a .txt extension
# Use a popup to display the filename chosen
import PySimpleGUI as sg

filename = sg.popup_get_file('Choose a text file', file_types=((("TXT Files", "*.txt"),)))

sg.popup('You chose:', filename)
"""

# Use a popup to get a text file filename
# Limit the files shown to only those with a .txt extension
# Use a popup to display the filename chosen
import PySimpleGUI as sg

filename = sg.popup_get_file('Choose a text file', file_types=((("TXT Files", "*.txt"),)))

sg.popup('You chose:', filename)