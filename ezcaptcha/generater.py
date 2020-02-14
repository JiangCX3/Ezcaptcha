import io
import random
import string

import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL.Image import alpha_composite

import ezcaptcha.work
from ezcaptcha import style

import matplotlib.pyplot as plt

# style demo


style_demo = {
    "height": 40,
    "width": 120,
    "background": "#ffffff",
    "colors": ["#000000"],
    "distortion": []
}


class FontSizeTooBig(ValueError):
    pass


class Captcha:
    def __init__(
            self,
            styles: dict,
            codes: list,
            word_spacing: int,
            font_size: int,
            height: int,
            width: int,
            **kwargs
    ):

        self.kwargs = kwargs

        # Checks
        if font_size / height > 0.8:
            raise FontSizeTooBig(
                "font_size should be less than 80% of style.height! Try smaller: >=" +
                str(int(height * 0.8))
            )

        # Image Style
        self.height = height
        self.width = width
        self.styles = styles
        self.background = self.styles["background"]
        self.word_spacing = word_spacing
        self.font_size = font_size

        # Codes
        self.codes = codes

        self.obj = self.create_background()
        self.draw = ImageDraw.Draw(self.obj)

        # ====================
        self.add_code_text()
        self.add_disturbs()

    def get_object(self):
        """
        Get Pillow Object

        :return:
        """

        return self.obj

    def get_base64(self):
        return

    def get_save_to_path(self, path):
        return

    """image edit"""

    def create_background(self):
        """
        Create Background

        :return:
        """
        image = Image.new('RGBA', (self.width, self.height), color=self.background)

        return image

    def add_code_text(self):
        """
        ADD CODE TEXT TO IMAGE

        :return:
        """
        op_layer = Image.new('RGBA', (self.width, self.height))
        op_layer_draw = ImageDraw.Draw(op_layer)

        for key in range(0, len(self.codes)):
            # The font size factor controls the basic font size,
            # and the font distortion factor controls the font size to change randomly.
            font_size = int(self.font_size + random.randint(-10, 10) * 2)

            font = ImageFont.truetype(random.choice(self.styles['text']['fonts']), size=font_size)

            text_y_pos = random.randint(-50, self.height - font_size)
            color = random.choice(self.styles["text"]["colors"])
            color = self.hex_to_rgb(color)

            op_layer_draw.text((key * self.word_spacing, text_y_pos), self.codes[key], fill=color, font=font)

        for st in ezcaptcha.style.registered_styles:
            op_layer = st(op_layer, options=self.styles["text"])

        self.obj = alpha_composite(self.obj, op_layer)
        print("add_code_text")

    def add_disturbs(self):
        """
        ADD disturbs

        :return:
        """
        op_layer = Image.new('RGBA', (self.width, self.height))
        op_layer_draw = ImageDraw.Draw(op_layer)

        font_size = int(self.height / 10)

        font = ImageFont.truetype(random.choice(self.styles['disturbs']['fonts']), size=font_size)

        x_quantity = int(self.width / font_size)
        y_quantity = int(self.height / font_size)

        for x_key in range(0, x_quantity):

            # text_y_pos = random.randint(1, self.height - font_size)
            color = random.choice(self.styles["disturbs"]["colors"])
            color = self.hex_to_rgb(color)
            for y_key in range(0, y_quantity):
                op_layer_draw.text(
                    (
                        x_key * font_size + random.randint(-font_size * 0.2, font_size * 0.2),
                        y_key * font_size + random.randint(-font_size * 0.2, font_size * 0.2)
                    ),
                    random.choice(string.ascii_letters),
                    fill=(color[0], color[1], color[2], 200),
                    font=font
                )

        for st in ezcaptcha.style.registered_styles:
            op_layer = st(op_layer, options=self.styles["disturbs"])

        self.obj = alpha_composite(self.obj, op_layer)
        print("add_disturbs")

    def apply_text_distortion(self):
        for st in self.styles["distortion"]:
            self.obj = st(self.obj)

    """translators"""

    @staticmethod
    def hex_to_rgb(hex_code: str):
        r = int(hex_code[1:3], 16)
        g = int(hex_code[3:5], 16)
        b = int(hex_code[5:7], 16)
        return r, g, b

    @staticmethod
    def rgb_to_hex(rgb_code: tuple):
        color = '#'
        for i in rgb_code:
            num = int(i)
            color += str(hex(num))[-2:].replace('x', '0').upper()
        print(color)
        return color


if __name__ == '__main__':
    code = [random.choices(string.ascii_letters + string.digits)[0] for s in range(5)]
    print(code)

    style = {
        "background": "#ffffff",
        "background-img": "",

        "disturbs": {
            "fonts": ["Nunito-Regular.ttf"],
            "colors": ezcaptcha.work.random_color_list(),
            "waves-amplitude": 10,
            # "waves-wavelength": 20,
            # "emp-level": 18,
            # "zebra-level": 8,
            # "zebra-width": 10,
        },
        "text": {
            "fonts": ["Nunito-Regular.ttf"],
            "colors": ezcaptcha.work.random_color_list(),
            "waves-amplitude": 10,
            # "waves-wavelength": 20,
            # "emp-level": 18,
            # "zebra-level": 8,
            # "zebra-width": 10,
        }
    }

    gc = Captcha(styles=style, codes=code, distortion=10, word_spacing=60, font_size=160, height=200, width=400)

    plt.imshow(gc.get_object())
    plt.show()
