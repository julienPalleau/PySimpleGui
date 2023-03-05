"""
The Official Python GUI Programming with PySimpleGUI Course
Multithreading
How to use threads with PySimpleGUI

Threading rule - There is ONE PySimpleGUI call allowed from threads:
Window.write_event_value

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import threading
import time

example_number = 3
sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================

def main_example1():
    sg.Print(font='Default 15', keep_on_top=True, size=(60, 14), relative_location=(200, -300))

    def my_function():
        time.sleep(15)
        sg.Print('*** DONE! ***', c='white on green')

    layout = [[sg.Text('Threading Example 1')],
              [sg.Button('Start'), sg.Button('Start 2'), sg.Button('Nothing'), sg.Button('Exit')], ]

    window = sg.Window('Threading Example 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=False)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)

        if event == 'Start':
            my_function()
        elif event == 'Start2':
            window.perform_long_operation(my_function, '-DONE-')

    window.close()


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    sg.Print(font='Default 15', keep_on_top=True, size=(60, 14), relative_location=(200, -300))

    def the_thread(window):
        window.write_event_value('-THREAD-', 'Thread Started...')
        for i in range(10):
            time.sleep(1)
            window.write_event_value('-THREAD-', f'counter = {i}')

        window.write_event_value('-THREAD-', '*** The thread says... "I am finished" ***')

    layout = [[sg.Text('Threading Example 2')],
              [sg.Button('Start'), sg.Button('Nothing'), sg.Button('Exit')], ]

    window = sg.Window('Threading', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'event = {event}', c='white on red', erase_all=False)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)

        if event == 'Start':
            thread = threading.Thread(target=the_thread, args=(window,), daemon=True)
            thread.start()
        elif event == '-THREAD-':
            sg.Print(f'Thread message: {values[event]}', c='white on purple')

    window.close()


# ========================== 3 - EXAMPLE ===============================================================================
def main_example3():
    def the_thread(window):
        for i in range(100):
            time.sleep(.1)
            window.write_event_value('-THREAD-', i)
        window.write_event_value('-COMPLETED-', None)

    layout = [[sg.Text('Threading Example 3')],
              [sg.ProgressBar(100, orientation='h', size=(20, 30), k='-PROGRESS-')],
              [sg.Button('Start'), sg.Button('Test'), sg.Button('Exit')], ]

    window = sg.Window('Threading', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Start':
            thread = threading.Thread(target=the_thread, args=(window,), daemon=True)
            thread.start()
        elif event == '-THREAD-':
            window['-PROGRESS-'].update(values[event] + 1, 100)
        elif event == '-COMPLETED-':
            sg.popup('The Thread completed')
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
