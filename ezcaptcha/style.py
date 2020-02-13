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
    list_len = len(_list)

    # 将后移到前
    result = _list

    for i in range(1, shift + 1):
        result.insert(0, _list[-i])

    # 切片
    return result[:list_len]


class Distortion:
    """
    扭曲样式
    """

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
    def waves(img):
        iarr = img_to_nparray(img)

        return nparray_to_img(np.array(iarr))

    @staticmethod
    def emp(img):
        width, height = img.size

        old_pixels = list(img.getdata())
        old_pixels = cut_x(old_pixels, width)

        new_pixels = []

        for px in old_pixels:
            moved = roll(px, random.randint(0, 10))
            new_pixels.append(moved)

        return nparray_to_img(new_pixels)

    @staticmethod
    def zebra(img):
        width, height = img.size

        old_pixels = list(img.getdata())
        old_pixels = cut_x(old_pixels, width)

        new_pixels = []

        move_distance = random.randint(0, 10)
        change_count = 0

        for px in old_pixels:
            change_count += 1
            if change_count >=20:
                if move_distance >= 0:
                    move_distance = random.randint(-5, -3)
                else:
                    move_distance = random.randint(3, 5)


                change_count = 0

            moved = roll(px, move_distance)
            new_pixels.append(moved)

        return nparray_to_img(new_pixels)
