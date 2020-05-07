from glob import glob

import cv2
import numpy as np
from skimage.exposure import rescale_intensity, equalize_adapthist, adjust_gamma
from skimage.filters import frangi
import matplotlib.pyplot as plt

fig, ax = plt.subplots(ncols=3)
for a in ax:
    a.axis('off')

for path in glob("healthy/*.jpg"):
    img = cv2.imread(path)
    img = cv2.resize(img, (700, 500))
    img_equalized = equalize_adapthist(img)

    # green = image[:, :, 1]
    # bluegreen = image[:, :, 1] + image[:, :, 0]
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # p2, p98 = np.percentile(gray_image, (0.5, 95))
    # gray_image = rescale_intensity(gray_image, in_range=(p2, p98))

    # gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

    ax[0].imshow(img, cmap=plt.cm.gray)
    ax[0].set_title('Original image')

    ax[1].imshow(img_equalized, cmap=plt.cm.gray)
    ax[1].set_title('Equalized')

    # ax[2].imshow(green, cmap=plt.cm.gray)
    # ax[2].set_title('green')


    plt.tight_layout()
    plt.show()
    # break

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # break
