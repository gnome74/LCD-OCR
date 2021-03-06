import math
import numpy as np

import cv2

from croppable.croppable_image import CroppableImage
from utilities.plotter import Plotter


class ShearTool:
    """
    >>> st = ShearTool(cv2.imread('assets/img/doctests/digits.jpg', 0))
    >>> # Plotter.image(st.shear(30), "shear")
    """
    img = None
    height = width = 0

    def __init__(self, img):
        assert isinstance(img, np.ndarray)
        i = CroppableImage(img)
        # i.crop_borders(0.05)
        self.img = i.get_ndarray()
        self.height, self.width = self.img.shape

    def shear(self, degrees):
        value = self.height * math.tan(math.radians(degrees))
        half = value / 2
        pts1 = np.float32([[0, 0], [self.height, 0], [0, self.width], [self.height, self.width]])
        pts2 = np.float32([[0 - value + half, 0],
                           [self.height - value + half, 0],
                           [0 + value + half, self.width],
                           [self.height + value + half, self.width]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        return cv2.warpPerspective(self.img, m, (self.width, self.height), borderMode=cv2.BORDER_REPLICATE)
