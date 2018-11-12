import cv2
import numpy as np


class CoordinateStore:
    def __init__(self, corners):
        self.nearest_corners = []
        self.corners = corners
        self.click_count = 0

    def find_closest_point(self, point):
        distances = np.sqrt((self.corners[:, :, 0] - point[0]) ** 2 + (self.corners[:, :, 1] - point[1]) ** 2)
        nearest_index = np.argmin(distances)
        return self.corners[nearest_index]

    def select_point(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
                point = (x, y)
                self.nearest_corners.append(self.find_closest_point(point))
                self.click_count += 1

    def get_left_calib_points(self):
        return [tuple(self.nearest_corners[0].ravel()), tuple(self.nearest_corners[1].ravel())]

    def get_right_calib_points(self):
        return [tuple(self.nearest_corners[4].ravel()), tuple(self.nearest_corners[5].ravel())]

    def get_middle_calib_points(self):
        return [tuple(self.nearest_corners[8].ravel()), tuple(self.nearest_corners[9].ravel())]

    def get_left_wheel_points(self):
        return [tuple(self.nearest_corners[2].ravel()), tuple(self.nearest_corners[3].ravel())]

    def get_right_wheel_points(self):
        return [tuple(self.nearest_corners[6].ravel()), tuple(self.nearest_corners[7].ravel())]
