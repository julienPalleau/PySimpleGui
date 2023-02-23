"""
The Official Python GUI Programming with PySimpleGUI Course
Canvas Element - A direct mapping to tkinter Canvas Widget
Can use Graph Element to get the same tkinter Canvas Widget, plus more
Aliases:
Additional methods:

Docs: http://wwww.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#canvas-element
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import turtle

example_number = 1

sg.set_options(font='Default 16', keep_on_top=True)


# ==================================== 1 - EXAMPLE =====================================================================
def main_example1():
    layout = [[sg.Text('Turtle With PySimpleGUI', font='Default 18')],
              [sg.Canvas(size=(800, 800), key='-canvas-')],
              # [sg.Graph((800, 800), (0, 0), (800, 800), key='-canvas-')],
              [sg.Button('Circles')]]

    window = sg.Window('Canvas Element', layout, finalize=True)
    canvas = window['-canvas-'].TKCanvas

    a_turtle = turtle.RawTurtle(canvas)
    a_turtle.pencolor("#ff0000")  # Red
    a_turtle.penup()
    a_turtle.pendown()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Circles':
            a_turtle.speed(0)
            for i in range(400):
                a_turtle.circle(2 * i * .25)
                a_turtle.circle(-2 * i * .25)
                a_turtle.left(i)
    window.close()


if __name__ == "__main__":
    example = [main_example1]
    example[example_number - 1]()
