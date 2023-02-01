"""
Lesson 35

Menu Element
Exercise 1

Add a Menu (Menubar) to your application
Instructions:

The most important part for you to understand with all PySimpleGUI menus is the data-structure for the menu specification. It has a specific format.

The easiest way to quickly make a menu is to copy an existing one. Grab a Demo Program or one of your other applications... copy, paste, edit, done. There's one right in the call reference.

Let's paste that one right here in the instructions.

menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
            ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Debugger', ['Popout', 'Launch Debugger']],
            ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
            ['&Help', '&About...'], ]

The format isn't incredibly difficult to understand. One basic rule - if an item has a list after it, then the list is a "submenu".

See if you can study the example, and make one up from scratch for this exercise.

    You've made an application that allows your user to take notes using a Multiline Element
    Rather than use buttons, let's use a Menubar
    Your Menu should have these top-level items:
        File
        Edit
        Help
        Disabled (make this item disabled)
    Under File list these options:
        Open
        Save
        Exit
    Under Edit:
        Clear
        Disabled (make this item disabled)
    And under Help:
        Help
        A SEPARATOR LINE
        About
    Add a submenu to Help:About with these items:
        About my program
        About PySimpleGUI
        About me
    Your layout needs to only contain the Menubar and a Multiline element with a size of 80 x 20
    Display the event value returned from reading your window in your Multiline Element
    When 'Exit' is chosen from the Menubar, have your program exit by breaking from the Event Loop

NOTE - when running on Trinket, you'll need to either set no_titlebar=True when creating your Window, or use the MenubarCustom Element instead of the plain Menu element. This is because Trinket doesn't supply a Titlebar.

Menu Element in the Call Reference Documentation

import PySimpleGUI as sg

menu_def =

layout = [
            [],     # Add your elements
            [],
        ]

# Note - on Trinket, you'll need to set no_titlebar so the menu displays correctly
window = sg.Window('Window Title', layout, no_titlebar=True)

while True:
    event, values = window.read()
    # add event processing

window.close()
"""
import PySimpleGUI as sg

menu_def = [['File', ['Open', 'Save', 'Exit', '!Disabled']],
            ['Edit', ['Clear', '!Disabled']],
            ['Help', ['Help', '---', 'About', ['About my program', 'About PySimpleGUI', 'About me']]],
            ['Disabled', []]]

layout = [
            [sg.MenuBar(menu_def, key='-MENU BAR-'), sg.Multiline(size=(80, 20), key='-MLINE-')],  # Add your elements
        ]


# Note - on Trinket, you'll need to set no_titlebar so the menu displays correctly
window = sg.Window('Window Title', layout, no_titlebar=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window['-MLINE-'].print(event)

window.close()