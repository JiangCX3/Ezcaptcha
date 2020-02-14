import random
import string

import os

from . import generater


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


class RandomCode:
    @staticmethod
    def letters(length: int = 5):
        return [random.choices(string.ascii_letters)[0] for s in range(length)]

    @staticmethod
    def numbers(length: int = 5):
        return [random.choices(string.digits)[0] for s in range(length)]

    @staticmethod
    def letters_numbers(length: int = 5):
        return [random.choices(string.ascii_letters + string.digits)[0] for s in range(length)]


class Entry:
    def __init__(self):
        pass

    @staticmethod
    def get(
            codes: list,
            word_spacing: int,
            font_size: int,
            height: int,
            width: int,
            styles: dict,
    ):
        if styles is None:

            styles = {
                "background": "#ffffff",
                "background-img": "",

                "disturbs": {
                    "fonts": [os.path.split(os.path.realpath(__file__))[0] + "/Nunito-Regular.ttf"],
                    "colors": random_color_list(),
                    "waves-amplitude": 10,
                },
                "text": {
                    "fonts": [os.path.split(os.path.realpath(__file__))[0] + "/Nunito-Regular.ttf"],
                    "colors": random_color_list(),
                    "waves-amplitude": 10,
                }
            }

        gc = generater.Captcha(
            styles=styles,
            codes=codes,
            word_spacing=word_spacing,
            font_size=font_size,
            height=height,
            width=width
        )

        return gc
