"""
Lesson 11

Debug Print
Exercise 1
Instructions

    Use a loop to print the numbers 0-999 in the Debug Print window
    Add a popup window at the end of your program to stop the window from closing

import PySimpleGUI as sg

# Make a for loop and print to the Debug Print window


# Add a popup to keep program from exiting
"""
import PySimpleGUI as sg


# Make a for loop and print to the Debug Print window
for number in range(0,1000):
    sg.Print(number)

sg.popup('Click ok to exit')

# Add a popup to keep program from exiting