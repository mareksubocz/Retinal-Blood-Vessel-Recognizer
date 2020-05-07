from glob import glob

import cv2
import numpy as np
from skimage.exposure import rescale_intensity, equalize_adapthist, adjust_gamma
from skimage.filters import frangi, unsharp_mask
import matplotlib.pyplot as plt

def firstPhase(img):
    img = equalize_adapthist(img)
    img = adjust_gamma(img)
    img = unsharp_mask(img, 1, 1)
    return img

def secondPhase(img):
    img = frangi(img)
    return img

for path in glob("healthy/*.jpg"):

    fig, ax = plt.subplots(nrows=2, ncols=3)
    for row in ax:
        for a in row:
            a.axis('off')

    img = cv2.imread(path)
    img = cv2.resize(img, (700, 500))
    imggreen = img[:, :, 1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = img[:, :, 1]
    # green = image[:, :, 1]
    # bluegreen = image[:, :, 1] + image[:, :, 0]
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # p2, p98 = np.percentile(gray_image, (0.5, 95))
    # gray_image = rescale_intensity(gray_image, in_range=(p2, p98))

    # gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

    ax[0][0].imshow(img, cmap=plt.cm.gray)
    ax[0][0].set_title('Original image')

    ax[0][1].imshow(firstPhase(img), cmap=plt.cm.gray)
    ax[0][1].set_title('first')

    ax[0][2].imshow(secondPhase(firstPhase(img)), cmap=plt.cm.gray)
    ax[0][2].set_title('second')

    ax[1][0].imshow(imggreen, cmap=plt.cm.gray)
    ax[1][0].set_title('Original green')

    ax[1][1].imshow(firstPhase(imggreen), cmap=plt.cm.gray)
    ax[1][1].set_title('first')

    ax[1][2].imshow(secondPhase(firstPhase(imggreen)), cmap=plt.cm.gray)
    ax[1][2].set_title('second')

    plt.tight_layout()
    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close(fig)
    # break

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # break
