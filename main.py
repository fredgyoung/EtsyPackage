"""
https://pillow.readthedocs.io/en/stable/reference/index.html
"""
from PIL import Image, ImageDraw, ImageColor

OUTPUT_FOLDER = './Output/'
DPI = 300
PAGE_WIDTH, PAGE_HEIGHT = int(12 * DPI), int(12 * DPI)


def dots1(colors):
    pass


def dots2(colors):
    pass


def dots3(colors):
    pass


def dots4(colors):
    pass


def dots5(colors):
    pass


def dots6(colors):
    pass


def horizontal_stripes(colors, rectangle_width=50):

    # Because lists are Pass-by-Value, make a copy
    colors = colors[:]

    # Remove the first color which should be the bg color
    bg_color = colors.pop(0)

    filename = f"{OUTPUT_FOLDER}horizontal_stripes_{rectangle_width}.jpg"
    img = Image.new('RGB', (PAGE_WIDTH, PAGE_HEIGHT), ImageColor.getrgb(bg_color))
    canvas = ImageDraw.Draw(img)

    for y in range(rectangle_width//2, PAGE_HEIGHT, rectangle_width*2):
        color = colors.pop(0)
        canvas.rectangle(xy=((0, y), (PAGE_WIDTH, y+rectangle_width)), fill=ImageColor.getrgb(color))
        # print(y, y+line_width)
        colors.append(color)

    img.save(filename, "JPEG", dpi=(DPI, DPI))
    # colors.append(bg_color)
    # print()


def diagonal_stripes(colors, line_width=50):

    # Because lists are Pass-by-Value, make a copy
    colors = colors[:]

    # Remove the first color which should be the bg color
    bg_color = colors.pop(0)
    num_colors = len(colors)

    filename = f"{OUTPUT_FOLDER}diagonal_stripes_{line_width}.jpg"
    img = Image.new('RGB', (PAGE_WIDTH, PAGE_HEIGHT), ImageColor.getrgb(bg_color))
    canvas = ImageDraw.Draw(img)

    for y in range(line_width // 2, PAGE_HEIGHT, line_width * 2):
        color = colors[y % num_colors]
        points = [
            (0, y),
            (y, 0),
            (y+line_width, 0),
            (0, y+line_width)
        ]
        canvas.polygon(xy=points, fill=ImageColor.getrgb(color))

    img.save(filename, "JPEG", dpi=(DPI, DPI))


def thin_chevrons(colors):
    pass


def thick_chevrons(colors):
    pass


if __name__ == '__main__':

    color_list = ["white", "teal", "pink", "navy"]
    # color_list = ["white", "teal", "pink"]

    # horizontal_stripes(color_list, rectangle_width=50)
    # horizontal_stripes(color_list, rectangle_width=100)
    # horizontal_stripes(color_list, rectangle_width=200)
    diagonal_stripes(color_list, line_width=70)
    diagonal_stripes(color_list, line_width=140)
    diagonal_stripes(color_list, line_width=280)

