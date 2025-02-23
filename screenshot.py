import mss
import numpy as np
import cv2


def get_screen_shot():
    box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    with mss.mss() as sct:
        img = sct.grab(box)
        img = np.array(img)
        return img


if __name__ == '__main__':
    while True:
        img = get_screen_shot()
        cv2.imshow('img', img)
        cv2.waitKey(1)
