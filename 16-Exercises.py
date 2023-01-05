"""
Lesson 16

Popups - Input Text
Exercise 1

Use popup calls to request a person's login name and password.
Instructions

    Use popup_get_text to request a person's login name
    Use another popup_get_text to request a person's password (hide the password as it is entered)
    Display the values returned in another popup window

Documentation on popup calls can be found here:
https://pysimplegui.readthedocs.io/en/latest/call%20reference/#popups-pep8-versions

import PySimpleGUI as sg

name = sg.popup_get_text(')
password = sg.popup_get_text()
# Add code to output the entered values
"""
import PySimpleGUI as sg



name = sg.popup_get_text('Enter your name')
password = sg.popup_get_text('Enter your passwd')
# Add code to output the entered values


sg.popup(f'Name: {name}, Password: {password}')

sg.popup('Exit')