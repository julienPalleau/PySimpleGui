"""
Lesson 24

Checkbox Element
Exercise 1

Make a Hamburger Toppings GUI (Don't forget the cheese please!)
Instructions:

As part of an order entry GUI, make the Hamburger Toppings Section

    Include a "Place Order" button
        When clicked it will show a popup with containing the values dictionary returned from `window.read()
    Include a "Clear" button that will clear all checkboxes
    Make each checkbox on a separate row in the window. Multiple ways of solving this including:
        Manually making your layout with a checkbox per row
        Using a list comprehension inside your layout
        Building the layout in code, using a for loop for the toppings portion

Checkbox in the Call Reference Documentation

import PySimpleGUI as sg

toppings = ['Cheese', 'Lettuce', 'Tomato', 'Pickles', 'Onions', 'Ketchup', 'Mayonnaise', 'Mustard']

# You can start with this layout as a guide to the first and last rows
# Your exercise is to fill in the middle part of the window's layout
# Note - you do not have to start with this exact code. You can build a layout similar to it instead
layout = [  [sg.Text('Hamburger Toppings', font='Default 15')],
            [sg.Button('Place Order'), sg.Button('Clear')]]


window = sg.Window('Food Order GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Place Order':
        sg.popup(values, title='Values')
    # add your Clear button code

window.close()
"""
# import PySimpleGUI as sg

# toppings = ['Cheese', 'Lettuce', 'Tomato', 'Pickles', 'Onions', 'Ketchup', 'Mayonnaise', 'Mustard']
#
# # You can start with this layout as a guide to the first and last rows
# # Your exercise is to fill in the middle part of the window's layout
# # Note - you do not have to start with this exact code. You can build a layout similar to it instead
# layout = [[sg.Text('Hamburger Toppings', font='Default 15')],
#           [sg.Button('Place Order'), sg.Button('Clear')], [sg.Checkbox(elmt) for elmt in toppings]]
#
#
# window = sg.Window('Food Order GUI', layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event == 'Place Order':
#         sg.popup(values, title='Values')
#     # add your Clear button code
#     if event == 'Clear':
#         for elmt in toppings:
#             elmt = ''
#             layout = [[sg.Text('Hamburger Toppings', font='Default 15')],
#                       [sg.Button('Place Order'), sg.Button('Clear')], [sg.Checkbox(elmt) for elmt in toppings]]
#         window = sg.Window('Food Order GUI', layout)
#
# window.close()

# Proposed Solution
import PySimpleGUI as sg

toppings = ['Cheese', 'Lettuce', 'Tomato', 'Pickles', 'Onions', 'Ketchup', 'Mayonnaise', 'Mustard']

layout = [  [sg.Text('Hamburger Toppings', font='Default 15')],
            [[sg.Checkbox(topping, key=topping)] for topping in toppings],
            [sg.Button('Place Order'), sg.Button('Clear')]]


window = sg.Window('Food Order GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Place Order':
        sg.popup(values, title='Values')
    elif event == 'Clear':
        for topping in toppings:
            window[topping].update(False)
window.close()