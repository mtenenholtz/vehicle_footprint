import cv2
import numpy as np


class CoordinateStore:
    def __init__(self, corners):
        self.nearest_corners = []
        self.corners = corners

    def find_closest_point(self, point):
        distances = np.sqrt((self.corners[:, :, 0] - point[0]) ** 2 + (self.corners[:, :, 1] - point[1]) ** 2)
        nearest_index = np.argmin(distances)
        return self.corners[nearest_index]

    def select_point(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
                point = (x, y)
                self.nearest_corners.append(self.find_closest_point(point))
