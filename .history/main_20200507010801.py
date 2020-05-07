from glob import glob

import cv2
import numpy as np
from skimage.exposure import rescale_intensity

for path in glob("healthy/*.jpg"):
    image = cv2.imread(path)
    image = cv2.resize(image, (500, 500))
    image_blue = image[:, :, 0]
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    p2, p98 = np.percentile(gray_image, (0.5, 95))
    gray_image = rescale_intensity(gray_image, in_range=(p2, p98))
    # gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)
    cv2.imshow('rescaled', gray_image)
    cv2.imshow('onecolor', image_blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break
