#!/usr/bin/env python
# encoding=utf-8
from PIL import Image

from ezcaptcha.generater import Captcha
from .work import RandomCode
from . import work


def easy_get(
        width: int = 400,
        height: int = 200,
        length: int = 4,
        complexity: int = 5,
        return_type: str = "image",
        filepath: str = None,
        **kwargs
):
    """
    最简单，最不用动脑子的解决办法。传入需要的长度以及复杂度，立即生成验证码图片。

    length      验证码长度
    complexity  复杂度，1-10简单到复杂
    return_type 返回数据类型，可以是 imageObject\base64Code\filepath

    :param height:
    :param width:
    :param return_type:
    :param filepath:
    :param length:
    :param complexity:
    :return:
    """
    result = None

    try:
        styles = kwargs["styles"]
    except KeyError:
        styles = None

    font_size = int(height / 1.3)
    word_spacing = int((width * 0.8) / length)
    codes = RandomCode.letters_numbers(length)

    gc = work.Entry.get(
        styles=styles,
        codes=codes,
        word_spacing=word_spacing,
        font_size=font_size,
        height=height,
        width=width,
    )

    if return_type is "image":
        result = gc.get_object()
    elif "base64":
        result = gc.get_base64()
    elif "filepath":
        result = gc.get_save_to_path(filepath)

    return result


def get_img(
        codes: list = RandomCode.letters_numbers(),
        word_spacing: int = 60,
        font_size: int = 160,
        height: int = 200,
        width: int = 400,
        styles: dict = None
) -> Image:
    """"""
    return work.Entry.get(
        styles=styles,
        codes=codes,
        word_spacing=word_spacing,
        font_size=font_size,
        height=height,
        width=width
    ).get_object()


def get_base64(
        codes: list = RandomCode.letters_numbers(),
        word_spacing: int = 60,
        font_size: int = 160,
        height: int = 200,
        width: int = 400,
        styles: dict = None
) -> Image:
    """"""
    return work.Entry.get(
        styles=styles,
        codes=codes,
        word_spacing=word_spacing,
        font_size=font_size,
        height=height,
        width=width
    ).get_base64()


def save_to_path(
        path: str,
        codes: list = RandomCode.letters_numbers(),
        word_spacing: int = 60,
        font_size: int = 160,
        height: int = 200,
        width: int = 400,
        styles: dict = None

) -> Image:
    """"""

    return work.Entry.get(
        styles=styles,
        codes=codes,
        word_spacing=word_spacing,
        font_size=font_size,
        height=height,
        width=width
    ).get_save_to_path(path=path)
