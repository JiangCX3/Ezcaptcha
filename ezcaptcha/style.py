import random

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def img_to_nparray(img):
    return np.asarray(img)


def nparray_to_img(array):
    return Image.fromarray(np.uint8(array))


def cut_x(img_array, width):
    """沿着x轴剪切img array"""

    height = int(len(img_array) / width)

    new = []

    for line_key in range(0, height):
        line_start = width * line_key
        line_end = width * line_key + width

        line = []

        for px_key in range(line_start, line_end):
            line.append(img_array[px_key])

        new.append(line)

    return new


def roll(_list, shift):
    result = list(_list)
    list_len = len(_list)

    if shift >= 0:
        # 将后移到前
        for i in range(1, shift + 1):
            result.insert(0, _list[-i])

        # 切片
        return result[:list_len]
    else:
        # 将前移到后
        for i in range(0, abs(shift)):
            result.append(_list[i])

        # 切片
        for i in range(0, abs(shift)):
            del result[0]

        return result


class Distortion:
    @staticmethod
    def normal(img):
        """
        The Normal Style

        :param img:
        :return:
        """
        imar = img_to_nparray(img)

        return nparray_to_img(imar)

    @staticmethod
    def inverting(img):
        """
        Inverting

        :param img:
        :return:
        """
        imar = img_to_nparray(img)

        imar = 255 - imar

        return nparray_to_img(imar)

    @staticmethod
    def waves(img, options):

        # ==== Register Options ====
        options_list = [
            ("waves-amplitude", int(img.size[0] / 10)),
            ('waves-wavelength', int(img.size[1] / 10))
        ]

        key_err_count = 0
        for o in options_list:
            try:
                options[o[0]]
            except KeyError:
                options[o[0]] = o[1]
                key_err_count += 1

        if key_err_count == len(options_list):
            return img

        # ==== Register Options ====

        width, height = img.size

        old_pixels = list(img.getdata())
        old_pixels = cut_x(old_pixels, width)

        new_pixels = []

        for px_k in range(0, len(old_pixels)):
            moved = roll(old_pixels[px_k], int(np.sin(px_k / options['waves-wavelength']) * options['waves-amplitude']))
            new_pixels.append(moved)

        return nparray_to_img(new_pixels)

    @staticmethod
    def emp(img, options):

        # ==== Register Options ====
        options_list = [
            ("emp-level", 0),
        ]

        key_err_count = 0
        for o in options_list:
            try:
                options[o[0]]
            except KeyError:
                options[o[0]] = o[1]
                key_err_count += 1

        if key_err_count == len(options_list):
            return img

        # ==== Register Options ====


        width, height = img.size

        old_pixels = list(img.getdata())
        old_pixels = cut_x(old_pixels, width)

        new_pixels = []

        for px in old_pixels:
            moved = roll(px, random.randint(0, 10))
            new_pixels.append(moved)

        return nparray_to_img(new_pixels)

    @staticmethod
    def zebra(img, options):

        # ==== Register Options ====
        options_list = [
            ("zebra-level", int(img.size[1] / 15)),
            ('zebra-width', int(img.size[1] / 10))
        ]

        key_err_count = 0
        for o in options_list:
            try:
                options[o[0]]
            except KeyError:
                options[o[0]] = o[1]
                key_err_count += 1

        if key_err_count == len(options_list):
            return img

        # ==== Register Options ====


        # Register Options
        try:
            if options["zebra-level"] is None and options['zebra-width'] is None:
                return img
            elif options["zebra-level"] is None:
                options["zebra-level"] = 10
            elif options['zebra-width'] is None:
                options['zebra-width'] = 10

        except KeyError:
            return img

        width, height = img.size

        old_pixels = list(img.getdata())
        old_pixels = cut_x(old_pixels, width)

        new_pixels = []

        move_distance = random.randint(0, 10)
        change_count = 0

        for px in old_pixels:
            change_count += 1
            if change_count >= 20:
                if move_distance >= 0:
                    move_distance = random.randint(-5, -3)
                else:
                    move_distance = random.randint(3, 5)

                change_count = 0

            moved = roll(px, move_distance)
            new_pixels.append(moved)

        return nparray_to_img(new_pixels)


registered_styles = [
    Distortion.waves,
    Distortion.emp,
    Distortion.zebra
]
