"""
Ne marche pas correctement en attente d'une correction du formateur

The Official PythonGUI Programming with PySimpleGUI Course
Exec API
    Simplified Exectuion of Python programms, subprocess, your IDE/editor

Functions:
    execute_command_subprocess
    execute_editor
    execute_file_explorer
    execute_find_callers_filename
    execture_get_results
    execute_py_file
    execute_py_get_interpreter
    execute_subprocess_still_running

Docs:
    http://www.PySimpleGUI.org
    https://www.pysimplegui.org/en/latest/call%20reference/#exec-apis-launching-subprocesses

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import sys
import subprocess
import threading
import time

example_number = 4

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - EXAMPLE ===============================================================================
def main_example1():
    # sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300)
    layout = [[sg.Text('Right-click me...')],
              [sg.Button('Main'), sg.Button('Exit')]]

    window = sg.Window('Exec API 1', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        if event == 'Main':
            sg.main()

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f' values = {values}', c='white on red', erase_all=False)

    window.close()


# ========================== 2 - EXAMPLE ===============================================================================
def main_example2():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300))

    layout = [[sg.Text(f'Ppython = {sys.version}')],
              [sg.Button('Main'), sg.Button('File'), sg.Button('Exit')]]

    window = sg.Window('Exec API 2', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Main':
            sp = sg.execute_command_subprocess(r'psgmain')
        elif event == 'File':
            sp = sg.execute_py_file(__file__)

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)


# # ========================== 3 - EXAMPLE ===============================================================================
# def main_example3():
#     layout = [[sg.Multiline(size=(70, 20), font='courier 14', reroute_stdout=True, autoscroll=True, k='-ML-',
#                             write_only=True)],
#               [sg.Button('Dir'), sg.Button('Exit')]]
#
#     window = sg.Window('Exec API 3', layout, resizable=True)
#
#     while True:
#         event, values = window.read()
#         if event in (sg.WIN_CLOSED, 'Exit'):
#             break
#         if event == 'Dir':
#             sp = sg.execute_command_subprocess(r'dir', pipe_output=True)
#             results = sg.execute_get_results(sp)
#             print('== RESULTS ==', results)
#             if results[0]:
#                 print('*** RESULTS STDOUT ***')
#                 print(results[0])
#             if results[1]:
#                 print('*** RESULTS STDERR ***')
#                 print(results[1])
#
#     window.close()


# ========================== 3 - EXAMPLE   ==========================

def main_example3():
    layout = [[sg.Multiline(size=(70, 25), font='courier 14', reroute_stdout=True, autoscroll=True, k='-ML-',
                            write_only=True)],
              [sg.Button('Dir'), sg.Button('Exit')]]

    window = sg.Window('Exec API 3', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Dir':
            # result = subprocess.run([sys.executable, "-c", "print('Ocean')"])
            sp = sg.execute_command_subprocess('"C:\Program Files\Git\git-bash.exe"', "--cd-to-home", wait=False,
                                               pipe_output=True)
            results = sg.execute_get_results(sp)
            print('== RESULTS ==')
            if results[0]:
                print('*** RESULTS STDOUT ***')
                print(results[0])
            if results[1]:
                print('*** RESULTS STDERR ***')
                print(results[1])

    window.close()


# ========================== 4 - EXAMPLE   ==========================
def scratch_305():
    for i in range(1000):
        print(i)
        # time.sleep(.1)


def main_example4():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300))

    def the_thread(window: sg.Window, sp: subprocess.Popen):
        window.write_event_value('-THREAD-', '===THREAD STARTING===')
        window.write_event_value('-THREAD-', '----- STDOUT & STDERR Follows ----')
        for line in scratch_305():
            oline = line.decode().rstrip()
            window.write_event_value('-THREAD-', oline)
        window.write_event_value('-THREAD-', '===THREAD DONE===')

    layout = [[sg.Multiline(size=(40, 25), font='courier 16', reroute_stdout=True, autoscroll=True, k='-ML-',
                            write_only=True)],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Exec API 4', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Go':
            thread = threading.Thread(target=the_thread, args=(window, scratch_305()), daemon=True)
            thread.start()
        elif event == '-THREAD-':
            print(values[event])

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3, main_example4]
    example[example_number - 1]()
