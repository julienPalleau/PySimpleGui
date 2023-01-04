import PySimpleGUI as sg

font1 = 'Courier, 12'
font2 = 'Courier', 30, 'bold'

layout = [  [sg.Text('Time Application', font=font1)],
            [sg.Text('00:00', font=font2)],
            [sg.Button('Start', 'padding', size=(6, 1), pad=((0, 3)), tooltip='Start the timer'),
             sg.Button('Pause', 'padding', size=(6, 1), pad=((0, 3)), tooltip='Pause the timer'),
             sg.Button('Stop', 'padding', size=(6, 1), pad=((0, 3)), tooltip='Stop the timer')],
            [sg.Text('X', background_color='red', text_color='white', enable_events=True, key='Exit')]
        ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()