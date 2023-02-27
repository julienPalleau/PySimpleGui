"""
The Official Python GUI Programming with PySimpleGUI Course
Tree Element:
Additional methods:
Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
import os

example_number = 3

sg.set_options(font='Default 16', keep_on_top=True)


# ========================== 1 - Example ==============================================================================
def main_example1():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(750, -300))

    treedata = sg.TreeData()

    treedata.Insert('', '-A-', 'A', [1, 2, 3])
    treedata.Insert('', '-B-', 'B', [1, 5, 6])
    treedata.Insert('', '-C-', 'C', [1])
    treedata.Insert('-A-', '-A1-', 'A1', [2, 'be', 'anything'])
    treedata.Insert('-A-', '-A2-', 'A2', [2, None])
    treedata.Insert('-A-', '-A3-', 'A3', [2])
    treedata.Insert('-A3-', '-A4-', 'A4', [3])
    treedata.Insert('-B-', '-B1-', 'B1', [2, None])
    treedata.Insert('-C-', '-C1-', 'C1', [2])
    treedata.Insert('-C-', '-C2-', 'C2', [2, 'nothing', 'at', 'all'])  # Note1 too many values

    layout = [[sg.Tree(treedata,
                       headings=['level', 'Col 2', 'Col 3'],
                       col0_width=8,
                       col0_heading='Items',
                       show_expanded=True,
                       enable_events=True,
                       expand_x=True,
                       expand_y=True,
                       header_font='_ 18',
                       auto_size_columns=True,
                       key='-TREE-')],
              [sg.Button('Show Image'), sg.Button('Print Treedata')]]
    window = sg.Window('Tree - Example 1', layout, resizable=True, )
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Show Image':
            sg.popup_non_blocking('', image='tree_image.png')
        elif event == 'Print Treedata':
            sg.popup_scrolled(str(treedata), non_blocking=True, font='Courier 16')
        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=True)
    window.close()


# ========================== 2 - Table of contents =====================================================================
def main_example2():
    sg.Print(font='Default 18', keep_on_top=True, size=(55, 14), relative_location=(750, -300))

    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAB/klEQVR4nO2XP28TQRDF38yu9xL70EGsSEBEmhRIgJQyDQV00NBQ' \
                  b'0FFSUebL5EPwLUhFA6KgIDTQRQLiyP/ubM+jOBvbYGM7sE7Da0/a37w3s6s5AQCSgjVKRLhO3jT8xdFRZWuQpmg01kPMMnxzzaa' \
                  b'vn7n7GopXfRcogqiRk6DPC6kX7qkXp0HVX1MlROK2miRUPegYvJlRaSzriT5kJE3MjB4AOt1ciryARLZMEiEJUlGFB4AHB/vYq' \
                  b'Pjyayz08AJ1e30cv3lfgh8e7KO2mUQiTqvVycfgdifHZlIBOR4wVcHf2SfMxu/E6Ox2JweAEqwqUFWQBCAQAc7ahndfcnj9md' \
                  b'JSEgDFANjb9tite5CAyBhcGhqCZ+m8Yzj+2EXwAq5AVgFaBZH4jRKM2bn9Bh7N9a0tj8NH2fLEX+SGznROt+Y6FgGCj3e7N' \
                  b'NrJCzTXcSsnTk57uH29AhI4Oe3BLTFoAqBvwI3MYfuKW77HI1WD4O5OgBtmcudmWGxjsgAZFzJLf+zxZIvdP27K6lEvyFrkf' \
                  b'9Qrgi9vqhPBvZ0AvWDUeuGoMR1vlKjNjAbQzKLtXSShztHMSrCqSlqrigKizkWBTkjSWhWqKp4DK95++PQ9rSbDZS/i7iPCZ' \
                  b'jsXDqzwX68OXj9+frjX+LyehT7bzfDs5ZPmWmCzJMDl/LT9AFiM1R1uh330AAAAAElFTkSuQmCC'

    book_table_of_contents = {
        'Chapter 1 - Popups': [('popup', 10), ('popup_get_text', 12), ('popup_get_file', 14), ('popup_get_folder', 16)],
        'Chapter 2 - Basic Elements': [('Text', 20), ('Input', 24), ('Button', 28)]}

    # ------------ Convert "Table of Contents" Dictionary to TreeData ------------
    def toc_to_treedata(toc):
        treedata = sg.TreeData()
        for chapter in toc:
            # Chapter has STRING key
            treedata.insert('', key=chapter, text=chapter, values=[], icon=folder_icon)
            for detailed_info in toc[chapter]:
                # Topic has TUPLE Key
                key = (chapter, detailed_info[1])  # key is (Chapter, page)
                treedata.insert(parent=chapter, key=key, text=detailed_info[0], values=[detailed_info[1]])
        return treedata

    # ------------ Delete a section from table of contents based on page number ------------
    def del_section(toc, page):
        for chapter in toc:
            for i, detailed_info in enumerate(toc[chapter]):
                if detailed_info[1] == page:
                    del toc[chapter][i]
                    break
        return toc

    treedata = toc_to_treedata(book_table_of_contents)
    col0_width = max([len(c) for c in book_table_of_contents])

    layout = [[sg.Tree(treedata,
                       headings=['Page #'],
                       col0_width=col0_width,
                       show_expanded=True,
                       enable_events=True,
                       expand_x=True,
                       expand_y=True,
                       header_font='_ 20',
                       key='-TREE-')],
              [sg.T('New Page #'), sg.In(s=4, key='-PAGE-'), sg.B('Change'), sg.B('Print Treedata'), sg.B('Delete')], ]
    window = sg.Window('Tree - Example 2', layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Change' and len(values['-TREE-']):
            for key in values['-TREE-']:
                window['-TREE-'].update(key=key, value=values['-PAGE-'])
        elif event == 'Delete':
            if len(values['-TREE-']):
                for key in values['-TREE-']:
                    new_toc = del_section(book_table_of_contents, key[1])
                new_treedata = toc_to_treedata(new_toc)
                window['-TREE-'].update(values=new_treedata)
        elif event == 'Print Treedata':
            sg.popup_scrolled(str(treedata), non_blocking=True, font='Courier 10')

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)
    window.close()


# ========================== 3 - EXAMPLE - Header operations ============================================================
def main_example3():
    sg.Print(font='Default 18', keep_on_top=True, size=(40, 14), relative_location=(750, -300))

    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='

    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    starting_path = r'Y:\\movies'

    treedata = sg.TreeData()

    def add_files_in_folder(parent, dirname):
        files = os.listdir(dirname)
        for f in files:
            fullname = os.path.join(dirname, f)
            if os.path.isdir(fullname):  # if it's a folder, add folder
                treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
                add_files_in_folder(fullname, fullname)
            else:
                treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)

    add_files_in_folder('', starting_path)

    layout = [[sg.Text('File and folder browser Test')],
              [sg.Tree(data=treedata,
                       headings=['Size (Bytes)'],
                       auto_size_columns=True,
                       num_rows=20,
                       col0_width=40,
                       key='-TREE-',
                       expand_x=True,
                       expand_y=True)],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Tree - Example 3', layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(f'values = {values}', c='white on red', erase_all=False)
    window.close()


if __name__ == '__main__':
    example = [main_example1, main_example2, main_example3]
    example[example_number - 1]()
