import numpy as np

import cv2

from croppable_image import Coordinates
from utilities.utils import Utils


class Outline:
    ndarray = None
    coord_list = []

    def __init__(self, ndarray, first_coord_list, second_coord_list=None):
        """Visual representation of target areas

        :param ndarray: visible
        :param first_coord_list, second_coord_list: list of Coordinate objects
        :return:

        >>> arr = cv2.imread('assets/img/doctests/photo.jpg', 0)
        >>> r1 = Coordinates(400, 500, 1200, 300)
        >>> r2 = Coordinates(100, 400, 150, 300)
        >>> r3 = Coordinates(250, 200, 500, 100)
        >>> i = Outline(arr, [r1, r2], [r3])
        >>> # i.show()
        """
        assert isinstance(ndarray, np.ndarray)
        self.ndarray = ndarray
        for coord in first_coord_list:
            self.draw_outline(coord, (0, 255, 0))
        for coord in second_coord_list or []:
            self.draw_outline(coord, (255, 0, 255))

    def draw_outline(self, coord, color):
        self.ndarray = cv2.rectangle(self.ndarray,
                                     (int(coord.left), int(coord.top)), (int(coord.right), int(coord.bottom)),
                                     color,
                                     10)

    def show(self, window_title="Outline"):
        Utils.show_image(self.ndarray, window_title)
