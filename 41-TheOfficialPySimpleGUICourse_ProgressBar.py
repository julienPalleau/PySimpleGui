"""
The Official Python GUI Programming with PySimpleGUI Course
ProgressBar Element - A horizontal or vertical progress bar / progress meter
Aliases:
    PBar = Prog = Progress = ProgressBar
Docs: http://www.PySimpleGUI.org
https://www.pysimplegui.org/en/latest/call%20reference/#progressbar-element
Built-in help: sg.sdk_help()
"""

import PySimpleGUI as sg
import threading
import time

example_number = 3
sg.set_options(font='Default 18')
if example_number:
    sg.Print('', font='Default 18', keep_on_top=True, size=(45, 8), location=(1000, 500))


# ========================== 1 - Intro (element only)  =================================================================

def main_intro():
    layout = [[sg.T('Progress Bars')],
              [sg.ProgressBar(100, orientation='h', size_px=(250, 30), k='-P-')]]

    window = sg.Window("ProgressBars", layout, keep_on_top=True, element_justification='c')

    i = 0
    while True:
        event, values = window.read(10)
        if event == sg.WIN_CLOSED:
            break
        window['-P-'].update(i % 100, 100)
        i += 1

    window.close()


# ================================== 2 - Simulated ProgressBar EXAMPLE =================================================
def main_simulated():
    layout = [[sg.Text('ProgressBar can be simulated using')],
              [sg.Text('Text Element')],
              [sg.Text(background_color='black', text_color='yellow', s=(30, 1), relief=sg.RELIEF_SUNKEN,
                       border_width=3, k='-T-', metadata=0, font='courier 20')],
              [sg.Text('Input Element')],
              [sg.Input(background_color='red', text_color='blue', s=(30, 1), k='-I-', border_width=0, metadata=0,
                        font='courier 20')],
              [sg.Button('Start'), sg.Button('Stop'), sg.Button('Exit')],
              ]
    window = sg.Window("Progress Bars", layout, keep_on_top=True)

    running = False
    while True:
        event, values = window.read(timeout=50)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        running = True if event == 'Start' else False if event == 'Stop' else running

        if running:
            count = window['-T-'].metadata = (window['-T-'].metadata + 1) % 30
            window['-T-'].update(sg.SYMBOL_SQUARE * count)

            count = window['-I-'].metadata = (window['-I-'].metadata + 1) % 30
            window['-I-'].update(' ' * count + sg.SYMBOL_SQUARE)

    window.close()


# ================================== 3 - ProgressBar EXAMPLE ===========================================================
def main_progress_bar():
    sg.theme('dark green 7')

    layout = [[sg.Text('A typical custom progress meter')],
              [sg.ProgressBar(100, orientation='v', size_px=(200, 30), key='-P1-', bar_color=('red', 'white')),
               sg.ProgressBar(0, orientation='h', size_px=(300, 20), key='-P2-', bar_color='red on white')],
              [sg.Cancel()]]
    window = sg.Window("ProgressBars", layout, keep_on_top=True)

    i = 0
    while True:
        event, values = window.read(timeout=10)
        if event in ('Cancel', sg.WIN_CLOSED):
            break
        i += 1
        window['-P1-'].update(i % 100)
        window['-P2-'].update(i % 100, max=100)

    window.close()


# ================================== 4 - ProgressBar Threaded EXAMPLE ==================================================
def the_thread(window: sg.Window):
    for i in range(100):
        time.sleep(.05)
        window.write_event_value('-THREAD-', (i + 1, 100))
    window.write_event_value('-THREAD-', (0, 0))


def main_pbar_threaded():
    layout = [[sg.Text('Video Downloader')],
              [sg.ProgressBar(0, size_px=(200, 10), orientation='h', k='-PB-')],
              [sg.Button('Start')]]

    window = sg.Window("Threaded ProgressBar", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Start':
            threading.Thread(target=the_thread, args=(window,), daemon=True).start()
        if event == '-THREAD-':
            if values[event][1] == 0:
                window.close()
                sg.popup('Download complete', keep_on_top=True)
                break
            else:
                window['-PB-'].update(values[event][0], values[event][1])

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')


if __name__ == '__main__':
    example = [main_intro, main_simulated, main_progress_bar, main_pbar_threaded]
    example[example_number - 1]()
