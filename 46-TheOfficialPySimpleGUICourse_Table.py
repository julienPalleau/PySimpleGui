"""
Additional methods:
Docs: http:www.PySimpleGUI.org
https://www.udemy.com/course/pysimplegui/learn/lecture/30060916#questions

Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import random
import string
import operator

example_number = 2
sg.theme('light green 5')
# sg.theme('dark red')

sg.set_options(font='Default 16', keep_on_top=True)


# ----- Some functions to help generate data for the table
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


def number(max_val=1000):
    return random.randint(0, max_val)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(0, num_rows):
        data[i] = [i, word(), *[number() for i in range(num_cols - 1)]]
    return data


def sort_table(table, cols):
    """ Sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list represents a row
        cols: a list (or tuple) specifying the column numbers to sort by e.g. (1, 0) would sort by column 1, then by
        column 0"""
    print(f"Debug cols: {cols}")
    for col in reversed(cols):
        try:
            table = sorted(table, key=operator.itemgetter(col))
        except Exception as e:
            sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return table


# ========================== 1 - Example ==============================================================================
def main_example():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(750, -300))

    # ----- Make the Table Data -----
    data = make_table(num_rows=100_000, num_cols=6)
    headings = [f'Col {col}' for col in range(len(data[0]))]
    sg.Print('Done creating table. Creating GUI...')
    layout = [[sg.Table(values=data,
                        headings=headings,
                        # visible_column_map=(False, False, False, True, True, False),
                        # col_widths=(8, 10, 20, 20, 20, 20),
                        # row_height=35,
                        # font='_ 15',
                        # header_font='_ 25,
                        def_col_width=10,
                        vertical_scroll_only=True,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color=sg.theme_button_color()[1],
                        key='-TABLE-',
                        selected_row_colors='red on yellow',
                        bind_return_key=True,
                        expand_x=True,
                        expand_y=True,
                        right_click_selects=True,
                        # enable_events=True,
                        # enable_click_events,
                        )],
              [sg.Button('Delete'), sg.Button('Highlight'), sg.T('Containing'), sg.In(s=4, k='-HIGHLIGHT-')]]

    window = sg.Window('Table - Example 1', layout, resizable=True, right_click_menu=['_', ['Delete', 'Exit']])

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Delete':
            for row in reversed(values['-TABLE-']):
                del data[row]
            window['-TABLE-'].update(data)
        elif isinstance(event, tuple):
            cell = event[2]
            window['-CLICKED-'].update(cell)
        elif event == 'Highlight':
            zero_rows = []
            for i, row in enumerate(data):
                if int(values['-HIGHLIGHT-']) in row:
                    zero_rows.append(i)
            window['-TABLE-'].update(row_colors=((i, 'red', 'white') for i in zero_rows))
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        if len(values['-TABLE-']) < 10:
            sg.Print(f'values = {values}', c='white on red', erase_all=True)

    window.close()


# ========================== 2 - Example - Header operations ===========================================================
def main_example2():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(750, -300))

    # --------- Make the Table Data ---------
    data = make_table(num_rows=5_000, num_cols=6)
    headings = [f'Col {col}' for col in range(len(data[0]))]
    # sg.Print('Done creating table. Creating GUI...')
    layout = [[sg.T('Filter:', s=15), sg.In(size=10, key='-FILTER-')],
              [sg.T('Click Sets Cell To:', s=15), sg.In(size=10, key='-CELL VALUE-')],
              [sg.Table(values=data,
                        headings=headings,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color=sg.theme_button_color()[1],
                        key='-TABLE-',
                        selected_row_colors='red on yellow',
                        bind_return_key=True,
                        expand_x=True,
                        expand_y=True,
                        right_click_selects=True,
                        enable_click_events=True,
                        # enable_events=True,
                        )],
              [sg.Text('Cell Clicked:'), sg.T(k='-CLICKED-')]]

    window = sg.Window('Table - Example 2', layout, resizable=True, right_click_menu=['_', ['Delete', 'Exit']])
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Delete':
            for row in reversed(values['-TABLE-']):
                del data[row]
            window['-TABLE-'].update(data)
        elif isinstance(event, tuple):      # clicked a header or cell
            cell = event[2]
            window['-CLICKED-'].update(cell)
            if event[0] == '-TABLE-':
                col_num_clicked = event[2][1]
                print(event[2][0], col_num_clicked)
                if event[2][0] == -1 and col_num_clicked != -1:  # Header was clicked and wasn't the "row" column
                    print("test1")
                    if not values['-FILTER-']:
                        print("test2")
                        new_table = sort_table(data, (col_num_clicked, 0))
                        window['-TABLE-'].update(new_table)
                        data = new_table
                    else:
                        new_table = []
                        for row in data:
                            if str(row[col_num_clicked]) == values['-FILTER-']:
                                new_table.append(row)
                        window['-TABLE-'].update(new_table)
                        window['-FILTER-'].update('')
                        data = new_table
                elif col_num_clicked != -1 and values['-CELL VALUE-'] and None not in cell:
                    data[cell[0]][cell[1]] = int(values['-CELL VALUE-'])
                    window['-TABLE-'].update(data)

            window['-CLICKED-'].update(cell)
        sg.Print(f'event={event}', c='white on red', erase_all=False)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)

    window.close()


if __name__ == '__main__':
    example = [main_example, main_example2]
    example[example_number - 1]()
