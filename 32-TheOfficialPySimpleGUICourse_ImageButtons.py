"""
The Official Python GUI Programming with PySimpleGUI Course

Button Element - Lesson Part 3 - Buttons with Image

Normal buttons can have PNG and GIF images from a file or base64 bytestring

Docs: http://www.PySimpleGUI.org
Built-in help: sg.sdk_help()
"""
import PySimpleGUI as sg
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import base64

# sg.sdk_help()

sg.set_options(font='Default 18')
sg.Print(font='Default 18', keep_on_top=True, size=(30, 14), location=(292, 545))
example_number = 4


# ============================= 1 - Button with Image File & Base64 ====================================================
def main_button_image_file():
    # sg.TRANSPARENT_BUTTON is the same as (sg.theme_background_color(), sg.theme_background_color())
    layout = [
        [sg.Button(image_filename='Play.png', key='-PLAY-', button_color=(sg.theme_background_color(),
                                                                          sg.theme_background_color()),
                   border_width=0)],
        [sg.Button(image_data=sg.EMOJI_BASE64_HAPPY_THUMBS_UP, key='-HAPPY EMOJI-',
                   button_color=sg.TRANSPARENT_BUTTON, border_width=0)],
        [sg.Button('Go'), sg.B('Exit')]
    ]
    window = sg.Window("Button Image Basics", layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f' {k} = {values[k]}' for k in values], sep='\n')


# ============================= 2 - Toggle Button BASE64 ===============================================================
def main_toggle_basic():
    layout = [
        [sg.Button(image_data=toggle_btn_off, key='-TOGGLE-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   disabled_button_color=('red', 'green'), border_width=0, metadata=False)],
        [sg.B('Disable', disabled_button_color=('red', 'green')), sg.B('Enable'), sg.B('Exit')]]

    window = sg.Window('Toggle Button', layout, keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

        if event == 'Disable':
            window['-TOGGLE-'].update(disabled=True)
            window['Disable'].update(disabled=True)
        elif event == 'Enable':
            window['-TOGGLE-'].update(disabled=False)
            window['Disable'].update(disabled=False)
        elif event == '-TOGGLE-':
            window['-TOGGLE-'].metadata = not window['-TOGGLE-'].metadata
            window['-TOGGLE-'].update(image_data=toggle_btn_on if window['-TOGGLE-'].metadata else toggle_btn_off)
    window.close()


# ============================= 3 - PIL EXAMPLE ========================================================================
def resize_base64_image(image64, size=(120, 75)):
    """
    May not be the original purpose, but this code is being used to resize an image for use with PySimpleGUI (tkinter)
    button graphics
    :param image64: (str) The Base64 image
    :param size: Tuple[int, int] Size to make the image in pixels (width, height
    :return: (bytes) A new Base 64 image
    """
    image_file = BytesIO(base64.b64decode(image64))
    img = Image.open(image_file)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    bio = BytesIO()
    img.save(bio, format='PNG')
    imgbytes = bio.getvalue()
    return imgbytes


def rounded_rectangle(text, font=('arial.ttf', 14), button_color=None, ):
    """
    Generate rounded image with text aligned center.
    :param text: text to show on image, '\n' to split lines.
    :type font: Tuple
    :return image in bytes
    :type: bytes
    """
    pad, radius, spacing = 5, 10, 5
    ttf_font = ImageFont.truetype(font=font[0], size=font[1])
    if not text:
        text = ' '
    paragraph = text.split('n')
    w = max(map(lambda x: ttf_font.getbbox(x)[0], paragraph)) + 2 * pad
    h = sum(map(lambda x: ttf_font.getbbox(x)[1], paragraph)) + 2 * pad + len(paragraph) + spacing
    c0, c1 = button_color if button_color else sg.theme_button_color()
    c0 = c0 if c0 != sg.COLOR_SYSTEM_DEFAULT else 'white'
    c1 = c1 if c1 != sg.COLOR_SYSTEM_DEFAULT else 'white'
    im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), fill=c1, width=0, radius=radius)
    draw.multiline_text((pad, pad), text, align='center', font=ttf_font, fill=c0, spacing=spacing)
    with BytesIO() as buffer:
        im.save(buffer, format='PNG')
        data = buffer.getvalue()
    return data


def main_PIL_rounded_rect():
    sg.theme("dark red")
    # sg.theme("dark green 7")

    layout = [[sg.pin(sg.Col([[sg.Image(r'C:\Users\MOTTIER LUCIE\Documents\GitHub\PySimpleGui\PIL_Book_Cover.png')],
                              [sg.Text('www.TeachMePython.com/books')],
                              [sg.Text('Learn PIL using PySimpleGUI')]], k='-IMAGE-'))],
              [sg.Button('Normal Button')],
              [sg.Button(image_data=sg.EMOJI_BASE64_HAPPY_THUMBS_UP, border_width=0,
                         button_color=sg.TRANSPARENT_BUTTON, k='-EMOJI-')],
              [sg.Button(image_data=rounded_rectangle('Button text\nwith 2 lines', font=('arial.ttf', 25)),
                         button_color=sg.TRANSPARENT_BUTTON, border_width=0, k='-PIL BUTTON-'),
               sg.Button('Button text\nwith 2 lines', size=(10, 2), font='arial 18', border_width=0)],
              [sg.Button('Start', image_data=resize_base64_image(start_image),
                         button_color=('white', sg.theme_background_color()), font='_ 20', border_width=0),
               sg.Button('Exit', image_data=resize_base64_image(exit_image),
                         button_color=('white', sg.theme_background_color()), border_width=0, font='_ 20'),
               sg.B(sg.SYMBOL_X, k='-HIDE-', border_width=0)]]

    window = sg.Window('Image and Rounded Button', layout, finalize=True, keep_on_top=True, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.Print(f'event = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

        if event == '-HIDE-':
            window['Start'].update(visible=False)


# ============================= 4 - PIL Toggle Button EXAMPLE ==========================================================

def toggle_button(button_color=None, size=(100, 40), on=True):
    """
    : return image in bytes
    : type: bytes
    """
    pad, radius, spacing = 5, 10, 5
    w, h = size
    c1, c2 = button_color if button_color else (sg.theme_input_background_color(), sg.theme_background_color())
    im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), fill=c1, width=3, radius=radius)
    if on:
        draw.rounded_rectangle((2, 1, w - size[1], h - 3), fill=c2, width=3, radius=radius)
    else:
        draw.rounded_rectangle((size[1], 2, w - 2, h - 3), fill=c2, width=3, radius=radius)
    with BytesIO() as buffer:
        im.save(buffer, format='PNG')
        data = buffer.getvalue()
    return data


def main_PIL_toggle():
    sg.theme("dark red")
    # sg.theme("dark green 7")
    # sg.theme("dark gray 13")
    button_on = toggle_button()
    button_off = toggle_button(on=False)

    layout = [[sg.T('PIL Mode Toggle Buttons')],
              [sg.T('On'),
               sg.Button(image_data=button_on, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         border_width=0, k='-B1-', metadata=True),
               sg.T('Off')],
              [sg.Button(image_data=button_off, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         border_width=0, k='-B2-',
                         metadata=False)]
              ]
    window = sg.Window('PIL Buttons', layout, finalize=True, element_justification='c', use_custom_titlebar=True,
                       font='_ 18', keep_on_top=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.Print(f'element = {event}', c='white on red', erase_all=True)
        sg.Print(*[f'{k}={values[k]}' for k in values], sep='\n')

        window[event].metadata = not window[event].metadata
        window[event].update(image_data=button_on if window[event].metadata else button_off)

    window.close()


if __name__ == "__main__":
    toggle_btn_off = b'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'
    toggle_btn_on = b'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'
    start_image = b'iVBORw0KGgoAAAANSUhEUgAAAiIAAADLCAMAAABkvgh7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANtvJ99sId5tIt5uI91tJNxuJNxuJttvKN90NN91Ntt3PN52ONx3Otx3PNt4Pdp4Ptx4PepfD+pfEOtgD+piD+tkD+ttD+dnFOdoE+doFOVoFuNqG+JrHOFrHuFsHuRpGORpGuRqGORqGupgEOpiEOpkEOlmEOhnEupoEOpoEupqFettEetsF+tuFOxqFetrGOtsGetvHOxrGOxsGOxtGuxuG+xuHexxFutwH+xxGOxyGOxyGuxxHuBsIOJvJ+NvKORvKONwKeNwKuJxLONyLeJyLuRwKeRwKuRxLOtxIexyIexzJOx0JOx1Ju11KOx2KOx2Kux5Iux4Kux5Le1/LeFyMOFzMuB0NOB1Nux7MOx8MOx8Mu19NO1+NO1+Ntd7RdV8RtN+S9J/TdF/TtV9SNR9Stl5QNl6Qdh6Qth7RK+Tfa+Tfq6Ufr+JZb+JZr+KZ7uMbr6KaL6LaryMbLyNb7yOb7WPdLuNcLqOcLmOcrmPdLOQd7SQdrKReLKRerGSerCTfLCTfrmQde2AN+2AOO2BOu2COu6DPO6EPe6EPsWDV8OFXcOFXsOGXcOGXsaDWMSEWsqCVs+AUM2AUs6CU82CVMqDWMmEWtCAT9CAUMKHYMCIYsCIZMCKZu6FQO6GQe6GQu6HRO6IRe6JRu6KR+6KSO+LSu+MS++MTO+OTe+OTu+OUO+RUu+TVfCNTvCOTvCPUPCQUfCQUvCSU/CRVPCSVPCSVvCUV/CUWPCVWvGWWvGXXPGYXvCWYPGaYfGcYvGcZPKdZvKeZ/GdavKeaPKebfKebvKgavKhbPKibfGibvKjcPGkcfKmdPKiePOod/OpePSpePSqevSrfPSsfPSsfvSqg/SugfWwgvWwhPWyhfWyhvWxi/Wyj/W0ifW2jfa4j/a1kPW2kva2lfW2lvW4kPa6kfa7kva5lvW7lPa8lPW8lve+l/a4mva5nPa6nPa7nva+mPa+mva/nPa8oPa9ovbAm/bAnfXAnvbCofbEo/XGp/bGqPbIqQAAAC/NnaUAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAAJXElEQVR4Xu3de3zVdR3H8Xb9/sJh60LlOTtubdIZEyckSdedMzkdZyRGIePmZdqki8s0KllJmtGCTAXRlUAyrireUeZga2JRkooYRWR0JbXMLsIqZ5fT7/L5nRvj9/md0/fhw/Px/fyHP+D33fb4vPj+LvsxXpMA8IREgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgJF7Ih1Xf3bVsuu/AYXu+mUrL+u8iqbqIcdErvhme0V8SjQCIpwWe+0nli+k2R5NTolc0jYzqpQBcigV+UDltZ57SQ6JfLqyRRXRyiCIis7u7qAhj8B3Ip1tLdg/pFLR0Z+hOR/JbyIrWxGIZCp289E2Ep+J3HzEFqLKy0qhUJUfeUkZnf8lGnYWX4l0tDfTOg5VEqoJNNTXh6EgmaMLBKuaymmcJFLRSfPO5CuRtgitYisPBehDQUFrqC3O2EtUxRdo4Bn8JHJhlNawlNZh85Aj2JQeiRp9JY08nY9Euk+nFUwq1ECLgww1ZTRaS+R8mnk6PpEF8dTDkNIgLQxiHFdNw7U0d9PU07CJdLw+tRUVpy5Cxo19+bz9lYI+n5cNfdhcjWGZf2jsCTTJcDiUmnBR/HKaewqbSHfqQqSJrkLGvuuctZu3jOgBD1u99B7Fg6a+Vwrrk8kNfRX+0XE2+qg527adsc38M723d01yK3lbqhH1SZp7CpfIolnJw4udQk44ddPOn/3q6b+M6K8+/c2vF+jXVw29X/ALI7N+Z3jome+f/QZ7pOG6VCMtl9Dkk7hElifvd0uPs1cb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'
    exit_image = b'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'

    example = [main_button_image_file, main_toggle_basic, main_PIL_rounded_rect, main_PIL_toggle]
    example[example_number - 1]()
