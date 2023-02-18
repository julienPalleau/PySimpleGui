"""
Lesson 39

Graph Element
Exercise 1

Create a Status "User Defined Element"
Instructions:

You are going to make a new element using a technique called "User Defined Element". A User Defined Element is simply a function that returns a PySimpleGUI element or a list of PySimpleGUI element. In this case, your Status element will return a Graph element.

Your Status element will display the status as a circle, much like an LED light. It will display a colored circle to indicate "status".

Detailed instructions:

    Write a function called Status
        It should return a Graph element that is 40 pixels by 40 pixels
    Write a function called change_status that creates a circle with the specified color
        It should take these parameters status_change(window, key, color)
            window - your GUI's window
            key - the key you used to create your Graph element
            color - the color you want the circle to be
    When drawing the circle should:
        Be roughly centered in the Graph
        Have a radius of 18 pixels
        Have no line around it
    Your layout should have:
        3 rows for the Status
            On each row have a Text element that says what the status represents and your Status element.
            The text for the rows should be - 'Main server:', 'Secondary server:', 'Network Link:'
        Include a Button called "Status" as a way to generate an event
        In your event loop, change the color of your Status elements to a randome color from the list of the colors in
        the variable colors that is pre-defined for you.
    When you create your window:
        Use a font that's "Default" and has a size of 15
        Right justify the elements in the Window
        font='Default 15'
        element_justification='r'

Graph Element in the Call Reference Documentation

Just for fun....

Once you have completed your code, try making these changes to get an idea of what "polling" for status on a periodic
basis could be like.

    If you check for the Button key explicitly in your event loop, remove the check so that every time through your
    event loop the status will be changed for your 3 Status elements
    In your call to window.read(), add a parameter timeout=1000
        This will cause your event loop to run every 1000 milliseconds

The result will be blinking status indicators. For a more realistic program, you would check the status for the 3 items
being shown and set the color according to the measured status. For example, if you find the network link is down, then
you would maybe set the color of the status to "red".

import PySimpleGUI as sg
import random             # You will use a function from the random standard library to choose a random color

def status_change(window, key, color):
  return

# List oif colors you will randomly choose from
colors = ('blue', 'yellow', 'black', 'purple', 'orange', 'red', 'green')

layout = [  []  ]

window = sg.Window('Status Elements', layout)

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break

  # Add your event processing here


window.close()
"""
import random
import PySimpleGUI as sg


def Status(key):
    return sg.Graph(canvas_size=(40, 40), graph_bottom_left=(0, 0), graph_top_right=(40, 40), key=key)


def status_change(window, key, color):
    window[key].erase()
    window[key].draw_circle((20, 20), radius=18, fill_color=color, line_width=0)


colors = ('blue', 'yellow', 'black', 'purple', 'orange', 'red', 'green')

layout = [[sg.Text('Main server:'), Status('-STATUS MAIN-')],
          [sg.Text('Secondary server:'), Status('-STATUS SECONDARY-')],
          [sg.Text('Network link:'), Status('-STATUS NETWORK-')],
          [sg.Button('Status')]]

window = sg.Window('Status Elements', layout, element_justification='r', font='Default 15')

while True:
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED:
        break

    status_change(window, '-STATUS MAIN-', random.choice(colors))
    status_change(window, '-STATUS SECONDARY-', random.choice(colors))
    status_change(window, '-STATUS NETWORK-', random.choice(colors))

window.close()
