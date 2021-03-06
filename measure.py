class PixelMeasurer:
    def __init__(self, coordinate_store, is_one_calib_block, correction_factor):
        self.coordinate_store = coordinate_store
        self.is_one_calib_block = is_one_calib_block
        self.correction_factor = correction_factor

    def get_distance(self, calibration_length):
        distance_per_pixel = calibration_length / self.pixel_distance_calibration()
        if not self.is_one_calib_block:
            calibration_difference = float(self.pixel_distance_calibration_side()) / \
                                     float(self.pixel_distance_calibration())
            distance_correction = 1 - self.correction_factor*(1 - calibration_difference)
            return self.pixel_distance_between_wheels() * distance_per_pixel * distance_correction
        else:
            return self.pixel_distance_between_wheels() * distance_per_pixel

    def get_left_wheel_midpoint(self):
        points = self.coordinate_store.get_left_wheel_points()
        return int(abs(points[0][0] + points[1][0]) / 2)

    def get_right_wheel_midpoint(self):
        points = self.coordinate_store.get_right_wheel_points(is_one_calib_block=self.is_one_calib_block)
        return int(abs(points[0][0] + points[1][0]) / 2)

    def pixel_distance_between_wheels(self):
        return abs(self.get_right_wheel_midpoint() - self.get_left_wheel_midpoint())

    def pixel_distance_calibration(self):
        calibration_points = self.coordinate_store.get_middle_calib_points()
        return abs(calibration_points[0][0] - calibration_points[1][0])

    def pixel_distance_calibration_side(self):
        calibration_points = self.coordinate_store.get_side_calib_points()
        return abs(calibration_points[0][0] - calibration_points[1][0])
