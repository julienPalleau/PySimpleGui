"""
The Official Python GUI Programming with PySimpleGUI Course

Graph Element - Your "Gateway Element"
Aliases:
    Gr

    Additional methodes:
        bring_figure_to_front
        change_coordinates
        delete_figure
        draw_arc
        draw_cirle
        draw_image
        draw_lines
        draw_oval
        draw_point
        drawl_polygon
        draw_rectangle
        draw_text
        erase
        get_bounding_box
        get_figures_at_location
        move
        move_figure
        reloate_figure
        send_figure_to_back

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg

example_number = 3

sg.set_options(font='Default 16', keep_on_top=True)


# ==================================== 1 - EXAMPLE - Bar Chart =========================================================

def main_example1():
    data_points = [50, 10, 20, 80]
    graph = sg.Graph((600, 600), (0, 0), (10, 100), k='-GRAPH-')
    layout = [[graph],
              [sg.Button('Draw')]]

    window = sg.Window('Graph Element - Example 1', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        for i, data in enumerate(data_points):
            graph.draw_rectangle((i * 2 + 1, data), (i * 2 + 2, 0), fill_color='blue', line_width=2)
            graph.draw_text(f'{data}', (i * 2 + 1, data + 2), font='_ 18')

    window.close()


# ==================================== 2 - EXAMPLE - Drawing & Moving Images ===========================================
def main_example2():
    sg.Print(font='Default 19', keep_on_top=True, size=(30, 14), relative_location=(600, -300))
    image = r'image.png'
    graph = sg.Graph((600, 600), (0, 0), (600, 600), drag_submits=True, enable_events=True, k='-GRAPH-')
    layout = [[graph],
              [sg.Button('Draw')]]
    window = sg.Window('Graph Element - Exemple 2', layout)

    image_fig = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Draw':
            image_fig = graph.draw_image(filename=image, location=(0, 600))
        elif event == '-GRAPH-':
            graph.relocate_figure(image_fig, values[event][0], values[event][1])

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')

    window.close()


# ==================================== 3 - EXAMPLE - Drawing & Moving Images ===========================================
def main_example3():
    sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), relative_location=(600, -300))
    graph = sg.Graph((600, 600), (-300, -300), (300, 300), enable_events=True, drag_submits=True, k='-GRAPH-')
    layout = [[graph],
              [sg.Button('Draw Heart'), sg.Button('Draw Check'), sg.Button('Draw Happy')]]
    window = sg.Window('Graph Element - Example 2', layout)

    figures = drag = False
    last_location = (0, 0)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Draw Happy':
            graph.draw_image(data=sg.EMOJI_BASE64_HAPPY_THUMBS_UP, location=(0, 0))
        if event == 'Draw Heart':
            graph.draw_image(data=sg.HEART_3D_BASE64, location=(0, 0))
        if event == 'Draw Check':
            graph.draw_image(data=sg.GREEN_CHECK_BASE64, location=(0, 0))
        elif event == '-GRAPH-':
            x, y = values[event]

            if drag:
                delta_x, delta_y = x - last_location[0], y - last_location[1]
            else:
                last_location = values['-GRAPH-']
                delta_x = delta_y = 0
                drag = True

            if figures:
                for figure in figures:
                    graph.move_figure(figure, delta_x, delta_y)
                last_location = x, y
        if event.endswith('+UP'):
            drag = False
            figures = graph.get_figures_at_location(values['-GRAPH-'])
            if figures:
                graph.send_figure_to_back(figures[-1])

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k} = {values[k]}' for k in values], sep='\n')
    window.close()


if __name__ == "__main__":
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
