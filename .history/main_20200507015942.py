from glob import glob

import cv2
import numpy as np
from skimage.exposure import rescale_intensity
from skimage.filters import frangi
import matplotlib.pyplot as plt

fig, ax = plt.subplots(ncols=3)
for a in ax:
    a.axis('off')

for path in glob("healthy/*.jpg"):
    image = cv2.imread(path)
    image = cv2.resize(image, (700, 500))
    green = image[:, :, 1]
    bluegreen = image[:, :, 1] + image[:, :, 0]
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # p2, p98 = np.percentile(gray_image, (0.5, 95))
    # gray_image = rescale_intensity(gray_image, in_range=(p2, p98))

    # gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

    # cv2.namedWindow("gray", cv2.WINDOW_AUTOSIZE)
    # cv2.moveWindow('gray', 0, 0)
    # cv2.imshow('gray', image)

    # cv2.namedWindow("green", cv2.WINDOW_AUTOSIZE)
    # cv2.moveWindow('green', 700, 0)
    # cv2.imshow('green', green)

    # cv2.namedWindow("bluegreen", cv2.WINDOW_AUTOSIZE)
    # cv2.moveWindow('bluegreen', 300, 1400)
    # cv2.imshow('bluegreen', bluegreen)

    ax[0].imshow(gray, cmap=plt.cm.gray)
    ax[0].set_title('Original image')

    ax[1].imshow(frangi(green), cmap=plt.cm.gray)
    ax[1].set_title('Frangi filter result')

    ax[2].imshow(green, cmap=plt.cm.gray)
    ax[2].set_title('green')


    plt.tight_layout()
    plt.show()

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # break
