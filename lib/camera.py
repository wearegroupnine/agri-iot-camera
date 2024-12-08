import cv2
import time
import config
import numpy as np

def rectify(gray_img):
    try:
        npz_file = np.load('/agri/calib/camera_calibration.npz')
        if 'map1' and 'map2' in npz_file.files:
            map1 = npz_file['map1']
            map2 = npz_file['map2']
        else:
            print("Camera data file found but data corrupted.")
            exit(0)
    except:
        print("Camera calibration data not found in cache, file ")
        exit(0)

    # We didn't load a new image from file, but use last image loaded while calibration
    undistorted = cv2.remap(gray_img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted

def capture():
    cap = cv2.VideoCapture(0)

    # set
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(config.param_img_w))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(config.param_img_h))

    # Get the default frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            i += 1
            # the first few frame will be every dark, so we save image after the camera finish the warm up.
            if i == 15:
                #cv2.imwrite("rbg.png", frame)
                break
    rectified_img = rectify(frame)
    cap.release()
    return rectified_img


