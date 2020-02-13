import io
import random
import string

import style as style
from PIL import Image, ImageDraw, ImageFont

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
    def __init__(self, styles: dict, codes: list,
                 distortion: int, word_spacing: int, font_size: int,
                 **kwargs):
        self.kwargs = kwargs
        # Checks
        if font_size / styles["height"] > 0.8:
            raise FontSizeTooBig(
                "font_size should be less than 80% of style.height! Try smaller: >=" +
                str(int(styles["height"] * 0.8))
            )

        # Image Style
        self.styles = styles
        print(styles)
        self.background = self.styles["background"]
        self.word_spacing = word_spacing
        self.font_size = font_size

        # Codes
        self.codes = codes

        # Distortion and noises
        self.distortion = distortion

        self.obj = self.create_background()
        self.draw = ImageDraw.Draw(self.obj)

        # ====================

        self.add_code_text()
        self.apply_text_distortion()

        return

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
        image = Image.new('RGB', (self.styles["width"], self.styles["height"]), color=self.background)
        ofile = io.BytesIO()

        image.save(ofile, 'JPEG')

        return image

    def add_code_text(self):
        """
        ADD CODE TEXT TO IMAGE

        :return:
        """
        for key in range(0, len(self.codes)):
            # The font size factor controls the basic font size,
            # and the font distortion factor controls the font size to change randomly.
            font_size = int(self.font_size + random.randint(-self.distortion, self.distortion) * 2)
            font = ImageFont.truetype("Nunito-Regular.ttf", size=font_size)

            text_y_pos = random.randint(1, self.styles["height"] - font_size)
            color = random.choice(self.styles["colors"])
            color = self.hex_to_rgb(color)

            self.draw.text((key * self.word_spacing, text_y_pos), self.codes[key], fill=color, font=font)

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
    code = [random.choices(string.ascii_letters)[0] for s in range(5)]
    print(code)

    style = {
        "height": 200,
        "width": 400,
        "background": "#ffffff",
        "colors": ezcaptcha.work.random_color_list(),
        "distortion": [
            style.Distortion.zebra,
            style.Distortion.emp,
        ]
    }

    gc = Captcha(styles=style, codes=code, distortion=10, word_spacing=60, font_size=160)

    plt.imshow(gc.get_object())
    plt.show()
