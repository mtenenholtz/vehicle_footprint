from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import filedialog

import numpy as np
import cv2 as cv
import configparser

root = tk.Tk()
root.withdraw()

config_file_path = filedialog.askopenfilename(title='Select configuration file',
                                              filetypes=(('ini files', '*.ini'),
                                                         ('all files', '*.*'))
                                              )

file_open_path = filedialog.askopenfilename(title='Select image to open',
                                            filetypes=(('jpeg files', '*.jpg'),
                                                       ('png files', '*.png'),
                                                       ('all files', '*.*'))
                                            )

config = configparser.ConfigParser()
config.read(config_file_path)
drawing_options = config['Drawing']
detection_options = config['Detection']

img = cv.imread(file_open_path, 1)

rect = cv.selectROI(img=img,
                    fromCenter=False
                    )

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)  # should this be BGR2GRAY?
mask = np.zeros(gray.shape, np.uint8)
mask[int(rect[1]):int(rect[1] + rect[3]), int(rect[0]):int(rect[0] + rect[2])] = 1
corners = cv.goodFeaturesToTrack(gray,
                                 int(detection_options['max_corners']),
                                 float(detection_options['corner_quality']),
                                 int(detection_options['min_distance']),
                                 mask=mask
                                 )
corners = np.int0(corners)

circle_color = (int(drawing_options['circle_b']), int(drawing_options['circle_g']), int(drawing_options['circle_r']))
for i in corners:
    x, y = i.ravel()
    cv.circle(img,
              (x, y),
              int(drawing_options['circle_radius']),
              circle_color,
              -1
              )

if drawing_options.getboolean('flip_colors'):
    img = np.fliplr(img.reshape(-1, 3)).reshape(img.shape)

file_save_path = filedialog.asksaveasfilename(title='Select location to save image',
                                              filetypes=(('png files', '*.png'),
                                                         ('all files', '*.*'))
                                              )

plt.imsave(file_save_path, img)
