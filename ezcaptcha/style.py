import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def img_to_nparray(img):
    return np.asarray(img)


def nparray_to_img(array):
    return Image.fromarray(np.uint8(array))


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
        print(iarr.shape)

        lines = [iarr[i, :, :] for i in range(0, iarr.shape[0])]

        x = [60 * np.sin(0.1 * a) for a in np.arange(0, len(lines))]
        new = []
        for i, line in enumerate(lines):
            new.append(np.roll(line, int(x[i])))

        plt.imshow(np.array(new))
        plt.show()

        return nparray_to_img(np.array(new))


if __name__ == '__main__':
    img = Image.open("2.bmp")
    Distortion.waves(img).show()
