import random


def random_color_list():
    """
    Get Random Color List

    :return:
    """
    colors = []

    for s in range(0, 24):
        color_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""

        for t in range(0, 6):
            color += random.choice(color_arr)

        colors.append("#" + color)

    return colors
