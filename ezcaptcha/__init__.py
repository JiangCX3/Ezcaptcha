#!/usr/bin/env python
# encoding=utf-8

def easy_get(length: int = 4, complexity: int = 5, return_type: str = "image", **kwargs):
    """
    最简单，最不用动脑子的解决办法。传入需要的长度以及复杂度，立即生成验证码图片。

    length      验证码长度
    complexity  复杂度，1-10简单到复杂
    return_type 返回数据类型，可以是 imageObject\base64Code\filepath

    :param length:
    :param complexity:
    :return:
    """

    image = None
    code = ""
    return (image, code)


def get(code: str = None, length: int = 4,  # 自定义验证码Code，验证码长度
        have_letter: bool = True, have_number: bool = True, characters: str = None,  # 是否包含字母，是否包含数字，额外自定义字符集
        noise: int = 8, word_spacing: int = 10, font_size: int = 10,  # 噪声系数，字体扭曲度系数，字体间隔系数，字体大小系数
        style: dict = None,  # 样式
        **kwargs):
    """
    :param style:
    :param characters:
    :param code:
    :param length:
    :param have_letter:
    :param have_number:
    :param kwargs:
    :return:
    """
    if style is None:
        style = {
            "height": 40,
            "width": 120,
            "background": "#ffffff",
            "colors": ["#000000"],
        }
    if characters is None:
        characters = []

    code = "1234"
    image = None

    return (image, code)
