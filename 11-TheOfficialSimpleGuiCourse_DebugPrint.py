"""
The Official Python GUI Programming with PySimpleGUI Course
"Debug Output" - The print function

The functions Print, eprint, EasyPrint all refer to the same funtion. There is no difference whic hyou use as they point
 to identical code. The one you'll see used in Demo Programs is Print.

One method for routing your print statements to the debuyg window is to reassign the print keyword to be the PySimpleGUI
 function Print. This can be done through simple assignment.

print = sg.Print

You can also remap stdout to the debug window by calling Print with the parameter do_not_reroute_stdout = False. This
will reroute all of your print statements out to the debug window.
"""
import PySimpleGUI as sg

sg.Print('Hello, World', text_color='blue')

# print = sg.Print you create an alias to redirect print console in window debug print

# First solution
sg.Print(1,2,3, text_color='red', background_color='blue', font='courier 16', sep='', end='')
sg.Print(1,2,3, text_color='yellow', background_color='green')

# Other alternative:
# sg.EasyPrint(4,5,6) # EasypPrint and Print can be closed with sg.EasyPrintClose() and sg.printClose()

def main():

    layout = [[sg.Text('My Window')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(30, 1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)

    while True:         # Event loop
        event, values = window.read()
        sg.Print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        sg.PrintClose() # or sg.EasyPrintClose()

        window['-OUT-'].update(f'You clicked {event}')

    window.close()

if __name__ == '__main__':
    main()