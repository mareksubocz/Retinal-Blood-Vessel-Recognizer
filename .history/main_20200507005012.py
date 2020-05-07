from glob import glob

import cv2
import numpy as np
from skimage.exposure import rescale_intensity

for path in glob("healthy/*.jpg"):
    print(path)

p2, p98 = np.percentile(gray_image, (0.5, 90))
gray_image = rescale_intensity(gray_image, in_range=(p2, p98))
